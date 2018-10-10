# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'syllabus_minister.course'
    _inherit = 'mail.thread'
    _description = 'Course'

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
    faculty_id = fields.Many2one('syllabus_minister.faculty',string='Faculty',
    domain="['|', ('university_id.university_user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")

    # program_id = fields.Many2one('syllabus_minister.program',string='Program',
    # domain="['|', ('faculty_id.university_id.university_user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")

    # Groups Involved in Course
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        course = super(Course, self).create(vals)
        course.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return course
    
    # This function filters the course record for the user of certain university.
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        domain = (domain or []) + ['|', ('faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
        return super(Course, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
                                                     order=order)
