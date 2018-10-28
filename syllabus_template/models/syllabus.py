# -*- coding: utf-8 -*-
import inflect
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class Syllabus(models.Model):
    _inherit = 'syllabus_minister.syllabus'

     = fields.Many2one('ir.ui.view', string="Template")
    temp_content = fields.Html("Temporary content")

    @api.multi
    def onCreateButtonClicked(self):
        for record in self:
            if record.:
                record.write({
                    "temp_content": record.env['ir.ui.view'].render_template(record..id, {'object': record})
                })
                return {'type': 'ir.actions.act_window', 'res_model': 'syllabus.display', 'view_type': 'form', 'view_mode': 'form', 'target': 'new', 'name': 'Syllabus Display'}
            else:
                raise UserError("Please select a template to render the syllabus.")

    # # Semester prefixing
    # semester_prefix = fields.Char("Semester Prefix")
    # semester_sufix = fields.Char("Semester Sufix")

    # @api.model
    # def create(self, vals):
    #     response = super(Syllabus, self).create(vals)
    #     if response:
    #         if 'semester' in vals:
    #             try:
    #                 p = inflect.engine()
    #                 s = p.ordinal(int(vals['semester']))
    #                 response.semester_sufix = s[-2:]
    #                 response.semester_prefix = s[:-2]
    #             except Exception:
    #                 response.semester_sufix = "undefined"
    #                 response.semester_prefix = "undefined"
    #     return response
    
    # @api.multi
    # def write(self, vals):
    #     response = super(Syllabus, self).write(vals)
    #     if response:
    #         if 'semester' in vals:
    #             try:
    #                 p = inflect.engine()
    #                 s = p.ordinal(int(vals['semester']))
    #                 self.semester_sufix = s[-2:]
    #                 self.semester_prefix = s[:-2]
    #             except Exception:
    #                 self.semester_sufix = "undefined"
    #                 self.semester_prefix = "undefined"
    #     return response
