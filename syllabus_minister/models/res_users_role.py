# Copyright 2014 ABF OSIELL <http://osiell.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResUsersRole(models.Model):
    _inherit = 'res.users.role'

    rpn = fields.Integer('RPN', help="This is the role priority number of the role.")

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        _logger.warning("User ID " + str(self.env.user.rpn))
        domain = (domain or []) + [('rpn', '<', self.env.user.rpn)]
        return super(ResUsersRole, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
