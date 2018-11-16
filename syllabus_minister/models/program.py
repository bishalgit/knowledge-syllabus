# -*- coding: utf-8 -*-
from datetime import datetime,date
from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class Program(models.Model):
    _name = 'syllabus_minister.program'
    _inherit = 'mail.thread'
    _description = 'Program'

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
    # courses_id = fields.Many2many('syllabus_minister.course',string='Course')
    year = fields.Selection([(num, str(num)) for num in range(2000, (datetime.now().year)+5 )], 'Batch Year')
    related_course = fields.Many2one(related='courseline_ids.course_id', string="Course")
    related_syllabus = fields.Many2one(related='courseline_ids.syllabus_id', string="Syllabus")
    total_credit = fields.Integer(string='Total Credit')
    faculty_id = fields.Many2one('syllabus_minister.faculty',string='Faculty')
    courseline_ids = fields.One2many('syllabus_minister.courseline','program_id',string="Courseline")
    total_foundation_cr_hr = fields.Integer(compute='_compute_foundation')
    total_core_cr_hr = fields.Integer(compute='_compute_core')
    total_concentration_cr_hr = fields.Integer(compute='_compute_concentration')
    total_elective_cr_hr = fields.Integer(compute='_compute_elective')
    total_project_cr_hr = fields.Integer(compute='_compute_project')
    total_sem1_cr_hr = fields.Integer(compute='_compute_sem1')
    total_sem2_cr_hr = fields.Integer(compute='_compute_sem2')
    total_sem3_cr_hr = fields.Integer(compute='_compute_sem3')
    total_sem4_cr_hr = fields.Integer(compute='_compute_sem4')
    total_sem5_cr_hr = fields.Integer(compute='_compute_sem5')
    total_sem6_cr_hr = fields.Integer(compute='_compute_sem6')
    total_sem7_cr_hr = fields.Integer(compute='_compute_sem7')
    total_sem8_cr_hr = fields.Integer(compute='_compute_sem8')

    # Groups Involved in Program
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    #This constraints make fields unique
    _sql_constraints = [
         ('short_form_unique', 'unique(short_form)','Short Form must be unique')]

    @api.multi
    def _compute_foundation(self):
        for record in self:
            for r in record.courseline_ids:
                if r.course_id.course_type == "Foundation":
                    record.total_foundation_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_core(self):
        for record in self:
            for r in record.courseline_ids:
                if r.course_id.course_type == "Core":
                    record.total_core_cr_hr += r.course_id.credit_hours  

    @api.multi
    def _compute_concentration(self):
        for record in self:
            for r in record.courseline_ids:
                if r.course_id.course_type == "Concentration":
                    record.total_concentration_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_elective(self):
        for record in self:
            for r in record.courseline_ids:
                if r.course_id.course_type == "Elective":
                    record.total_elective_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_project(self):
        for record in self:
            for r in record.courseline_ids:
                if r.course_id.course_type == "Project Work and Internship":
                    record.total_project_cr_hr += r.course_id.credit_hours


    @api.multi
    def _compute_sem1(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 1:
                    record.total_sem1_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_sem2(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 2:
                    record.total_sem2_cr_hr += r.course_id.credit_hours  

    @api.multi
    def _compute_sem3(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 3:
                    record.total_sem3_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_sem4(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 4:
                    record.total_sem4_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_sem5(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 5:
                    record.total_sem5_cr_hr += r.course_id.credit_hours

    @api.multi
    def _compute_sem6(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 6:
                    record.total_sem6_cr_hr += r.course_id.credit_hours  

    @api.multi
    def _compute_sem7(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 7:
                    record.total_sem7_cr_hr += r.course_id.credit_hours
    @api.multi
    def _compute_sem8(self):
        for record in self:
            for r in record.courseline_ids:
                if r.semester == 8:
                    record.total_sem8_cr_hr += r.course_id.credit_hours

    @api.model
    def create(self, vals):
        program = super(Program, self).create(vals)
        program.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return program

    # create program history if new batch year
    @api.onchange("year")
    def create_program_history(self):
        program_old_version = self.env['syllabus_minister.program_old_version']
        if not program_old_version.search_count([('year', '=', self.year)]):
            old_version = program_old_version.create({
                'name': self.name,
                'short_form': self.short_form,
                'level': self.level,
                'objectives': self.objectives,
                'curricular_structure': self.curricular_structure,
                'features': self.features,
                'semester_system': self.semester_system,
                'eligibility': self.eligibility,
                'documents_required': self.documents_required,
                'admission_procedures': self.admission_procedures,
                'academic_schedule': self.academic_schedule,
                'course_registration': self.course_registration,
                'additional_withdrawal_course': self.additional_withdrawal_course,
                'attendance_requirements': self.attendance_requirements,
                'study_duration': self.study_duration,
                'normal_study_duration': self.normal_study_duration,
                'max_study_duration': self.max_study_duration,
                'min_credit_fulltime_student': self.min_credit_fulltime_student,
                'evaluation_system': self.evaluation_system,
                'evaluation_elective_concentration_courses': self.evaluation_elective_concentration_courses,
                'grading_system': self.grading_system,
                'repeating_course': self.repeating_course,
                'credit_transfer_withdrawal': self.credit_transfer_withdrawal,
                'project_work': self.project_work,
                'internship': self.internship,
                'unfair_means': self.unfair_means,
                'provision_retotaling_rechecking': self.provision_retotaling_rechecking,
                'dismissal_from_program': self.dismissal_from_program,
                'degree_requirements': self.degree_requirements,
                'deanslist': self.deanslist,
                'year': self.year,
                'related_course': self.related_course,
                'related_syllabus': self.related_syllabus,
                'total_credit': self.total_credit,
                'faculty_id': self.faculty_id.id,
                'total_foundation_cr_hr': self.total_foundation_cr_hr,
                'total_core_cr_hr': self.total_core_cr_hr,
                'total_concentration_cr_hr': self.total_concentration_cr_hr,
                'total_elective_cr_hr': self.total_elective_cr_hr,
                'total_project_cr_hr': self.total_project_cr_hr,
                'total_sem1_cr_hr': self.total_sem1_cr_hr,
                'total_sem2_cr_hr': self.total_sem2_cr_hr,
                'total_sem3_cr_hr': self.total_sem3_cr_hr,
                'total_sem4_cr_hr': self.total_sem4_cr_hr,
                'total_sem5_cr_hr': self.total_sem5_cr_hr,
                'total_sem6_cr_hr': self.total_sem6_cr_hr,
                'total_sem7_cr_hr': self.total_sem7_cr_hr,
                'total_sem8_cr_hr': self.total_sem8_cr_hr,
                'program_id': self._origin.id
            })
            if old_version:
                for courseline in self.courseline_ids:
                    old_version.write({
                        'courseline_ids': [(4, courseline.id, 0)]
                    })
    
    # button function for view program old versions
    @api.multi
    def program_history_tree_view(self):
        form_view = self.env.ref('syllabus_minister.program_old_version_view_form')
        tree_view = self.env.ref('syllabus_minister.program_old_version_view_tree')
        self.ensure_one()
        domain = [('program_id', '=', self.id)]
        return {
            'name': _('Program Old Versions'),
            'res_model': 'syllabus_minister.program_old_version',
            'type': 'ir.actions.act_window',
            'domain': domain,
            'views': [[tree_view.id, 'list'], [form_view.id, 'form']],
            # 'view_id': False,
            'view_mode': 'tree, form',
            # 'view_type': 'form',
            'limit': 80,
            'context': "{'default_res_model': '%s','default_res_id': %d, 'create': False, 'edit': False}" % (self._name, self.id)
        }
