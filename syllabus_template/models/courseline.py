# -*- coding: utf-8 -*-
import inflect
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class Courseline(models.Model):
    _inherit = 'syllabus_minister.courseline'

    # Semester prefixing
    semester_prefix = fields.Char("Semester Prefix")
    semester_sufix = fields.Char("Semester Sufix")

    @api.model
    def create(self, vals):
        response = super(Courseline, self).create(vals)
        if response:
            if 'semester' in vals:
                try:
                    p = inflect.engine()
                    s = p.ordinal(int(vals['semester']))
                    response.semester_sufix = s[-2:]
                    response.semester_prefix = s[:-2]
                except Exception:
                    response.semester_sufix = "undefined"
                    response.semester_prefix = "undefined"
        return response
    
    @api.multi
    def write(self, vals):
        response = super(Courseline, self).write(vals)
        if response:
            if 'semester' in vals:
                try:
                    p = inflect.engine()
                    s = p.ordinal(int(vals['semester']))
                    self.semester_sufix = s[-2:]
                    self.semester_prefix = s[:-2]
                except Exception:
                    self.semester_sufix = "undefined"
                    self.semester_prefix = "undefined"
        return response
