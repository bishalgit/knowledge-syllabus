# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Unit(models.Model):
    _name = 'syllabus_minister.unit'
    _inherit = 'mail.thread'
    _description = 'Unit'
    _order = 'sequence,id'

    name = fields.Char(string='Name')
    study_hours = fields.Integer(string='Study hours')
    description = fields.Html(string='Description')
    course_id = fields.Many2one('syllabus_minister.course',string='Course',domain="[('group_ids.users.id', '=', uid)]")
    sequence = fields.Integer(string='sequence',default=1)
    display_name = fields.Char(string='Display Name', compute='_display_name')

    @api.depends('name','course_id')
    def _display_name(self):
        for r in self:
            r.display_name = str(r.course_id.name) + ", " + str(r.name)

    # Groups Involved in Unit
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        unit = super(Unit, self).create(vals)
        unit.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return unit
    
    # This function filters the unit record for the user of certain course.
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     domain = (domain or []) + ['|', ('course_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
    #     return super(Unit, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
    #                                                  order=order)
