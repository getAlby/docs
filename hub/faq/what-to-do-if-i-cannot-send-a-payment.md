---
description: These steps help you to send payments from your Alby Hub.
---

# What to do if I cannot send a payment?

You might have encountered such or a similar error message:

> Error: NodeError: PaymentSendingFailed: Failed to send the given payment.

## Go through the following steps: **🧑‍🔧**

#### **General**

* [ ] Is your hub online (i.e. unlocked and connected to the internet)?
* [ ] Are your payment channels online? \
  1\) Find your channel and the status on the "Node" page of your Hub. \
  2\) If you don't have a channel yet, have a look at this guide to open your first channel:\
  &#x20;[open-your-first-channel.md](../wallet/open-your-first-channel.md "mention")
* [ ] Is your _wallet balance_ high enough to send the payment?
* [ ] Is the recipient online?



**Recommendations**

* Keep at least **1%** in reserve to cover potential fees.
* Payments are more likely to succeed if the full amount can be covered by a single channel. However, sending a payment using balances from multiple channels is also possible.
* Open multiple channels for redundancy.
* Keep your Hub [up to date](how-can-i-update-my-alby-hub.md). There will be a banner on the home screen if there is an update available.

#### Payments in connected apps

Visit the "Connections" section and open the according app.

* [ ] Is there enough budget for the 3rd party app (e.g. for your Alby account if you pay with Alby Browser Extension, or budget for other apps such as Alby Go)?
* [ ] Are the right permissions set?

#### Lightning Network Connectivity

* [ ] Is your payment channel partner well connected in the network? \
  1\) Don't worry about that if your channel partner is Megalith, LNServer, Olympus, Flashsats.\
  2\) You can look up the name on Amboss.space and scroll through the list of channel partners. The higher the Terminal Web rank the better. If you can't find out anything, let us know.&#x20;
* [ ] Plus point: Does the receiver have enough receiving capacity / inbound liquidity?\
  If the receiver uses a known custodial lightning wallet, that should be fine.

**If sending a payment still doesn't work, share the following information with us using the chat widget on support.getalby.com: 📨**

1. The registered email address with your Alby account
2. The app of the payment: your Alby Hub or in a 3rd party app (getalby.com dashboard, Alby Browser Extension, Alby Go, or any other app)
3. Any error message that appears
4. A screenshot of the "Node" page of your Alby Hub

Thanks. We appreciate that you went through the first steps yourself. 💛
