# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)


class ProgramOldVersion(models.Model):
    _name = 'syllabus_minister.program_old_version'
    _inherit = 'mail.thread'
    _description = 'Program History'

    name = fields.Char(string='Name')
    short_form = fields.Char(string='Short Form', required='True')
    level = fields.Selection([('Bachelor','Bachelor'),('Master','Master'),('Phd','Phd')],string="Level")
    objectives = fields.Html(string='Objectives')
    curricular_structure = fields.Html(string='Curricular Structure')
    features = fields.Html(string='Features')
    semester_system = fields.Html(string='Semester System')
    eligibility = fields.Html(string='Eligibility')
    documents_required = fields.Html(string='Document Required')
    admission_procedures = fields.Html(string='Admission Procedures')
    academic_schedule = fields.Html(string='Academic Schedule')
    course_registration = fields.Html(string='Course Registration')
    additional_withdrawal_course = fields.Html(string='Additional Withdrawal Course')
    attendance_requirements = fields.Html(string='Attendance Requirements')
    study_duration = fields.Html(string='Normal and Maximum Duration of Study')
    normal_study_duration = fields.Char(string='Normal Study Duration')
    max_study_duration = fields.Char(string='Maximum Study Duration')
    min_credit_fulltime_student = fields.Integer(string='Minimum no. of credits for full time student')
    evaluation_system = fields.Html(string='Evaluation System')
    evaluation_elective_concentration_courses = fields.Html(string='Evaluation of elective and concentration courses')
    grading_system = fields.Html(string='Grading System')
    repeating_course = fields.Html(string='Repeating Course')
    credit_transfer_withdrawal = fields.Html(string='Credit Transfer and withdrawal')
    project_work = fields.Html(string='Project Work')
    internship = fields.Html(string='Internship')
    unfair_means = fields.Html(string='Unfair Means')
    provision_retotaling_rechecking = fields.Html(string='Provision for retotaling and rechecking')
    dismissal_from_program = fields.Html(string='Dismissal from the program')
    degree_requirements = fields.Html(string='Degree Requirement')
    deanslist = fields.Html(string='Distinction and deans list')
    year = fields.Selection([(num, str(num)) for num in range(2000, (datetime.now().year)+5 )], 'Batch Year')
    related_course = fields.Many2one(related='courseline_ids.course_id', string="Course")
    related_syllabus = fields.Many2one(related='courseline_ids.syllabus_id', string="Syllabus")
    total_credit = fields.Integer(string='Total Credit')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string='Faculty')
    courseline_ids = fields.One2many('syllabus_minister.courseline','old_program_id',string="Courseline", store=True)
    course_type_ids = fields.Many2many('syllabus_minister.course_type', 'syllabus_coursetype_program_old', string="Course Type", readonly=True)
    semester_id = fields.Many2many('syllabus_minister.semester', 'syllabus_semester_program_old', string="Semester", readonly=True)


    program_id = fields.Many2one('syllabus_minister.program', 'Program')

    # Groups Involved in Program
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        program_old_version = super(ProgramOldVersion, self).create(vals)
        program_old_version.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return program_old_version

    # this computes the total credit of the certain course types under this program
    # this method is called from the report template
    def _compute_course_types_total_credit(self, course_type_id):
        total_credit = 0
        for courseline in self.courseline_ids:
            if int(courseline.course_id.course_type.id) == int(course_type_id):
                total_credit += int(courseline.course_id.credit_hours)
        return total_credit

