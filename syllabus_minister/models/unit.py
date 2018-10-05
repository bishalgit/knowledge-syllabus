# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Unit(models.Model):
    _name = 'syllabus_minister.unit'
    _inherit = 'mail.thread'
    _order = 'sequence,id'

    name = fields.Char(string='Name')
    study_hours = fields.Integer(string='Study hours')
    description = fields.Html(string='Description')
    course_id = fields.Many2one('syllabus_minister.course',string='Course')
    sequence = fields.Integer(string='sequence',default=1)