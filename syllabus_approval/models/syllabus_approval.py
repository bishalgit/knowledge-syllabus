from odoo import api, fields, models
from ast import literal_eval

import logging

_logger = logging.getLogger(__name__)


class SyllabusApproval(models.Model):
    """Useful to know the state of a syllabus."""

    _inherit = 'syllabus_minister.syllabus'

    history_ids = fields.One2many(
        order='approved_date DESC',
        domain=[('state', '=', 'approved')],
    )

    approved_date = fields.Datetime(
        'Approved Date',
        related='history_head.approved_date',
        store=True,
        index=True,
        readonly=True,
    )

    approved_uid = fields.Many2one(
        'res.users',
        'Approved by',
        related='history_head.approved_uid',
        store=True,
        index=True,
        readonly=True,
    )

    approval_required = fields.Boolean(
        'Require approval',
        help='Require approval for changes on this syllabus.',
    )

    approver_gid = fields.Many2one(
        "res.groups",
        "Approver group",
        help='Users must also belong to the Approvers group',
    )

    is_approval_required = fields.Boolean(
        'Approval required',
        help='If true, changes of this syllabus require approval',
        compute='_compute_is_approval_required',
    )

    am_i_approver = fields.Boolean(
        compute='_compute_am_i_approver'
    )

    approver_group_ids = fields.Many2many(
        'res.groups',
        string='Approver groups',
        help='Groups that can approve changes to this document',
        compute='_compute_approver_group_ids',
    )

    has_changes_pending_approval = fields.Boolean(
        compute='_compute_has_changes_pending_approval',
        string='Has changes pending approval'
    )

    @api.multi
    @api.depends('approval_required')
    def _compute_is_approval_required(self):
        """Check if the document required approval."""
        for syllabus in self:
            res = syllabus.approval_required
            syllabus.is_approval_required = res

    @api.multi
    @api.depends('approver_gid')
    def _compute_approver_group_ids(self):
        """Compute the approver groups based on his parents."""
        for syllabus in self:
            res = syllabus.approver_gid
            syllabus.approver_group_ids = res


    @api.multi
    @api.depends('is_approval_required', 'approver_group_ids')
    def _compute_am_i_approver(self):
        """Check if the current user can approve changes to this syllabus."""
        for rec in self:
            rec.am_i_approver = rec.can_user_approve_this_syllabus(self.env.user)

    @api.multi
    def can_user_approve_this_syllabus(self, user):
        """Check if a user can approve this syllabus."""
        self.ensure_one()
        # if it's not required, anyone can approve
        if not self.is_approval_required:
            return True
        # to approve, you must have approver rights
        approver_group_id = self.env.ref(
            'syllabus_approval.syllabus_approval_group_approver')
        if approver_group_id not in user.groups_id:
            return False
        # and belong to at least one of the approver_groups (if any is set)
        if not self.approver_group_ids:
            return True
        return len(user.groups_id & self.approver_group_ids) > 0

    @api.multi
    def _compute_has_changes_pending_approval(self):
        history = self.env['syllabus_minister.syllabus_history']
        for rec in self:
            changes = history.search_count([
                ('syllabus_id', '=', rec.id),
                ('state', '=', 'to approve')])
            _logger.warning("Changes >>>>>>>>>>>>>>>>>>>> " + str(changes))
            rec.has_changes_pending_approval = (changes > 0)

    @api.multi
    def _create_history(self, vals):
        res = super(SyllabusApproval, self)._create_history(vals)
        _logger.warning("Change History Created >>>>>>>>>>>>>>>>>>>> " + str(res))
        res.syllabus_auto_confirm()

    @api.multi
    def action_changes_pending_approval(self):
        self.ensure_one()
        action = self.env.ref('syllabus_approval.action_change_requests')
        action = action.read()[0]
        context = literal_eval(action['context'])
        context['search_default_syllabus_id'] = self.id
        context['default_syllabus_id'] = self.id
        action['context'] = context
        return action
