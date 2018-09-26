# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusMinister(http.Controller):
#     @http.route('/syllabus_minister/syllabus_minister/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_minister/syllabus_minister/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_minister.listing', {
#             'root': '/syllabus_minister/syllabus_minister',
#             'objects': http.request.env['syllabus_minister.syllabus_minister'].search([]),
#         })

#     @http.route('/syllabus_minister/syllabus_minister/objects/<model("syllabus_minister.syllabus_minister"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_minister.object', {
#             'object': obj
#         })