---
description: You can run Alby Hub on cloud service from almost any provider!
---

# ☁️ Cloud Hosting

You can find all releases, script binaries and install scripts of Alby Hub on [GitHub](https://github.com/getAlby/hub?tab=readme-ov-file#deploy-it-yourself).\
\
To make the deployment of Alby Hub in the cloud as easy as possible, find guides and 1-click deploy options below 👇

{% hint style="warning" %}
Use the HTTPS endpoint provided by the deployment platform. Do not expose Alby Hub's raw HTTP port `8080` directly to the public internet. If you configure a cloud deployment manually, keep the HTTP service behind a restricted HTTPS reverse proxy or access it through a VPN.
{% endhint %}

## Protect initial setup

For a new self-hosted cloud deployment running Alby Hub v1.24.7 or later, we recommend setting a random `SETUP_CODE` environment variable **before the first start**, not after the public URL becomes available. This prevents someone without the code from completing the initial setup or importing a migration file before you do.

Generate a random code locally with `openssl rand -hex 16` and configure it as `SETUP_CODE` in your hosting platform's environment variables or secrets. For Docker deployments, follow the [setup-code instructions](docker.md#protect-initial-setup-with-a-setup-code), including passing the variable into the container. Do not assume a one-click deployment template enables it automatically.

Open your Hub using the platform's HTTPS URL and enter the code when prompted. Alternatively, append `?c=YOUR_RANDOM_CODE` to the URL, replacing the placeholder with your code. Keep the code and any link containing it private.

The official Linux and Raspberry Pi install scripts generate a setup code automatically and print it with a setup link. If you use one of these scripts on your cloud server, use the generated code with your secure access URL rather than exposing the raw HTTP port.

The setup code is not your unlock password or recovery phrase. It is no longer required once setup is complete and does not replace the network-access precautions above.

## Overview

### Deploy on Fly.io

[<img src="../.gitbook/assets/fly.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/fly)

### Deploy on Render

[<img src="../.gitbook/assets/render.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/render)

### Deploy on DigitalOcean

[<img src="../.gitbook/assets/digitalocean.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/digitalocean)

### Deploy on Railway

[<img src="../.gitbook/assets/railway.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/railway)

### Deploy on Google Cloud

[<img src="../.gitbook/assets/google-cloud.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/google-cloud)

### Deploy on AWS Lightsail

[<img src="../.gitbook/assets/aws-lightsail.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/aws-lightsail)

### Deploy on AWS EC2

[<img src="../.gitbook/assets/aws-ec2.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/aws-ec2)

### Deploy on Linode

[<img src="../.gitbook/assets/linode.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/linode)

### Deploy on Vultr

[<img src="../.gitbook/assets/vultr.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/vultr)

### Deploy on Hetzner

[<img src="../.gitbook/assets/hetzner.png" alt="Deploy to Hetzner" data-size="original">](https://getalby.com/alby-hub/cloud/hetzner)
