{
    'name': 'Test Module',
    'version': '19.0.1.0.0',
    'category': 'Uncategorized',
    'summary': 'A simple module for testing Odoo development',
    'depends': ['base', 'mail'],  # Added 'mail' dependency
    'data': [
        'security/ir.model.access.csv',
        'views/test_model_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}