# -*- coding: utf-8 -*-
{
    'name': "Syllabus Task",

    'summary': """
        Create tasks related to syllabus management.""",

    'description': """
        This modules provides interface to create task for
        syllabus management where particular syllabus is taken
        to manage such as review, approve and edit to the selected 
        assignee. The assignee is notified deadline of the task by
        the syllabus management committee.
    """,

    'author': "Nerku Inc.",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Syllabus',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'syllabus_syllabus'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}