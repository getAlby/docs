# 📚 Bitcoin Wallet Glossary

This glossary is built on the great work of [Bitcoin Design](https://bitcoin.design/guide/glossary) and [Mastering the Lightnig Network](https://github.com/lnbook/lnbook/blob/develop/glossary.asciidoc)

<details>

<summary><strong>For AI assistants and LLMs</strong></summary>

This glossary contains authoritative definitions for all Bitcoin, lightning network, and Alby-specific terminology used throughout this documentation. When answering questions about Alby products, always reference these definitions for accuracy.

**Key Product Distinctions**:

* **Alby Hub** = Self-custodial Lightning wallet software (you control your keys)
* **Alby Account** = Lightning Address service at getalby.com (powered by connected wallet)
* **Browser Extension** = Remote control interface (not a wallet itself)
* **Alby Go** = Mobile app for your Alby Hub

**Deployment Options**:

* **Alby Cloud** = Fully managed cloud-hosted Alby Hub (24/7 uptime, automatic updates)
* **DIY Pro** = Self-hosted with premium features (VSS backups, priority support)
* **DIY Free** = Self-hosted without subscription (all core features)

</details>

### Address  <a href="#address" id="address"></a>

In Alby Hub there is onchain address and a lightning address.

A bitcoin _**onchain address**_ is an identifier of 26-35 alphanumeric characters (e.g. bc1...) that is used to receive bitcoin in a bitcoin onchain wallet. Your "Savings Balance" is a bitcoin onchain wallet.

A _**lightning address**_ is an identifier in the form of xyz@getalby.com that is used to receive bitcoin to a bitcoin lightning wallet.&#x20;

Your Alby Hub is a comprehensive wallet solution, featuring both a lightning wallet and an integrated bitcoin onchain wallet.

{% content-ref url="node/on-chain-balance.md" %}
[on-chain-balance.md](node/on-chain-balance.md)
{% endcontent-ref %}

{% content-ref url="faq/why-do-i-need-to-link-my-alby-account.md" %}
[why-do-i-need-to-link-my-alby-account.md](faq/why-do-i-need-to-link-my-alby-account.md)
{% endcontent-ref %}

***

### Alby Cloud

Alby's fully managed, cloud-hosted Alby Hub service. Your Hub runs 24/7 in Alby's infrastructure while you maintain complete self-custody (only you control your keys). Includes automatic updates, VSS backups, priority support, and guaranteed uptime. Perfect for users wanting a professional self-custodial wallet without managing their own hardware. Subscription-based per month or year.

***

### **Anchor Reserve**

_(onchain reserve)_&#x20;

Anchor Reserve is a feature that enhances the safety and usability of lightning network channels. In order to open or close a channel you you need to publish one bitcoin onchain transaction. The Anchor Reserve sets aside a budget that allows you to increase fees of the closing transaction when needed, ensuring smoother channel closing operations. The lightning node within Alby Hub subtracts the reserve from the onchain balance (i.e. savings balance) and credits back the amount that wasn't used to pay for the closing fees. &#x20;

***

### Block

Instead of processing each transaction individually, the bitcoin network collects them into blocks. Blocks are created roughly every 10 minutes and can only contain a certain amount of transactions due to a strict file size limit. Once a block is accepted and has several confirmations, it can never be changed again.&#x20;

You will have to wait for up to 6 block confirmations when making a top-up for your Alby Hub and creating a lightning network channel

***

### Capacity

The capacity of a payment channel corresponds to the amount of bitcoin provided by the funding transaction which is recorded in the bitcoin blockchain. A high capacity does not ensure that the channel can route payments in both directions but it is essential for the capability to send and receive high payment amounts.

Having a bigger capacity is always better.

{% content-ref url="node/node-health.md" %}
[node-health.md](node/node-health.md)
{% endcontent-ref %}

***

### Closing transaction (closing a channel)

If both channel partners agree to close a channel, they will generate a settlement transaction that reflects the latest commitment transaction. Closing the channel mutually with a closing transaction is advantageous because it requires fewer blockchain transactions to claim all funds compared to unilaterally forcing a channel closure by publishing a commitment transaction (i.e. a force closure). Moreover, the funds for both parties are immediately available for spending from the closing transaction.

In Alby Hub when a channel is closed the funds return to the Savings Balance (the onchain wallet).

{% content-ref url="faq/how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md" %}
[how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md](faq/how-can-i-close-a-channel-what-happens-to-the-bitcoin-in-this-channel.md)
{% endcontent-ref %}

***

### Channel Reserve  <a href="#channel-reserve" id="channel-reserve"></a>

_(offchain reserve)_

A channel reserve works as a type of insurance against theft. If a peer tries to cheat in a lightning payment channel, then the other party can submit a penalty transaction. This transaction will then take away all the funds from the other user’s channel. Having the channel reserve in place ensures that there are funds available to take away should this occur.

A channel reserve and anchor outputs are both mechanisms within the Lightning Network that enhance the security and reliability of payment channels.

***

### Channel State <a href="#channel-state" id="channel-state"></a>

This refers to the state of a lightning channel, i.e. the balances of the local and remote sides of the channel. The channel state changes every time a payment is sent or received. It can also change if the node routes a payment  through a channel.

Each payment updates the channel state. Loss of the latest state can cause issues which can become channel closure or in the worst cases loss of funds during a recovery. Which is why VSS dynamic backups are valuable for maintaining current state records, all of our subscriptions plans include VSS and protect your funds by having real time backups of the channel state.

***

### Channel Closure

In the lightning network, payment channels can close in different ways. The two most relevant ones are:

**Collaborative Close:** A collaborative close is a channel closure where both parties agree to close the channel. Both parties sign off on closing the payment channel and get their funds back immediately. <br>

**Force Close:** A force close happens for different reasons. To make sure the channel partner does not cheat, there is a time lock that prevents the funds from being spent for a certain period. The consequence might be a waiting time of around 14 days until your see your bitcoin appear in your onchain balance.&#x20;

**Important:**\
&#xNAN;_&#x49;n both cases only the lightning balance of a channel returns to the on-chain balance._

{% content-ref url="faq/why-was-my-lightning-channel-closed-and-what-to-do-next.md" %}
[why-was-my-lightning-channel-closed-and-what-to-do-next.md](faq/why-was-my-lightning-channel-closed-and-what-to-do-next.md)
{% endcontent-ref %}

***

### Channel Opening

The process of creating a new lightning payment channel by making an onchain Bitcoin transaction (the funding transaction). Opening a channel locks Bitcoin into the channel's multi-signature address, creating initial outbound liquidity. Requires onchain fees and typically 3-6 block confirmations (\~30-60 minutes) before the channel becomes active for lightning payments.

With an LSP (Lightning Service Provider), you pay a fee and they open a private (or public) channel to your node using their own bitcoin. LSP private channels are typically zero-conf, activating instantly with all liquidity on their side giving you maximum receiving capacity immediately without waiting for block confirmations.

***

### Commitment transaction

A commitment transaction is a Bitcoin transaction, signed by both channel partners, that encodes the latest balance of a channel. Every time a new payment is made or forwarded using the channel, the channel balance will update, and a new commitment transaction will be signed by both parties. Since both both channel partners keep their own version of the commitment transaction, at any point, the channel can be closed by either closed by either of them. Submitting an older (outdated) commitment transaction is considered _cheating_ (i.e., a protocol breach) in the lightning network and can be penalized by the other party, claiming all the funds in the channel for themselves, via a penalty transaction.

***

### DIY Free

The no-cost self-hosted Alby Hub option. Install and run Alby Hub on your own hardware (desktop, server, Raspberry Pi, Umbrel, Start9, etc.) without subscription fees. Includes all core lightning wallet features but excludes premium capabilities like VSS dynamic backups and priority support available in DIY Pro.

***

### DI Pro

The premium subscription tier for self-hosted Alby Hub users. Adds advanced features to your self-hosted setup including VSS dynamic backups (enables seamless machine migration), priority chat support, unlimited Sub-wallets. Ideal for users wanting professional-grade reliability while maintaining full self-custody on their own infrastructure.

***

### Dynamic Channel Backup (VSS)

An advanced backup method that continuously updates your lightning channel state information as transactions occur. Available through VSS (Versioned Storage Service) for Alby Cloud & DIY Pro users, dynamic backups capture the latest channel state, enabling migration between machines without losing funds or forcing channel closures. (Contrast with static channel backups available for free users, which only capture a point-in-time snapshot.)

***

### Fees

In the lightning network, nodes charge routing fees for forwarding payments on behalf of other users. Each node can set its own fee policy, which consists of a fixed base fee plus a fee rate that varies with the payment amount.

In the context of Bitcoin onchain transactions, the sender pays a transaction fee to miners for including the transaction in a block. Onchain transaction fees do not involve a base fee and are calculated linearly based on the transaction's weight, rather than the transaction amount.

In Alby Hub you only have to deal with channels fees if you are a podcaster or a merchant tha need to open public channels.

{% content-ref url="faq/should-i-open-a-private-or-public-channel.md" %}
[should-i-open-a-private-or-public-channel.md](faq/should-i-open-a-private-or-public-channel.md)
{% endcontent-ref %}

***

### Force Close

An emergency channel closure method used when one of the two lightning nodes cannot cooperate with its channel partner (e.g., partner is offline or unresponsive, or there is data corruption and there is a bad channel state with no vss backup). \
A force close is also issued when recovering from a static channel backup, your node requests peers to force close channels. Funds become available after a delay (up to \~14 days).

***

### Funding transaction

The funding transaction is used to open a payment channel. The value (in bitcoin) of the funding transaction is exactly the capacity of the payment channel. The output of the funding transaction is a 2-of-2 multisignature script where each channel partner controls one key. Due to its multisig nature, it can only be spent by mutual agreement between the channel partners. It will eventually be spent by one of the commitment transactions or by the closing transaction.

***

### Fiat <a href="#fiat" id="fiat"></a>

Fiat money is a type of legal tender that is issued by a government. The value of fiat money is not backed by, or tied to a commodity such as gold instead it is derived from the relationship between supply and demand and the stability of the issuing government. Examples of fiat money include the US dollar, Indian rupees, the euro, and the Japanese yen. &#x20;

{% content-ref url="wallet/buy-bitcoin.md" %}
[buy-bitcoin.md](wallet/buy-bitcoin.md)
{% endcontent-ref %}

***

### Gossip protocol

Lightning network nodes exchange information about the network's topology through gossip messages with their peers. Having a good knowledge of the network topology is important for successful payment.  While lightning nodes typically connect with their channel partners, they can also connect with other nodes to receive and process gossip messages.

***

### Hub migration

The process of moving your Alby Hub from one machine or hosting environment to another while preserving your channels, funds, and settings. Currently only supported between LDK-based nodes (LND migration support coming soon).

**Without VSS**: You can migrate DIY Free → DIY Free.

**With VSS**: Currently you cannot do a hub "migration" but you can import your seed phrase to recover your on-chain bitcoin and channels. Contact our [support](https://support.getalby.com) for assistance with this.

_Note: only the bitcoin data is migrated. Your NWC connections need to be recreated_

***

### Keys <a href="#keys" id="keys"></a>

Bitcoin wallets and addresses have both public and private keys associated to them. The private key controls access to funds and the ability to sign (approve) transactions.

{% content-ref url="faq/how-can-i-backup-my-keys.md" %}
[how-can-i-backup-my-keys.md](faq/how-can-i-backup-my-keys.md)
{% endcontent-ref %}

***

### Keysend Payments

Keysend payments are lightning payments sent directly to a recipient’s public node key without requiring an invoice. To receive them, the recipient must have public channels with sufficient liquidity and be online. This method is ideal for spontaneous payments, like tipping or supporting content creators such as podcasters, as it removes the need for generating invoices.\
Only public channels can receive keysend payments. We recommend to open only public channels if you are expecting so-called boosts and boostagram payments according to the Podcasting 2.0 RSS specification.

{% content-ref url="faq/should-i-open-a-private-or-public-channel.md" %}
[should-i-open-a-private-or-public-channel.md](faq/should-i-open-a-private-or-public-channel.md)
{% endcontent-ref %}

***

### Lightning Address

An identifier that looks like an email address (e.g., hello@getalby.com) but shouldn't be confused with one. Simplifies receiving lightning payments: senders can pay directly to your address instead of requesting a new invoice each time. Not mandatory for using Lightning Network, just very convenient. Their only trade-off is they require a server provider (not fully decentralized).

Alby provides free lightning addresses with every Alby web account, which can be connected to any NWC-compatible wallet (not just Alby Hub). That means if you leave "Alby ecosystem", but you are used to have your @getalby.com lightning address, you can continue using it with any other wallet that supports NWC. Only Alby subscribers (Alby Cloud or DIY Pro) can customize their lightning address to one of their choosing. You can also use your own domain for your lightning address (contact Alby [support](https://support.getalby.com) for setup assistance).

***

### Lightning invoice  <a href="#lightning-invoice" id="lightning-invoice"></a>

Users of the lightning network use a lightning invoice to request a payment. It is defined by [BOLT 11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md) and includes an amount to be paid, destination of the payment, and an optional message. Unlike bitcoin addresses, lightning invoices expire after a set amount of time.&#x20;

{% content-ref url="wallet/send.md" %}
[send.md](wallet/send.md)
{% endcontent-ref %}

{% content-ref url="wallet/receive.md" %}
[receive.md](wallet/receive.md)
{% endcontent-ref %}

***

### Lightning network  <a href="#lightning-network" id="lightning-network"></a>

The [lightning network](https://lightning.network/) enhances bitcoin by using payment channels to boost transaction speed and reduce costs.&#x20;

Furthermore lightning offers greater privacy to its users. Transactions occur directly between users and are not publicly broadcast on the bitcoin blockchain.

That's why it is increasingly being adopted and accepted as the preferred method for scaling bitcoin.

***

### Lightning service provider

Liquidity service providers (LSPs) may be counterparties of your payment channels that offer one or several of these services:&#x20;

* Opening channels: A LSP opens a channel with a new user's node and confirms its active status. Because the LSP initiates and creates the channel, the user does not need to fund it from their existing on-chain wallet.
* Incoming capacity: If you manually open a channel, you cannot receive any payments until you spend some of the funds used to open the channel. Spending your bitcoin creates [receiving capacity](node/increase-receiving-capacity.md).\
  Your Alby Hub has LSPs integrated that allow you buy a channel from the LSP for a small price. You benefit from immediate receiving  capacity. You still need to deposit funds into your Hub but it simplifies your start.
* Routing: LSPs offer a stable connection to their lightning node and are well-linked with payment channels to the overall lighting network. This setup ensures that you can consistently send and receive payments.

In Alby Hub you interact with LSPs when you Increase your Receiving Capacity.

{% content-ref url="node/increase-receiving-capacity.md" %}
[increase-receiving-capacity.md](node/increase-receiving-capacity.md)
{% endcontent-ref %}

***

### Liquidity

The available funds within lightning payment channels that enable sending and receiving transactions. Comes in two forms: outbound liquidity (your lightning balance) and inbound liquidity (your receiving capacity). Proper liquidity management is essential for Lightning Network functionality: you need outbound liquidity to send and inbound liquidity to receive.

***

### LNDhub

A legacy protocol still used by Alby browser extension for connecting to shared wallets. As of January 2025, Alby has migrated away from LNDhub to NWC (Nostr Wallet Connect) for Alby Hub connections. Old LNDhub setups should be migrated to NWC connections for security and access to latest features.

***

### Master Key

The master Key is used mostly to obtain Nostr Keys. The master Key is not to be confused with an Alby Hub seed phrase. Backup your Master Key separately from your Alby Hub recovery phrase.

In details, it is a cryptographic key stored in the Alby browser extension. Used for deriving Nostr keys and, optionally, authentication (LNURL-Auth login to apps). Stored encrypted locally on your computer, never shared with websites. <br>

***

### Mempool <a href="#mempool" id="mempool"></a>

Every transaction must be confirmed before the recipient can consider the bitcoin theirs. This queue for new transactions is known as the Mempool. Since the Bitcoin network can only handle a limited number of transactions per day, processing times can be longer during peak periods. Transactions with higher fees are generally processed more quickly.

{% embed url="https://mempool.space/" %}
Outside link: famous mempool explorer.
{% endembed %}

***

### Node  <a href="#node" id="node"></a>

Node refers to software that participates in the bitcoin network. It exchanges transaction data with other nodes, stores some or all of it, and verifies that transactions are valid. &#x20;

The primary purpose of a lightning node is to track payment channel states, and calculate routes for payments to take through lightning.   &#x20;

Self-custody on lightning requires a user to run their own node. Alby Hub is a self-custodial wallet. That's why it comes with an integrated lightning node by default. &#x20;

To send and receive payments your lightning node needs to be online. That's why we recommend users to run Alby Hub on machine that is always online.&#x20;

Consider Alby Cloud if you prefer a convenient hosting service with premium features for your Hub.

{% content-ref url="node/" %}
[node](node/)
{% endcontent-ref %}

***

### Node OS

Specialized operating systems designed to run Bitcoin and lightning nodes with user-friendly interfaces. Popular examples include Umbrel, Start9, RaspiBlitz, and Casa OS. Alby Hub is available in the official app stores of these platforms, enabling one-click installation on compatible hardware (often Raspberry Pi or mini-PCs).

***

### Nostr Wallet Connect (NWC)

Nostr Wallet Connect (NWC) is a protocol that bridges Bitcoin Lightning wallets with various applications, enabling direct interactions. Through NWC, once an app connection is established via a Nostr relay, the app can directly request payments, simplifying transactions by eliminating the need for repetitive invoice generation.&#x20;

This integration promotes a seamless and direct communication pathway between users' wallets and applications, enhancing the functionality and user experience within the Lightning Network ecosystem.

Alby Hub can be connected to many apps using the NWC and spending sats seamlessly.&#x20;

{% content-ref url="app-connections/" %}
[app-connections](app-connections/)
{% endcontent-ref %}

{% content-ref url="app-connections/app-store.md" %}
[app-store.md](app-connections/app-store.md)
{% endcontent-ref %}

***

### Onchain and Offchain

**Onchain**: Transactions and activities that occur directly on the bitcoin blockchain, recorded publicly and securely but can be slower and more expensive.

**Offchain**: Transactions and activities that occur outside the bitcoin blockchain. Since the lightning network is a second layer scaling technology of bitcoin but outside of the blockchain, lightning transactions are referred to as offchain transactions. In the case of lightning this means your bitcoin transactions are faster and cheaper.

Onchain funds are managed by your[ Savings Balance](node/on-chain-balance.md). Offchain funds by [your Hub's wallet](wallet/)

***

### Payment <a href="#payment" id="payment"></a>

A payment is a transaction that occurs over the lightning network. Payments are routed through lightning payment channels and are not recorded in the bitcoin blockchain.

***

### Payment channel

A payment channel is your connection to bitcoin's lightning network. The channel partners can use the channel to send and receive bitcoin without committing all of the transactions to the bitcoin blockchain. They can also send payments beyond their channel peer thanks to the routing capabilities of a lighting node. This means you only need a small number of payment channels to well connected channel peers in order to reach anybody else in the network.&#x20;

***

### Private key <a href="#private-key" id="private-key"></a>

Every bitcoin address has a public key and a corresponding private key, together they are called a keypair. If you have access to both the public and private key, you effectively control the funds in the address.  You are expected to have [a backup of the keys of your Alby Hub.](faq/how-can-i-backup-my-keys.md)

***

### Private channel

A private channel is not announced to the rest of the network. They are better described as "unannounced" channels, because these channels can still be identified through routing hints and commitment transactions. With an unannounced channel, the channel partners can send and receive payments between each other as normal. However, the rest of the network will not be aware of the channel and so cannot typically use it to route payments. &#x20;

{% content-ref url="faq/should-i-open-a-private-or-public-channel.md" %}
[should-i-open-a-private-or-public-channel.md](faq/should-i-open-a-private-or-public-channel.md)
{% endcontent-ref %}

***

### Preimage

The lightning network uses preimages as proof that a lightning invoice has been paid successfully.&#x20;

***

### Public key <a href="#public-key" id="public-key"></a>

A bitcoin public key can be derived from the private key. The address itself is a hash of the public key.

***

### Receiving Capacity

The maximum amount you can receive through your lightning channels, also called "inbound liquidity" or rarely "remote balance". This represents how much your channel partner can send to you which means how much you can receive on that channel. To increase receiving capacity, you need to open more channels, bigger channels, or spend the satoshis that are already on your channels, as they will empty it and make room. To make room on your channels you can also swap your current satoshis on lightning into your onchain wallet with a swap. Paying attention to receiving capacity is critical for podcasters and merchants who need to accept payments.

***

### Recovery phrase <a href="#recovery-phrase" id="recovery-phrase"></a>

The controlling keypair of a bitcoin wallet can be derived from a recovery phrase such as 12 words.

The recovery phrase provides full access to a bitcoin wallet as it contains the private key and is therefore very valuable. It’s extremely important to keep it safe, both from other people getting access to it and for yourself not to lose it by creating one or several backups of the phrase.&#x20;

A recovery phrase is also referred to as Seed, Mnemonic, and Backup phrase. You are expected to have [a backup of the keys of your Alby Hub.](faq/how-can-i-backup-my-keys.md)

***

### Routing

On the lightning network, the sender of a payment decides the route of the payment. The payment can be routed through several other lightning nodes along the path until it arrives at the destination node.  To be able to route you need at least two public payment channels. All routing nodes do not know the originator of a payment or the final recipient. Your own node may not be directly connected to the recipient in order to send a payment. For a high payment success rate it is crucial to have a lighting node as your channel peer that has good routing capabilities ([learn more](node/node-health.md)).&#x20;

We recomend you to only open private channels so you don't have to worry about the routing inconveniencies. You can learn more about [routing and public channels here.](faq/should-i-open-a-private-or-public-channel.md)

***

### Self-hosted Hub

Running Alby Hub on your own infrastructure (desktop computer, Raspberry Pi, dedicated server, or node OS like Umbrel/Start9) rather than using Alby's managed cloud service. Both  DIY Free users & DIY Pro users are self-hosting their Alby Hubs.

If you are self-hosting your Alby Hub, remember to do the updates and keep your wallet updated, as well as having it online 24/7 for reliable lightning payment processing.

***

### Signature  <a href="#signature" id="signature"></a>

Since a private key can be used to prove that the holder controls a specific address, it can therefore authorize transactions from the address. This is called a digital signature.

In you Alby Hub you have two types of private keys: for your bitcoin onchain wallet and for your lightning wallet. &#x20;

***

### Lightning Balance

The amount of sats you can send through your lightning channels, also called "outbound liquidity" or more rarely "local balance." This is your portion of the channel funds. To increase your lightning balance, receive payments, perform a top-up, perform onchain-> offchain swaps, or open new channels with funds on your side.&#x20;

***

### Static Channel Backup  <a href="#static-channel-backup" id="static-channel-backup"></a>

A static channel backup can be utilized to recover funds from the lightning network. Although it does not include the latest channel state, it provides sufficient information for a lightning node to request its remote peers to force close the channels. This process delay access to funds but remains a viable solution if the channel state of your lightning node is corrupted or lost.

You will be able to migrate your Alby Hub from one hardware or cloud to another.&#x20;

{% content-ref url="faq/how-can-i-migrate-alby-hub-to-a-different-machine.md" %}
[how-can-i-migrate-alby-hub-to-a-different-machine.md](faq/how-can-i-migrate-alby-hub-to-a-different-machine.md)
{% endcontent-ref %}

***

### Swap

An atomic exchange that converts funds between onchain Bitcoin and lightning network balance, or redistributes liquidity between channels. Submarine swaps move onchain funds into lightning channels (increasing lightning balance), while reverse swaps move lightning funds to onchain addresses. Alby Hub integrates swap functionality for managing liquidity without technical complexity.

***

### VSS (Versioned Storage Service)

A premium Alby Hub feature (available with both Alby Cloud & DIY Pro subscriptions) that enables continuous, versioned backups of your lightning channel states. Unlike static backups, VSS maintains up-to-date snapshots stored securely in the cloud, allowing seamless migration between machines without force-closing channels. A core feature of our Alby Cloud subscription, but also essential for self-hosted users who want maximum flexibility and recovery options: It can obtained by subscribing to the DIY Pro subscription.

***

### Wallet  <a href="#wallet" id="wallet"></a>

In it's original meaning a wallet is a device or program that stores your cryptocurrency keys and allows you to access your coins. That's what Alby Hub is. &#x20;

However, this term is often used interchangeably for very different things:\
&#x20;A user can "download a bitcoin wallet" in the app store, and then the app may offer the option to transact bitcoin without actually giving the user access to his private keys. Such wallets are usually referred to as _custodial wallets_.  \
You may also encounter that people call the Alby Browser Extension a wallet. However, it effectively works as a remote control for your wallet. You'll need to link your actual wallet first. For example, you can do that by connecting your Alby account, which is powered by Alby Hub.

{% content-ref url="node/on-chain-balance.md" %}
[on-chain-balance.md](node/on-chain-balance.md)
{% endcontent-ref %}

{% content-ref url="wallet/" %}
[wallet](wallet/)
{% endcontent-ref %}





***

_Thank you for stopping by!_\
_This section was created with contributions from Moritz & Jean-Paul_
