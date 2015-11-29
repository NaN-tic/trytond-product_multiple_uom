# This file is part of the product_multiple_uom module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductMultipleUomTestCase(ModuleTestCase):
    'Test Product Multiple UOM module'
    module = 'product_multiple_uom'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductMultipleUomTestCase))
    return suite
