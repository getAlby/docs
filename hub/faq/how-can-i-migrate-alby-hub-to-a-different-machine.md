# How can I migrate Alby Hub to a different machine?

1. [Self-hosted (Free) -> Self-hosted (Free)](how-can-i-migrate-alby-hub-to-a-different-machine.md#id-1.-self-hosted-free-greater-than-self-hosted-free-migration)
2. [Self-hosted (Pro) -> Self-hosted (Pro)](how-can-i-migrate-alby-hub-to-a-different-machine.md#id-2.-self-hosted-pro-greater-than-self-hosted-pro)
3. [Hosted Hub -> Self-hosted (Pro)](how-can-i-migrate-alby-hub-to-a-different-machine.md#id-3.-hosted-hub-greater-than-self-hosted-pro-migration)

### Important Notice: Please Read Before Continuing

You can migrate your Alby Hub to another device while maintaining full access to your funds.

Alby Hub is encrypted with the password you chose during setup. Only you can decrypt and access its data even if your Hub is running in the cloud. This also means that only you can perform a migration.

#### Scope of This Guide

* This guide only refers to migrating Alby Hubs using the embedded lightning node. If you connected an external lightning node (e.g. LND), you can install Alby Hub on any other device and link it again.
* Migrations from or to Alby Hubs with an externally connected lightning node (e.g. LND) are not supported currently.

#### Before You Start

{% hint style="danger" %}
* Make sure to have your **12-word recovery phrase** and **unlock password** securely backed up.
* During and after the migration, **do not restart your original Alby Hub instance**. Running both instances may cause issues such as force-closing lightning channels.
{% endhint %}

***

### 1. Self-hosted (Free) -> Self-hosted (Free) migration

**How to migrate your self-hosted Alby Hub (without a subscription) to another device**

These steps help you move your self-hosted Alby Hub to another device without a subscription, while keeping all channels active.

{% embed url="https://demos.getalby.com/demo/cm4io0lhm0rdt5pt8m5welv6b" %}

***

### 2. Self-hosted Pro -> Self-hosted Pro

**How to migrate your self-hosted Alby Hub (Pro) to another device**

These steps help you move your self-hosted Alby Hub with an active Pro subscription to another device, while keeping all channels active. You will only need to reconnect your apps afterward.

#### Before you start

* A self-hosted Alby Hub with an active **Pro subscription**
* **Dynamic Channels Backup** enabled: Alby Hub → Settings → Backup
* Access to your **12-word recovery phrase**

#### Migration steps

1.  **Shut down your old self-hosted Hub.**

    > ⚠️ **Important:** Do not start it again. Restarting the old instance may force-close your lightning channels.
2. Install your self-hosted Alby Hub on the new device.\
   ⚠️ **Important:** We recommend using a device that is always online (e.g., a cloud server, Start9, or Umbrel).
3. Start your new Alby Hub and go through the onboarding process.
4. During onboarding, connect the Hub to the **same Alby Account** you used previously. This keeps your Pro subscription active — there is no need to unsubscribe or subscribe again.
5. Click **“Advanced Setup”.**
6. Click **"Import Existing Recovery Phrase"**.
7. Choose an **unlock password** (can be the same as your old one, or a new one) and then **enter your 12-word recovery phrase**.

**That's it. The migration is done.** 🎉

**Note**, at the moment it is not possible to migrate a self-hosted Alby Hub with a Pro subscription with enabled dynamic channels backup to a self-hosted Alby Hub without a subscription. If you would like this feature, please submit a feature request to our [feedback board](https://feedback.getalby.com/-alby-hub-request-a-feature).

***

### 3. Hosted Hub -> Self-hosted (Pro) migration

**How to migrate your Alby Hub from a hosted Hub to a self-hosted setup with a Pro subscription**

These steps help you move your Alby Hub from a hosted Hub to a self-hosted device with a Pro subscription, while keeping all channels active. You will only need to reconnect your apps afterward.

#### **Before you start**

1. **Enable Dynamic Channels Backup**\
   In your current Alby Hub, go to: Settings → Backup\
   Make sure _Dynamic Channels Backup_ is enabled.
   * If it is not enabled, activate it.
   * Click the red restart button in the top-right corner.
   * Unlock your Hub again.
   * Double-check that Dynamic Channels Backup is now enabled.
2. **Confirm access to your 12-word recovery phrase.**

#### Migration steps

1.  Go to **getalby.com/subscription** and unsubscribe.

    > This will delete your current hosted Hub.
2. Go to **getalby.com/subscription/pro** and subscribe to **Pro**.\
   This ensures you can continue using Dynamic Channels Backup.
3. Install your self-hosted Alby Hub.\
   ⚠️ **Important:** We recommend using a device that is always online (e.g., a cloud server, Start9, or Umbrel).
4. Start your new Alby Hub and go through the onboarding process.
5. During onboarding, connect the Hub to the **same Alby Account** you used previously.
6. Click **“Advanced Setup”.**

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

9. Click **"Import Existing Recovery Phrase"**
10. Choose an **unlock password** (can be the same as your old one, or a new one) and then **enter your 12-word recovery phrase**.

**That's it. The migration is done.** 🎉
