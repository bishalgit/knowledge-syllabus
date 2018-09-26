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
    'depends': ['base'],

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