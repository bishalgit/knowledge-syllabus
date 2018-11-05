# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.tools.safe_eval import safe_eval

class SyllabusTask(models.Model):
    _name = "syllabus.task"
    _description = "Syllabus Task"
    _date_name = "date_start"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _mail_post_access = 'read'
    _order = "priority desc, sequence, id desc"


    active = fields.Boolean(default=True)
    name = fields.Char(string='Task Title', track_visibility='always', required=True, index=True)
    description = fields.Html(string='Description')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ], default='0', index=True, string="Priority")
    sequence = fields.Integer(string='Sequence', index=True, default=10,
        help="Gives the sequence order when displaying a list of tasks.")
    create_date = fields.Datetime(index=True)
    write_date = fields.Datetime(index=True)  
    # not displayed in the view but it might be useful with base_automation module (and it needs to be defined first for that)

    date_start = fields.Datetime(string='Starting Date',
    default=fields.Datetime.now,
    index=True, copy=False)
    date_end = fields.Datetime(string='Ending Date', index=True, copy=False)
    date_assign = fields.Datetime(string='Assigning Date', index=True, copy=False, readonly=True)
    date_deadline = fields.Date(string='Deadline', index=True, copy=False)
    syllabus_id = fields.Many2one('document.page',
        string='Syllabus',
        default=lambda self: self.env.context.get('default_syllabus_id'),
        index=True,
        track_visibility='onchange',
        domain="[('type', '=', 'content')]",
        change_default=True)
    notes = fields.Text(string='Notes')
    planned_hours = fields.Float(string='Initially Planned Hours', help='Estimated time to do the task, usually set by the syllabus manager when the task is in draft state.')
    remaining_hours = fields.Float(string='Remaining Hours', digits=(16,2), help="Total remaining time, can be re-estimated periodically by the assignee of the task.")
    user_id = fields.Many2one('res.users',
        string='Assigned to',
        default=lambda self: self.env.uid,
        index=True, track_visibility='always')
    manager_id = fields.Many2one('res.users', string='Syllabus Task Manager')
    color = fields.Integer(string='Color Index')
    attachment_ids = fields.One2many('ir.attachment', compute='_compute_attachment_ids', string="Task Attachments",
        help="Attachment that don't come from message.")
    
    # Computed field about working time elapsed between record creation and assignation/closing.
    working_hours_open = fields.Float(compute='_compute_elapsed', string='Working hours to assign', store=True, group_operator="avg")
    working_hours_close = fields.Float(compute='_compute_elapsed', string='Working hours to close', store=True, group_operator="avg")
    working_days_open = fields.Float(compute='_compute_elapsed', string='Working days to assign', store=True, group_operator="avg")
    working_days_close = fields.Float(compute='_compute_elapsed', string='Working days to close', store=True, group_operator="avg")
    
    # customer portal: include comment and incoming emails in communication history
    website_message_ids = fields.One2many(domain=lambda self: [('model', '=', self._name), ('message_type', 'in', ['email', 'comment'])])

    def _compute_attachment_ids(self):
        for task in self:
            attachment_ids = self.env['ir.attachment'].search([('res_id', '=', task.id), ('res_model', '=', 'syllabus.task')]).ids
            message_attachment_ids = task.mapped('message_ids.attachment_ids').ids  # from mail_thread
            task.attachment_ids = list(set(attachment_ids) - set(message_attachment_ids))

    @api.multi
    @api.depends('create_date', 'date_end', 'date_assign')
    def _compute_elapsed(self):
        task_linked_to_calendar = self.filtered(
            lambda task: task.syllabus_id.resource_calendar_id and task.create_date
        )
        for task in task_linked_to_calendar:
            dt_create_date = fields.Datetime.from_string(task.create_date)

            if task.date_assign:
                dt_date_assign = fields.Datetime.from_string(task.date_assign)
                task.working_hours_open = task.syllabus_id.resource_calendar_id.get_work_hours_count(
                        dt_create_date, dt_date_assign, False, compute_leaves=True)
                task.working_days_open = task.working_hours_open / 24.0

            if task.date_end:
                dt_date_end = fields.Datetime.from_string(task.date_end)
                task.working_hours_close = task.syllabus_id.resource_calendar_id.get_work_hours_count(
                    dt_create_date, dt_date_end, False, compute_leaves=True)
                task.working_days_close = task.working_hours_close / 24.0

        (self - task_linked_to_calendar).update(dict.fromkeys(
            ['working_hours_open', 'working_hours_close', 'working_days_open', 'working_days_close'], 0.0))

    def _compute_portal_url(self):
        super(SyllabusTask, self)._compute_portal_url()
        for task in self:
            task.portal_url = '/my/task/%s' % task.id

    @api.multi
    def copy(self, default=None):
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = _("%s (copy)") % self.name
        if 'remaining_hours' not in default:
            default['remaining_hours'] = self.planned_hours
        return super(SyllabusTask, self).copy(default)

    @api.multi
    def get_access_action(self, access_uid=None):
        """ Instead of the classic form view, redirect to website for portal users
        that can read the task. """
        self.ensure_one()
        user, record = self.env.user, self
        if access_uid:
            user = self.env['res.users'].sudo().browse(access_uid)
            record = self.sudo(user)

        if user.share:
            try:
                record.check_access_rule('read')
            except AccessError:
                pass
            else:
                return {
                    'type': 'ir.actions.act_url',
                    'url': '/my/task/%s' % self.id,
                    'target': 'self',
                    'res_id': self.id,
                }
        return super(SyllabusTask, self).get_access_action(access_uid)
