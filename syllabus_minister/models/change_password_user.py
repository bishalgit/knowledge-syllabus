# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import _, api, exceptions, fields, models, modules
from odoo.exceptions import AccessDenied, AccessError, UserError, ValidationError


_logger = logging.getLogger(__name__)

class SyllabusMinisterChangePasswordUser(models.TransientModel):
    """ A model to configure users in the change password wizard. """
    _name = 'syllabus_minister.change.password.user'
    _description = 'Syllabus Minister Change Password Wizard User'

    wizard_id = fields.Many2one('syllabus_minister.change.password.wizard', string='Wizard', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade')
    user_login = fields.Char(string='User Login', readonly=True)
    new_passwd = fields.Char(string='New Password', default='')

    @api.multi
    def change_password_button(self):
        for record in self:
            if not record.new_passwd:
                raise UserError(_("Before clicking on 'Change Password', you have to write a new password."))
            record.user_id.write({'password': record.new_passwd})
            _logger.warning('Related User: ' + str(record.user_id))
            _logger.warning('New Password: ' + str(record.new_passwd))
            _logger.warning('User Name: ' + str(record.user_id.name))
            _logger.warning('Password: ' + str(record.user_id.password))
        # don't keep temporary passwords in the database longer than necessary
        self.write({'new_passwd': False})
        _logger.warning('Password After Set: ' + str(record.user_id.password))
