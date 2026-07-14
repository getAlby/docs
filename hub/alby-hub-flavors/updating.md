---
description: >-
  Keep your Alby Hub up to date for the latest and greatest features. Don't
  worry, it's super easy!
---

# 🆙 Updating

The Alby team and open-source contributors are constantly researching and working on Alby Hub to ensure you have the latest features and security improvements.\
\
Let's get started! Keep your Alby Hub up to date! 💪

You can find the current Alby Hub version in Settings > About. All releases are published on [GitHub](https://github.com/getAlby/hub).

## How to Update 🚀

When an Alby Hub update becomes available, you'll be notified directly in the Hub. The update process depends on how you run Alby Hub.

### Before you update

Please note the following before you update your Hub:

* Make sure you have backed up your Alby Hub recovery phrase consisting of 12 words (for the embedded node option only).
* Make sure you have your Alby Hub password saved.
* Update might take a few minutes.
* After the update, unlock Alby Hub with your password.

## Choose your Alby Hub update path 📦

### Cloud Hosting

If you deployed Alby Hub using one of the cloud provider guides, follow the update instructions in that guide: [https://getalby.com/alby-hub/cloud](https://getalby.com/alby-hub/cloud)

If you run Alby Hub on a cloud server that you manage yourself with Docker, use the [Docker](updating.md#docker) update steps instead.

### Desktop

{% tabs %}
{% tab title="Windows" %}
{% embed url="https://demos.getalby.com/demo/clz2s4mtz00c0ypj47uxq5cq7" %}
Updating Alby Hub on Windows
{% endembed %}
{% endtab %}

{% tab title="macOS" %}
{% embed url="https://demos.getalby.com/demo/cm6iqdoqm004lpekcufcyqbsf" %}
Updating Alby Hub on macOS
{% endembed %}
{% endtab %}

{% tab title="Ubuntu" %}
1. Download latest release from [GitHub releases](https://github.com/getAlby/hub/releases)
2. Stop current Hub instance
3. Install new version
4. Restart Hub
{% endtab %}
{% endtabs %}

#### Updating older Hub versions (<=1.10.2) on macOS

<details>

<summary>Follow these steps if you have done the above and see two Hubs in your Launchpad</summary>

* Close all instances of the Hub
* Open your Terminal and type `cd "/System/Volumes/Data/Users/<your-user-name>/Library/Containers"` and then do `ls`
* You should be able to see two folders in the list `com.getalby.albyhub` and `com.getalby.Alby-Hub`
* Your old data resides in `com.getalby.albyhub`, so we should move that to `com.getalby.Alby-Hub`
* To do that do `cd "/System/Volumes/Data/Users/<your-user-name>/Library/Containers/com.getalby.albyhub/Data/Library/Application Support"` and then do `cp -r albyhub "/System/Volumes/Data/Users/<your-user-name>/Library/Containers/com.getalby.Alby-Hub/Data/Library/Application Support/albyhubold` - this should copy the old Hub data to the new one
* Now do `cd "/System/Volumes/Data/Users/im-adithya/Library/Containers/com.getalby.Alby-Hub/Data/Library/Application Support"` and `ls` to see if there is `albyhubold` listed
* Do `mv albyhub albyhubempty` and then `mv albyhubold albyhub`
* Close your terminal(s) and run the new Hub again, it should work as normal. Delete the old Hub to avoid confusion
* From the next update, you can follow the regular MacOS guide as usual

</details>

### Docker

If you run Alby Hub with Docker, pull the latest image and recreate the container while keeping the same persistent data directory.

{% code overflow="wrap" %}
```bash
docker pull ghcr.io/getalby/hub:latest
```
{% endcode %}

Stop and remove the old container:

{% hint style="info" %}
If your container uses a different name, replace `albyhub` with your container name.
{% endhint %}

```bash
docker stop albyhub
docker rm albyhub
```

Start Alby Hub again with the same data volume:

```bash
docker run -d --name albyhub \
  -v ~/.local/share/albyhub:/data \
  -e WORK_DIR='/data' \
  -p 8080:8080 \
  ghcr.io/getalby/hub:latest
```

These commands keep your existing data in `~/.local/share/albyhub` and start Alby Hub with the latest image.

If you use Docker Compose, update by pulling the latest image and recreating the service with your existing compose file.

```bash
docker compose pull
docker compose up -d
```

### Umbrel, Start9, etc.

Go to your Node OS app store, check whether a newer Alby Hub version is available, and install the update from there.

### Ubuntu

If you built and run Alby Hub manually from source, update it from the project repository.

Go to your terminal and run these commands:

{% code overflow="wrap" %}
```bash
# Update Snap packages
sudo snap refresh go

# Update build-essential
sudo apt update
sudo apt upgrade -y build-essential

# Navigate to the app directory
cd /path/to/your/app # Update this to the actual path where Alby Hub is

# Pull the latest changes from GitHub
git pull origin main

# Update dependencies and rebuild the app
cd frontend
yarn install
yarn build:http
cd ..

# Run the Alby Hub
go run http/alby_http_service.go
```
{% endcode %}

## After the update 🎉

Your Alby Hub is Updated and ready to go! Unlock your Hub now to send and receive payments:

1. **Open your Hub on the desktop or via the browser.**
2. **Enter your unlock password to launch Alby Hub**
