# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Syllabus(models.Model):
    _name = 'syllabus_minister.syllabus'
    _inherit = 'mail.thread'

    name = fields.Char('Name')
    course_id = fields.Many2one('syllabus_minister.course',string='Courses')
    content = fields.Html('Content')