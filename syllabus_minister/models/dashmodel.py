from odoo import models, fields, api
from odoo.http import request
import logging
import random

_logger = logging.getLogger(__name__)

class SyllabusDashboard(models.Model):
    _name = 'syllabus_minister.dashboard'
    _description = 'Dashboard'

    name = fields.Char(default="Syllabus Dashboard")

    def random_color(self):     
        r = lambda: random.randint(55,180)
        return('#%02X%02X%02X' % (r(),r(),r()))

    @api.model
    def get_syllabus_info(self):
        uid = request.session.uid
        cr = self.env.cr

        users = self.env['res.users'].sudo().search([])
        faculties = self.env['syllabus_minister.faculty'].sudo().search([])
        no_program = self.env['syllabus_minister.program'].sudo().search_count([])
        no_course = self.env['syllabus_minister.course'].sudo().search_count([])
        no_faculty = self.env['syllabus_minister.faculty'].sudo().search_count([])
        no_syllabus = self.env['document.page'].sudo().search_count([])
        no_users = self.env['res.users'].sudo().search_count([])
             
        faculty_list = []
        program_list = []
        syllabus_list = []
        random_color_list = []
        for faculty in faculties:
            program_count = self.env['syllabus_minister.program'].sudo().search_count([('faculty_id','=', faculty.id)])
            syllabus_count = self.env['document.page'].sudo().search_count([('faculty_id','=', faculty.id)])
            faculty_color = self.random_color()
            random_color_list.append(faculty_color)
            faculty_list.append(faculty.name)
            program_list.append(program_count)
            syllabus_list.append(syllabus_count)

        if users:
            data = {
                'no_program': no_program,
                'no_course': no_course,
                'no_faculty': no_faculty,
                'no_syllabus': no_syllabus,
                # 'no_users': no_users,
                'faculty_list': faculty_list,
                'program_list': program_list,
                'syllabus_list': syllabus_list,
                'random_color_list': random_color_list,
            }
            _logger.warning(data)
            return data
        else:
            return