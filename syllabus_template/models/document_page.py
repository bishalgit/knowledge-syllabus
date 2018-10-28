# -*- coding: utf-8 -*-
import inflect
from odoo import models, fields, api
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)


class DocumentPage(models.Model):

    _inherit = 'document.page'
    _description = 'Syllabus'
    
    syllabus_template_id = fields.Many2one('ir.ui.view', string="Template")
    temp_content = fields.Html("Temporary content")

    @api.multi
    def onCreateButtonClicked(self):
        for record in self:
            if record.syllabus_template_id:
                record.write({
                    "temp_content": record.env['ir.ui.view'].render_template(record.syllabus_template_id.id, {'object': record})
                })
                return {'type': 'ir.actions.act_window', 'res_model': 'syllabus.display', 'view_type': 'form', 'view_mode': 'form', 'target': 'new', 'name': 'Syllabus Display'}
            else:
                raise UserError("Please select a template to render the syllabus.")