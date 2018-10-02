# -*- coding: utf-8 -*-
{
    'name': "Syllabus Expert Group",

    'summary': """
        Provide Expert security group """,

    'description': """
        This module provides expert group who reviews the syllabus, generate report 
            regarding syllabus change and sends report to the syllabus approver""",

    'author': "Nerku",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Syllabus',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}