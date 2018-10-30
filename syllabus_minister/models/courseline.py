# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courseline(models.Model):
    _name = 'syllabus_minister.courseline'
    _description = 'Course Line'
    _order =  'sequence, id'

    name = fields.Char(string='Name')
    semester = fields.Integer(string='Semester')
    course_id = fields.Many2one('syllabus_minister.course', string='Related Course')
    sequence = fields.Integer(string='sequence',default=1)
    program_id = fields.Many2one('syllabus_minister.program',string="Program")
    syllabus_id = fields.Many2one('document.page',string="Syllabus", 
    domain="[('type', '=', 'content')]")

    # Groups Involved in Courseline
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        courseline = super(Courseline, self).create(vals)
        courseline.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return courseline


