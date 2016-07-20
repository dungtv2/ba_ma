{
    'name': 'Dynamic Odoo Advance v9 (Big Sale)',
    'summary': 'Change The Odoo ListView/FormView On the fly without any technical knowledge',
    'version': '1.0',
    'category': 'Web',
    'description': """
            Change The Odoo ListView/FormView On the fly without any technical knowledge
    """,
    'author': "Hanel Software Solution",
    'website': 'http://www.hanelsoft.vn/',
    'images': ['images/1.jpg'],
    'depends': ['web'],
    'data': ['templates.xml',
             'security/show_fields_security.xml',
             'security/ir.model.access.csv'],
    'price': 299.99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': ['static/src/xml/listview_button_view.xml'],
}
