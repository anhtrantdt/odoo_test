# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Student Management',
    'version': '1.1',
    'sequence': 10,
    'category': 'Human Resources/Student',
    'summary': 'Student Management system',
    'description': """Student Management system""",
    'website': 'https://www.anhtrantdt.asia',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/student_information.xml',
        'views/subject_information.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
