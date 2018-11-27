# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CourseType(models.Model):
    _name = 'syllabus_minister.course_type'
    _inherit = 'mail.thread'

    name = fields.Char(string='Course Type')
    course_ids = fields.One2many('syllabus_minister.course','course_type', string="Course")
    total_cr_hr = fields.Integer(_compute='_compute_cr_hr',store=True)

    def _compute_cr_hr(self):
        tc = 0
        for record in self:
            for r in record.course_ids:
                tc += r.credit_hours
                _logger.warning('TC' + str(tc))
                _logger.warning('TCcccccccccccccccccccc' + str(r.credit_hours))
            record.total_cr_hr = tc