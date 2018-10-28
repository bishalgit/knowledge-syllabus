# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Program(models.Model):
    _name = 'syllabus_minister.program'
    _inherit = 'mail.thread'
    _description = 'Program'

    name = fields.Char(string='Name')
    short_form = fields.Char(string='Short Form')
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
    courses_id = fields.Many2many('syllabus_minister.course',string='Course')
    total_credit = fields.Integer(string='Total Credit')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string='Faculty')
    courseline_ids = fields.One2many('syllabus_minister.courseline','program_id',string="Courseline")

    # Groups Involved in Program
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    #This constraints make fields unique
    _sql_constraints = [
         ('short_form_unique', 'unique(short_form)','Short Form must be unique')]

    @api.model
    def create(self, vals):
        program = super(Program, self).create(vals)
        program.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return program

    # This function filters the program record for the user of certain university.
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     domain = (domain or []) + ['|', ('faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
    #     return super(Program, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
    #                                                  order=order)
