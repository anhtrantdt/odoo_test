# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School management system',
    'version': '1.1',
    'sequence': 10,
    'category': 'Human Resources/School',
    'summary': 'School management system',
    'description': """School management system""",
    'website': 'https://www.anhtrantdt.asia',
    'depends': ["hr_class_management"],
    'data': [
        'views/school_information.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
