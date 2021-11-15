# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Class Management',
    'version': '1.1',
    'sequence': 10,
    'category': 'Human Resources/Class',
    'summary': 'Class Management system',
    'description': """Class Management system""",
    'website': 'https://www.anhtrantdt.asia',
    'depends': ['hr_student_management'],
    'data': [
        'views/class_information.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
