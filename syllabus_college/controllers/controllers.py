# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusCollege(http.Controller):
#     @http.route('/syllabus_college/syllabus_college/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_college/syllabus_college/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_college.listing', {
#             'root': '/syllabus_college/syllabus_college',
#             'objects': http.request.env['syllabus_college.syllabus_college'].search([]),
#         })

#     @http.route('/syllabus_college/syllabus_college/objects/<model("syllabus_college.syllabus_college"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_college.object', {
#             'object': obj
#         })