# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CourseType(models.Model):
    _name = 'syllabus_minister.course_type'
    _inherit = 'mail.thread'

    name = fields.Char(string='Course Type')
    course_ids = fields.One2many('syllabus_minister.course','course_type', string="Course")
