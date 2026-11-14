---
description: How to run Alby Hub on Linux?
---

# 🐧 Linux

Do you want to build and run Alby Hub from source on an Ubuntu VM or other Linux architecture? We've got you covered.

{% hint style="warning" %}
The Alby Hub HTTP server listens on all network interfaces by default. Run it only on a secure private network and use a firewall to block its HTTP port from the public internet. For remote access, use a VPN or an HTTPS reverse proxy that restricts who can connect.
{% endhint %}

## Setup code

The official Linux and Raspberry Pi install scripts generate a random setup code automatically and print both the code and a setup link containing it. Open that link on your trusted network, or enter the code when Alby Hub prompts you. Keep the code and link private. The setup-code feature requires Alby Hub v1.24.7 or later.

If you install the HTTP server manually or run it from source instead of using the install scripts, we recommend setting a random `SETUP_CODE` environment variable before the first start. Generate a code with `openssl rand -hex 16` and pass it to the Hub process through your environment or service configuration.

The code protects initial setup, including importing a migration file into a new Hub. It is not your unlock password or recovery phrase and is no longer required once setup is complete. It does not make exposing the HTTP port to the public internet safe.

[Click here to get started.](https://github.com/getAlby/hub?tab=readme-ov-file#deploy-it-yourself)
