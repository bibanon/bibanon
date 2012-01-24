
# Introduction #

Obtaining other peoples passwords can sometimes be extremely difficult, but with the tools available today... it is usually trivial. This paper will cover various tools and techniques for getting those passwords. While passwords can be obtained by brute force using software such as L0phtcrack, Ophcrack, John the Ripper, Guess, Merlin, etc. this paper documents a less intrusive style of obtaining passwords. The reason for this paper is not to teach script-kiddies how to obtain the passwords of others, but to teach network admin just how insecure a network can be...

# Disclaimer #

The standard disclaimer applies. You do what you will and I am not responsible. If you can read this, you obviously have some form of intellect, and as such; your actions are controlled by you. Not me. This document was written under the influence of many many Corona's (with lime), as such, please do not flame me for not covering enough details, poor grammar, etc.

# Concepts #

This paper mainly deals with the Data-Link layer of the OSI Model.

# Data-Link Important terms and information #

MAC address (Hardware address): a 48-bit number which is supposed to be unique to each network adapter (ex. John's 3com network adapter does not have the same MAC address as Dave's 3com adapter).
Note: In Linux, you can change your adapters MAC address with the ifconfig hw class address command.
ARP (Address Resolution Protocol): Ethernet IP uses ARP to locate the hardware address of a given IP address (RFC 826). For example, a router would use an ARP request to determine the MAC address of a host with the IP address of 69.69.69.69. This would be a broadcast (sent to all hosts on the network) and only the NIC with the IP address of 69.69.69.69 would respond by sending an ARP reply to the aforementioned router. The router would then pass all traffic destined to 69.69.69.69 to that MAC address.
Example:
Router- "Who is 69.69.69.69?"
69.69.69.69 Host- "That would be me and my hardware (MAC) address is 00:XX:DB:27:XX:10"
Router- "Ok. I will add you to my ARP table and send all traffic destined to 69.69.69.69 to MAC address 00:XX:DB:27:XX:10"
ARP Table/cache: Internal database containing IP address to MAC address mappings (dynamic or static).
To view ARP tables, enter the following commands:
Cisco IOS: show arp
Linux: arp
Windows: arp -a
Switch: Works at the data-link layer (layer 2). Switches listen to network traffic and learn which MAC address/addresses reside off which ports, the switch then adds the entries to its ARP table. If a switch does not have the MAC address in it's ARP table, it will send the traffic (frame) to all ports (ie. broadcast).
Network Layer Important Terms and Information:
IP address: I'm going to assume you know what it is.

# Important General terms and Information #

Man-in-the-middle (MiM): When a third-party or host relays or observes information not intended for it. By placing a computer in between communication endpoints, we see all data that passes between those endpoints. This is useful for not only observing and relaying traffic, but also for injecting commands or information into the communication channel, and for session hijacking. For example, if I installed a proxy server on a network and configured every client web browser to direct HTTP traffic to me, I could observe you trading on-line and get your username and password, etc. I may also be able to wait for you to log in and then steal that connection from you and sell off your Cisco stock to buy shares of netflood.net
While that's not likely because your not going to allow me to come in and set up a proxy server on your network and because netflood isn't a publicly traded company, all it takes is someone with the correct tools to logically (if not physically) do that on your network. This is referred to as a man-in-the-middle attack.

# Details #

There are numerous man-in-the-middle attack tools, this article will only focus on tools capable of ARP spoofing/poisoning with the sole intention of obtaining passwords. ARP spoofing/poisoning is the act of pretending to be someone else by falsely sending non-requested ARP replies or by answering ARP requests regardless of what host (IP address) the communication is intended for, strictly for observing or relaying* the data that passes between the two hosts. ARP is stateless (or unreliable). It doesn't matter if a host sent an ARP request or not, it will usually accept your reply ARP (with the bogus information) regardless. ARP spoofing/poisoning can only be done on local area networks (even switched LAN's). Obviously you cannot spoof a MAC address of a host on a different network because that traffic would never be routed to you.
Note: ARP requests/replies, RARP requests/replies, etc are simply indicators in the Operation portion of an ARP packet, all we need to spoof MAC addresses is a tool which can modify the Operation portion. 1 = ARP Request, 2 = ARP Reply, 4 = RARP Request, etc.

* make sure you are forwarding the traffic if you are going to spoof the gateway. Otherwise you could hose your entire network segment (subnet).

# The Tools #


## Ettercap (v0.4.3) ##

An Excellent tool for sniffing networks (and password discovery). Collects passwords for the following protocols: TELNET, FTP, POP, RLOGIN, SSH1, ICQ, SMB, MySQL, HTTP, NNTP, X11, Napster, IRC, RIP, BGP, SOCKS 5, IMAP 4, VNC (other protocols coming soon...).
That means that if I am on a non-switched network and I have ettercap installed, I will get almost every password from every user on my segment (network), including MS share passwords.. A scary proposition for administrators with Linux/*BSD boxes on their network. If I am on a switched network I can poison the switch's ARP table, so that I will receive all traffic destined for the victim.
YouÂve got it in one. CouldnÂt have put it bteter.

## Dsniff ##

Written by Dug Song
dsniff is a collection of tools for network auditing and penetration testing. dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor a network for interesting data (passwords, e-mail, files, etc.). arpspoof, dnsspoof, and macof facilitate the interception of network traffic normally unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and webmitm implement active "monkey-in-the-middle attacks" against redirected SSH and HTTPS sessions by exploiting weak bindings in ad-hoc PKI.
As mentioned in a previous netflood article:
dsniff -w Filename.txt will write all sniffed passwords to Filename.txt
dsniff -r Filename.txt will read the file and list sniffed passwords
To arp poison, after installing dsniff:

1. arpspoof -i [interface] -t [target] host
Choose interface, if necessary. Choose target, for example if I wanted to poison the ARP table on just the switch I would enter the IP address of the switch using the -t variable (it's my target). If I do not use the -t variable, I will attempt to poison all hosts on the LAN. The host is whose traffic you want to see.
Detecting ARP spoofing/poisoning:
Use the Ettercap "Detect Poisoner" option
Use Arpwatch:
Arpwatch is a tool that monitors ethernet activity and keeps a database of ethernet/ip address pairings. It also reports certain changes via email. Arpwatch requires tcpdump and libpcap. Includes FDDI support, updated ethercodes, uses autoconf.
RARP a MAC address and watch for a return of multiple IP addresses.

## Cain ##

Cain is a tool for windows definitely worth mentioning. It can be used for a lot more than just sniffing.
It has an easy-to-use GUI, and is pretty effective.
    1.First go configure the shit using top menu. Choose the which adapter you want to use. 
      If you are doing it wifi, check the "Don't use Promiscuous mode", else leave it. Click Apply&OK.
    2.Click the little green thing with a red arrow and the friggin mouse-over text: "Start/Stop Sniffer"
    3.Go to the tab called "Sniffer". 
    4.Right-click and select "Scan MAC Addresses", or just click the blue cross in the top. Scan.
    5.Move on to "APR" tab in the bottom. Click blue cross, and add IPs. 
PROTIP:Choose router IP in left column.
    6.Click little nuclear sign in the top to start sniffing.
    7.????
    8.Profit! go to Passwords tab in bottom, to collect your loot.
Should you get hashes (from some protocols) then just right-click, and send them to cracker.
Cain crack nearly everything. It's able to use brute force, dictionaries, rainbowtables etc.

