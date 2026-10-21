---
description: Request the balance of the wallet account
---

# get\_balance

### **Use case**

The app requests the balance of the account from the wallet.

### **Request**

```json
{
    "method": "get_balance",
    "params": {
    }
}
```

### **Response**

```json
{
    "result_type": "get_balance",
    "result": {
        "balance": 10000, // user's balance in msats
    }
}
```
