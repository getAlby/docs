---
description: >-
  You can run Alby Hub on your own computer, whether it is running on Windows,
  MacOS, or Linux.
---

# 🖥️ Desktop

## Install Alby Hub on:&#x20;

1\.  [Windows](desktop.md#windows)\
2\. [macOS](desktop.md#macos)\
3\. [Linux](desktop.md#linux)\
4\. [Instruction for all systems and download links](desktop.md#all-systems)\
5\. [Uninstalling and deleting everything](desktop.md#id-5.-uninstalling-and-deleting-everything)

{% hint style="info" %}
Alby Hub for desktop is well-suited for self-hosting for users who have a basic understanding of software configuration and network settings, and have their computers online 24/7 in order to send or receive payments.  Therefore, consider this option if you keep the desktop computer **always online**.&#x20;

Otherwise, we recommend subscribing to Alby Cloud to ensure your wallet is always online. 👍
{% endhint %}

***

## Windows **💻**

{% embed url="https://demos.getalby.com/demo/clyxrnjdh00uwh5yz026de5x6" %}

***

## macOS **🍏**

{% embed url="https://demos.getalby.com/demo/cm6b1rq9p0pkk280i2407f09m" %}

***

## Linux **🐧**

{% embed url="https://demos.getalby.com/demo/clz0o1u7p0074dr84mv73tvxg" %}

<details>

<summary>Installing on Linux for advanced users</summary>

Click [here](https://github.com/getAlby/hub?tab=readme-ov-file#custom-ubuntu-vm) to get started.

</details>

<details>

<summary>Linux Troubleshooting: Common Errors</summary>

* **Ubuntu 22.04 Crash on Startup**: If AlbyHub crashes on startup, try running `sudo apt-get install libwebkit2gtk-4.0-37`. This resolves a known issue with missing dependencies.
* **Blank White Screen with Graphics Acceleration**: If after installing the necessary libraries, AlbyHub still shows a blank white screen, launch the app with the command `export WEBKIT_DISABLE_DMABUF_RENDERER=1` to disable the problematic renderer.
* **Server Version Recommendation**: For users experiencing persistent issues, we recommend using the server version of AlbyHub. It lacks a GUI, making it less prone to graphical errors.

</details>

***

## All systems&#x20;

### 1. Select your operating system below

The download of Alby Hub app files starts automatically.&#x20;

<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td></td><td><strong>💻 Windows</strong></td><td></td><td><a href="https://getalby.com/install/hub/windows">https://getalby.com/install/hub/windows</a></td></tr><tr><td></td><td><strong>🍏 MacOS</strong></td><td></td><td><a href="https://getalby.com/install/hub/macos">https://getalby.com/install/hub/macos</a></td></tr><tr><td></td><td><strong>🐧 Linux</strong></td><td></td><td><a href="https://getalby.com/install/hub/desktop-linux">https://getalby.com/install/hub/desktop-linux</a></td></tr></tbody></table>

### 2. Extract the zip file

This may vary slightly between systems.

### 3. Find the Alby Hub file in the extracted order and install it.&#x20;

Open the file manually or add it to the system startup if you want it to run permanently each time you restart your computer.

{% hint style="success" %}
**Congrats!** 🎉 Your Alby hub is now running on your desktop. 👏 \
Remember, keeping your Alby Hub online is crucial to send and receive payments at any point in time.
{% endhint %}

***

## Uninstalling and deleting everything

{% hint style="danger" %}
Warning: This may result in a loss of funds. Make sure your Hub is empty before following these instructions to completely remove it.
{% endhint %}

To completely remove Alby Hub from a Windows desktop, first close the app, then uninstall it from Settings under Apps if it appears there. After that, delete its data folder located at C:\Users\AppData\Local\albyhub.&#x20;

On a Mac, close the app, drag Alby Hub from the Applications folder to the Trash, and then delete its data folder, which may be found at \~/Library/albyhub or, in some cases, at \~/Library/Containers/com.getalby.Alby-Hub/Data/Library/Application Support/albyhub.
