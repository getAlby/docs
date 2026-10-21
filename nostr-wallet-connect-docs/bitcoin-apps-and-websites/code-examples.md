---
description: Fast-track your NWC integration with these examples
icon: square-terminal
---

# Code Examples

## TypeScript Project (NodeJS, Browser, React Native) <a href="#sample-typescript-project" id="sample-typescript-project"></a>

### Install the SDK

```
npm install @getalby/sdk
```

or

```javascript
yarn add @getalby/sdk
```

## Quick Start

You can use the JS SDK `LN` class to quickly send and receive payments.

```
import { LN } from "@getalby/sdk";
const credentials = "nostr+walletconnect://..."; // the NWC connection credentials
const ln = new LN(credentials);

// to send
await ln.pay("lnbc..."); // pay a lightning invoice

// generate an invoice and act upon it once it's paid
const request = await ln.receive({satoshi: 21});
request.onPaid(giveAccess);
```



## Web Project

### Bitcoin Connect

See also [Bitcoin Connect](https://github.com/getAlby/bitcoin-connect/) if you are developing a web application. Bitcoin Connect is a front end library that does the heavily lifting for you. The library includes web components letting users connect from both desktop and mobile devices or make one time payments from wallets that do not yet support NWC.

You can also filter by NWC wallets, allowing users to create a new NWC connection that can be used by your service (for example: [ZapPlanner](https://zapplanner.albylabs.com/)).&#x20;

### Alby JS SDK

The `NostrWebLNProvider` exposes the [WebLN](https://webln.guide/) interface to execute lightning wallet functionality through Nostr Wallet Connect, such as sending payments, making invoices and getting the node balance.

<details>

<summary>Example: <a href="https://github.com/getAlby/js-sdk/blob/master/examples/nwc/get-balance.js">get-balance.js</a> </summary>

```typescript
// import "websocket-polyfill"; // required in node.js

import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

import { webln as providers } from "../../dist/index.module.js";

const rl = readline.createInterface({ input, output });

const nwcUrl =
  process.env.NWC_URL ||
  (await rl.question("Nostr Wallet Connect URL (nostr+walletconnect://...): "));
rl.close();

const webln = new providers.NostrWebLNProvider({
  nostrWalletConnectUrl: nwcUrl,
});
await webln.enable();
const response = await webln.getBalance();

console.info(response);

webln.close();
```

</details>

[list-transactions.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/list-transactions.js)

[make-invoice.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/make-invoice.js)

[send-payment.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/send-payment.js)

You can explore all the examples [here](https://github.com/getAlby/js-sdk/blob/master/examples/nwc).&#x20;

## Mobile Project <a href="#sample-typescript-project" id="sample-typescript-project"></a>

The `NWCClient` exposes the NWC interface directly, which is more powerful than the WebLN interface and is recommended if you plan to create an application outside of the web (e.g. native mobile/command line/server backend etc.). See [Alby SDK NWCClient documentation](https://github.com/getAlby/js-sdk/blob/master/docs/nwc.md).

<details>

<summary>Example: <a href="https://github.com/getAlby/js-sdk/blob/master/examples/nwc/client/get-balance.js">get-balance.js</a></summary>

```typescript
// import "websocket-polyfill"; // required in node.js

import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

import { nwc } from "../../../dist/index.module.js";

const rl = readline.createInterface({ input, output });

const nwcUrl =
  process.env.NWC_URL ||
  (await rl.question("Nostr Wallet Connect URL (nostr+walletconnect://...): "));
rl.close();

const client = new nwc.NWCClient({
  nostrWalletConnectUrl: nwcUrl,
});
const response = await client.getBalance();

console.info(response);

client.close();
```

</details>

[list-transactions.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/client/list-transactions.js)

[make-invoice.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/client/make-invoice.js)

[pay-invoice.js](https://github.com/getAlby/js-sdk/blob/master/examples/nwc/client/pay-invoice.js)

You find all examples [here](https://github.com/getAlby/js-sdk/tree/master/examples/nwc/client).
