from odoo import api, fields, models, _

import logging

_logger = logging.getLogger(__name__)


class DocumentPage(models.Model):

    _inherit = 'document.page'
    _description = 'Syllabus'

    resource_calendar_id = fields.Many2one(
        'resource.calendar', string='Working Time',
        default=lambda self: self.env.user.company_id.resource_calendar_id.id,
        help="Timetable working hours to adjust the gantt diagram report")