---
description: You can always recover your funds even if you lose access to your hub.
---

# What happens if I lose access to my Hub while a swap is in progress?

In Alby Hub can seamlessly transfer bitcoin between your wallet balance (lightning) and on-chain balance through so called swaps.

{% hint style="info" %}
If a swap is in progress, please keep your Hub online to ensure the swap completes successfully. If you restart your Hub, pending swaps will be resumed.
{% endhint %}

## Swap Out (Lightning ➡️ On-chain)

Lightning to on-chain swaps are atomic. Make sure to read our [backup guide](https://guides.getalby.com/user-guide/alby-hub/backups-and-recover) to ensure you can always recover funds from your Hub.

## Swap In (On-chain ➡️ Lightning)

Swapping in requires you to send on-chain bitcoin from your wallet to an on-chain address. These funds will be claimed by Boltz if the swap succeeds. In case the swap fails (for example, Boltz cannot reach your Hub to make the payment, or you do not have enough receiving capacity in your channels, or you accidentally send the wrong amount), you must be able to recover the funds that you have sent to the on-chain address.

As long as you leave your Hub online, Alby Hub will automatically recover funds from failed swaps into your Hub's on-chain balance.

### Initiating Refunds

If the swap does still not succeed 24 hours after you initiated the swap, you can go to **Settings -> Debug Tools** in your Hub and press the **List Swaps** button. Find the swap ID of the failed swap, and then click the **Refund Swap** button on the same page. You'll see a field to **paste the swap ID** and **click confirm** to request the refund.

### Last-Resort Recovery

In case you lose access to your Hub (e.g. you self-host and your hard-drive dies - [Alby Cloud](../alby-hub-flavors/alby-cloud.md) doesn't have this problem :wink:) or if the **Refund Swap** button does not work, you can still recover funds from failed swaps as long as you have [backed up your recovery phrase](https://guides.getalby.com/user-guide/alby-hub/backups-and-recover).

#### Step 1: Derive Your Boltz Mnemonic From Your Recovery Phrase

{% hint style="info" %}
In the following section you will need to enter your recovery phrase in an application to derive your Boltz mnemonic. **DO NOT enter your recovery phrase in any website or application that you do not trust. If you have any concerns, please contact** [**Alby Support**](https://support.getalby.com/)**.**
{% endhint %}

{% hint style="warning" %}
If you still have access to Alby Hub, you can go to **Settings -> Debug Tools** and press the **Swap Mnemonic** button to reveal your Boltz Mnemonic.
{% endhint %}

Alby Hub uses a dedicated mnemonic derived from your main recovery phrase for Boltz swaps (see [BIP-85](https://bip85.com/)). To derive this mnemonic you can import your Hub's recovery phrase into any wallet that supports BIP-85. Some hardware wallets support BIP-85 child mnemonic derivation. [Ian Coleman's BIP39 tool](https://github.com/iancoleman/bip39) (_Standalone offline version recommended_) also supports deriving BIP-85 child mnemonics - search for "Show BIP85" and check the checkbo&#x78;**.**

Use the following derivation index: **128260**

#### Step 2: Execute Boltz Rescue

Visit the [Boltz Refund Page](https://boltz.exchange/refund/external/btc?mode=rescue-key). Enter your **Boltz Mnemonic.** DO NOT enter your boltz mnemonic in any website other than the official boltz.exchange website. Your Boltz mnemonic will not be sent to Boltz - it will only be used client-side by the [Boltz Web App](https://github.com/BoltzExchange/boltz-web-app/).&#x20;

The swaps that can be rescued will show up in a list. When you click on one you will be able to provide a refund address from your on-chain bitcoin wallet.

