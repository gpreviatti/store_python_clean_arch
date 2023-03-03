import unittest

from src.modules.domain.entity.order_entity import OrderEntity
from src.modules.domain.entity.product_entity import ProductEntity

class OrderEntityTest(unittest.TestCase):

    def test_create_order_with_success(self):
        order = OrderEntity(1, '10/01/2023', 'CREATE', 10)

        self.assertEqual(order.id, 1)
        self.assertEqual(order.date, '10/01/2023')
        self.assertEqual(order.status, 'CREATE')
        self.assertEqual(order.total, 10)
        self.assertEqual([], order.items)

    
    def test_add_item_to_order_with_success(self):
        order = OrderEntity(1, '10/01/2023', 'CREATE', 10)
        items : list = []
        items.append(ProductEntity(1, 'Computer', 'Nvidia GeForce GTX 1080 Ti', 1000, 10))
        items.append(ProductEntity(2, 'Keyboard', 'Logitech', 100, 30))


        order.add_items(items)


        self.assertEqual(len(order.items), 2)

        self.assertEqual(order.items[0].id, 1)
        self.assertEqual(order.items[0].name, 'Computer')
        self.assertEqual(order.items[0].description, 'Nvidia GeForce GTX 1080 Ti')
        self.assertEqual(order.items[0].price, 1000)
        self.assertEqual(order.items[0].quantity, 10)

        self.assertEqual(order.items[1].id, 2)
        self.assertEqual(order.items[1].name, 'Keyboard')
        self.assertEqual(order.items[1].description, 'Logitech')
        self.assertEqual(order.items[1].price, 100)
        self.assertEqual(order.items[1].quantity, 30)
