Certain games, such as Second Life and Habbo Hotel, and sites and chat rooms will sometimes ban your MAC address, which is specific to your network card. This means that changing your IP is useless. Also, some ISPs will not normally change your IP address, but with a new (fake) MAC they will give you a new one. Fear not, you can change your MAC address too!

## Software ##


* Technitium Mac changer <http://anonym.to/http://www.technitium.com/tmac/index.html> <-- best
* <s>SMAC <http://anonym.to/http://www.klcconsulting.net/smac/#Download> <-- Shit Shareware, dont werk
* Mac Shift <http://anonym.to/http://devices.natetrue.com/macshift/> <-- werk only on MAC

## Tutorial ##

Under Windows XP, the MAC address can be changed in the Ethernet adapter's Properties menu, in the Advanced tab, as "MAC Address", "Locally Administered Address", "Ethernet Address" or "Network Address". The exact name depends on the Ethernet driver used; not all drivers support changing the MAC address in this way.
However, a better solution - requiring Administrative User Rights - is to pass over the System Registry Keys under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}. Here settings for each network interface can be found. The contents of the string value called 'NetworkAddress' will be used to set the MAC address of the adapter when next it is enabled. Resetting the adapter can be accomplished in script with the freely available command line utility devcon from Microsoft, or from the adapters context menu in the Network Connections control panel applet.
There is a nice tool to change the MAC address for all cards (even those that can't be changed through the adapter's Properties menu): SMAC MAC Address Changer
Note: to check your MAC address easily on a Windows XP box, go to Run, type CMD, then type "ipconfig /all" without quotation in the command prompt. The number under physical address is the MAC address. If multiple IP are displayed, you should look under the label "Ethernet adapter x", where x is the name of your connection (which is Local Area Connection by default).

## Self MACID Support ##

Based on the Technitium MAC Address Changer, though the others are more of the same type, not hard. 

* Not much to say. You select the network adapter with you surf the interbutts, and make up a MAC address. The Technitium MAC  Address Changer can generate some for you, even let you know what card maker's address range you're using.
* If you're not sure which network adapter you're using, just change one at a time and try accessing the game again.
* If you wanna switch back to your original address, it lets you do that too, so you can roll back at any time. 

## If you're using a router ##


* Go into your gateway site edit page.
* Goto MACID
* Change the ID with random numbers.
* Click Apply.
* Unplug your modem and wait 2 minutes.
* Plug it back in and enjoy your new IP.

## Self Router MACID Support. ##


* Sometimes, if you have a router, THAT might be the MAC that your game/chat room/ISP uses. 
* It is best to spoof your MAC on your computer and see if your router has a changeable MAC or a MAC cloner (that will copy your computer's MAC). 
* On a Linksys this should be under your main panel, a tab labeled "MAC Address Clone;" enable it.

## Linux users ##

GNU Mac Changer is a useful tool for vaporizing b&s with one simple command. You can get it on Debian/Ubuntu based systems with _sudo apt-get install macchanger_ You can download the source or packages for other distros at [the homepage](http://www.alobbs.com/macchanger). Change your MAC like so (eth0 in this example): mac changer eth0 Alternatively, you can use ifconfig (interface needs to be stopped first): ifconfig eth0 hw ether 00:00:00:00:00:00

## Mac Users ##

Your OS is soo chill you dont have to install shit. First, you’re going to want your current wireless MAC address so you can set it back without rebooting. To do this click on the airport icon, click on the join other network, type in some crap and click join. It will fail to join and you will press cancel, your airport is still on but you are not collected.
Launch the Terminal and type the following command:
<tt>ifconfig en1 | grep ether</tt>
You’ll know see something like:
<tt>ether 00:12:cb:c6:24:e2</tt>
And the values after ‘ether’ makeup your current MAC address. Write this down somewhere so you don’t forget it. If you do, it’s not the end of the world, you’ll just have to reboot to reset it from a change.
To spoof your MAC address, you simply set that value returned from ifconfig to another hex value in the format of aa:bb:cc:dd:ee:ff
For this example, we will set our wireless MAC address to 00:e2:e3:e4:e5:e6 by issuing the following command:
<tt>sudo ifconfig en1 ether 00:e2:e3:e4:e5:e6</tt>
The sudo command will require that you enter your root password to make the change.
Verifying the Spoofed MAC address worked
If you want to check that the spoof worked, type the same command as earlier:
<tt>ifconfig en1 | grep ether</tt>
Now you will see:
`ether 00:e2:e3:e4:e5:e6`
Meaning your MAC address is now the value you set it to. If you want to further verify the spoof, simply login to your wireless router and look at the ‘available devices’ (or attached devices) list, and your spoofed MAC address will be part of that list.

