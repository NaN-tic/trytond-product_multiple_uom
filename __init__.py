# This file is part product_multiple_uom module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from .product import *


def register():
    Pool.register(
        Template,
        TemplateProductUom,
        module='product_multiple_uom', type_='model')
