---
description: Get specific information about the wallet account
---

# get\_info

### **Use case**

The app requests specific information about the account from the wallet.

### **Request**

```json
{
    "method": "get_info",
    "params": {
    }
}
```

### **Response**

```json
{
    "result_type": "get_info",
    "result": {
            "alias": "string",
            "color": "hex string",
            "pubkey": "hex string",
            "network": "string", // mainnet, testnet, signet, or regtest
            "block_height": 1,
            "block_hash": "hex string",
            "methods": ["pay_invoice", "get_balance", "make_invoice", "lookup_invoice", "list_transactions", "get_info"], // list of supported methods for this connection
    }
}
```
