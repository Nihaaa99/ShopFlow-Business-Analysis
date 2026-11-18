# ShopFlow — E-commerce Business Analysis

A practice business analysis case study for a small online store.

## Scenario

ShopFlow is a fictional online store selling everyday products. The store wants to make checkout easier and give customers clearer updates after they place an order.

This project focuses on a first version of the checkout and order-tracking experience. It is a self-directed portfolio exercise, not work completed for a real client.

## What's included

- `business-requirements.md` — problem statement, scope and business requirements
- `user-stories.md` — user stories with acceptance criteria
- `process-flow.md` — proposed checkout process
- `stakeholder-register.md` — stakeholder roles and involvement
- `requirements-traceability.csv` — links business requirements to stories and tests
- `uat-test-cases.csv` — sample user acceptance test scenarios
- `uat-execution-log.csv` — blank template for recording actual UAT results
- `checkout_rules.py` — small Python simulation of checkout rules
- `test_checkout_rules.py` — automated unit tests for the checkout simulation
- `validate_case_study.py` — checks that document references are consistent

## Run the checks

Run these commands from the project folder:

```bash
python validate_case_study.py
python -m unittest -v
```

The validation script checks that the key files exist, IDs are unique, and requirements, stories and test cases are linked consistently.

The automated unit tests check the Python checkout simulation, including cart operations, delivery validation, order totals, payment outcomes and order status. The tests use simulated data and do not connect to a live store or payment gateway.

## Main workflow

A customer reviews the cart, enters delivery details, checks the final total, chooses a payment method and places an order. The system confirms the order after successful payment and displays its status.

## Assumptions

- This is a small, fictional business.
- Payments are handled by an external payment service.
- The first release covers a basic checkout and order-status view.
- Product catalogue management and warehouse operations are outside this case study.

## Project status

Documentation and traceability are prepared as a portfolio exercise. The validation script checks document consistency. The checkout simulation's automated tests have passed (13 tests). UAT has not been executed, and the proposed requirements have not been reviewed by real business stakeholders.
