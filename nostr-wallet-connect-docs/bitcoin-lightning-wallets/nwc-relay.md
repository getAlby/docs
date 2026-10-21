---
icon: globe-pointer
---

# NWC Relay

## Running or connecting to a relay

Relay servers route messages between client apps and wallets. NWC requires `relay` as an URL of the relay where the **wallet service** is connected and will be listening for events. &#x20;

There are four event kinds:

* `NIP-47 info event`: 13194
* `NIP-47 request`: 23194
* `NIP-47 response`: 23195
* `NIP-47 notification`: 23197 (and 23196: legacy NIP-04 notifications)

The info event should be a replaceable event that is published by the **wallet service** on the relay to indicate which commands it supports. The content should be a plaintext string with the supported commands, space-separated, eg. `pay_invoice` `get_balance`.

Both the request and response events SHOULD contain one `p` tag, containing the public key of the **wallet service** if this is a request, and the public key of the **user** if this is a response. The response event SHOULD contain an `e` tag with the id of the request event it is responding to.

The content of requests and responses is encrypted with [NIP04](https://github.com/nostr-protocol/nips/blob/master/04.md), and is a JSON-RPCish object with a semi-fixed structure:

**Request:**

```json
{
    "method": "pay_invoice", // method, string
    "params": { // params, object
        "invoice": "lnbc50n1..." // command-related data
    }
}
```

**Response:**

```json5
{
    "result_type": "pay_invoice", //indicates the structure of the result field
    "error": { //object, non-null in case of error
        "code": "UNAUTHORIZED", //string error code, see below
        "message": "human readable error message"
    },
    "result": { // result, object. null in case of error.
        "preimage": "0123456789abcdef..." // command-related data
    }
}
```

The `result_type` field MUST contain the name of the method that this event is responding to. The `error` field MUST contain a `message` field with a human readable error message and a `code` field with the error code if the command was not successful. If the command was successful, the `error` field must be null.

### Using a dedicated relay

NWC does not specify any requirements on the type of a [Nostr](https://github.com/nostr-protocol/nostr)-compatible relay. However, it makes sense to use a dedicated relay to prevent metadata leaks and improve reliability.\
Wallets can set up their own relay or leverage existing infrastructure listed [here](references-and-sdks.md#relays).
