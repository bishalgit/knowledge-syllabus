# -*- coding: utf-8 -*-

from odoo import models, fields, api


class University(models.Model):
    _name = 'syllabus_minister.university'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
    faculty_ids = fields.One2many('syllabus_minister.faculty','university_id', string='Faculty')