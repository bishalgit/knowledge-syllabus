# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Syllabus(models.Model):
    _inherit = 'syllabus_minister.syllabus'

    package_id = fields.Many2one('syllabus_college.package',string='Syllabus Package')