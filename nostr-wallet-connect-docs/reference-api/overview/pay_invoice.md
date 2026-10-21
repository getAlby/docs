---
description: Requests payment of an invoice.
---

# pay\_invoice

### **Use case**

The app request a payment from a user by presenting a [BOLT-11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) invoice to the wallet.

### **Request**

```json
{
    "method": "pay_invoice",
    "params": {
        "invoice": "lnbc50n1..." // bolt11 invoice
    }
}
```

### **Response**

```json
{
    "result_type": "pay_invoice",
    "result": { 
        "preimage": "0123456789abcdef..." // preimage of the payment
    }
}
```

### **Errors**

* `PAYMENT_FAILED`: The payment failed. This may be due to a timeout, exhausting all routes, insufficient capacity or similar.
