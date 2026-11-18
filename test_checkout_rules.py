"""Automated checks for the ShopFlow checkout practice model.

Run:
    python -m unittest -v
"""
import unittest

from checkout_rules import (
    calculate_total,
    get_order_status,
    place_order,
    remove_item,
    summarize_cart,
    update_quantity,
    validate_delivery_details,
)


def sample_cart():
    return [
        {"name": "Notebook", "unit_price": 100, "quantity": 2, "stock": 5},
        {"name": "Pen", "unit_price": 20, "quantity": 1, "stock": 10},
    ]


def valid_details():
    return {"name": "Asha Rao", "phone": "9876543210", "address": "12 Lake Road"}


class ShopFlowCheckoutTests(unittest.TestCase):
    def setUp(self):
        self.cart = sample_cart()
        self.orders = {}

    def test_tc01_view_cart_with_items(self):
        result = summarize_cart(self.cart)
        self.assertEqual(len(result["items"]), 2)
        self.assertEqual(result["subtotal"], 220)

    def test_tc02_empty_cart(self):
        result = summarize_cart([])
        self.assertEqual(result["items"], [])
        self.assertEqual(result["subtotal"], 0)

    def test_tc03_increase_item_quantity(self):
        update_quantity(self.cart, "Notebook", 3)
        self.assertEqual(summarize_cart(self.cart)["subtotal"], 320)

    def test_tc04_remove_item(self):
        remove_item(self.cart, "Pen")
        self.assertEqual(len(summarize_cart(self.cart)["items"]), 1)
        self.assertEqual(summarize_cart(self.cart)["subtotal"], 200)

    def test_tc05_missing_required_delivery_field(self):
        details = valid_details()
        details["phone"] = ""
        with self.assertRaisesRegex(ValueError, "Phone is required"):
            validate_delivery_details(details)

    def test_tc06_valid_delivery_details(self):
        self.assertTrue(validate_delivery_details(valid_details()))

    def test_tc07_order_total_includes_delivery_fee(self):
        self.assertEqual(calculate_total(self.cart, 40), 260)

    def test_tc08_successful_payment_creates_order(self):
        order = place_order(self.cart, valid_details(), 40, True, self.orders)
        self.assertIsNotNone(order)
        self.assertEqual(order["status"], "Confirmed")
        self.assertIn(order["order_id"], self.orders)

    def test_tc09_failed_payment_does_not_create_order(self):
        order = place_order(self.cart, valid_details(), 40, False, self.orders)
        self.assertIsNone(order)
        self.assertEqual(self.orders, {})

    def test_tc10_retry_after_failed_payment(self):
        first_attempt = place_order(self.cart, valid_details(), 40, False, self.orders)
        second_attempt = place_order(self.cart, valid_details(), 40, True, self.orders)
        self.assertIsNone(first_attempt)
        self.assertIsNotNone(second_attempt)
        self.assertEqual(len(self.orders), 1)

    def test_tc11_successful_order_has_confirmation_reference(self):
        order = place_order(self.cart, valid_details(), 40, True, self.orders)
        self.assertRegex(order["order_id"], r"^SF-\d{4}$")
        self.assertEqual(order["total"], 260)
        self.assertEqual(len(order["items"]), 2)

    def test_tc12_existing_order_status(self):
        order = place_order(self.cart, valid_details(), 40, True, self.orders)
        self.assertEqual(get_order_status(order["order_id"], self.orders), "Confirmed")

    def test_tc13_unknown_order_reference(self):
        self.assertIsNone(get_order_status("SF-9999", self.orders))


if __name__ == "__main__":
    unittest.main()
