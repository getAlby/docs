# What permissions does the extension require at installation?

This is the list of requirements required to run the Alby extension:

```json
...
"host_permissions": ["*://*/*"],
"permissions": [
    "identity"
    "nativeMessaging",
    "notifications",
    "scripting",
    "storage",
    "tabs",
    "unlimitedStorage"
]
...
```

**Host Permissions**\
Allows the extension to read information from websites you visit (e.g. meta tags with lightning information) and inject JavaScript to provide websites with APIs such as WebLN, Nostr, webbtc and liquid.&#x20;

**Identity**\
Needed to connect to your Alby Account via OAuth2 APIs.&#x20;

**Native messaging**\
If you want to connect your own node via TOR this allows the extension to communicate with the Alby Companion App (which connects your browser to the TOR network)

**Notifications**\
Alby notifies you of successful or failed payments through browser notifications.

**Scripting**\
Allows Alby to inject JavaScript into websites to offers APIs for websites to interact with your wallet.&#x20;

**Storage**\
Allows the extension to save credentials (always encrypted with your password) and other information (e.g. permissions you gave to certain websites, etc).

**Tabs**\
Allows to get the active tab and fetch payment information provided by websites in their meta tags.&#x20;

**Unlimited Storage**\
Storage is usually hard-limited to 10 MB, this is mostly just a preemptive measure for users not to hit this limit.&#x20;

<br>
