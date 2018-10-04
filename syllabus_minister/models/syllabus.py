# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Syllabus(models.Model):
    _name = 'syllabus_minister.syllabus'
    _inherit = 'mail.thread'

    name = fields.Char('Name')
    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    content = fields.Html('Content')

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

    @api.onchange("parent_id")
    def _onchange_parent_id(self):
        """We Set it the right content to the new parent."""
        if not self.content or self.content == '<p><br></p>':
            if self.parent_id and self.parent_id.type == "category":
                    self.content = self.parent_id.template
