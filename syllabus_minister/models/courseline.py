# -*- coding: utf-8 -*-
from datetime import datetime,date

from odoo import models, fields, api

import logging

_logger = logging.getLogger(__name__)



class Courseline(models.Model):
    _name = 'syllabus_minister.courseline'
    _description = 'Course Line'
    _order =  'sequence, id'

    name = fields.Char(string='Name')
    semester = fields.Integer(string='Semester', default=1)
    course_id = fields.Many2one('syllabus_minister.course', string='Course')
    sequence = fields.Integer(string='sequence',default=1)
    program_id = fields.Many2one('syllabus_minister.program',string="Program")
    related_faculty = fields.Many2one(related="program_id.faculty_id",string="Faculty", store=True)
    syllabus_id = fields.Many2one('document.page.history',string="Syllabus", domain="[('final_draft', '=', True)]")
    # syllabus_version = fields.Integer(related="syllabus_id.syllabus_version", string='Syllabus Version', store=True)
    # year = fields.Datetime('Year')
    issued_year = fields.Selection([(num, str(num)) for num in range(2000, (datetime.now().year)+5 )], 'Issued Year')


    # Groups Involved in Courseline
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        courseline = super(Courseline, self).create(vals)
        courseline.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return courseline

    # get syllabus of the related course
    @api.onchange('course_id')
    def _campus_onchange(self):
        res = {}
        res['domain']={'syllabus_id':[('final_draft', '=', True)]}
        return res

    # @api.onchange('create_date')
    # def _onchange_year(self):
    #     self.year = datetime.strptime(self.create_date, "%Y").date()
