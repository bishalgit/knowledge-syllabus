# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusTask(http.Controller):
#     @http.route('/syllabus_task/syllabus_task/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_task/syllabus_task/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_task.listing', {
#             'root': '/syllabus_task/syllabus_task',
#             'objects': http.request.env['syllabus_task.syllabus_task'].search([]),
#         })

#     @http.route('/syllabus_task/syllabus_task/objects/<model("syllabus_task.syllabus_task"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_task.object', {
#             'object': obj
#         })