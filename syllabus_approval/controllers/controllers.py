# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusApproval(http.Controller):
#     @http.route('/syllabus_approval/syllabus_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_approval/syllabus_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_approval.listing', {
#             'root': '/syllabus_approval/syllabus_approval',
#             'objects': http.request.env['syllabus_approval.syllabus_approval'].search([]),
#         })

#     @http.route('/syllabus_approval/syllabus_approval/objects/<model("syllabus_approval.syllabus_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_approval.object', {
#             'object': obj
#         })