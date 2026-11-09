{
    'name': 'Test Module',
    'version': '19.0.1.0.1',  # <-- Increment this last number
    'category': 'Uncategorized',
    'summary': 'A simple module for testing Odoo development',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/test_model_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}