---
description: Run Alby Hub with a single docker command 🐋
---

# 🐋 Docker

Click the link below to get started

[https://github.com/getAlby/hub?tab=readme-ov-file#docker](https://github.com/getAlby/hub?tab=readme-ov-file#docker)

**Minimum Requirements:**

* Memory: 512MB (1GB recommended) + 1GB Swap (2GB recommended)
* Storage: 1GB+
* Persistent storage. When using Docker, it’s important to configure a **persistent volume** or a **bind mount** to ensure the data isn’t lost when the container restarts. \*

(\*) Our Docker examples contain the volume.&#x20;

You can manually download the docker-compose.yml file and then run: docker compose up . Here is the command to run the Hub on Docker:

```
docker run -v ~/.local/share/albyhub:/data -e WORK_DIR='/data' -p 8080:8080 --pull always ghcr.io/getalby/hub:latest
```

{% hint style="warning" %}
We recommend having a solid understanding of Docker management before attempting to host your Alby Hub in a Docker container. If you're not experienced with Docker, please avoid this method, as it could lead to potential loss of funds.
{% endhint %}
