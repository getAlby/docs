---
description: '"Don''t panic! Stay cool, stay curious, and keep those channels open! ⚡"'
---

# Why was my lightning channel closed and what to do next?

Channel closures are a **protective measure** designed to safeguard your funds 🔒. Nodes may close channels if the counterparty goes offline or becomes unresponsive to keep funds secure.

1\. [Why channels close unexpectedly?](why-was-my-lightning-channel-closed-and-what-to-do-next.md#why-channels-close-unexpectedly) \
2\. [How to prevent this?](why-was-my-lightning-channel-closed-and-what-to-do-next.md#how-to-prevent-this)\
3\. [Forced closures vs cooperative closures](why-was-my-lightning-channel-closed-and-what-to-do-next.md#forced-closures-vs.-manual-closures)\
4\. [Recovering from a channel closure](why-was-my-lightning-channel-closed-and-what-to-do-next.md#recovering-from-a-channel-closure)

***

## Why Channels Close?

1. **Inactivity:** Channels may be closed after long periods of inactivity (e.g., not using them for two weeks when the first 3 months passed). More info [here](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/faq-alby-hub/how-to-open-a-payment-channel).
2. **Offline:** If you your node is frequently offline (e.g. if you installed Alby Hub on your desktop and shut if off or has network issues), your peer may close the channel.&#x20;
3. **LSP lease period ended**: The LSP may close a channel after the lease period expires. More info [here](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/faq-alby-hub/how-to-open-a-payment-channel).

## **How to Prevent This?**&#x20;

Minimize these three risk factors:\
1️⃣ **Stay Active:** Regularly use your channels to prevent inactivity-related closures.\
2️⃣ **Stay Online:** Avoid frequent reboots and ensure a stable internet connection to prevent forced closures.

{% hint style="info" %}
Choose [**Alby Hub on Alby Cloud**](https://getalby.com/subscription/new) to reduces closure risk. It runs **24/7 on highly reliable data centers**.
{% endhint %}

## Forced closures vs. cooperative closures&#x20;

Not all channel closures are the same. Some happen unexpectedly due to network conditions, while others are **planned and controlled**. Understanding the difference between **forced closures** and **cooperative closures** can help you manage your channels effectively.

#### Force closures

Force closures happen for different reasons. For instance, when your Hub has been offline for too long. If your Alby Hub stays offline, your channel peer may close the channel, as they have no way of knowing why your node is unresponsive. Your funds in the closed channel return to your on-chain balance within two weeks.

#### Cooperative closures

Cooperative closures occur when both nodes are online. These are planned closures where funds return to your on-chain balance after a few block confirmations. If a channel remains inactive for too long, the peer may choose to close it. These closures are not errors but intentional actions to keep the network efficient. 🔒

**Remember:** Keep your bitcoin flowing. The Lightning Network works great if you regularly send and receive payments. &#x20;

## Recovering from a Channel Closure 🔄

The spending balance inside a closed channel returns to your on-chain balance. If it was a cooperative closure that might happen after a few on-chain block confirmations, if it was a forced closure that can take up to 2 weeks. A closed channel means you may have less receiving and spending capacity, but don’t worry, this is only temporarily until you open a new channel.&#x20;

Channel closures are part of being sovereign in lightning. You cannot really completely remove this unfortunate experience, you can only reduce its frequency as much as you can.&#x20;

To prevent future closures, remember to:\
✅ **Stay active** and use your channels regularly.\
✅ **Stay Online:** Minimize downtime and maintain a stable internet connection.

{% hint style="success" %}
If a channel was closed, the best way forward is to **open a new one** 💪. This will restore your Hub’s capacity and keep your lightning experience smooth.&#x20;
{% endhint %}

#### Here is a guide on how to open a channel:&#x20;

{% content-ref url="../node/advanced-increase-spending-balance-with-on-chain-bitcoin.md" %}
[advanced-increase-spending-balance-with-on-chain-bitcoin.md](../node/advanced-increase-spending-balance-with-on-chain-bitcoin.md)
{% endcontent-ref %}
