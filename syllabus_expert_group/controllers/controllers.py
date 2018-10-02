# -*- coding: utf-8 -*-
from odoo import http

# class SyllabusExpertGroup(http.Controller):
#     @http.route('/syllabus_expert_group/syllabus_expert_group/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus_expert_group/syllabus_expert_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus_expert_group.listing', {
#             'root': '/syllabus_expert_group/syllabus_expert_group',
#             'objects': http.request.env['syllabus_expert_group.syllabus_expert_group'].search([]),
#         })

#     @http.route('/syllabus_expert_group/syllabus_expert_group/objects/<model("syllabus_expert_group.syllabus_expert_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus_expert_group.object', {
#             'object': obj
#         })