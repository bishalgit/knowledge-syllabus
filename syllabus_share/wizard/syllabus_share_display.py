# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SyllabusShareDisplay(models.TransientModel):
    _name = "syllabus_share.display"
    _description = "Syllabus Share display wizard"

    def _get_share_link(self):
        return self.env['document.page'].browse(self._context.get('active_ids'))[0].share_link

    share_link = fields.Char(string="Shareable link", default=_get_share_link)
