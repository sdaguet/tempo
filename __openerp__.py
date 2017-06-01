# -*- coding: utf-8 -*-
{
    'name': "darb_puthod",

    'summary': """
        Darbtech's module to realise modification
        for Puthod""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Darbtech",
    'website': "https://darbtech.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account',
	            'account_accountant', 'hr', 'mrp',
                'website',
                'sale_layout', 'hr_timesheet', 'hr_equipment', 'hr_holidays', 'hr_timesheet_sheet',
				'website_customer_order_delivery_date'
                ],

    # always loaded
    'data': [
        'data/menus.xml',
		'data/product.xml',
        'views/fichechantier.xml',
        'views/fc_workflow.xml',
        'views/teaminfo.xml',
        'crons/template.xml',
		'report/quotations.xml',
		'views/report_amenagement.xml',
		'views/modif_quotation.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/template.xml',
    ],
	#'qweb': ['static/src/js/*.js'],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
