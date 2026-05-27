---
description: >-
  HOLD (or often called "HODL") invoices are invoices that do not need to be
  settled immediately after they have been paid.
---

# ⚖️ HOLD Payments

## How it Works

An invoice is a smart contract that must be settled before the receiver can access the funds of the invoice. This is done by the receiver returning the preimage (proof of payment) to the sender. However, the receiver can choose to delay releasing the preimage, or completely reject the payment. Some situations where HOLD invoices are useful are:

* Games where you only pay if you lose, but lock up your funds in advance to ensure the payment is made
* A bond which you only pay if you break a contract (similar to a rental deposit)
* P2P trading escrows

## Alby HOLD Payments

Please note that HOLD payments will not appear in the transaction list while they are pending or canceled (i.e. in the HOLD phase). The payment amount is deducted from your balance during the HOLD phase and returned afterward.

However, if you completed the payment successfully using the Alby Browser Extension, you will see the specific HOLD payment listed among other payments for that connected site (e.g. RoboSats).

## Lightning apps that use HOLD invoices

* [Robosats](https://learn.robosats.com/)

## 📖 Further resources

* [How to build conditional payment logic into your app](https://getalby.com/blog/build-conditional-payment-logic-into-your-app)

