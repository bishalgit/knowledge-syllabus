# -*- coding: utf-8 -*-

import logging
import uuid

from odoo import models, fields, api
from odoo.exceptions import UserError
from werkzeug.urls import url_join
_logger = logging.getLogger(__name__)


class DocumentPage(models.Model):

    _inherit = 'document.page'

    @api.multi
    def _default_access_token(self):
        return str(uuid.uuid4())

    @api.multi
    def _compute_share_link(self):
        for record in self:
            record.share_link = url_join(self.env['ir.config_parameter'].sudo().get_param('web.base.url'), 'share/syllabus/%s/%s' % (record.id, record.access_token))

    access_token = fields.Char('Security Token', required=True, default=_default_access_token, readonly=True)
    share_link = fields.Char(string="Shareable link", compute=_compute_share_link)

    @api.multi
    def onShareButtonClicked(self):
        for record in self:
            return {'type': 'ir.actions.act_window', 'res_model': 'syllabus_share.display', 'view_type': 'form', 'view_mode': 'form', 'target': 'new', 'name': 'Syllabus Share'}
