# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Syllabus(models.Model):
    _inherit = 'syllabus_minister.syllabus'

    template_id = fields.Many2one('ir.ui.view', string="Template")
    temp_content = fields.Html("Temporary content")

    @api.multi
    def onCreateButtonClicked(self):
        for record in self:
            if record.template_id:
                record.write({
                    "temp_content": record.env['ir.ui.view'].render_template(record.template_id.id, {object: record})
                })
                return {'type': 'ir.actions.act_window', 'res_model': 'syllabus.display', 'view_type': 'form', 'view_mode': 'form', 'target': 'new', 'name': 'Syllabus Display'}
            else:
                raise UserError("Please select a template to render the syllabus.")
