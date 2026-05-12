---
description: >-
  Keep your Alby Hub up to date for the latest and greatest features. Don't
  worry, it's super easy!
---

# 🆙 Updating

The Alby team and open-source contributors are constantly researching and working on Alby Hub to ensure you have the latest features and security improvements. \
\
Let's get started! Keep your Alby Hub up to date! 💪

You'll find the current version of your Alby Hub in the top left corner of the app. All releases are published on [GitHub](https://github.com/getAlby/hub).

## Overview

1 .  [How to Update](updating.md#id-1.-how-to-update)\
2 . [Choose your Alby Hub specific flavor](updating.md#id-2.-choose-your-alby-hub-specific-flavor)\
&#x20;     2.1.  [Pro Cloud](updating.md#alby-cloud)\
&#x20;     2.2. [Desktop](updating.md#desktop)\
&#x20;     2.3. [Docker](updating.md#docker)\
&#x20;     2.4. [Umbrel, Start9, etc.](updating.md#umbrel-start9-etc)\
&#x20;     2.5. [Ubuntu](updating.md#ubuntu)\
3 .[ Congratulations!](updating.md#id-3.-congratulations)

***

## 1. How to Update 🚀

When an Alby Hub update becomes available you'll be notified directly in the Hub. The update process depends on how you run Alby Hub.&#x20;

### Before you Update&#x20;

Please note the following before you update your hub:

* Make sure you have backed up your Alby Hub recovery phrase consisting of 12 words (for the embedded node option only)
* Make sure you have your Alby Hub password saved&#x20;
* Update might take a few minutes
* Unlock is required after the update by entering your Alby Hub password

***

## 2. Choose your Alby Hub specific flavor 🍕

Find the perfect version of Alby Hub that you are running that fits your specific needs and apply its unique update!

It is recommended to do regular updates, as Alby developers are improving it every week.

### Alby Cloud

<details>

<summary>Updating your Hub running on Alby Cloud</summary>

1. Go to getalby.com and click "Login".&#x20;
2. Inside your Alby web account, go to "Wallet Configuration"
3. Click on "Update now".

<img src="../.gitbook/assets/Aspect ratio 31 (8).png" alt="" data-size="original">

</details>

{% embed url="https://demos.getalby.com/demo/clywujo361gpsz9kdn5nu50bm" %}

<details>

<summary>Other Cloud Options</summary>

The currently recommended deployment options on our [GitHub repository ](https://github.com/getAlby/hub/tree/master)are Digital Ocean, Render, and Fly. All three load the latest version from the GitHub repository. If your Alby Hub is outdated, shut down and reboot your instance. \
\
Those instances are using docker images, so if needed you can also updated them manually just like you would for a [docker image](updating.md#docker).

</details>

***

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
4. Restart Hub&#x20;
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

***

### Docker

<details>

<summary>Updating Alby Hub running from Docker</summary>

When running on docker, these are the steps to run the latest version:

{% code overflow="wrap" %}
```bash
docker pull ghcr.io/getalby/hub:latest
```
{% endcode %}

```bash
docker stop albyhub
```

```bash
docker rm albyhub
```

```bash
docker run -d --name albyhub \
  -v ~/.local/share/albyhub:/data \
  -e WORK_DIR='/data' \
  -p 8080:8080 \
  ghcr.io/getalby/hub:latest
```

These commands will run the docker image with the previous data, with no data loss and an updated Alby Hub

</details>

***

### Umbrel, Start9, etc.

<details>

<summary>Updating on Umbrel,  Start9, etc.</summary>

Go to your Node OS app store, check the current version of Alby Hub. If it is outdated, then proceed to make sure you have the latest version available for your Node OS. \
**For Start9**: [Visit their guide](https://docs.start9.com/0.3.4.x/user-manual/overview/managing-services#id4)\
**For Umbrel**: Click "Check for updates".\
<img src="../.gitbook/assets/Heading (11).png" alt="" data-size="original">

<img src="../.gitbook/assets/Heading (10).png" alt="" data-size="original">



</details>

***

### Ubuntu

<details>

<summary>Manual installation (Ubuntu)</summary>

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

</details>

***

## 3. Congratulations! 🎉

Your Alby Hub is Updated and Ready to Go!&#x20;

You have successfully updated your Alby Hub! However, your Alby Hub will be locked and inaccessible for connected apps. Payments will not work until you unlock your Hub. You need to unlock it after the update: &#x20;

1. **Visit Your Hub URL:** Go to the URL of your Alby Hub.
2. **Enter Your Unlock Password:** Log in with your unlock password to launch Alby Hub and re-enable your wallet.

