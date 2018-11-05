# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = "res.users"

    rpn = fields.Integer(string='RPN', help="This is the role priority number of the user.", store=True)

    @api.onchange('name')
    def _compute_rpn(self):
        if self.env.uid != 1:
            self.rpn = 1
