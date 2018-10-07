from datetime import datetime
from odoo.tools.translate import _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo import api, fields, models
from odoo.exceptions import UserError


class SyllabusHistoryWorkflow(models.Model):
    """Useful to manage edition's workflow on a syllabus."""

    _name = 'syllabus_minister.syllabus_history'
    _inherit = ['syllabus_minister.syllabus_history', 'mail.thread']

    state = fields.Selection([
        ('draft', 'Draft'),
        ('to approve', 'Pending Approval'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled')],
        'Status',
        readonly=True,
        default='draft'
    )

    approved_date = fields.Datetime(
        'Approved Date',
    )

    approved_uid = fields.Many2one(
        'res.users',
        'Approved by',
    )

    is_approval_required = fields.Boolean(
        related='syllabus_id.is_approval_required',
        string="Approval required",
    )

    am_i_owner = fields.Boolean(
        compute='_compute_am_i_owner'
    )

    am_i_approver = fields.Boolean(
        compute='_compute_am_i_approver'
    )

    syllabus_url = fields.Text(
        compute='_compute_syllabus_url',
        string="URL",
    )

    @api.multi
    def syllabus_approval_draft(self):
        """Set a change request as draft"""
        if self.filtered(lambda r: r.state not in [
                         'cancelled', 'approved']):
            raise UserError(_("It's not cancelled or approved"))
        if self.filtered(lambda r:
                         r.state == 'approved' and not self.am_i_approver):
            raise UserError(_("You are not an appover to reset to draft"))
        self.write({'state': 'draft'})

    @api.multi
    def syllabus_auto_confirm(self):
        """Automatic Transitions for change requests created directly from
        documents
        """
        if self.filtered(lambda r: r.state != 'draft'):
            raise UserError(_("It's not in draft state"))
        to_approve = self.filtered(lambda r: r.is_approval_required)
        to_approve.write({'state': 'to approve'})
        approved = (self - to_approve)
        approved.write({'state': 'approved'})
        approved.mapped('syllabus_id')._compute_history_head()

    @api.multi
    def syllabus_approval_to_approve(self):
        """Set a change request as to approve"""
        self.write({'state': 'to approve'})
        template = self.env.ref(
            'syllabus_approval.email_template_new_draft_need_approval')
        approver_gid = self.env.ref(
            'syllabus_approval.syllabus_approval_group_approver')
        for rec in self:
            if rec.is_approval_required:
                guids = [g.id for g in rec.syllabus_id.approver_group_ids]
                users = self.env['res.users'].search([
                    ('groups_id', 'in', guids),
                    ('groups_id', 'in', approver_gid.id)])
                rec.message_subscribe_users([u.id for u in users])
                rec.message_post_with_template(template.id)

    @api.multi
    def syllabus_approval_approved(self):
        """Set a change request as approved."""
        self.write({
            'state': 'approved',
            'approved_date': datetime.now().strftime(
                DEFAULT_SERVER_DATETIME_FORMAT),
            'approved_uid': self.env.uid
        })
        for rec in self:
            # Trigger computed field update
            rec.syllabus_id._compute_history_head()
            # Notify state change
            rec.message_post(
                subtype='mt_comment',
                body=_(
                    'Change request has been approved by %s.'
                    ) % (self.env.user.name)
            )
            # Notify followers a new version is available
            rec.syllabus_id.message_post(
                subtype='mt_comment',
                body=_(
                    'New version of the document %s approved.'
                    ) % (rec.syllabus_id.name)
            )

    @api.multi
    def syllabus_approval_cancelled(self):
        """Set a change request as cancelled."""
        self.write({'state': 'cancelled'})
        for rec in self:
            rec.message_post(
                subtype='mt_comment',
                body=_(
                    'Change request <b>%s</b> has been cancelled by %s.'
                    ) % (rec.display_name, self.env.user.name)
                )

    @api.multi
    def _compute_am_i_owner(self):
        """Check if current user is the owner"""
        for rec in self:
            rec.am_i_owner = (rec.create_uid == self.env.user)

    @api.multi
    def _compute_am_i_approver(self):
        """check if current user is a approver"""
        for rec in self:
            rec.am_i_approver = rec.syllabus_id.can_user_approve_this_syllabus(
                self.env.user)

    @api.multi
    def _compute_syllabus_url(self):
        """Compute the syllabus url."""
        for syllabus in self:
            base_url = self.env['ir.config_parameter'].sudo().get_param(
                'web.base.url',
                default='http://localhost:8069'
            )

            syllabus.syllabus_url = (
                '{}/web#db={}&id={}&view_type=form&'
                'model=syllabus_minister.syllabus_history').format(
                    base_url,
                    self.env.cr.dbname,
                    syllabus.id
                )

    @api.multi
    def _compute_diff(self):
        """Shows a diff between this version and the previous version"""
        history = self.env['syllabus_minister.syllabus_history']
        for rec in self:
            domain = [
                ('syllabus_id', '=', rec.syllabus_id.id),
                ('state', '=', 'approved')]
            if rec.approved_date:
                domain.append(('approved_date', '<', rec.approved_date))
            prev = history.search(domain, limit=1, order='approved_date DESC')
            if prev:
                rec.diff = self.getDiff(prev.id, rec.id)
            else:
                rec.diff = self.getDiff(False, rec.id)
