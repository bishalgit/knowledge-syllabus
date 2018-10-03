# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusPackage(http.Controller):
#     @http.route('/syllabus_package/syllabus_package/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_package/syllabus_package/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_package.listing', {
#             'root': '/syllabus_package/syllabus_package',
#             'objects': http.request.env['syllabus_package.syllabus_package'].search([]),
#         })

#     @http.route('/syllabus_package/syllabus_package/objects/<model("syllabus_package.syllabus_package"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_package.object', {
#             'object': obj
#         })