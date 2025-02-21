{
    "name": "Custom Product Barcode Generator",
    "author": "Muhammad Usman Hussain",
    "License": "LGPL-3",
    "version": "1.0",
    "summary": 'generate barcode for product',
    'description': """
This module offers the basic functionalities to generate barcode for product.
    """,
    'category': 'Inventory',
    'depends': ['product'],
    "data": [
        'data/ir_sequence_data.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
}
