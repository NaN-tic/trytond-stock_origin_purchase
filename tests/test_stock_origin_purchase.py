# This file is part of the stock_origin_purchase module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class StockOriginPurchaseTestCase(ModuleTestCase):
    'Test Sale POS Discount module'
    module = 'stock_origin_purchase'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        StockOriginPurchaseTestCase))
    return suite
