# How to export transactions for my tax report?

The tax on bitcoin transactions depends on your country of residence and the nature of the activity (investing vs. business activity). Generally, most jurisdictions treat bitcoin as property or an asset, not  yet as currency, and apply either income tax or capital gains tax. \
\
No worries. Alby Hub makes it extremely easy for you to export your transactions in a convenient .csv format to insert it in any accounting and tax reporting software.&#x20;

**Open Alby Hub -> Wallet page -> click on "..." -> select "Export Transactions"**<br>

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

#### Why your Alby Hub wallet balance may differ from your calculated balance:

There are several reasons why the balance shown in your Alby Hub wallet may not match the balance you calculate from your transaction export:

**Transaction fees**\
Outgoing transactions incur transaction fees. These fees are included in the wallet export and are categorized as `feesPaid`. Make sure to account for them (e.g. as an expense).

**Transfers**\
Alby Hub allows you to create sub-wallets. You can increase or reduce the balances of these sub-wallets at any time. Since all sub-wallet balances are still part of your overall Alby Hub wallet balance, you will see corresponding incoming and outgoing transactions in your transaction list. These transactions are marked as _transfer_ in the `description` column.&#x20;

**Channel closures**\
Closing a channel reduces your Alby Hub balance by the amount of BTC held in that channel. These transactions are not included in your export. The BTC from a closed channel is credited to your on-chain balance and may therefore appear as a transfer rather than a spend or income event.

**Channel openings funded with on-chain BTC**\
Opening a channel using on-chain funds increases your Alby Hub balance by the channel’s capacity. These transactions are not included in your export. If you used your own BTC, this is typically a transfer, not an income transaction.\
Channels purchased from Lightning Service Providers (LSPs) are opened empty and therefore do not increase your wallet balance.

**Channel reserves**\
Each channel requires a small channel reserve. While you own this BTC, it is not spendable until the channel is closed and is therefore excluded from the displayed Alby Hub wallet balance. However, the transactions that fund the channel reserve are included in the wallet export.

**On-chain balance**\
You may have funds in your on-chain balance, which you can view on the **Node** page in your Alby Hub. On-chain transactions are not included in your wallet export and must be accounted for separately when reconciling your balances.

{% hint style="info" %}
This is not tax advice. If you have questions or suggestions on how we can make tax reporting easier, please [let us know](https://feedback.getalby.com/-alby-hub-request-a-feature).
{% endhint %}
