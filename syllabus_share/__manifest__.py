# -*- coding: utf-8 -*-
{
    'name': "Syllabus Share",

    'summary': """
        This module adds the feature of sharing the syllabus using a shareable link.""",

    'description': """
        This module adds the feature of sharing the syllabus using a shareable link.
        The person with the link can view the content of the syllabus.
    """,

    'author': "Nerku",
    'website': "https://www.nerku.com",
    'category': 'web',
    'version': '11.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_widget_m2o_image', 'syllabus_minister', 'syllabus_syllabus', 'portal'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/data.xml',
        # 'wizard/syllabus_display_views.xml',
        'views/syllabus_share_templates.xml',
        'views/document_page_views.xml',
        'wizard/syllabus_share_display_views.xml',
        # 'views/syllabus_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}