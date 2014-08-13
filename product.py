#This file is part product_multiple_uom module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.model import ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['Template', 'TemplateProductUom']
__metaclass__ = PoolMeta


class Template:
    __name__ = 'product.template'
    uoms = fields.Many2Many('product.template-product.uom',
        'template', 'uom', 'UOMs')


class TemplateProductUom(ModelSQL):
    'Template - Product UOM'
    __name__ = 'product.template-product.uom'
    _table = 'product_template_product_uom_rel'
    template = fields.Many2One('product.template', 'Template', ondelete='CASCADE',
            required=True, select=True)
    uom = fields.Many2One('product.uom', 'UOM',
        ondelete='CASCADE', required=True, select=True)
