---
description: Master your channels like a pro and keep your bitcoin safe! 💼
---

# How can I close a channel? What happens to the bitcoin in this channel?

While the channel is open, you will be able to send and receive bitcoin with anyone on the lightning network. You can have more than one channel. And just as you can open channels, you can also close them at will.

1 . [Reasons for closing a channel](how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md#reasons-for-closing-a-channel)\
2\. [Close a channel](how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md#close-a-channel)\
3\. [So, where are my bitcoin?](how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md#so-where-are-the-funds)

***

## Reasons for closing a channel

**Stay in control of your channels and keep your Alby Hub self-custodial wallet in good shape!** 💪

You may occasionally want to close a channel to keep your Alby Hub self-custodial wallet in good shape.

Here are some common reasons to do so:

* You accidentally opened a public channel, and it’s interfering with your private channels. Closing it can help restore normal functionality.
* You opened a channel (public or private) with a peer who has lost access to their node and asked you to close it so both of you can recover funds on-chain.
* You need funds in your on-chain balance and want to close a channel to access them.
* You want to optimize or reduce routing fees by selecting more cost-efficient channel partners. With Alby Hub, you’re in full control of your routing strategy.
* Any other situation where closing a channel better fits your setup or needs.

***

## How to close a channel

In the **“Node”** section, click the three dots next to the channel and select **“Close Channel.”** A popup will appear with a warning and details about the peer you opened the channel with. Review the information, then click **“OK.”** &#x20;

{% hint style="danger" %}
Closing a channel is an irreversible process. It may take up to 6 blockchain confirmations, or about an hour, to be fully closed. If it was your only channel, you won't be able to send or receive bitcoin through the lightning network.
{% endhint %}

<figure><img src="../.gitbook/assets/Screenshot 12-18-2024 15.01.45.png" alt=""><figcaption><p>All your channels are available in the "Node" section of your Alby Hub.</p></figcaption></figure>

#### There are two types of channel closures: normal and force close.

{% tabs %}
{% tab title="COOPERATIVE CLOSE" %}
**Cooperative closures** occur when the counterparty is online. The closure can be initiated by you or by your counterparty. When the channel is closed, the funds will be returned to your On-Chain Balance accessible on the Node page of your Hub.
{% endtab %}

{% tab title="FORCE CLOSE" %}
**Force closures** happen for different reasons. For instance, when the counterparty is offline, and you need to close the channel without waiting for them to come back online. These types of closures should be even rarer. The channel will take up to 15 days to close, this is a failsafe to avoid cheating. After 15 days the funds will be returned to your On-Chain Balance accessible on the Node page of your Hub.
{% endtab %}
{% endtabs %}

After clicking on **"Close Channel"** you'll see the following screens to finalize the closing.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 12-18-2024 15.02.09.png" alt=""><figcaption><p>"Normal close" is the default option and is recommended. Avoid force closures unless absolutely necessary.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/Screenshot 12-18-2024 15.02.25.png" alt=""><figcaption><p>The closing transaction will briefly appear after clicking on "Close Channel".</p></figcaption></figure>



***

## **So, where are my bitcoin?**&#x20;

**Channel closed? No worries! Your bitcoin are just taking a little break.** 💤🔒

The funds of your channel will appear on the On-Chain Balance of your Alby Hub self-custodial wallet. after waiting the period of time necessary for the channel to be closed. This means the funds will re-appear and be ready to use approximately 60 minutes after a normal close or 15 days after a force close.

Here you can see in the On-Chain Balance where to look for your funds after the channel was closed:

<figure><img src="../.gitbook/assets/Screenshot 12-18-2024 17.53.03.png" alt=""><figcaption><p>On-Chain Balance are the funds that you have on the bitcoin blockchain</p></figcaption></figure>

{% hint style="success" %}
Your funds can always be located: they're either in your channel or in your On-Chain Balance. If anything happens to your channel or your Alby Hub, you can always recover the funds on-chain with your recovery phrase consisting of 12-word keys. This another tremendous advantage over traditional monetary systems. 😊
{% endhint %}
