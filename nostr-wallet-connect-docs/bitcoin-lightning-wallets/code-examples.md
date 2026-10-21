---
description: Fast-track your NWC integration with these examples
icon: square-terminal
---

# Code Examples

## Example Web TypeScript Project <a href="#sample-typescript-project" id="sample-typescript-project"></a>

### Install the SDK

```
npm install @getalby/sdk
```

or

```javascript
yarn add @getalby/sdk
```

## Examples

```typescript
import { nwc } from "@getalby/sdk";

// setup the wallet service for your preferred relay
const walletService = new nwc.NWCWalletService({
  relayUrl: "wss://relay.getalby.com/v1",
});

// for each client/app connection you can publish a NIP-47
// info event and subscribe to requests
await walletService.publishWalletServiceInfoEvent(
  walletServiceSecretKey,
  ["get_info"], // NIP-47 methods supported by your wallet service
  [],
);

// each client app connection will have a unique keypair
const keypair = new nwc.NWCWalletServiceKeyPair(
  walletServiceSecretKey,
  clientPubkey,
);

// subscribe to and handle requests for each client app
const unsub = await walletService.subscribe(keypair, {
  getInfo: () => {
    return Promise.resolve({
      result: {
        methods: ["get_info"], // NIP-47 methods supported by your wallet service
        //... add other fields here
      },
      error: undefined,
    });
  },
  // ... handle other NIP-47 methods here
});
```

