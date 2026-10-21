---
description: List of error codes
icon: bug
---

# Error Codes

* `RATE_LIMITED`: The client is sending commands too fast. It should retry in a few seconds.
* `NOT_IMPLEMENTED`: The command is not known or is intentionally not implemented.
* `INSUFFICIENT_BALANCE`: The wallet does not have enough funds to cover a fee reserve or the payment amount.
* `QUOTA_EXCEEDED`: The wallet has exceeded its spending quota.
* `RESTRICTED`: This public key is not allowed to do this operation.
* `UNAUTHORIZED`: This public key has no wallet connected.
* `INTERNAL`: An internal error. Examples:
  * some required service is down which caused the request to fail,&#x20;
  * failure to save something to the database,&#x20;
  * some unexpected error occurred while processing a request.
* `OTHER`: Other error.

Please, [join the Discord community](https://discord.nwc.dev/) or [reach out](mailto:hello@getalby.com) directly if you encounter unknown errors or other problems during the implementation.
