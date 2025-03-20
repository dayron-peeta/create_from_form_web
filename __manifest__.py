# -*- coding: utf-8 -*-
{
    'name': "create_from_form_web",

    'summary': "Module to create records from a web form with all data types.",

    'description': """
        This module provides a web form accessible at /create_from_web,
        allowing users to create records in the model_all_types model.
        It includes fields of all possible data types in Odoo 16.
    """,

    'author': "Dayron Peeta",
    'website': "https://www.yourwebsite.com",

    'category': 'Tools',
    'version': '1.0',

    'depends': ['base', 'website'],

    'data': [
        'security/ir.model.access.csv',  
        'views/create_form_view.xml',
        'views/menu.xml',
        'views/create_form_template.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
