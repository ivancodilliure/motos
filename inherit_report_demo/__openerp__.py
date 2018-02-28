# -*- coding: utf-8 -*-
{
    'name': "inherit_report_demo",

    'summary': """
        Modificacions sobre Odoo""",

    'description': """
        Anem a probar - descripció
    """,

    'author': "Ivan",
    'website': "http://www.codilliure.cat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
