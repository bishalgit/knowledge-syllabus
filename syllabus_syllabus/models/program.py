# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class Program(models.Model):
    _inherit = 'syllabus_minister.program'

    # check if the syllabus required watermark logo of the university
    require_watermark = fields.Boolean("Require Watermark of the University?", default=False)

    @api.multi
    def write(self, vals):
        program = super(Program, self).write(vals)
        universities = self.env['res.company'].search([])
        if "require_watermark" in vals:
            for university in universities:
                university.write({
                    'require_watermark': vals['require_watermark']
                })
        else:
            for university in universities:
                university.write({
                    'require_watermark': self.require_watermark
                })
        return program
