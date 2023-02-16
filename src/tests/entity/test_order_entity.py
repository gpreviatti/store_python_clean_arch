import unittest

from src.domain.entity.order_entity import OrderEntity

class TestOrderEntity(unittest.TestCase):

    def test_create_order_with_success(self):
        order = OrderEntity(1, '10/01/2023', 'CREATE', 10)
