---
description: Run Alby Hub at home on a Raspberry Pi using a ready-to-flash image.
---

# 🍓 Raspberry Pi

Run Alby Hub on your own Raspberry Pi at home — your keys, your channels, on hardware you own. With the pre-built **Hub OS** image there's no command line and no manual install: flash the card, power on, and open your wallet in the browser.

{% hint style="info" %}
**Coming soon.** The ready-to-flash image and one-click Raspberry Pi Imager listing are being finalized. You can follow progress (and build it yourself) at [github.com/getAlby/hub-os](https://github.com/getAlby/hub-os).
{% endhint %}

## What you need

* A **Raspberry Pi** — a **Pi Zero 2 W** (512&nbsp;MB) is enough; a Pi 4 or 5 gives more headroom.
* A **microSD card** (8&nbsp;GB+). For an always-on wallet we recommend booting from a **USB SSD** instead — it's far more durable than an SD card for 24/7 use.
* A **power supply** and a case. A starter **kit that includes a case** gives the nicest finished result (no bare board on your desk).

{% hint style="warning" %}
The **Pi Zero 2 W uses micro-USB power and mini-HDMI** (not USB-C / full-size HDMI). If you buy a kit, make sure the power supply and adapters match — Pi 4/5 accessories won't fit.
{% endhint %}

## Flash the image

1. Download and open **[Raspberry Pi Imager](https://www.raspberrypi.com/software/)**.
2. Choose **Alby Hub** as the operating system. _(While the image is in preview, load it via the Hub OS release/custom repo — see [hub-os](https://github.com/getAlby/hub-os).)_
3. In Imager's settings (the gear icon), set your **Wi‑Fi network and password**, and choose a **hostname** (e.g. `albyhub`).
4. Select your SD card (or SSD) and **write**.

## First boot

1. Insert the card into your Pi and power it on. The first boot takes **2–3 minutes**.
2. Open **`http://albyhub.local`** in your browser.
3. Set a password, **write down your seed phrase** (this is your wallet backup), and [open your first channel](../wallet/open-your-first-channel.md).

That's it — you're running a self-custodial Lightning wallet on your own hardware.

{% hint style="info" %}
**Tip:** For long-term reliability, boot from a **USB SSD** rather than a microSD card, link your [Alby Account](../faq/why-do-i-need-to-link-my-alby-account.md) so your channel backups are stored encrypted, and use a quality power supply.
{% endhint %}

## Keeping it updated

No SSH needed. The image applies **operating-system security updates
automatically**, and checks for new **Alby Hub** versions weekly.

To get Alby Hub updates fully hands-off, **enable auto-unlock** (Alby Hub →
Settings). An update restarts the hub, so without auto-unlock it would come back
locked — therefore auto-update only runs when auto-unlock is on. The trade-off:
your unlock password is stored on the device, so keep your **seed phrase** safe
as your real backup. With manual unlock, just update when the hub shows the
**Update Available** banner.
