
## Networking 101 ##


### IP addresses ###

Every machine on the internet has an ip address. Far too often users in IRC ask "Whats the ip of www.x.com?"
Every domain name (that's in use) resolves to an IP address. Domain names are only aliases for IP addresses because www.google.com is easier to remember than 74.125.47.99. The inverse is not neccesarily true--an ip may have no domain name. Also note that several different sites under different domains may share an IP.

#### Finding IPs ####

The [ShowIP](https://addons.mozilla.org/en-US/firefox/addon/590) Firefox extension displays a site's IP address in the Firefox statusbar, and the extension works on Windows and Linux. Read: If you aren't a macfag, just use it.
       * nix, OS X 
januszeal@sumomo ~ $ host www.google.com
www.google.com is an alias for www.l.google.com.
www.l.google.com has address 74.125.47.99
www.l.google.com has address 74.125.47.103
www.l.google.com has address 74.125.47.104
www.l.google.com has address 74.125.47.147
or
chance@AMD64:~$ dig www.google.com
<dl>
<dt> <<>> DiG 9.5.0-P2 <<>> www.google.com
</dt>
</dl>
<dl>
<dt></dt>
<dt>www.google.com.                        IN      A
</dt>
</dl>
www.google.com.         42327   IN      CNAME   www.l.google.com.
www.l.google.com.       94      IN      A       209.85.225.103
www.l.google.com.       94      IN      A       209.85.225.99
www.l.google.com.       94      IN      A       209.85.225.147
www.l.google.com.       94      IN      A       209.85.225.104
<dl>
<dt></dt>
</dl>
<dl>
<dt></dt>
</dl>
       * Windows 
C:\Documents and Settings\janus zeal>ping www.lulzhost.net
Pinging www.lulzhost.net [209.62.62.138] with 32 bytes of data:
Reply from 209.62.62.138: bytes=32 time=40ms TTL=50
Reply from 209.62.62.138: bytes=32 time=44ms TTL=50
Reply from 209.62.62.138: bytes=32 time=38ms TTL=50
PINGING A HOST WILL NOT CAUSE ANY KIND OF HARM TO IT, STOP TRYING TO TAKE DOWN SITES BY PINGING THEM YOU FUCKING RETARDS.
Hmm... The FireFox extension FoxyFlag may be interesting. It supposedly gives you a site's IP, although when I did on google it gave me 64.233.161.147
       * That is correct, however I find Domain Details to be a better add-on janus zealtalkwat 01:54, 8 July 2008 (UTC)

## Web hosting ##

Every site is being hosted on someone's server. Finding out which company hosts a site is a good way to find out what kind of bandwidth packages they have, etc.

### Finding domain name registrar ###

       * go here [<http://whois.domaintools.com/>](http://whois.domaintools.com/)
       * Enter the domain name
       * look for Registrar 

#### *nix based systems ####

On all *nix based systems it's pretty easy to find out any available details about a domain. That's what the command 'whois' is for. Every domain registrar runs a whois database for the domains it is hosting. Their database usually contains information about the owner of the domain, a technical and an administrative contact including addresses of them (admins doing semi-legal/illegal things may lie on these forms).
Some registrars require that the administrative contact is a natural person, not an organization.
Some domain owners subscribe to privacy services (such as Domains by Proxy) in which case you will have to try another way to get the information.
    Usage example:
    $ whois partyvan.info

### Finding host ###

Once you have an IP address, you can find out who is hosting a site.
       * go here [<http://www.ripe.net/db/whois.html>](http://www.ripe.net/db/whois.html)
       * enter IP address
       * look for OrgName
       * ???
       * PROFIT!

