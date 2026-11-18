# Proposed Checkout Process

The flow below describes the basic customer journey for the first release.

```mermaid
flowchart TD
    A[Customer opens cart] --> B{Cart has items?}
    B -- No --> C[Show empty cart]
    C --> D[Continue browsing]
    B -- Yes --> E[Review and update cart]
    E --> F[Enter delivery details]
    F --> G{Details valid?}
    G -- No --> H[Show validation messages]
    H --> F
    G -- Yes --> I[Review order total]
    I --> J[Select payment method]
    J --> K[Send payment request]
    K --> L{Payment successful?}
    L -- No --> M[Show payment failure]
    M --> J
    L -- Yes --> N[Create order]
    N --> O[Show order confirmation]
    O --> P[Customer views order status]
```

## Process notes

- The customer can return to the cart and change items before payment.
- Delivery details must pass validation before the payment step.
- The final payable amount is shown before the payment request.
- The order is confirmed only after a successful payment response.
- A failed or cancelled payment returns the customer to the payment step.

## Items to confirm with stakeholders

- Whether cash on delivery is supported.
- How stock is reserved during checkout.
- What happens if payment succeeds but the store does not receive the response.
- Which order statuses are visible to customers.
