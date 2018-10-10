# -*- coding: utf-8 -*-

from odoo import models, fields, api


class College(models.Model):
    _name = 'syllabus_college.college'
    _inherit = 'mail.thread'
    _description = 'College'

    name = fields.Char(string='Name')
    packages_id = fields.Many2many('syllabus_college.package', string='Packages')


    university_id = fields.Many2one('syllabus_minister.university', string='University', domain="['|', ('user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")

    # Groups Involved in College
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        college = super(College, self).create(vals)
        college.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id),
                          (4, self.env.ref('syllabus_minister.syllabus_minister_group_university').id)]
        })
        return college