
## Packets ##

When data is sent over the internet, it is sent in smaller more manageable pieces called Packets. A packet has a Header, a Payload, and a Trailer. 
The data included in the Header is as follows.

* The Size of the packet. 
* Synchronization Information. (Allows the receiver to match up the sending network.)
* The packet number. (If the packet came in a set, it will include which packet it is in sequence.)
* What protocol is used. 
* The destination address.
* The sending address. 
The data in the Payload is the data being sent. For instance part of a video or plain text. 
The payload may be padded with blank data to make it meet an acceptable size. 
The data in the footer includes a few bits to tell the receiving device that the packet is finished. May include CRC error checking. 
All data on the internet is sent and received in packets.

## Addressing ##


### IP addressing ###

With the TCP/IP Protocol suite all devices connected to a network, is assigned an IP address. 
An IP address consists of 4 8-bit binary numbers Each group is known as an octet. The address is represented to you as 4 groups of 3 numbers. Also known as Dotted Decimal Notation. As with binary, one of the portions of the address is known as an octet.
An octet can be any number from 0 to 255. 
An example being 192.168.1.1. To your computer, that looks like 11000000.10101000.00000001.00000001.
There are 5 Classes of IP addresses, Ranging from A to E. The class is determined by one of two things, either A: The Subnet Mask, or B: The range of the first octet. IP address classes define which part of the IP represent the network you are on, and the computer you are on. Class D and E addresses are special, used in rare cases for research, broadcasting, and multicasting. 

* Class A: Addresses range from 0.0.0.0 to 127.255.255.255. The first octet identifies the network, the other 3 represent the nodes. 
* Class B: Addresses range from 128.0.0.0 to 191.255.255.255 The first 2 octets identify the network, the other 2, the nodes. 
* Class C: Addresses range from 192.0.0.0 to 223.255.255.255 The first 3 octets identify the network, the other octet, the nodes. 
* Class D: Addresses range from 224.0.0.0 to 239.255.255.255 Class D IP addresses are used for multicasting. 
* Class E: Addresses range from 240.0.0.0 to 254.255.255.255 Class E IP addresses are reserved for research concerning TCP/IP. 
The IP address 255.255.255.255 is used for Broadcasting. A broadcast is used for sending one packet to every host on the network. Routers filter all packets going to 255.255.255.255 in between the private network (you) and the public network (internet). 
The IP address 127.0.0.1 is associated with yourself. Or "localhost". This address cannot be used for anything other then localhost, and is reserved. 

### Subnet Masks ###

When you type ipconfig into cmd, you see something called the Subnet Mask in what is returned. The subnet mask is used to identify what class an IP address is, and in other words, what portion of the IP is the network, and which portion of the IP is reserved for hosts. 
Subnet masks are shown in dotted decimal notation (xxx.xxx.xxx.xxx) like IP addresses. And occupied octet in the subnet mask, identifies the network portion of the address. 255.255.255.0 is the subnet mask for Class C IP addresses. 

* 255.0.0.0: Class A IP. First octet represents network. 
* 255.255.0.0. Class B IP. First 2 octets represent network. 
* 255.255.255.0 Class C IP. First 3 octets represent network. 
The mask may have a digit other then 255 or 0. Masks with this feature, have been subnetted. Subnetting is an advanced technique That divides computers on a network into different groups based on their routing prefix. 

### Public & Private IPs ###

There are 2 kinds of IP Addresses in the world. Public, and Private. When you sent a packet, it's attached with your private IP address & MAC address until it reaches the router, which replaces the private with the public IP. The packet with the public IP does it's business, and when a packet is sent back to your computer, your router checks a record of which IP address is associated with which MAC address, and sends the packet on. 
Private IP addresses stay within the confines of your network, and are found found in certant IP ranges based on the classes. 

* Class A Private IP Range: 10.0.0.0 to 10.255.255.255
* Class B Private IP Range: 172.16.0.0 to 172.31.255.255
* Class C Private IP Range: 192.168.0.0 to 192.168.255.255
The class of the IP determines what the private IP address will be prefixed by. Most commonly, soho networks (Small office/Home office) use Class C IP addresses, and their network will run with addresses in the 192.168 range.
