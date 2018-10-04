# -*- coding: utf-8 -*-

from odoo import models, fields, api


class View(models.Model):
    _inherit = 'ir.ui.view'

    syllabus_template = fields.Boolean(string="Syllabus", default=False, help="This boolean value indicates if this view should be used to render a syllabus.")
    image = fields.Binary(string="Image", help="Image to represent the view.")
