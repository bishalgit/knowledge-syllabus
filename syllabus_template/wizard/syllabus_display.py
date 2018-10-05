# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SyllabusDisplay(models.TransientModel):
    _name = "syllabus.display"
    _description = "Syllabus display wizard"

    def _get_default_syllabus(self):
        return self.env['syllabus_minister.syllabus'].browse(self._context.get('active_ids'))[0]

    def _get_temp_syllabus(self):
        return self.env['syllabus_minister.syllabus'].browse(self._context.get('active_ids'))[0].temp_content

    syllabus_id = fields.Many2one("syllabus_minister.syllabus", string="Syllabus", default=_get_default_syllabus)
    temp_syllabus = fields.Html(string="Temporary syllabus", default=_get_temp_syllabus)

    @api.multi
    def saveSyllabus(self):
        for record in self:
            record.syllabus_id.write({
                'content': record.temp_syllabus
            })
        return {'type': 'ir.actions.act_window_close'}
