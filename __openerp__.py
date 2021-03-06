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
    'depends': ['base', 'sale', 'account','calendar',
	            'account_accountant', 'hr', 'mrp',
                'website','hr_attendance',
                'sale_layout', 'hr_timesheet', 'hr_equipment', 'hr_holidays', 'hr_timesheet_sheet',
				'website_customer_order_delivery_date',
                'manufacturing_google_maps', 'sale_order_acompte'
                ],

    # always loaded
    'data': [
        'wizard/sale_order_confirm.xml',
        'data/menus.xml',
		'data/product.xml',
        'views/fichechantier.xml',
        'views/teaminfo.xml',
        'crons/template.xml',
        'report/quotations.xml',
		'views/iframe.xml',
		'views/report_amenagement.xml',
		'views/report_bilan_puthod_chantier.xml',
		'views/report_bilan_chantier.xml',
		'views/report_entretien.xml',
		'views/modif_quotation.xml',
		'views/modif_hr_employee.xml',
		'views/tmpputhod.xml',
        'views/template.xml',
        'views/sale_order.xml',
        'views/chantier.xml',
        'views/emplacement.xml',
        'views/calendar.xml',
        'views/puthod_partner.xml',
        'report/report_employee_view.xml',
        'data/puthod_product_data.xml',
        'data/puthod_product_attribute.xml',
        'report/annexes_product_report_view.xml',
        'views/report_productlabel.xml',
        'views/puthod_product_report.xml',
        'views/report_saleorder_mail.xml',
        'views/liasse_preparation.xml',
        'views/report_liasse_preparation.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/pricelist_view.xml',
    ],
    #'qweb': ['static/src/js/*.js'],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
