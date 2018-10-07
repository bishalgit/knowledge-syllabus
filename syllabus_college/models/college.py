# -*- coding: utf-8 -*-

from odoo import models, fields, api


class College(models.Model):
    _name = 'syllabus_college.college'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
