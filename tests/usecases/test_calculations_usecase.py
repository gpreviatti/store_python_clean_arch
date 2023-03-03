import unittest

from src.modules.usecases.calculation_usecase import CalculationUseCase

class TestCalculationsUseCase(unittest.TestCase):
    def setUp(self):
        self.calculation_usecase = CalculationUseCase()

    def test_sum(self):
        self.assertEqual(self.calculation_usecase.get_sum(8, 2), 10, 'The sum is wrong.')

    def test_diff(self):
        self.assertEqual(self.calculation_usecase.get_difference(8, 2), 6, 'The difference is wrong.')

    def test_product(self):
        self.assertEqual(self.calculation_usecase.get_product(8, 2), 16, 'The product is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculation_usecase.get_quotient(8, 2), 4, 'The quotient is wrong.')
