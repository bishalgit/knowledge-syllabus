# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Syllabus(models.Model):
    _name = 'syllabus_minister.syllabus'
    _inherit = 'mail.thread'

    name = fields.Char('Name')
    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    content = fields.Html(
        "Content",
        compute='_compute_content',
        inverse='_inverse_content',
        search='_search_content',
        required=True,
    )

    # no-op computed field
    summary = fields.Char(
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

    def get_name(self):
        for record in self:
            n = ""
            if record.course_id:
                n = n + record.course_id.course_code
                if record.course_id.program_id:
                    n = n + " / " + record.course_id.program_id.name
                    if record.course_id.program_id.faculty_id:
                        n = n + " / " + record.course_id.program_id.faculty_id.name
            return n

    def _compute_required_name_change(self):
        for record in self:
            n = record.get_name()
            if n != record.name:
                record.required_name_change = True
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
                'required_name_change': False
            })

    @api.multi
    def _search_content(self, operator, value):
        return [('history_head.content', operator, value)]

    @api.model
    def create(self, vals):
        syllabus = super(Syllabus, self).create(vals)
        if syllabus:
            if not syllabus.name:
                n = syllabus.get_name()
                syllabus.write({
                    'name': n
                })
        return syllabus

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
        vals['syllabus_id'] = self.id
        return history.create(vals)
