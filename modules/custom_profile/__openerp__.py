# -*- coding: utf-8 -*-
# © 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Custom Profile',
    'summary': 'Custom Profile for installing all default module',
    'version': '0.3',
    'author': 'Akretion',
    'summarize': "",
    'maintainer': 'Akretion',
    'category': 'custom',
    'depends': [
        'connector_nosql_algolia_product',
        'connector_devise',
        'sale',
        'connector_dev',
    ],
    'website': 'http://www.akretion.com/',
    'data': [
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'tests': [],
    'sequence': 1,
    'installable': True,
    'license': 'AGPL-3',
    'external_dependencies': {
        'python': ['unidecode'],
    },
}
