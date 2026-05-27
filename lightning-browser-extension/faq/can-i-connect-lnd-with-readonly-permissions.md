# Can I connect LND with readonly permissions?

Depends on what you want to do with Alby. But if you for example only want to receive payments you can give the Alby extension a LND macaroon with limited permissions.&#x20;

The following permissions are typically used. Depending on your usage you can limit these permissions. Use [LND's macaroon bakery](https://github.com/lightningnetwork/lnd/blob/master/macaroons/README.md#bakery) to generate a custom macaroon. ([learn more](https://github.com/lightningnetwork/lnd/blob/master/macaroons/README.md#bakery))

* invoices:write - create invoices
* invoices:read - check invoices
* offchain:read - display the balance
* info:read - read node information
* peers:write - for LNURL-channel requests
* message:write - sign a message (e.g. for LNURL-auth)
* offchain:write - to send payments

Note: some lightning web applications using [webln.request()](https://www.webln.guide/building-lightning-apps/webln-reference/webln.request) might request other calls.
