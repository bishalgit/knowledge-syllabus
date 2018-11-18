# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class Program(models.Model):
    _inherit = 'syllabus_minister.program'

    # check if the syllabus required watermark logo of the university
    require_watermark = fields.Boolean("Require Watermark of the University?", default=False)

    @api.onchange('require_watermark')
    def _toggle_watermark_bool(self):
        universities = self.env['res.company'].search([])

        for university in universities:
            if self.require_watermark:
                university.write({
                    'require_watermark': True
                })
            else:
                university.write({
                    'require_watermark': False
                })