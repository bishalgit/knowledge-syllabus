# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CourseType(models.Model):
    _name = 'syllabus_minister.course_type'
    _inherit = 'mail.thread'

    name = fields.Char(string='Course Type')