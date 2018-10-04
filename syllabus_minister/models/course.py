# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'syllabus_minister.course'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Html(string='Course Description')
    course_objectives = fields.Html(string='Course Objectives')
    credit_hours = fields.Integer(string='Credit Hours')
    general_course_objectives = fields.Html(string='General Course Objectives')
    specific_course_objectives = fields.Html(string='Specific Course Objectives')
    course_content_areas = fields.Html(string='Course Content Areas')
    unit_ids = fields.One2many('syllabus_minister.unit','course_id',string='Course Contents')
    course_content_nonunits = fields.Html(string='Course content(Non units)')
    teaching_method = fields.Html(string='Teaching Methods')
    course_outcomes = fields.Html(string='Course Outcomes')
    basic_text = fields.Html(string='Basic Texts')
    references = fields.Html(string='References')
    is_elective = fields.Boolean(string='Is elective?')
    semester = fields.Char(string='Semester')
    program_id = fields.Many2one('syllabus_minister.program',string='Program')