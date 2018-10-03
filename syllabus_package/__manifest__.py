# -*- coding: utf-8 -*-
{
    'name': "Syllabus Package",

    'summary': """
        Syllabus Package is the package system that creates syllabus of a whole program.
        E.g. B.SC,B.A.,B.E.S.E.,etc.""",

    'description': """
        Syllabus Package is the package system that creates syllabus of a whole program.
        E.g. B.SC,B.A.,B.E.S.E.,etc.
        The features are given below:
        - Packaging courses for specific semester and program
        - Easy and Quick search
        - Generating PDF Format of the Syllabus and program wise
    """,

    'author': "Nerku",
    'website': "http://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','syllabus_minister'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/package.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}