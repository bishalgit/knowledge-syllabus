# -*- coding: utf-8 -*-

from odoo import models, fields, api


class University(models.Model):
    _name = 'syllabus_minister.university'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
    faculty_ids = fields.One2many('syllabus_minister.faculty','university_id', string='Faculty')

    # Related University User
    university_user_ids = fields.One2many('res.users', 'university_id', string="Related University User")

    # Groups Involved in University
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        university = super(University, self).create(vals)
        university.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return university
