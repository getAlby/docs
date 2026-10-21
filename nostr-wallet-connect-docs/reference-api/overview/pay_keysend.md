# pay\_keysend

### U**se case**

The app requests a [keysend](https://github.com/alexbosworth/keysend_protocols) payment from the wallet.

### **Request**

```json
{
    "method": "pay_keysend",
    "params": {
        "amount": 123, // invoice amount in msats, required
        "pubkey": "03...", // payee pubkey, required
        "preimage": "0123456789abcdef...", // preimage of the payment, optional
        "tlv_records: [ // tlv records, optional
            {
                "type": 5482373484, // tlv type
                "value": "0123456789abcdef" // hex encoded tlv value
            }
        ]
    }
}
```

### **Response**

```json
{
    "result_type": "pay_keysend",
    "result": {
        "preimage": "0123456789abcdef...", // preimage of the payment
    }
}
```
