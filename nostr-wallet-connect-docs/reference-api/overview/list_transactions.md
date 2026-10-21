---
description: List invoices and payments.
---

# list\_transactions

### **Use case**

The app asks for a list of invoices and payments.&#x20;

### **Request**

```json
{
    "method": "list_transactions",
    "params": {
        "from": 1693876973, // starting timestamp in seconds since epoch (inclusive), optional
        "until": 1703225078, // ending timestamp in seconds since epoch (inclusive), optional
        "limit": 10, // maximum number of invoices to return, optional
        "offset": 0, // offset of the first invoice to return, optional
        "unpaid": true, // include unpaid invoices, optional, default false
        "type": "incoming", // "incoming" for invoices, "outgoing" for payments, undefined for both
    }
}
```

### **Response**

If `type` is not specified, both invoices and payments are returned. The `from` and `until` parameters are timestamps in seconds since epoch. If `from` is not specified, it defaults to 0. If `until` is not specified, it defaults to the current time. Transactions are returned in descending order of creation time.

```json
{
    "result_type": "list_transactions",
    "result": {
        "transactions": [
            {
               "type": "incoming", // "incoming" for invoices, "outgoing" for payments
               "invoice": "string", // encoded invoice, optional
               "description": "string", // invoice's description, optional
               "description_hash": "string", // invoice's description hash, optional
               "preimage": "string", // payment's preimage, optional if unpaid
               "payment_hash": "string", // Payment hash for the payment
               "amount": 123, // value in msats
               "fees_paid": 123, // value in msats
               "created_at": unixtimestamp, // invoice/payment creation time
               "expires_at": unixtimestamp, // invoice expiration time, optional if not applicable
               "settled_at": unixtimestamp, // invoice/payment settlement time, optional if unpaid
               "metadata": {} // generic metadata that can be used to add things like zap/boostagram details for a payer name/comment/etc.
           }
        ],
    },
}
```
