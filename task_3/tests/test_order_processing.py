import unittest
import json
from producer import send_order
from consumer import process_order
from unittest.mock import MagicMock

class TestOrderProcessing(unittest.TestCase):

    def setUp(self):
        self.channel_mock = MagicMock()
        self.method_mock = MagicMock()
        self.properties_mock = MagicMock()
        self.order_data = json.dumps({
            "order_id": "test123",
            "user_id": "user123",
            "product": "Laptop",
            "quantity": 1,
            "status": "Pending"
        })

    def test_send_order(self):
        order_id = send_order("user123", "Laptop", 1)
        self.assertIsNotNone(order_id)

    def test_process_order(self):
        process_order(self.channel_mock, self.method_mock, self.properties_mock, self.order_data)
        self.channel_mock.basic_ack.assert_called_once()

if __name__ == '__main__':
    unittest.main()
