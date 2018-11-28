# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class CourseType(models.Model):
    _name = 'syllabus_minister.course_type'
    _inherit = 'mail.thread'
    _order = 'sequence asc'

    name = fields.Char(string='Name')
    course_ids = fields.One2many('syllabus_minister.course','course_type', string="Course")

    
    description = fields.Html(string="Description")
    parent_type = fields.Many2one('syllabus_minister.course_type',
                                       string="Parent Course Type",
                                       ondelete="cascade")
    child_types = fields.One2many('syllabus_minister.course_type', 'parent_type', string="Sub Course Types")
    sequence = fields.Integer('Sequence')

    @api.multi
    def name_get(self):
        name_array = []
        for record in self:
            if record.parent_type:
                name_array.append((record.id, "%s / %s" % (record.parent_type.name, record.name)))
            else:
                name_array.append((record.id, record.name))
        return name_array

    # calulate toal credit of the courses of certain course type
    @api.multi
    def calculate_total_credit(self, courses):
        for rec in self:
            tc = 0
            if rec.child_types:
                for child_type in rec.child_types:
                    tc += child_type.calculate_total_credit(courses)
            elif rec.course_ids:
                for course in rec.course_ids:
                    if course.id in courses:
                        tc += course.credit_hours
            else:
                tc = 0
            return tc

    # this method returns the parent id of the course type
    @api.multi
    def get_parent_course_type(self):
        for rec in self:
            ct_list = []
            ct_list.append(rec.id)
            if rec.parent_type:
                ct_list += rec.parent_type.get_parent_course_type()
            return ct_list
