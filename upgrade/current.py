# -*- python -*-
# coding: utf-8

# Mettez vos upgrades dans ce fichier comme ci-dessous

# sample script
#     # from branch 'feature-partner++mieux-bien
#     env['res.partner'].search([('field', '=', '...')]).write({'key': val})

from openerp.api import Environment

UPDATE = [
]

INSTALL = [
    'custom_profile'
]

def uninstall(env, modules):
    module_obj = env['ir.module.module']
    modules = module_obj.search([('name', 'in', modules)])
    modules.module_uninstall()


def run(session, logger):
    if INSTALL:
        session.install_modules(INSTALL)
    if UPDATE:
        session.update_modules(UPDATE)
    env = Environment(session.cr, 1, {})
    index = env['nosql.index'].search([], limit=1)
    for tmpl in env['product.template'].search([]):
        if not tmpl.nosql_bind_ids:
            env['nosql.product.template'].create({
                'record_id': tmpl.id,
                'index_id': index.id,
                })
