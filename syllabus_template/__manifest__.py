# -*- coding: utf-8 -*-
{
    'name': "syllabus_template",

    'summary': """
        This module adds the feature of template selection and generate the
        syllabus based on the template selected.""",

    'description': """
        This module adds the feature of template selection and generate the
        syllabus based on the template selected.
    """,

    'author': "Nerku",
    'website': "https://www.nerku.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'web',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_widget_m2o_image', 'syllabus_minister'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ir_ui_view_views.xml',
        'views/syllabus_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}