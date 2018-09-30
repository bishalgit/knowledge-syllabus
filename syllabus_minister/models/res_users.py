# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = "res.users"

    rpn = fields.Integer('RPN', help="This is the role priority number of the user.")

    @api.model
    def create(self, vals):
        user = super(ResUsers, self).create(vals)
        _logger.warning("User ID " + str(user.id))
        _logger.warning("User Role Name " + str(user.role_ids))
        
        # to assure that the user creator in from university group
        if not self.env.user.id == 1:
            user.write({
                'rpn': 1
            })
        return user

