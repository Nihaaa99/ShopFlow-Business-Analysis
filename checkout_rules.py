"""Small, local simulation of the ShopFlow checkout rules.

This is a practice model for testing requirements. It is not a live store,
payment integration, or production checkout application.
"""


def summarize_cart(cart):
    """Return cart lines and subtotal for a list of product dictionaries."""
    lines = []
    subtotal = 0
    for item in cart:
        quantity = item["quantity"]
        if quantity < 1 or quantity > item["stock"]:
            raise ValueError("Quantity must be between 1 and available stock.")
        line_total = item["unit_price"] * quantity
        lines.append({
            "name": item["name"],
            "quantity": quantity,
            "unit_price": item["unit_price"],
            "line_total": line_total,
        })
        subtotal += line_total
    return {"items": lines, "subtotal": subtotal}


def update_quantity(cart, item_name, new_quantity):
    """Change an item's quantity after checking the stock limit."""
    for item in cart:
        if item["name"] == item_name:
            if new_quantity < 1 or new_quantity > item["stock"]:
                raise ValueError("Quantity must be between 1 and available stock.")
            item["quantity"] = new_quantity
            return
    raise ValueError("Item not found in cart.")


def remove_item(cart, item_name):
    """Remove an item from the cart."""
    for index, item in enumerate(cart):
        if item["name"] == item_name:
            del cart[index]
            return
    raise ValueError("Item not found in cart.")


def validate_delivery_details(details):
    """Check required delivery fields and a basic 10-digit phone format."""
    required = ("name", "phone", "address")
    for field in required:
        if not str(details.get(field, "")).strip():
            raise ValueError(f"{field.title()} is required.")
    phone = str(details["phone"]).strip()
    if not phone.isdigit() or len(phone) != 10:
        raise ValueError("Phone must contain exactly 10 digits.")
    return True


def calculate_total(cart, delivery_fee):
    """Calculate subtotal plus delivery fee."""
    if not cart:
        raise ValueError("Cart must contain at least one item.")
    if delivery_fee < 0:
        raise ValueError("Delivery fee cannot be negative.")
    return summarize_cart(cart)["subtotal"] + delivery_fee


def place_order(cart, delivery_details, delivery_fee, payment_success, orders):
    """Create an order only when the simulated payment succeeds."""
    if not cart:
        raise ValueError("Cart must contain at least one item.")
    validate_delivery_details(delivery_details)
    total = calculate_total(cart, delivery_fee)
    if not payment_success:
        return None
    order_id = f"SF-{len(orders) + 1:04d}"
    order = {
        "order_id": order_id,
        "items": summarize_cart(cart)["items"],
        "delivery_details": dict(delivery_details),
        "total": total,
        "status": "Confirmed",
    }
    orders[order_id] = order
    return order


def get_order_status(order_id, orders):
    """Return the order status, or None when the reference is unknown."""
    order = orders.get(order_id)
    return order["status"] if order else None
