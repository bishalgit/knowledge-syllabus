# -*- coding: utf-8 -*-
{
    'name': "Syllabus",

    'summary': """
        Syllabus of the Program""",

    'description': """
        This module simply generates the syllabus of the certain course of the program
        of the University.
    """,

    'author': "Nerku",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Syllabus',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'syllabus_minister', 'document_page_approval', 'knowledge'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/document_page.xml',
        'views/res_company.xml',
        'report/syllabus_report.xml',
        'report/program_syllabus_report.xml',
        'report/syllabus_history_report.xml',
        'report/report.xml',
        'report/curriculum_structure_report.xml',
        'report/program_old_version_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}