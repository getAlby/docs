---
description: How to use your Alby lightning address with own domain?
---

# How to use my own domain as lightning address

{% hint style="info" %}
**Please read and fill out the form first.**\
To use your own domain, you will need to upload a file to the server of your own domain. We need a way to contact and inform you, if the file requires a change.\
\
For advanced users, we recommend setting up a redirect rather than hosting a copy of your lightning address data.
{% endhint %}

{% embed url="https://form.jotform.com/231085718548059" %}

### **Prerequisites**

* An active Alby Account with a lightning address (can be free or paid)
* Your own domain with web hosting access
* Ability to upload files to your domain's root directory

### Steps

#### 1. Get your Alby lightning address configuration

* Open your browser and go to  `https://getalby.com/.well-known/lnurlp/YOUR_ALBY_USERNAME`&#x20;
* Replace `YOUR_ALBY_USERNAME` with your actual Alby username
* Save the page (Ctrl+S or Cmd+S) to download the JSON configuration file

#### 2. Prepare the configuration file

* Remove the file extension from the downloaded file (e.g. json)
* Example: If you want  `payments@yourdomain.com`  rename the file to just `payments` (no extension)

#### 3. Verify the configuration content

Your file should contain JSON similar to this

{% code title="Example" overflow="wrap" %}
```json
{
   "status": "OK",
   "tag": "payRequest",
   "commentAllowed": 255,
   "callback": "https://getalby.com/lnurlp/YOUR_USERNAME/callback",
   "metadata": "[[\"text/identifier\",\"YOUR_USERNAME@getalby.com\"],[\"text/plain\",\"Sats for Alby\"]]",
   "minSendable": 1000,
   "maxSendable": 11000000000,
   "payerData": {
    "name": {
      "mandatory": false
    },
    "email": {
      "mandatory": false
    },
    "pubkey": {
      "mandatory": false
    }
  },
   "nostrPubkey": "your_nostr_pubkey_here",
   "allowsNostr": true
}
```
{% endcode %}

#### 4. Upload to your own domain

* Upload the file to your domain's root directory at this specific path `https://yourdomain.com/.well-known/lnurlp/FILENAME`
* **Important:** Your domain must be accessible without `www` (hosted on the root domain)

{% hint style="info" %}
Would you like to have separate lightning addresses with your own domain—for example, for family members, friends or business purposes?\
Repeat step 1-4  and upload other files to your domain's root directory.
{% endhint %}

#### 5. Example setup

Let's say you want to create `payments@example.com`&#x20;

* Download the configuration from:  `https://getalby.com/.well-known/lnurlp/alice`&#x20;
* Rename the file to `payments` (no extension)
* Upload to `https://example.com/.well-known/lnurlp/payments`&#x20;

#### 6. Test your setup

* **Check the URL**: Open `https://yourdomain.com/.well-known/lnurlp/FILENAME`  in your browser
* **Test a payment**: Try sending a small payment to your new lightning address
* **Verify receipt**: Confirm the payment arrives in your wallet

#### Troubleshooting

* 404 Error: Check that the file is uploaded to the correct `.well-known/lnurlp/` directory
* Payment fails: Verify the `"callback"` URL in your JSON file matches your Alby username
* Domain issues: Ensure your domain works without `www` prefix



✅ **That's it. You just turned your own domain into a lightning address! 🙌**

