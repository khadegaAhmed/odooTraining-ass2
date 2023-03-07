# -*- coding: utf-8 -*-
{
    'name': 'Care Card ',
    'version': '1.6',
    'website': 'https://www.odoo.com',
    'category': 'website',
    'summary': 'html',
    'description': """
this module is care card for the beneficiaries.
""",
    'depends': ['website'],
'data': [
'security/ir.model.access.csv',
#     'views/event.xml',
 'views/card.xml',
'templates/templates.xml',
'data/data.xml',
    ],
}
