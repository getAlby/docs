# Should I open multiple channels with the same counterparty?

You might have encountered the situation where you need more receiving capacity or want to increase your lightning balance, and you plan to open a new channel as you did before.

However there are some things to consider.

1. Opening new channels is expensive. Consider swapping out or rebalancing existing channels.
2. You increase your dependence on a single counterparty. Can you open a channel with a different counterparty instead?

## Swap out

This will increase your receiving capacity by transfering bitcoin from your wallet balance to your on-chain balance: [#swap-out](../wallet/swaps.md#swap-out "mention")

## Rebalancing **🧑‍🔧**

If you have more than one channel, consider rebalancing them. This redistributes your bitcoin across channels: [can-i-rebalance-funds-from-one-channel-to-another.md](can-i-rebalance-funds-from-one-channel-to-another.md "mention") <br>

## Choose Another Counterparty [🤓](https://emojipedia.org/nerd-face)

You can check which counterparty nodes you have channels with on your "Node" page.  Then, when opening a new channel, you can select another counterparty when you choose the "Advanced" option.

By default Alby Hub will try to pick a new counterparty for you to reduce dependency on one channel partner and improve your [node health](../node/node-health.md).

**Thanks. We appreciate that you went through the first steps yourself. 💛**
