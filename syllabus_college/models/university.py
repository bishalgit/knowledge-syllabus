# -*- coding: utf-8 -*-

from odoo import models, fields, api


class University(models.Model):
    _inherit = 'syllabus_minister.university'

    user_ids = fields.One2many('res.users', 'university_id', string="Related University User")

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        else:
            args = ['|', ('name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
            records = self.search(args, limit=limit)
        return [(record.id, record.display_name) for record in records]
