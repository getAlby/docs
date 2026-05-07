# How to earn routing fees?

## What are routing fees?

Payment routing fees are the small charges you pay when sending a bitcoin payment across the lightning network through intermediate routing nodes (not directly to your peer).

With Alby Hub you can operate such a routing node yourself and earn fees from routing payments through the network.&#x20;

## How to earn routing fees?

To start routing you need take care of four aspects

1. [Public lightning channels](how-to-earn-routing-fees.md#id-1.-public-lightning-channels)
2. [Routing fees](how-to-earn-routing-fees.md#id-2.-routing-fees)
3. [Receiving capacity (aka channel liquidity)](how-to-earn-routing-fees.md#id-3.-receiving-capacity-aka-channel-liquidity)
4. [Analytics](how-to-earn-routing-fees.md#id-4.-analytics)

Let's break it down together.

## 1. Public Lightning Channels

The lightning network consists of public and private channels. Only public lightning channels are able to route payments between nodes. \
\
**Key properties of public channels**

1. **Announced in the network graph**
   * When you open a public channel, your node broadcasts a message that includes the channel ID, capacity, and fees (base fee, fee rate).
   * Other nodes then know they can try to use your channel for routing payments.
2. **Visible in explorers**
   * Public channels show up in tools like Amboss.space or mempool.space lightning explorer.
   * Anyone can see your node’s alias, capacity, uptime, and fee policies.
3. **Routable**
   * Other nodes can attempt to forward payments through your channel if the liquidity and fees make sense.
   * This allows you to earn **routing fees**.

Note, if you don't want to route payments, you are better off with a private channel. You are still able to send or receive payments across the whole network.

👉 [How to open a public channel](https://guides.getalby.com/user-guide/alby-hub/faq/should-i-open-a-private-or-public-channel#id-4.-choosing-private-or-public)

## 2. Routing Fees

Each node operator sets their own fee policy. The total fee for a routed payment has two components:

1. **Base Fee (Fixed per payment attempt)**
   * A small flat amount, usually denominated in **millisatoshis (msat)**.
   * Default is often **1 satoshi** (1,000 msat), but many nodes set it to zero to attract routing traffic.
   * This fee is independent of payment size.
2. **Fee Rate (Proportional Fee)**
   * A percentage of the payment amount, expressed in **parts per million (ppm)**.
   * Example: A fee rate of **1,000 ppm = 0.1%** of the forwarded amount.
   * So, if you route 100,000 sats through a node charging 1,000 ppm, you pay 100 sats in proportional fees.

#### **2.1 Formula of the routing fee for one payment:**

`Fee = Base Fee + ( Amount × Fee Rate )`

#### 2.2 Example

Suppose someone sends **100,000 sats** and it passes through your node:

* **Your fee policy:** base 1 sat, 100 ppm. **Your fee income** = 1 + (100,000 × 0.0001) = **11 sats**&#x20;

#### **2.3 How to change routing fees in Alby Hub**

Navigate to "Node" -> click on the three dots next to the channel and select "Set Routing Fees".

<figure><img src="../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>

Routing fees can only be changed for public channels. If you only open private channels, you will not see the option to change the routing fees. If you would like to route payments yourself, you should set a competitive routing fee. Otherwise leave the default fees unchanged.

<figure><img src="../.gitbook/assets/image (229).png" alt=""><figcaption></figcaption></figure>

## 3. Receiving Capacity (aka Channel Liquidity)

When you route payments, the liquidity in the channel shifts from one side to the other. Sometimes payments flow in both directions through channels with zero effect on the liquidity. But if payments mainly flow in one direction you may also need to rebalance it yourself to keep enough liquidity on each side for routing.

Alby Hub offers you several options to manage your liquidity:

#### 3.1 Open a payment channel

Great when you need a lot of capacity in the direction of your channel partner

[advanced-increase-spending-balance-with-on-chain-bitcoin.md](../node/advanced-increase-spending-balance-with-on-chain-bitcoin.md "mention")

#### 3.2 Swaps

Great to increase or reduce liquidity for a certain channel

[swaps.md](../wallet/swaps.md "mention")

#### 3.3 Rebalancing

Great to balance the liquidity equally across several channels

👉[can-i-rebalance-funds-from-one-channel-to-another.md](can-i-rebalance-funds-from-one-channel-to-another.md "mention")

## 4. Analytics

Alby Hub provides you with valuable insights into your routing activities. Check the "Home" tab of your Hub.&#x20;

<figure><img src="../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

