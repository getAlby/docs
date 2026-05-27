---
description: Connect Umbrel to the Alby Browser Extension
---

# Umbrel

## Use Alby Hub to link your Umbrel to the Alby Browser Extension

#### **Step 1: Install Alby Hub on your Umbrel**

<figure><img src="../.gitbook/assets/Screenshot from 2025-01-15 07-38-34.png" alt=""><figcaption><p>Go to the Umbrel App Store, search for "Alby Hub", Install it.</p></figcaption></figure>

#### **Step 2: Setup Alby Hub**

You can either use the Lightning Node app (LND), if you have it installed, or install Alby Hub with its embedded Lightning node (LDK).

{% hint style="info" %}
The embedded node is more resource-efficient and provides full channel backups without closing them, even if your Umbrel device fails.
{% endhint %}

If you already have the Lightning Node app installed and want to use it, Alby Hub will display the option **“Get Started (LND)”** during onboarding. Click it to continue.

<figure><img src="../.gitbook/assets/Screenshot from 2025-01-15 07-48-19.png" alt="" width="375"><figcaption></figcaption></figure>

If you prefer to use Alby Hub with the embedded LDK node, follow these steps:

1. Click **“Advanced Setup”**
2. Connect your Alby account or choose **“Maybe Later”**
3. Click **“Create Wallet with Custom Node”**
4. Set a password
5. Select the **“LDK”** option

Afterward, you’ll need to open a channel with Alby Hub. For detailed instructions, please refer to this guide:

{% content-ref url="https://app.gitbook.com/s/WIUBf3ZZaBGu2ee6Y8lU/getting-started" %}
[Getting Started](https://app.gitbook.com/s/WIUBf3ZZaBGu2ee6Y8lU/getting-started)
{% endcontent-ref %}

#### **Step 3: Link Alby Hub to the Alby Browser Extension**

Open Alby Hub → **Connections** → find and click on the **Alby Browser Extension** → click **“Connect to Alby Extension”** -> Follow the instructions -> Copy the **NWC connection secret**.

{% content-ref url="alby-hub-via-nwc-link.md" %}
[alby-hub-via-nwc-link.md](alby-hub-via-nwc-link.md)
{% endcontent-ref %}

🎉 Congratulations! You have successfully linked your Umbrel via Alby Hub to the Alby Browser Extension.
