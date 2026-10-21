---
description: Follow this page to learn about best practices as an app developer
icon: person-carry-box
---

# Best Practices

### Permission requests

App developers should seek permissions responsibly, ensuring that they only request the necessary permissions automatically and for the specific duration required.

### Setting up a connection

App developers should pass the application name when setting up a connection

### Manually adding a connection

Users should always be given the option to paste a connection string from an NWC wallet application. Connection string input fields should be `password` type so they are not leaked in recorded videos or screenshots.

### **Don't assume a particular wallet service**

NWC allows anyone to connect their own wallet or node, so don't assume the user is using a particular one. Stay agnostic in your language about the user's wallet, e.g. instead of saying `Pay`_`with X`_, just say `Pay`.

### Check the supported methods from the connection

Apps should do a `get_info` request to check what the connection supports to ensure that the app does not execute commands that are not supported. A positive side effect of this is it will do a request to the wallet service, notifiying the wallet service that the connection is created (which allows the wallet service to tell the user the connection has been successfully created).
