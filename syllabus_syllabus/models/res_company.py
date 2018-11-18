# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import os
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError


class Company(models.Model):
    _inherit = "res.company"
    
    # watermark for syllabus print file
    watermark_logo = fields.Binary(string="Watermark")

    # check if the syllabus required watermark logo of the university
    require_watermark = fields.Boolean("Require Watermark of the University?", default=False)

