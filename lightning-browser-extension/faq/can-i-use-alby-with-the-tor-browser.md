# Can I use Alby with the Tor Browser?

**Yes**, Alby works fine! The Tor Browser is one of the most important tools for internet privacy and we are committed to unlock the best bitcoin lightning experience for Tor Browser users. In fact the Tor Browser has the advantage that connecting Tor your own home node running behind Tor is even easier as it natively can connect to Tor nodes.&#x20;

You can install the Alby extension from the [Firefox add-ons store](https://addons.mozilla.org/en-US/firefox/addon/alby/)

**BUT** the Tor Browser prevents persisting accounts by default. This means after a restart you would need to add your account connection again.&#x20;

If you want to enable persistence:&#x20;

* Go to  `about:config`
* Search for `webextensions.storage.sync.enabled`&#x20;
* Enable (`true)` the storage.sync option

![](<../.gitbook/assets/image (156).png>)

Also make sure that Alby is enabled in "Private Browsing" mode which is the default in Tor Browser. After installing the Alby extension from the [Firefox add-ons store](https://addons.mozilla.org/en-US/firefox/addon/alby/) go to "Add-ons and themes" and allow Alby to "Run in Private Windows".

![](<../.gitbook/assets/image (135).png>)



{% hint style="info" %}
Add-ons in the Tor Browser will always have certain privacy and anonymity implications. Depending on what you want to do, do your own research.
{% endhint %}
