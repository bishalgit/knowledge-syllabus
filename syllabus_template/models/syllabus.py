# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class Syllabus(models.Model):
    _inherit = 'syllabus_minister.syllabus'

    template_id = fields.Many2one('ir.ui.view', string="Template")

    @api.multi
    def onCreateButtonClicked(self):
        for record in self:
            if record.template_id:
                record.write({
                    "content": record.env['ir.ui.view'].render_template(record.template_id.id, {object: record})
                })
            else:
                raise UserError("Please select a template to render the syllabus.")
