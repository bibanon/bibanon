User Agents are strings that [browser](/browser)s send out in order to identify themselves. A User Agent usually identifies the browser version and operating system being used. This information is sometimes used by websites to control what the user can see. Spoofing a User Agent is extremely simple; the browser just needs to send out a false User Agent string. 

# Uses of User Agent Spoofing #


## [Anonymity](/Anonymity) ##

We can throw off some attempts at being identified by supplying fake User Agents. If the site is looking for someone using Firefox 2.0.12, and you look like Opera 9, they won't notice you. However, this method isn't foolproof. More advanced sites can find out who you are, using methods such as examining your [HTTP header](/HTTP_header)s, or by using Javascript. More info [here](http://www.net-security.org/dl/articles/browser_ident.pdf)

## Pretending to be a specific browser/device ##

Some sites will only display content to users with certain browsers or devices (such as mobile phones). Spoofing the right User Agent is most likely all you need to do in order to gain access to this content.

## Pretending to be a Web crawler ##


### Google ###

Have you ever searched something on Google, clicked a link, and been given an 'access denied' error? The reason for this is that some sites allow Google bots to access places a normal person can't, so that the site can still be indexed. We can use this to our advantage, by pretending to be one of Google's spiders, which will allow us to see the protected content. Certain versions of IPB are vulnerable to this, and one major example was the cheating site msxsecurity.com (before it closed down), in which you could gain access to the VIP area with this trick. The UserAgent to use when impersonating Google is:
    Googlebot/2.1 (+<http://www.googlebot.com/bot.html)>

# Tools #


## Firefox Add-ons ##


* [User Agent Switcher](https://addons.mozilla.org/en-US/firefox/addon/59)

# Lists #


* <http://www.user-agents.org/>
* <http://www.useragentstring.com/pages/useragentstring.php>
* [AgentStrings20070304.xml (for use with User Agent Switcher)](http://www1.qainsight.net:8080/content/binary/AgentStrings20070304.xml)

# Moar #


* [HTTP header](/HTTP_header)

