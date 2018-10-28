# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courseline(models.Model):
    _name = 'syllabus_minister.courseline'
    _description = 'Course Line'
    _order =  'sequence, id'

    name = fields.Char(string='Name')
    semester = fields.Char(string='Semester')
    course_id = fields.Many2one('syllabus_minister.course', string='Related Course',
    domain="[('group_ids.users.id', '=', uid)]")
    sequence = fields.Integer(string='sequence',default=1)
    program_id = fields.Many2one('syllabus_minister.program',string="Program",
    domain="['|', ('faculty_id.university_id.university_user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")
    syllabus_id = fields.Many2one('syllabus_minister.syllabus',string="Syllabus",
    domain="['|', ('faculty_id.university_id.university_user_ids', '=', uid), ('group_ids.users.id', '=', uid)]")

    # Groups Involved in Courseline
    group_ids = fields.Many2many('res.groups', string="Related Groups")

    @api.model
    def create(self, vals):
        courseline = super(Courseline, self).create(vals)
        courseline.write({
            'group_ids': [(4, self.env.ref('syllabus_minister.syllabus_minister_group_administrator').id)]
        })
        return courseline
    
    # This function filters the courseline record for the program of certain university.
    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     domain = (domain or []) + ['|', ('program_id.faculty_id.university_id.name', '=', self.env.user.university_id.name), ('group_ids.users.id', '=', self.env.uid)]
    #     return super(Courseline, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
    #                                                  order=order)

    # Semester prefixing
    semester_prefix = fields.Char("Semester Prefix")
    semester_sufix = fields.Char("Semester Sufix")

    @api.model
    def create(self, vals):
        response = super(Courseline, self).create(vals)
        if response:
            if 'semester' in vals:
                try:
                    p = inflect.engine()
                    s = p.ordinal(int(vals['semester']))
                    response.semester_sufix = s[-2:]
                    response.semester_prefix = s[:-2]
                except Exception:
                    response.semester_sufix = "undefined"
                    response.semester_prefix = "undefined"
        return response
    
    @api.multi
    def write(self, vals):
        response = super(Courseline, self).write(vals)
        if response:
            if 'semester' in vals:
                try:
                    p = inflect.engine()
                    s = p.ordinal(int(vals['semester']))
                    self.semester_sufix = s[-2:]
                    self.semester_prefix = s[:-2]
                except Exception:
                    self.semester_sufix = "undefined"
                    self.semester_prefix = "undefined"
        return response