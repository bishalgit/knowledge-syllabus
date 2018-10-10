# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Package(models.Model):
    _name = 'syllabus_college.package'
    _inherit = 'mail.thread'
    _description = 'Package'

    name = fields.Char(string='Name')
    syllabus_ids = fields.One2many('syllabus_minister.syllabus','package_id',string='Syllabus')
    colleges_id = fields.Many2many('syllabus_college.college', string='Related College')