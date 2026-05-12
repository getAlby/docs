---
description: >-
  Backing up your Alby Hub is essential to ensure your funds can be recovered in
  case you lose access to your node. Taking the time to do it right ensures
  everything is safe and easily recoverable.
---

# 🔐 Backups & Recover

{% hint style="info" %}
This guide applies to the default node implementation of Alby Hub (LDK) only. If you're using a different node backend, please refer to its own documentation for backup instructions.
{% endhint %}

**Jump directly to the setup that applies to you:**

1. [Alby Hub with Pro Cloud](backups-and-recover.md#alby-hub-with-pro-cloud)
2. [Alby Hub with Pro](backups-and-recover.md#alby-hub-with-pro)
3. [Alby Hub self-hosted with an Alby account](backups-and-recover.md#alby-hub-self-hosted-diy-with-an-alby-account)
4. [Alby Hub self-hosted without an Alby account](backups-and-recover.md#alby-hub-self-hosted-without-an-alby-account)

## Alby Hub with Pro Cloud&#x20;

### On-chain Balance and Lightning Balance

**Backup:** Find and backup your 12-word recovery phrase in your Alby Hub [here](faq/how-can-i-backup-my-keys.md)  to recover your On-chain Balance and Lightning Balance anytime.&#x20;

Your Lightning Balance data is securely encrypted using your 12-word recovery phrase and is dynamically updated in your Alby account. \
To see if automatic channel backups are enabled for your Hub go to Settings and select "Backups". &#x20;

**Recover:** Start a new Alby Hub in the same Alby account -> Select "Advanced Setup" -> enter your 12-word recovery phrase. Your On-chain and Lightning Balance will be fully restored 🚀.

{% hint style="info" %}
As Pro Cloud subscriber you only need to backup your recovery phrase and remember your Alby account.
{% endhint %}

## Alby Hub with Pro&#x20;

### On-chain Balance and Lightning Balance

**Backup:** Find and backup your 12-word recovery phrase in your Alby Hub [here](faq/how-can-i-backup-my-keys.md)  to recover your On-chain Balance and Lightning Balance anytime.&#x20;

Your Lightning Balance data is securely encrypted using your 12-word recovery phrase and is dynamically updated in your Alby account. \
To see if automatic channel backups are enabled for your Hub go to Settings and select "Backups". &#x20;

**Recover:** Start a new Alby Hub in the same Alby account -> Select "Advanced Setup" -> enter your 12-word recovery phrase. Your On-chain and Lightning Balance will be fully restored 🚀.

{% hint style="info" %}
As Pro subscriber you only need to backup your recovery phrase and remember your Alby account.
{% endhint %}

## Alby Hub self-hosted (DIY) with an Alby account

### On-chain Balance

**Backup:** Find and backup your 12-word recovery phrase in your Alby Hub [here](faq/how-can-i-backup-my-keys.md) to recover your on-chain balance anytime.

**Recover:** Enter the 12-word recovery phrase into a new Alby Hub or another bitcoin wallet.

### Lightning Balance

**Backup:** Alby stores a static channel backup automatically in your Alby account.

**Recover:** Use [this app](https://github.com/getAlby/hub-recovery) to recover the sats of your Lightning Balance. It asks your channel partners to force-close the channels to your node. Funds from channels may take up to 14 days to return to your on-chain balance. You will need to open new channels to continue sending and receiving transactions.

{% hint style="info" %}
As an Alby account user you only need to backup your recovery phrase.&#x20;
{% endhint %}

## Alby Hub self-hosted without an Alby account

### On-chain Balance

**Backup:** Find and backup your 12-word recovery phrase in your Alby Hub [here](faq/how-can-i-backup-my-keys.md) to recover your on-chain balance anytime.&#x20;

**Recover:** Enter the 12-word recovery phrase into a new Alby Hub or another bitcoin wallet.

### Lightning Balance

**Backup:** You need to make this backup each time you have a new lighting channel. If new channels were made after the backup, you could risk losing funds.

* Go to the working directory of your Alby Hub
* Back up the newest file in `.data/ldk/static_channel_backups/`

**Recover:** Use [this app](https://github.com/getAlby/hub-recovery) to recover the sats of your Lightning Balance. It asks your channel partners to force-close the channel to your node. Funds from channels may take up to 14 days to return to your on-chain balance. You will need to open new channels to continue sending and receiving transactions.

{% hint style="warning" %}
Without an Alby account you need to manually back up your recovery phrase and create backups of your channels each time you have a new channel. If new channels were made after the backup, you could risk losing funds.&#x20;
{% endhint %}

## Backup Checklist

{% tabs %}
{% tab title="✨ Pro & Pro Cloud Subscription" %}
* [ ] Recovery phrase
* [ ] Access to your Alby account: Immediate recovery of your funds
{% endtab %}

{% tab title="Self-hosted (no subscription)" %}
* [ ] Recovery Phrase (Recovery process will force close your lightning channels)
{% endtab %}

{% tab title="Self-hosted (no Alby account)" %}
* [ ] Recovery Phrase
* [ ] Latest static channel backup file (Recovery process will force close your lightning channels)
{% endtab %}
{% endtabs %}

<details>

<summary>Where are Alby Hub self-hosted internal files on Windows?</summary>

Please note that the data files for Alby Hub on Windows can be found here: `C:\Users\<YourUsername>\AppData\Local\albyhub`. ⚠️ Be very careful with these files, as they contain crucial information about your lightning network channels and cannot be recovered if deleted. If you wish to migrate your hub to another computer, it's recommended to use the proper migration flow instead of simply copying and pasting this folder to ensure all data is safely transferred. 😊\
\
![](<.gitbook/assets/image (22).png>)

</details>

<details>

<summary>Where are Alby Hub self-hosted internal files on Unix or macOS?</summary>

For other operating systems, we use the XDG implementation, specifically the XDG\_DATA\_HOME folder type.

On Unix, Alby Hub stores important data in `~/.local/share`, while on macOS, it’s located in `~/Library/albyhub`. 😊 For more details about XDG folder implementation, you can check this link: [XDG Implementation Guide](https://github.com/adrg/xdg) 📂👍

Thanks for your understanding!

</details>

***

{% hint style="success" %}
**Congratulations! 🎉 You've successfully learned how to back up your Alby Hub, ensuring the safety of your funds and channels.** Remember to always keep your Recovery Phrase and latest channel backup handy. With your backups in place, your hub is now well-protected and ready for any situation! 🔐
{% endhint %}

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Get a subscription to Pro Cloud! ☁️</strong><br><br>Unlock 24/7 availability for your self-hosted wallet by subscribing to Pro Cloud. Never worry about downtime again!</td><td></td><td></td><td><a href="https://getalby.com/subscription/new">https://getalby.com/subscription/new</a></td></tr><tr><td><strong>Learn more about your on-chain balance! 💰</strong><br><br>Discover the on-chain side of your self-custodial wallet. Click here to learn more about managing your Savings Balance securely.</td><td></td><td></td><td><a href="node/on-chain-balance.md">on-chain-balance.md</a></td></tr><tr><td><strong>Migrate your Hub! 🔄</strong><br><br>Planning to move your Alby Hub? The migration process is similar to a backup in many ways. Click here to explore more on how to migrate your hub seamlessly!</td><td></td><td></td><td><a href="faq/how-can-i-migrate-alby-hub-to-a-different-machine.md">how-can-i-migrate-alby-hub-to-a-different-machine.md</a></td></tr></tbody></table>

***

_Thank you for stopping by!_ \
_This section was created with contributions from René, Roland & Jean-Paul_
