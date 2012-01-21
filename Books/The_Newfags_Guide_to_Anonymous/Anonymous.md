Anonymous is a term used to describe an internet collective and subculture known for raiding websites, creating humorous image macros, and visiting [03chan](/03chan).

# Staying Anon #

As the name would suggest, Anonymity is one of the most relevant and important things any Anon should know about. Your 7 proxies will prevent you from being banned from your favourite chatroom, your ISP cutting off your connection for all that CP you look at, and the police coming for a v&.
Maintaining Anonymity can be divided into two categories- Interweb and IRL

## Interweb Anonymity ##


### Make sure your PC is clean ###


* Get Spybot Search & Destroy and update the fucker. <http://www.safer-networking.org/>  Also run immunize after to make sure your shit doesnt come back.
* use spywareblaster, update & enable all protection - <http://www.javacoolsoftware.com/spywareblaster.html>
* Malwarebytes is also decent - <http://www.malwarebytes.org/>

* Get a fucking antivirus program.  Free ones are ok, I usually use a cracked copy of symantec corporate edition tho.  Shit doenst use as much resources and itll usually never expire.

* run windows updates. Yeah those 500 unpatched security holes you got in your outdated shit is bad. Or simply don't use Windows - [www.ubuntu.com]

* Also fucking update your adobe shit for the love of god. [adobe version check](https://www.adobe.com/software/flash/about/) if thats not at the latest version your asking for an assraeping.

### Browsers ###

Dont use IE.  Use firefox.  You can test how anonymous your browser is [here](https://panopticlick.eff.org/)
Firefox now has GeoLocation abilities. Turn that garbage off.
In the URL bar type in - about:config
Find the setting geo.enabled 
Disable that crap

#### Extensions ####


* BetterPrivacy - know all that porn you fap to? yeah even if you wipe cookies adobe keeps shit, its called a supercookie. This kills those fuckers - [Download](https://addons.mozilla.org/en-US/firefox/addon/6623/)
* TACO - Opts out of tracking on websites.  Just disable the gay popup - [TACO](https://addons.mozilla.org/en-US/firefox/addon/11073/)

* HTTPSEverywhere - eff made that shit, its good.  It forces SSL encryption on major sites so noone else can intercept your shit.  As a bonus when you use SSL referrer information gets stripped so in cases like using google with SSL pages cannot tell what you typed in to get there [Download](https://www.eff.org/https-everywhere)
Heres some XML definitions for it, go to start -> run -> %APPDATA% -> Mozilla -> firefox -> profile -> HTTPSEVERYWHEREUSERRULES.  In there right click make a new text document, one for each of these and rename it to RULENAME.XML.  DONT COPY THE MOTHERFUCKING ---------s, just whats between them
---------------------------------------------------------------------------

     <pre>
      <ruleset name="isohunt">
        <target host="isohunt.com"/>
        <target host="www.isohunt.com"/>
        <rule from="^http://(www\.)?isohunt\.com/" to="https://isohunt.com/"/>
      </ruleset>
      </pre>

     <pre>
      <ruleset name="thepiratebay">
        <target host="thepiratebay.org"/>
        <target host="www.thepiratebay.org"/>
        <rule from="^http://(www\.)?thepiratebay\.org/" to="https://thepiratebay.org/"/>
      </ruleset>
      </pre>

     <pre>
      <ruleset name="erowid">
        <target host="erowid.org"/>
        <target host="www.erowid.org"/>
        <rule from="^http://(www\.)?erowid\.org/" to="https://erowid.org/"/>
      </ruleset>
      </pre>

HTTPSEverywhere list of XML files [here](https://gitweb.torproject.org/https-everywhere.git/tree/HEAD:/src/chrome/content/rules)
---------------------------------------------------------------------------

Using the FireFox addon NoScript will make it easier to add new HTTPS rules if you don't like or understand XML. Once you've installed NoScript go to Add-ons Manager>>Options>>Advanced>>HTTPS>>Behavior and type in websites in a list format. Just type the domain without the frills...
<pre>
isohunt.com
thepiratebay.org
erowid.org
</pre>


### Erasing Data ###


#### Cookies ####

Websites use cookies to identify users who have visited the website before, and maintain information on them. Sometimes, if you have visited a site previously through Tor, then gone back to it without Tor, it will detect you and your identity is exposed. To avoid this, regularly delete cookies. 

##### CCleaner #####

CCleaner will do the job for you and thoroughly. Also makes viewing your history impossible, should the FBI be knocking on your door.

* Download [CCleaner](http://www.ccleaner.com/download)

##### BleachBit #####

Cleans more crap than CCleaner usually. 

* Download [BleachBit](http://bleachbit.sourceforge.net/)

#### Hard Drive Eraser ####

Similarly, Eraser erases deleted files from your hard drive, making them unrecoverable.

* Download [Eraser](http://anonym.to/?http://findfiles.com/list.php?string=EraserSetup32.exe&size=8944224&db=Mirrors)

#### XP AntiSpy ####

XPAntiSpy - disables alot of the windows tracking features. so logs arent created to begin with [Download](http://www.xp-antispy.org/index.php/en)

### IP Address ###

Your IP (Internet Protocol) address (namely external) is the thing you need to most worry about. Through it, you are traceable to the very place you are sitting now. When you enter a chatroom, you are recorded. When you enter an online game, you are recorded. When you enter a website, you are recorded. It is therefore important to hide it, to remain Anonymous.  If you have a dynamic IP address use that to your advantage.  Change your EXTERNAL IP nightly.  Sometimes resetting your router is enough, other ISPs you need change your MAC address to get a new IP.  Most routers have an option to spoof.
[Tor](/Tor) is the most effective for this. When used properly, even the FBI would have a shit-hard job tracking you down. 
For quick anonymous website browsing, you can pick from a variety of online proxies [here](http://proxy.org/cgi_proxies.shtml)
[Proxifier](/Proxifier) is a useful application that forces any online programme running to go through tor (or whatever proxy you configure it to).

### MAC Address ###

MAC (Media Access Control) address is a quasi-unique identifier assigned to most network adapters or network interface cards (NICs) by the manufacturer for identification. If assigned by the manufacturer, a MAC address usually encodes the manufacturer's registered identification number.
MAC Address is something that most websites don't usually pick up, though sometimes chatrooms/websites/online games will have ways of finding it. It is near impossible to trace an actual machine simply from a MAC Address, but it is also something unique to your machine, and bonus points are given to anyone who [spoofs](User:R3x/MAC_Address_Changer) it.

### DNS ###

If you use your ISPs they can record DNS requests and see wtf your doing. Use level3 dns its like the internets backbone servers. 
4.2.2.2 <br>
4.2.2.3 <br>
4.2.2.4 <br>

### User Agents ###

Slightly trivial, but websites tend to pick up on which web browser you are using (Firefox/Internet Explorer/Safari etc), so it can throw people off the trail if you appear to be using a [User_Agents](/User_Agents) to the one you really are. Using a proxy will change your user agent.

### Referrer ###

Site owners can see how you got to their site by looking at your referrer. If you click a link, the name of that page will be available to the site owner of the page the link takes you to. This is bad in a lot of occasions, such as when you are planning a raid.
There are some things you can do to block your referrer. For more, see [Referrer](/Referrer).

### Encryption ###

Yeah we know how much ceepee you got on that fuckin machine.  Dont leave it out in the open.  My best advice is to make a USB drive that uses encryption, pop it in, enter a password, load your ceepee on it.  Feds come a knocking break the goddamn thing or just "forget" your password.  
Travelers disk with truecrypt is your best bet. [tutorial](http://www.makeuseof.com/tag/encrypt-your-usb-stick-with-truecrypt-60/)

### Search Engines ###

Google keeps search history for 9 fucking months. DONT use it to search lolita and shit.  If you want to stay annon use [IXQuick Anon Search Engine](https://www.ixquick.com/)

### Torrents ###


* Use utorrent with encryption [- Encrypt your traffic](http://torrentfreak.com/how-to-encrypt-bittorrent-traffic/)
* Filter IPs- Utorrent uses a ipfilter.dat that will block known MPAA/RIAA/Fucktards IP ranges. - [blocklist updater](http://www.davidmoore.info/ipfilter-updater/) use that and update all the fucking time.

### WIFI ###

FUCKING HELL dont just have a open AP.  Thats asking for pigs to sit outside and trackyour ass. WEP doesn't counts, even your mom can crack it. Use WPA2 with AES encryption.  If you can stick DD-WRT on that fuckin router.  [DDWRT](http://www.dd-wrt.com) look in the router database.  Youll thank me later.

### EMAIL ###

When you need a email only once use a temp email address. Any real email providers log all your details such as IP and crap forever.

* [Mailinator](http://anonym.to/http://www.mailinator.com)
* [10MinuteMail](http://anonym.to/http://www.10minutemail.com)
* [GurrillaMail](http://anonym.to/http://www.guerrillamail.com)
* [FakeInbox](http://anonym.to/http://www.fakeinbox.com/)
* [Dodgeit](http://anonym.to/http://www.dodgeit.com)
* [YopMail](http://anonym.to/http://www.yopmail.com/)

## The Big TL;DR of Internet Paranoia. ##

Hypothetically speaking; a person who was extremely paranoid online would probably be simultaneously:

* Running a secure environment, which can be: 

1. A read only OS, such as a Live CD/DVD bootable OS
1. A browser set to have no history and no cache
1. [F/i/reLazorz](/F/i/reLazorz).
1. A virtual machine from an encrypted volume.

* Connecting from a free open WiFi hotspot.
* Spoofing their MAC address when connecting to open WiFi, as some access points do log MAC addresses.
* Spoofing their user agent, Use the UserAgentSwitcher addon, or F/i/reLazorz.
* Connecting through a proxy for that extra added measure of security.
* Making sure the proxy is in a foreign country that doesn't have an extradition treaty with the user's country.
* Wearing an approved model of tinfoil hat (Aluminum Foil Deflector Beanie) More info here: <http://zapatopi.net/afdb/>

## IRL Anonymity ##

When out in public, for example at an organised event, meetup, convention:

* Never give out personal information to anyone you don't trust, i.e. everyone.
* Never allow yourself to be followed to a place that might compromise your Anonymity, eg to your car, place of residence, etc

# Trivia #

Failure is not an option.<br><br>
Enemies of Anonymous are permanent.<br><br>
Enemies are to be eliminated swiftly and without incident.<br><br>
Anonymous must work as one. No single Anonymous knows everything.<br><br>
Anonymous does not tolerate action against Anonymous.<br><br>
Any action against Anonymous will be dealt with swiftly and thoroughly.<br><br>
Nothing can harm Anonymous.<br><br>
Anonymous is the will to power.<br><br>
Anonymous is always in control.<br><br>
Anonymous has no identity.<br><br>
Anonymous worships nothing.<br><br>
Anonymous has no leader, and is led by no-one.<br><br>
Human weakness is the virus; Anonymous is the cure.<br><br>
Anonymous is anonymous.<br><br>
Anonymous stays together through common ideas.<br><br>-->
> We are Anonymous.
> 
> We are Legion.
> 
> We do not forgive.
> 
> We do not forget.
> 
> Expect us.

# See Also #


* [/b/](//b/)
* [/i/](//i/)
* [Chan](/Chan)
* [lulz](/lulz)
* [Futaba Channel](/Futaba_Channel)
* [2channel](/2channel)

# External Links #


* [wikipedia page](http://en.wikipedia.org/wiki/Anonymous_(group))
* [ED page](http://encyclopediadramatica.ch/Anonymous)
