# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courseline(models.Model):
    _name = 'syllabus_minister.courseline'
    _description = 'Course Line'
    _order =  'sequence, id'

    name = fields.Char(string='Name')
    semester = fields.Char(string='Semester')
    course_id = fields.Many2one('syllabus_minister.course', string='Related Course')
    sequence = fields.Integer(string='sequence',default=1)
    program_id = fields.Many2one('syllabus_minister.program',string="Program")
    syllabus_id = fields.Many2one('syllabus_minister.syllabus',string="Syllabus")