# test_tax_calculator.py

import unittest
from ..tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    def test_no_tax_below_12000(self):
        self.assertEqual(calculate_tax(10000), 0)

    def test_tax_between_12000_and_36000(self):
        self.assertEqual(calculate_tax(20000), 1600)  # Expected: 20% of 8,000

    # test_tax_calculator.py

class TestTaxCalculator(unittest.TestCase):
    # Existing test
    def test_no_tax_below_12000(self):
        self.assertEqual(calculate_tax(10000), 0)

    # New test
    def test_tax_between_12000_and_36000(self):
        self.assertEqual(calculate_tax(20000), 1600)  # 20% of 8,000

    # test_tax_calculator.py

class TestTaxCalculator(unittest.TestCase):
    # Existing tests...
    def test_tax_above_36000(self):
        # Expected tax = (36,000 - 12,000) * 0.2 + (40,000 - 36,000) * 0.4 = 4800 + 1600 = 6400
        self.assertEqual(calculate_tax(40000), 6400)

