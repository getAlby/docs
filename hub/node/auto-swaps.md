---
description: >-
  Auto-Swaps in Alby Hub allow you to automatically convert funds on Lightning
  into on-chain Bitcoin once a certain threshold is met.
---

# 🔁 Auto-Swaps

### Why you should use it

* **Reduce exposure** to hot wallet balances
* **Automatically secure funds** in a on‑chain wallet (Hub on-chain wallet or cold storage)
* **Maintain receiving capacity** without manual intervention

{% hint style="info" %}
You define rules (threshold, swap amount and destination) and Alby Hub takes care of performing the swaps when the conditions are met.
{% endhint %}

### Use cases

* **Liquidity Management**\
  If you have very one-sided flows (mostly incoming, e.g. merchants) and want to maintain your receiving capacity (i.e. inbound liquidity)
* **Security & Risk management**\
  Automatically sweep exceeding funds to cold storage

### Example

1. Open the wallet page of Alby Hub and click the "Swaps" button
2. Switch to the "Swap out" tab and click the button "Auto-Swaps" at the top right
3. Configure auto-swap
   1. Destination (bitcoin address or xpub)
   2. Spending Balance Threshold (the swap will be triggered by exceeding this amount)
   3. Swap Amount&#x20;
4. Auto-Swaps will now be automatically performed, you'll see them show up in the transaction list

<figure><img src="../.gitbook/assets/Screen Shot 2025-08-27 at 13.05.49.png" alt=""><figcaption></figcaption></figure>

* **Threshold**: 3M sats
* **Swap amount:** 2.5M sats&#x20;
* **Destination**: Cold storage wallet (bitcoin address or xpub)

{% hint style="success" %}
Every time Lightning balance exceeds 3M sats, a new auto-swap is attempted with 2.5M sent to a bitcoin on-chain address, keeping a minimum of 0.5M sats in the hub for day-to-day usage
{% endhint %}

