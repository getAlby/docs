# What are Just-In-Time channels?

Just-In-Time (JIT) lightning channels are on-demand payment channels opened by a [Lightning Service Provider](../bitcoin-wallet-glossary.md#lightning-service-provider) (LSP). They allow you to receive bitcoin over the lightning network instantly, even if you do not have any existing receiving capacity.

The LSP connects your Alby Hub to the Lightning Network and provides the liquidity needed to receive payments. For this service, the LSP charges a small fee, which is displayed on the **Receive** screen in Alby Hub whenever a JIT channel is required.

This typically happens when an incoming payment exceeds your current receiving capacity. In that case, the LSP automatically opens a channel on demand, allowing the payment to be received successfully.

Learn more about receiving capacity and the different ways you can increase it here.

{% content-ref url="../node/increase-receiving-capacity.md" %}
[increase-receiving-capacity.md](../node/increase-receiving-capacity.md)
{% endcontent-ref %}

