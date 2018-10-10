# -*- coding: utf-8 -*-
{
    'name': "Syllabus College",

    'summary': """
        Affiliated Colleges of the University""",

    'description': """
        This module lists the colleges which are affiliated with the university.
        There are basic infomation of the colleges and the related syllabus packages 
        as provided by the university.
    """,

    'author': "Nerku Inc.",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Syllabus',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','syllabus_minister'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'views/package.xml',
        'views/college.xml',
        'report/syllabus_college_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}