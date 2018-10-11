# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Syllabus(models.Model):
    _name = 'syllabus_minister.syllabus'
    _inherit = 'mail.thread'
    _description = 'Syllabus'

    name = fields.Char('Name')
    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    semester = fields.Char(string='Semester')
    attachment_id = fields.Many2one('ir.attachment',string = 'Decision Attachment')
    content = fields.Html(
        "Content",
        compute='_compute_content',
        inverse='_inverse_content',
        search='_search_content',
        required=True,
    )

    # no-op computed field
    summary = fields.Html(
        help='Describe the changes made',
        compute=lambda x: x,
        inverse=lambda x: x,
    )
    history_head = fields.Many2one(
        'syllabus_minister.syllabus_history',
        'HEAD',
        compute='_compute_history_head',
        store=True,
        auto_join=True,
    )

    history_ids = fields.One2many(
        'syllabus_minister.syllabus_history',
        'syllabus_id',
        'History',
        order='create_date DESC',
        readonly=True,
    )

    content_date = fields.Datetime(
        'Last Contribution Date',
        related='history_head.create_date',
        store=True,
        index=True,
        readonly=True,
    )

    content_uid = fields.Many2one(
        'res.users',
        'Last Contributor',
        related='history_head.create_uid',
        store=True,
        index=True,
        readonly=True,
    )
    required_name_change = fields.Boolean('Require Name Change', compute="_compute_required_name_change")
    store_required_name_change = fields.Boolean('Store Required Name Change', default=False)

    def get_name(self):
        for record in self:
            n = ""
            if record.course_id:
                n = n + str(record.course_id.course_code)
                if record.course_id.program_id:
                    n = n + " / " + record.course_id.program_id.name
                    if record.course_id.program_id.faculty_id:
                        n = n + " / " + record.course_id.program_id.faculty_id.name
            return n

    def _compute_required_name_change(self):
        for record in self:
            _logger.warning("Name comptuted >>>> ")
            n = record.get_name()
            if n != record.name:
                record.store_required_name_change = True
    
    @api.multi
    @api.depends('history_head')
    def _compute_content(self):
        for rec in self:
            if rec.history_head:
                rec.content = rec.history_head.content
            else:
                # html widget's default, so it doesn't trigger ghost save
                rec.content = '<p><br></p>'

    @api.multi
    def _inverse_content(self):
        for rec in self:
            rec._create_history({
                'content': rec.content,
                'summary': rec.summary,
                })

    @api.multi
    def updateName(self):
        for record in self:
            n = record.get_name()
            record.write({
                'name': n,
                'store_required_name_change': False
            })

    @api.multi
    def _search_content(self, operator, value):
        return [('history_head.content', operator, value)]

    @api.multi
    @api.depends('history_ids')
    def _compute_history_head(self):
        for rec in self:
            if rec.history_ids:
                rec.history_head = rec.history_ids[0]

    @api.multi
    def _create_history(self, vals):
        self.ensure_one()
        history = self.env['syllabus_minister.syllabus_history']
        _logger.warning("Creating History in Syllabus >>>>>>>>>> ")
        vals['syllabus_id'] = self.id
        return history.create(vals)


    # Groups Involved in Syllabus
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        syllabus = super(Syllabus, self).create(vals)
        if syllabus:
            if not syllabus.name:
                n = syllabus.get_name()
                syllabus.write({
                    'name': n
                })
        syllabus.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return syllabus

    # This function filters the syllabus record for the user of certain course.
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        domain = (domain or []) + ['|', ('course_id.faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
        return super(Syllabus, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
                                                     order=order)

    # Since each syllabus is defined for specific program in the university, 
    # so related program object is linked for each syllabus object
    program_id = fields.Many2one('syllabus_minister.program', string='Program',
    domain="['|', ('faculty_id.university_id.university_user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")

