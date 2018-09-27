# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Program(models.Model):
    _name = 'syllabus_minister.program'

    name = fields.Char(string='Name')
    objectives = fields.Text(string='Objectives')
    curricular_structure = fields.Text(string='Curricular Structure')
    features = fields.Text(string='Features')
    semester_system = fields.Text(string='Semester System')
    eligibility = fields.Text(string='Eligibility')
    document_required = fields.Text(string='Document Required')
    admission_procedures = fields.Text(string='Admission Procedures')
    academic_schedule = fields.Text(string='Academic Schedule')
    course_registration = fields.Text(string='Course Registration')
    additional_withdrawal_course = fields.Text(string='Additional Withdrawal Course')
    attendance_requirement = fields.Text(string='Attendance Requirement')
    normal_study_duration = fields.Char(string='Normal Study Duration')
    max_study_duration = fields.Char(string='Maximum Study Duration')
    min_credit_fulltime_student = fields.Integer(string='Minimum no. of credits for full time student')
    evaluation_system = fields.Html(string='Evaluation System')
    evaluation_elective_concentration_courses = fields.Text(string='Evaluation of elective and concentration courses')
    grading_system = fields.Html(string='Grading System')
    repeating_course = fields.Text(string='Repeating Course')
    credit_transfer_withdrawal = fields.Text(string='Credit Transfer and withdrawal')
    project_work = fields.Text(string='Project Work')
    internship = fields.Text(string='Internship')
    unfair_means = fields.Html(string='Unfair Means')
    provision_retotaling_rechecking = fields.Text(string='Provision for retotaling and rechecking')
    dismissal_from_program = fields.Html(string='Dismissal from the program')
    degree_requirement = fields.Html(string='Degree Requirement')
    deanslist = fields.Text(string='Distinction and deans list')
    course_ids = fields.One2many('syllabus_minister.course','program_id',string='Course')
    total_credit = fields.Integer(string='Total Credit')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string='Faculty')