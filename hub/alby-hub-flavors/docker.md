---
description: >-
  Run your own Alby Hub using Docker or Docker Compose with persistent storage
  on your computer or server.
---

# 🐳 Docker

Docker is a good option if you already have a computer, home server, VPS, or other system where Docker is installed. It gives you full control over your Alby Hub deployment and keeps your Hub data on storage that you manage.

This guide walks you through creating persistent storage, starting Alby Hub with Docker Compose or a Docker command, opening your Hub in the browser, and updating it later.

{% hint style="warning" %}
We recommend having a solid understanding of Docker management before attempting to host your Alby Hub in a Docker container. If you're not experienced with Docker, please avoid this method, as it could lead to potential loss of funds.

Alby Hub is intended to run on a secure private network. Do not expose its HTTP port directly to the public internet. The examples below bind port `8080` to `127.0.0.1`, making the Hub reachable only from the Docker host by default.
{% endhint %}

## Prerequisites

Before you begin, make sure you have:

* A computer or server that can run continuously
* [Docker](https://www.docker.com/) installed
* [Docker Compose](https://docs.docker.com/compose/) installed if you plan to use the recommended Docker Compose method
* Basic familiarity with running terminal commands

Recommended minimum resources:

* **Memory:** 512 MB, with 1 GB recommended
* **Swap:** 1 GB, with 2 GB recommended on smaller servers
* **Storage:** At least 1 GB
* **Persistent storage** using a Docker volume or bind mount. The examples in this guide already configure persistent storage.

You can check that Docker and Docker Compose are available using:

```
docker --version
docker compose version
```

The exact version numbers may be different depending on your system.

### Step 1: Create a working folder for Alby Hub

Create a folder for your Alby Hub deployment:

```
mkdir albyhub
cd albyhub
mkdir albyhub-data
```

The `albyhub-data` folder stores your Hub data outside the container so that it is preserved when the container is restarted or updated.

Do not delete this folder unless you intentionally want to remove your Alby Hub data.

### Step 2: Add the Docker Compose file

Docker Compose is the recommended way to run Alby Hub because it keeps the container configuration in a file and makes future updates easier.

You can either download the official Docker Compose file or create it manually.

#### Option A: Download the Docker Compose file

Run:

```
wget https://raw.githubusercontent.com/getAlby/hub/master/docker-compose.yml
```

If `wget` is not available, you can use:

```
curl -O https://raw.githubusercontent.com/getAlby/hub/master/docker-compose.yml
```

#### Option B: Create the Docker Compose file manually

Create a new file:

```
nano docker-compose.yml
```

Paste the following content:

```
services:
  albyhub:
    container_name: albyhub
    image: ghcr.io/getalby/hub:latest
    volumes:
      - ./albyhub-data:/data
    ports:
      # Bound to 127.0.0.1 so Alby Hub is reachable only from this machine.
      - "127.0.0.1:8080:8080"
      # Required for Lightning peer communication when using LDK.
      # - "9735:9735"
    environment:
      - WORK_DIR=/data/albyhub
    stop_grace_period: 300s
    # Optional: restart Alby Hub automatically when Docker starts.
    # restart: unless-stopped
```

Remove the `#` before `"9735:9735"` if you plan to use LDK as your Lightning backend.

You can also enable:

```
restart: unless-stopped
```

This restarts the Alby Hub container automatically when Docker or the host system restarts. You will still need to unlock your Hub manually unless auto-unlock is enabled in Alby Hub settings.

Save the file and exit.

In nano, press `Ctrl + O`, then `Enter`, then `Ctrl + X`.

### Step 3: Start Alby Hub

Start Alby Hub in the background:

```
docker compose up -d
```

Depending on your Docker installation, you may need to run Docker commands with `sudo`:

```
sudo docker compose up -d
```

Check that the container is running:

```
docker compose ps
```

You can also view the logs:

```
docker compose logs -f
```

If the logs are running without repeated errors, Alby Hub has started successfully.

Press `Ctrl + C` to stop following the logs. This does not stop Alby Hub.

### Step 4: Open Alby Hub in your browser

If Docker is running on the same computer you are using, open:

```
http://localhost:8080
```

The default configuration does not make Alby Hub reachable from another device. To access it from a device on your trusted local network or VPN, bind the port to the server's private or VPN IP address in `docker-compose.yml`:

```
"<private-or-vpn-ip>:8080:8080"
```

For example, use `"192.168.1.100:8080:8080"` for a server with the private IP address `192.168.1.100`. Then restrict port `8080` with Docker-aware firewall rules or a provider network firewall so that only your local network or VPN can reach it. Open the Hub using the same private IP address:

```
http://192.168.1.100:8080
```

Do not allow access to port `8080` from the public internet in either the host or hosting-provider firewall. On a remote server, either keep the loopback binding and place a restricted HTTPS reverse proxy in front of Alby Hub, or bind the port only to a private or VPN interface.

The broader `"8080:8080"` mapping also enables access from other devices, but it publishes the port on every host interface. Use it only on a trusted local network with firewall rules that account for Docker-published ports.

If you are using LDK, port `9735` must be reachable from the internet for Lightning peer communication. This does not require exposing the Alby Hub HTTP port.

### Step 5: Set up Alby Hub

Click **Get Started** and follow the setup flow inside Alby Hub.

During setup, save any important recovery or backup information shown by Alby Hub.

Your Hub data is stored in the `albyhub-data` folder, but you should still maintain your own backups so that you can recover or migrate your Hub later.

<figure><img src="../.gitbook/assets/Screenshot 2026-06-12 at 9.45.26 AM.png" alt=""><figcaption></figcaption></figure>

## How to update Alby Hub with Docker Compose

Alby Hub will show an update banner inside the app when a new version is available.

When you see the update banner, open a terminal and go to your Alby Hub folder:

```
cd ~/albyhub
```

Pull the newest Alby Hub image:

```
docker compose pull
```

Recreate the container using the new image:

```
docker compose up -d
```

Check that Alby Hub started cleanly:

```
docker compose ps
docker compose logs -f
```

Press `Ctrl + C` to stop following the logs.

Your Alby Hub data remains in the `albyhub-data` folder and is not removed when the container is recreated.

## Alternative: Run Alby Hub with a Docker command

You can also run Alby Hub directly without Docker Compose.

First, create the persistent storage folder:

```
mkdir -p ~/albyhub/albyhub-data
```

Then start Alby Hub:

```
docker run -d \
  --name albyhub \
  -v ~/albyhub/albyhub-data:/data \
  -e WORK_DIR=/data/albyhub \
  -p 127.0.0.1:8080:8080 \
  --pull always \
  ghcr.io/getalby/hub:latest
```

If you plan to use LDK, also publish port `9735`:

```
docker run -d \
  --name albyhub \
  -v ~/albyhub/albyhub-data:/data \
  -e WORK_DIR=/data/albyhub \
  -p 127.0.0.1:8080:8080 \
  -p 9735:9735 \
  --pull always \
  ghcr.io/getalby/hub:latest
```

These commands make the Hub interface reachable only from the Docker host. If you intentionally make it available on a trusted local network or VPN, replace the mapping with `-p <private-or-vpn-ip>:8080:8080` and restrict port `8080` with Docker-aware firewall rules or a provider network firewall. Using `-p 8080:8080` instead publishes the port on every host interface.

The `~/albyhub/albyhub-data` folder stores your Hub data outside the container so that it is preserved when the container is stopped, removed, or updated.

Docker Compose is generally recommended because it makes the deployment configuration and update process easier to manage.

## How to update Alby Hub when using `docker run`

If you started Alby Hub using the direct `docker run` command, first pull the newest image:

```
docker pull ghcr.io/getalby/hub:latest
```

Stop and remove the existing container:

```
docker stop albyhub
docker rm albyhub
```

Then run the same `docker run` command again.

Removing the container does not remove the data stored in your bind-mounted folder. However, make sure you use the same `-v` storage path when creating the new container.

You only need to update when Alby Hub shows an update banner or when you know a new release is available.
