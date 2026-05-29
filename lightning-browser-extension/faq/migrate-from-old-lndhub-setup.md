---
description: >-
  We are constantly improving our systems, to make them more reliable and
  secure. We recommend our users to use updated methods of using the Alby
  Extension.
hidden: true
---

# Migrate from old LNDHub setup

If you see the notification below in your browser extension, it means that your Alby Extension is using the old LNDHub setup to access your Alby Account (getalby.com). You should migrate to the new connector method and reconnect the extension to access the latest features.&#x20;

![](<../.gitbook/assets/image (31).png>)

{% hint style="info" %}
In short:

a. Make sure you have backup of your keys (Master Key, Nostr Keys). Always.

b. Use "Connect a Wallet" in Alby Extension to create a new profile.

c. "Connect with Alby" to link the extension with your Alby Account on getalby.com.\
👌 It's reconnected now!&#x20;

d. Import your keys to your "new" wallet.

e. Enjoy [using ](https://getalby.com/discover)the Alby Extension, freshly linked to your Alby Account!&#x20;
{% endhint %}

{% hint style="warning" %}
Please make sure you **always have a backup of you keys and all your credentials**.

Please also note that this might change your LNURL-Auth details for logins. Please see point 5 of the step by step guide.
{% endhint %}

### Here's a quick, step-by-step guide to help you through the process 👇

1.  **Open Wallet Menu**: Begin by navigating to the wallet selector within the extension interface.<br>

    <figure><img src="../.gitbook/assets/image (191).png" alt=""><figcaption></figcaption></figure>
2. **Click " + Add "**&#x20;

This will create a new profile within the extension - wallet - that users must link to some node (shared node of Alby Account or your own) and that can store and use your keys on the web.

<figure><img src="../.gitbook/assets/Screenshot 10-24-2024 17.29.45.png" alt=""><figcaption></figcaption></figure>

3. **Choose "Connect with Alby"**: When prompted to Wallet Connect Page, opt for the "Connect with Alby" option. This will initiate linking the new wallet in the extension to the account on getalby.com.&#x20;

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

&#x20;      Log in, if necessary.

<div align="left"><figure><img src="../.gitbook/assets/image (34).png" alt="" width="199"><figcaption></figcaption></figure></div>

3. **Transfer Keys**: Import your Master Key/Nostr Keys from old wallet into the new wallet.

In "Wallet Settings" of the extension, under "Key Management" you can access the Master Key and Nostr Keys that are stored and used by your extension.

{% hint style="danger" %}
Before you import your keys, you have the remove the ones that are placed there automatically with each new account.
{% endhint %}

Please choose the old wallet from the selector menu, copy relevant keys and paste them in the same section in the new wallet.

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure you have also an offline copy of your Master Key and Nostr Keys.
{% endhint %}

5. **Migrate third-party accounts using LNDhub connector for Login with Lightning.**

This section is optional. If you have been using your old wallet using LNURL-Auth for login (e.g. to Geyser, Stacker News, LNMarkets) and if you did NOT use a master key so far then the new wallet connection and master key will be recognized as another profile.

If you did **NOT** have a master key you should first link those accounts first.\
Alternatively, if this is not possible, you can also keep the old LNDHub available in the extension and keep using this to login. (even though migrating to the more secure and easier to use master key is recommended)<br>

Please contact the app to migrate your account to the profile authenticated with your Master Key. Stacker News and Geyser allow their users to unlink and relink their accounts for ease.

If you need help or have questions, please visit [support.getalby.com](http://support.getalby.com).

5. **Remove the old wallet.**

Now, you are safe to remove old wallet from your extension (in "Wallet Setttings" -> "Danger Zone"). Enjoy using Bitcoin & Nostr on the web with Alby!

<figure><img src="../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

