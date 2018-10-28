# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusSyllabus(http.Controller):
#     @http.route('/syllabus_syllabus/syllabus_syllabus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_syllabus/syllabus_syllabus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_syllabus.listing', {
#             'root': '/syllabus_syllabus/syllabus_syllabus',
#             'objects': http.request.env['syllabus_syllabus.syllabus_syllabus'].search([]),
#         })

#     @http.route('/syllabus_syllabus/syllabus_syllabus/objects/<model("syllabus_syllabus.syllabus_syllabus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_syllabus.object', {
#             'object': obj
#         })