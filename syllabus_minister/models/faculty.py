# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Faculty(models.Model):
    _name = 'syllabus_minister.faculty'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
    introduction = fields.Html(string='Introduction')
    vision = fields.Html(string='Vision')
    mission = fields.Html(string='Mission')
    goals = fields.Html(string='Goals and Objectives')
    characteristics = fields.Html(string='Characterstics')
    program_ids = fields.One2many('syllabus_minister.program','faculty_id',string='Program')
    university_id = fields.Many2one('syllabus_minister.university',string='University')

    # Groups Involved in Faculty
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        faculty = super(Faculty, self).create(vals)
        faculty.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return faculty

