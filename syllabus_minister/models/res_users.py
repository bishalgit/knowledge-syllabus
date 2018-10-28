# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = "res.users"

    rpn = fields.Integer('RPN', help="This is the role priority number of the user.")
    # university_id = fields.Many2one('syllabus_minister.university', string='Related University')

    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     if args is None:
    #         args = []
    #     else:
    #         args = [('name', '=', self.env.user.university_id.name)]
    #         records = self.search(args, limit=limit)
    #     return [(record.id, record.display_name) for record in records]

