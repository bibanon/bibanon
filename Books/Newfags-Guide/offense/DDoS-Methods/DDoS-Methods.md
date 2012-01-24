(Archived from the [[Insurgency_Wiki]])

This page will explain the differences between (Distributed) Denial-of-Service and Bandwidth Raep attacks, as well as differentiate between different types of denial of service attacks. Reading this page will prevent confusion and asking of dumb questions on your part. 

## Bandwidth Raep

First off, the target of an attack is almost always a web server. In order to understand the differences between these two attacks, you must understand, at least on a very basic level, how a web server works. Note that technically a Bandwidth Rape **is** a form DoS attack, but they are separated because BWRaep is legal or questionably legal, while the other forms are just plain illegal. Also, Bandwidth Rape does not always work and can take time, depending on the target. 

### How Web Servers Work

This is a diagram of a standard web host:

[[Standard_Web_Host.gif]]

Notice that the internet is asking to see certain websites hosted on the server (Sites 1, 2, and 3). The server gets the request, the server's CPU looks at the request, finds the requested data, and sends it back out.

All web servers have some physical limit of data that they can process per second, due to a combination of access to internet hookups and available hardware to connect up to those hookups. We'll say our server can process 5 Gigabits of data each second - if more data than that is being requested, the server will appear to slow down, because it does not have the ability to send data any faster.

Web hosts/servers do not want to operate at their limit - that means that any additional load on the server, any extra visitors, or, say, being linked to from a popular site, will result in their server slowing down. So, they impose bandwidth limits on the sites hosted. The reasoning here is that if a site is taking up HUGE amounts of bandwidth, its data is "clogging" the available connection, and slowing down the other sites.

Now, let's say Site 1 is linked from a popular blog. Suddenly, Requests for Site 1 increase in number, and the server spends more time processing requests to see Site 1 than the other sites.

[[Requests_for_Site_1_increase.gif]]

No problem, yet. Now, however, Site 1 is linked to from Slashdot. Requests to see it surge in number. 

[[Requests_for_site_1_surge.gif]]

Keep in mind that most web hosts have many, many more than three sites on them - at this point, the server is nearing its physical limit. Usually, one of two things will happen next: 

* Site 1 exceeds its bandwidth quota, and is suspended
* The web host notices that requests for Site 1 are taking up a huge amount of server resources, and suspends Site 1 to protect Sites 2 and 3 (and 4, and 5, and 6, etc) from being disrupted.

There is only a slight difference between the "slashdot effect" and a Bandwidth Raep attack, illustrated below: 

### BANDWIDTH RAEP

[[BANDWIDTH_RAEP.gif]]

Result: Site 1 is taken down in a quasi-legal manner.

### Notes on effectiveness

The goal of a BWRaep attack is usually to cause the host to run out of monthly bandwidth. This will not work on anyone with a decent plan (read: larger sites) as they may have unmetered lines (This wiki has two unmetered gigabit lines). If the target has infinite BW, then then next best thing is to saturate their pipes. This works by having computers with a total downstream speed in excess of the targets upstream speed, each downloading constantly from the target server. (This type of attack is not suitable for large sites, e.g. Church of Scientology, because keeping such a huge constant download stream is hard, and more effective things can be done with less effort.)

Furthermore, by targeting dynamic pages (especially those that require a database back-end line mysql (e.g. forum search function)) you can effectively rape their CPU, using a lot more of their processing power than just downloading static content. 

## Denial of Service

Denial of Service (DoS), in the context of an attack on a website, means flooding the server with so many fake packets that it cannot process the legitimate requests of real visitors.

In order to understand how Denial-of-Service attacks are carried out, it is necessary to understand a bit about how connections are created over the internet. Here several methods of DoS attacks will be explained. Note that only flood type attacks are gone over, as it would be too confusing for many readers to understand denial of service attacks that are more specific to individual exploits, such as echo chargen.

### SYN Attack

#### TCP Handshake

First off, you need some technical information. Remember IP addresses? They have a use other than getting your ass doxed for posting a [[Personal Army]] request. [[An IP address]] identifies your computer as the recipient of data. In the case of browsing the internet, the web sites you ask to see are sent to your IP address by the web server.

The server has to know your IP address in order to send you anything, though, and your computer needs to know, after you tell it to go to a web page, whether or not the server responded.

On the internet, this is done with a process called the "TCP Handshake." This involves several "packets" of data being exchanged between your computer and the server, illustrated below. 

[[Tcphandshakebe9.gif]]

Afterwards, you are connected and can request a web page, etc. Additonally, RST = STFU, FIN = DONE SENDING. 

#### Exploiting the TCP Handshake

The internet spans many continents, with all sorts of different ways to get from one place to another. Sometimes packets get lost. If one of the packets in the above handshake does get lost, the connection fails. Packets get lost quite often, but most of the time, your attempts to view web pages succeed.

Why? Because computers send MULTIPLE packets, not just one, greatly increasing the chance that one will get through at each of the three steps, completing the handshake and getting you connected. Or, rather, web servers send multiple "SYN/ACK" packets (LOL YES) when the receive a "SYN" (HAY R U THAR?) packet. If the computer that started the handshake doesn't respond, the following occurs. 

[[Tcphandshakebrokehs5.gif]]

More importantly, the server has a limited number of connections it can maintain at once. When the server receives a SYN (HAY R U THAR?) packet from you, it takes up one slot sending SYN/ACK (LOL YES) packets back to you. 

[[Ports01pw8.gif]]

If someone else tries to connect while you're talking to the server, they just go to a different port. 

[[Ports02bn3.gif]]

If the TCP Handshake is completed, with your computer responding with a RST (KTHXBAI) packet, then the server is ready to process further requests from you, and it frees up the port that it was using to talk with you.

What if you send a bunch of SYN packets, though? 

[[Synfloodwe2.gif]]

#### CPURaep

However, once you stop sending SYN packets, the server will send SYN/ACKs to all the ones that it's received, your computer will send RST packets back, and the server will free up all its ports again. Thus, Crapflooding only keeps a site down while the flood continues.

If, however, the network hardware on the server is significantly better than the CPU, or the flood's dataforce has been doubled over 9000 times, the following can occur: 

[[Cpuraepsh8.gif]]

### SMURF Attack

This attack method involves using a machine as an unwitting proxy in the attack on another server. This works by sending ICMP packets (ping ICMP echo to be precise) to the 'proxy' machine, but spoofing the source address to that of the target machine. The unwitting proxy computer then floods the target with replies.

A more common (and more effective) form of this attack is to send SYN or SYN/ACK packets with spoofed source addresses. In the case of SYN packets with spoofed addresses, the "mirror" machine will send multiple SYN/ACK packets at the target for each SYN it receives. If SYN/ACK packets are sent, the "mirror" machine will merely blast the target with ACK packets. This is called a "Reflective" DoS attack.

If UDP Packets are used, it is called a "FRAGGLE Attack" 

[[Smurf.jpg]]

### Ping Flooding

Not to be confused with a Ping of Death attack (now defunct, patched most everywhere since ~1999), this attack consists of saturating the target's bandwidth with ICMP echo packets (pings). It is hoped that the target will respond with reply packets, so that it consumes bandwidth going both ways. This only works if the attacker bandwidth is superior to the target bandwidth. 

[[Pingflood.jpg]]

### UDP Flooding

This is a very simple type of flood, consisting of simply sending large numbers of UDP packets to the target to use up resources. For instance, the rok/i/ts program works by opening lots of UDP connections on lots of random ports. The server must then check for a listening program for each port, and then send a reply packet to the flooder (unless the flooder spoofs his ip). 

[[Udpflood.jpg]]

## DDoS

DDoS (with two Ds) refers to a Distributed Denial-of-Service attack. Literally, this means more than one computer attacking the target. In practice, this generally refers to use of a botnet to obtain the multiple computers to attack with.

You cannot DDoS with your home computer. Because it is only one computer. You can, however, DoS. If you DoS a site while lots of other people are launching DoS attacks on that same site, you are part of a DDoS attack. Whenever Anonymous goes on raids together it's a form of DDoS. We pronounce it "De De Oh Ess" but [[Hal_Turner|this fag]] always says "DeeDos" which is gay.

## Tools

*May need updating, from 2010*

### BWRaep

* Web based
    * [[JS_LOIC|LOIC#JS-LOIC]]
    * [[Vampire_raep|DDoS_Tools#Vampire_raep]]
* Windows
    * [[LOIC]]
    * [[BWraep|DDoS_Tools#BWraep]]
    * [[BWRaeper.NET|DDoS_Tools#BWRaeper.NET]]
    * [[PyRAEP|DDoS_Tools#PyRAEP]]
    * [[JMeter|DDoS_Tools#JMeter]]
    * [[Untitled|DDoS_Tools#Untitled]]
* Mac
    * [[pygetraep|DDoS_Tools#pygetraep]]
    * [[PyRAEP|DDoS_Tools#PyRAEP]]
    * [[JMeter|DDoS_Tools#JMeter]]
* Linux
    * [[LOIQ]]
    * [[LOIC|LOIC#Linux]] (With mono or wine libs)
    * [[pygetraep|DDoS_Tools#pygetraep]]
    * [[PyRAEP|DDoS_Tools#PyRAEP]]
    * [[JMeter|DDoS_Tools#JMeter]]

### DoS

These are tools designed to crapflood servers, either blocking anyone else from connecting or crashing the server.

* Windows
    * [[LOIC]] (TCP Flood)
    * [[DoS_5.5|DDoS_Tools#DoS_5.5]] (>1)
    * [[Longcat_Flooder|DDoS_Tools#Longcat_Flooder]] (HTTP, UDP, SYN Flood)
    * [[rok/i/ts|DDoS_Tools#rok/i/ts]] (UDP Flood)
    * [[Sinflood|DDoS_Tools#Sinflood]] (SYN Flood, Reflective SYN Flood)
    * [[Untitled|DDoS_Tools#Untitled]] (TCP Flood)

* Mac
    * [[Hping|DDoS_Tools#Hping]] (Everything)
    * [[UDP.pl|DDoS_Tools#UDP.pl]] (UDP Flood)
    * [[Zap_Attack|DDoS_Tools#Zap_Attack]] (UDP Flood)

* Linux
    * [[Hping||DDoS_Tools#Hping]] (Everything)
    * [[Ssyn.pl|DDoS_Tools#Ssyn.pl]] (UDP Flood)
    * Ping (ICMP Flood, as root 'ping -f -s 65507 <target IP address>')
    * [[UDP.pl|DDoS_Tools#UDP.pl]] (UDP Flood)