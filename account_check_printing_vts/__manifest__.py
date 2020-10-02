{
    "name": "Account Check Printing Customization",
    "version": "12.0.11.27",
    "category": "Account",
    "summary": """
	Check Print Customization.
	""",
    "author": 'Vraja Technologies',
    "depends": ['l10n_ca_check_printing','base'],
    "data": [
        'views/res_company.xml',
        'views/account_check_print.xml',
        'views/print_check_top.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
