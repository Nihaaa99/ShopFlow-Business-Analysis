# Business Requirements — ShopFlow Checkout

## 1. Background

ShopFlow is a fictional online store. For this case study, assume customers can browse products and add them to a cart, but the checkout journey needs to be made clearer and easier to complete.

The goal is to describe a simple first version of checkout and order tracking.

## 2. Problem statement

Customers need a straightforward way to review their cart, provide delivery details, pay for an order and understand whether the order was placed successfully. If the process is unclear, customers may abandon checkout or contact support to ask what happened.

## 3. Objectives

- Make the checkout steps clear and predictable.
- Show customers the final order total before they pay.
- Give customers a confirmation after a successful order.
- Let customers view a basic order status.

## 4. Scope

### In scope
- View and update cart items.
- Enter and validate delivery details.
- Review item total, delivery fee and final payable amount.
- Select an available payment method.
- Handle successful and unsuccessful payment responses.
- Create an order after successful payment.
- Display an order confirmation and order status.

### Out of scope
- Seller onboarding and product listing tools.
- Warehouse and courier management.
- Returns, refunds and exchange workflows.
- Loyalty points, coupons and promotional campaigns.
- Multiple delivery addresses saved to an account.

## 5. Stakeholders

| Stakeholder | Interest |
|---|---|
| Customer | Complete an order and receive clear updates |
| Store operations | Receive accurate order details |
| Customer support | Help customers understand order status |
| Product / development team | Build and maintain the checkout journey |
| Payment provider | Process payment requests and return a result |

## 6. Business requirements

| ID | Requirement | Priority |
|---|---|---|
| BR-01 | The customer must be able to review items and quantities in the cart. | Must |
| BR-02 | The customer must be able to change a quantity or remove an item before checkout. | Must |
| BR-03 | The checkout must collect the customer's name, phone number and delivery address. | Must |
| BR-04 | The system must show the order total, including any delivery fee, before payment. | Must |
| BR-05 | The customer must be able to choose from the payment methods currently supported by the store. | Must |
| BR-06 | The system must create an order only after receiving a successful payment result. | Must |
| BR-07 | The customer must see a confirmation with an order reference after a successful order. | Must |
| BR-08 | The customer must be able to view a basic status for an order. | Should |
| BR-09 | If payment fails, the customer must see a clear message and be able to try again. | Must |

## 7. Business rules and assumptions

- A cart must contain at least one available item to proceed.
- Quantity must be a positive whole number and cannot exceed available stock.
- The payable total is the item subtotal plus the delivery fee shown at checkout.
- An order reference is generated only after successful payment.
- A failed or cancelled payment must not create a confirmed order.
- Payment processing is assumed to be provided by an external service.

## 8. Success measures

For a real implementation, the business could monitor:
- Checkout completion rate.
- Payment success rate.
- Number of checkout-related support requests.
- Order creation errors.

No baseline or target values are set because this case study uses no real business data.

## 9. Open questions

These would need answers from the business before development:
- Which payment methods will be available at launch?
- How is the delivery fee calculated?
- Which locations can the store deliver to?
- What order statuses should customers see?
- How long should an unpaid cart remain active?
