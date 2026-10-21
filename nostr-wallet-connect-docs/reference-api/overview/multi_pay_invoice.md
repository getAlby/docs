---
description: Request payment of multiple invoices.
---

# multi\_pay\_invoice

### **Use case**

The app requests a payment of multiple [BOLT-11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) invoices from the wallet.

### **Request**

```json
{
    "method": "multi_pay_invoice",
    "params": {
        "invoices": [
          {"invoice": lnbc1...", "amount": 123}, // bolt11 invoice and amount in msats, amount is optional
          {"invoice": lnbc50n1..."},
        ],
    }
}
```

### **Response**

For every invoice in the request, a separate response event is sent. To differentiate between the responses, each response event contains an `payment_hash` **tag** with the payment hash of the invoice it is responding to.

```json
{
    "result_type": "multi_pay_invoice",
    "result": {
        "preimage": "0123456789abcdef..." // preimage of the payment
    }
}
```

### **Errors**

* `PAYMENT_FAILED`: The payment failed. This may be due to a timeout, exhausting all routes, insufficient capacity or similar.
