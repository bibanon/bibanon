
# tl;dr #

This article will walk you through how to change your Comcast IP address.

# Introduction #

So, you've been ip banned (aka permafucked).  There are a couple options before you: 

1. Suck the admin's white sausage until you are unbanned
1. Proxy up
1. Change your IP
Option 3 is usually the best option.  This is good for those with dynamic IPs, whose address changes frequently (such as every connect, which is the case with AOL and other dial-up companies).  However, many people use broadband connections which usually have static IPs.  These IP addresses can be leased for 6 months or more, which is far too long for a troll needing quick unbanning.
Comcast is one such provider.  However, there is a method to get around their IP lease.  Keep in mind that how well this work varies on your setup and your location.

# How it works #

Typically, your computer connects (via wifi or cable) to a 3rd party router (actiontek, d-link, etc), which itself plugs into your cable modem (these are provided by Comcast).  The following things happen:

1. When the Comcast modem turns on, it looks for a device connected via ethernet.
1. Upon finding a device, it notes the MAC address of the hardware of the device

  1. It will thereupon only work with that device (or another device with that MAC)
1. It requests an IP, which are assigned based on the MAC of the first device it found

# How to exploit this #

MAC addresses are not usually permanent.  In fact, they can be changed quite easily.  For most routers, you can change the MAC (hardware) address right in the web configuration.  This is true for NetGear, for instance, and is found under "basic settings".

1. Jot down your IP (check at [www.whatismyip.org](http://whatismyip.org/))
1. Go into the router web config
1. Find the section with the MAC **(01-23-45-67-89-ab)**
1. Change the MAC to something random
1. Apply
1. Reset the comcast modem

  1. Push the tip of a pen into the reset slot, which is usually by where you put in the power cord
  1. Hold there for 30 seconds, then release and remove
1. After the modem connects (check the status lights), try the internet.

  1. If it doesn't work, try resetting your 3rd party router.
Following those instructions, you should now have a new IP -- confirm by checking [www.whatismyip.org](http://whatismyip.org/) and comparing it with the IP you wrote down before.

## What if I don't have a router? ##

Some poorfags don't have a router, and instead connect to the modem directly.  Regardless, the principle is the same.  You can usually change the MAC address of your computer quite easily, following roughly the same instructions as above.  Substitute steps 2-5 for the instructions found on the [Changing MAC Address](/Changing_MAC_Address) article, setting a random MAC address.

# See also #


* [Changing MAC Address](/Changing_MAC_Address)
* [Anonymous](/Anonymous)
{{tutorials}}
