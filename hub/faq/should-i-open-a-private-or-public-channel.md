---
description: Choose the best channel type for your lightning network transactions!
---

# Should I open a private or public channel?

To send and receive bitcoin payments, you need to open channels to other peers. There are two types of channels: **private** and **public.**

1 . [Private channels](should-i-open-a-private-or-public-channel.md#id-1.-private-channels)\
2\. [Public channels](should-i-open-a-private-or-public-channel.md#id-2.-public-channels)\
3\. [Should I open private or public channels?](should-i-open-a-private-or-public-channel.md#id-3.-what-channel-should-i-open-then)\
4\. [How to choose private or public channels in Alby Hub](should-i-open-a-private-or-public-channel.md#id-4.-choosing-private-or-public)

***

## **1. Private channels**

Private channels on the lightning network are unannounced, direct peer-to-peer connections that are not broadcast to the public network. Since they are not included in the public network graph, details like channel capacity and channel peer are hidden from external observers.

You don’t need public channels to send or receive payments. Private channels work just fine. Payments can still reach any recipient through the network using routing hints embedded in the lightning invoice.

Nodes that only use private channels cannot route payments for others and are not visible in the network’s gossip protocol.

***

## **2. Public channels**

Public channels on the Bitcoin Lightning Network are announced to the network and included in its graph, making them visible and available for routing payments. They play a key role in decentralized, high-capacity routing, enabling users to facilitate instant payments and earn routing fees (sats) in the process. Individual payments are just as private as those made through private channels.

***

## 3. Should I open private or public channels?

Only two aspect should be taken into account for this decision

**1. If you are a podcaster or need Keysend payments open public channels.**&#x20;

**2. Only open one type of channel:** either make all your channels public or all your channels private.

#### Here is a small summary of their key-differencies

| PRIVATE CHANNEL                                          | PUBLIC CHANNEL                                                                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Cannot route payments of other users                     | If more than one channel, and a balanced inbound and outbound capacity, will route payments of other users on the network |
| Cannot set the routing fee                               | Can set the fee of routing payments                                                                                       |
| Cannot accept Keysend payments (required for podcasting) | Can accept Keysend payments (necessary for a podcaster)                                                                   |
| No channel information publicly broadcasted              | Certain channel information publicly broadcasted (e.g. capacity, channel partner)                                         |

***

## 4. How to choose private or public channels in Alby Hub

Open **Alby Hub** -> **Node** -> **Open Channel** -> click on "**Advanced Options**"

After clicking "Advanced Options," you will see an unchecked box named "Public Channel." By default, new channels are private.

<figure><img src="../.gitbook/assets/Heading (25).png" alt=""><figcaption><p>You can select whether you want a Public Channel or not inside "Advanced Options".</p></figcaption></figure>

{% hint style="success" %}
**Congratulations! 🎉**

Now you understand the difference between Public and Private channels, their uses, and why private channels are recommended as the default option.

You're now equipped to make an informed decision that best suits your needs. Keep up the great work!&#x20;
{% endhint %}
