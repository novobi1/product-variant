# Copyright 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# Copyright 2018 Fabien Bourgeois <fabien@yaltik.com>
# Copyright 2023 Novobi LLC <novobi.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Product Variant Sale Price",
    "summary": "Allows to write fixed prices in product variants",
    "version": "16.0.0.0.1",
    "category": "Product Management",
    "website": "https://github.com/OCA/product-variant",
    "author": "Tecnativa, Odoo Community Association (OCA), Novobi LLC",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["account", "sale"],
    "data": ["views/product_views.xml"],
    "post_init_hook": "set_sale_price_on_variant",
}
