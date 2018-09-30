# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    rpn = fields.Integer('RPN', help="This is the role priority number of the user.")
