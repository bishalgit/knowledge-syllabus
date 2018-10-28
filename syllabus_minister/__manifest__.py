# -*- coding: utf-8 -*-
{
    'name': "Syllabus Minister",

    'summary': """
        Syllabus Minister is a document versioning system which provides 
        universities to streamline their syllabus lifecycle.""",

    'description': """
        Syllabus Minister is a document versioning system which provides 
        universities to streamline their syllabus lifecycle. 
        The features are given below:
        - Manage Syllabus Lifecycle
        - Check uniqueness of Course Code/Subject Code
        - Syllabus Versioning
        - Syllabus Templating
        - Syllabus Approval (Verification) Process
        - Easy and Quick search
        - Generating PDF Format of the Syllabus and program wise
        - Packaging courses for specific semester and program

    """,

    'author': "Nerku",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_user_role','mail', 'document_page'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/change_password_wizard_views.xml',
        'views/change_password_user_views.xml',
        'views/res_users_views.xml',
        'views/base_user_role_views.xml',
        'views/views.xml',
        # 'views/university.xml',
        'views/faculty.xml',
        'views/program.xml',
        'views/faculty.xml',
        'views/course.xml',
        'views/unit.xml',
        # 'views/syllabus.xml',
        # 'views/syllabus_history.xml',
        'views/templates.xml',
        'views/courseline.xml',
        'data/base_user_role.xml',
        # 'report/syllabus_report.xml',
        # 'report/program_syllabus_report.xml',
        # 'report/syllabus_history_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}