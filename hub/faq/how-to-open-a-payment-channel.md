---
description: Learn how to open a payment channel in your Alby Hub.
hidden: true
---

# How to open a payment channel?

Payment channels are a foundational aspect of the lightning network. They are extremely powerful because they enable near instant and cheap bitcoin transactions. In Alby Hub, there are two main reasons to open a channel.&#x20;

1. Top up your Lightning Balance with BTC for spending on apps or sending to friends&#x20;
2. Ensure you have enough Receiving Capacity to receive tips, boostagrams, or payments

With Alby Hub you are **in control of your funds AND of the transaction fees**, because you choose the channel partner yourself. That's a big advantage over custodial wallets and most non-custodial wallets.

## Open a payment channel

Click on the link below to see an interactive demo of opening a payment channel in your Alby Hub:

{% content-ref url="../node/increase-receiving-capacity.md" %}
[increase-receiving-capacity.md](../node/increase-receiving-capacity.md)
{% endcontent-ref %}

{% hint style="info" %}
_**Important**_: channels can be public or private.

* **Only open private channels**. Unless you are a podcaster or musician planning to receive Value 4 Value payments or boostagrams. In that case you need public channels.
* **Do not mix** to mix private and public channels
{% endhint %}

## Which Lightning Service Provider to choose?

Alby Hub makes it extremely easy to open a payment channel. It offers a selection of Lightning Service Providers (LSPs) from which users can lease channels. In return you have a consistent and reliable payment experience. By default Alby Hub will automatically choose the best channel partner for you and you are free to choose yourself via "Advanced" settings.&#x20;

**Overview of available LSPs**

<table><thead><tr><th width="115.6666259765625">LSP</th><th width="128.5555419921875">Minimum Channel duration</th><th width="107.3333740234375">Sending fees*</th><th width="312.4444580078125">Comment</th><th>Support</th></tr></thead><tbody><tr><td>Flashsats</td><td>3 months</td><td>0.2% + 0.001 sat</td><td>Your channel stays open longer if you send or receive at least one payment per 30 days and a maximum of 12 months.<br>The channel will be closed if your Hub is offline for more than 2 weeks.</td><td><a href="https://flashsats.xyz/api-docs/index.html">Contact</a></td></tr><tr><td>LNServer</td><td>3 months</td><td>0%  </td><td></td><td><a href="https://lnserver.com/about-us">Contact</a></td></tr><tr><td>Megalith LSP</td><td>3 months</td><td>0.1% + 1 sat</td><td>Your channel stays open longer if you send or receive at least one payment per 30 days.</td><td><a href="https://megalithic.me/contact">Contact</a></td></tr><tr><td>Olympus by Zeus</td><td>12 months</td><td>0%</td><td>The channel will be closed immediately after the duration.</td><td><a href="https://docs.zeusln.app/category/services/">Contact</a></td></tr><tr><td>Magma by Amboss</td><td>1 month</td><td>variable</td><td>The channel stays open up to 6 months.</td><td><a href="mailto:info@amboss.tech">Contact</a></td></tr></tbody></table>

\*Total sending fees depend on routing nodes along the payment route to the recipient.\
There are zero fees for receiving payments.

{% hint style="success" %}
Great! 🎉 Now you understand why and how to open a channel!

_**Tip:**_ It is recommended to have more than one channel if you want to be insured against downtimes of a single channel partner.
{% endhint %}
