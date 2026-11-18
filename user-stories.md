# User Stories and Acceptance Criteria

These stories are written for the proposed first version of ShopFlow checkout.

## Epic: Checkout

### US-01 — Review cart
**As a** customer, **I want** to review the items in my cart, **so that** I can check what I am about to buy.

Acceptance criteria:
- Given the cart contains items, when I open it, then each item shows its name, quantity and price.
- The cart shows the subtotal.
- If the cart is empty, I see a message and a way to continue browsing.

### US-02 — Update cart
**As a** customer, **I want** to change quantities or remove items, **so that** my order is correct before I pay.

Acceptance criteria:
- I can increase or decrease an item's quantity.
- Quantity cannot be less than one.
- When I remove an item, it no longer appears in the cart.
- The subtotal updates after a cart change.

### US-03 — Enter delivery details
**As a** customer, **I want** to enter my delivery information, **so that** the store knows where to send my order.

Acceptance criteria:
- The form asks for name, phone number and delivery address.
- Required fields cannot be left blank.
- If a required field is invalid, I see a message explaining what needs to be corrected.
- Valid details can be reviewed before payment.

### US-04 — Review order total
**As a** customer, **I want** to see the full amount before paying, **so that** I know what I will be charged.

Acceptance criteria:
- The checkout shows the item subtotal.
- Any delivery fee is shown separately.
- The final payable amount is visible before I confirm payment.

### US-05 — Pay for order
**As a** customer, **I want** to choose an available payment method and pay, **so that** I can place my order.

Acceptance criteria:
- I can select a payment method offered at checkout.
- While payment is being processed, I see that the request is in progress.
- If payment succeeds, the system proceeds to order confirmation.
- If payment fails or is cancelled, I see a clear message and can retry.
- A failed payment does not create a confirmed order.

### US-06 — View order confirmation
**As a** customer, **I want** to receive an order confirmation, **so that** I know my order was placed.

Acceptance criteria:
- A successful order displays an order reference.
- The confirmation shows a summary of the order and the payable amount.
- The confirmation is not displayed as successful when payment has failed.

### US-07 — Check order status
**As a** customer, **I want** to see the current status of my order, **so that** I know what is happening after checkout.

Acceptance criteria:
- I can open an order using its reference from my account or confirmation.
- The page displays the latest status available to the store.
- If the order cannot be found, I see a helpful message.

## Notes

These are proposed requirements for a fictional scenario. They would normally be reviewed with stakeholders and refined before being treated as final development requirements.
