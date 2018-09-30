# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import _, api, exceptions, fields, models, modules
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError


_logger = logging.getLogger(__name__)


class SyllabusMinisterChangePasswordWizard(models.TransientModel):
    """ A wizard to manage the change of users' passwords. """
    _name = "syllabus_minister.change.password.wizard"
    _description = "Change Password Wizard"

    def _default_user_ids(self):
        user_ids = self._context.get('active_model') == 'res.users.role.line' and self._context.get('active_ids') or []
        return [
            (0, 0, {'user_id': record.user_id.id, 'user_login': record.user_id.login})
            for record in self.env['res.users.role.line'].browse(user_ids)
        ]

    user_ids = fields.One2many('syllabus_minister.change.password.user', 'wizard_id', string=' Syllabus Minister Users', default=_default_user_ids)

    @api.multi
    def change_password_button(self):
        self.ensure_one()
        self.user_ids.change_password_button()
        if self.env.user in self.mapped('user_ids.user_id'):
            return {'type': 'ir.actions.client', 'tag': 'reload'}
        return {'type': 'ir.actions.act_window_close'}
