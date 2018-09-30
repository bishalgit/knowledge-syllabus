# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Unit(models.Model):
    _name = 'syllabus_minister.unit'

    name = fields.Char(string='Name')
    study_hours = fields.Integer(string='Study hours')
    description = fields.Html(string='Description')
    course_id = fields.Many2one('syllabus_minister.course',string='Course')