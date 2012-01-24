{{Standard/Notices
| EDImport = true
}}
<br>
![ uses caller ID spoofing! THAT'S LEET!](Caller_ID_spoofing.JPG)
![If s can do this to your computer, just imagine what they can do to your phone!](USNEWSHACKERSCOMPUTERSBOMBS.jpg)
![Caller ID spoofing can be used to order someone boxes upon boxes of delicious pizza!](Anonymousdelivers.jpg)
**Caller ID Spoofing** is one of the greatest things known to trollkind (along with [proxies](/proxies).) It lets said troll display whatever number they want on their target's Caller ID, along with the number's associated name, leaving the victim of said spoofing wondering [Then who was phone](/Then_who_was_phone)
Caller ID Spoofing is in a lot of ways the phone version of using a [proxy](/proxy), and should be in every [troll](/troll)'s toolbox.
[You should also read TOW's caller ID spoofing article.](http://en.wikipedia.org/wiki/Caller_ID_spoofing)

## Technical Shit ##

There are three different types of info about the phone you are calling from that are sent to the called party's phone company, the three are:

* **ANI-II:** A two digit number used to identify what type of phone line you are calling from (eg. cell, landline, payphone run by the phone company, payphone run by shopkeeper, prison phone, hotel phone, operator service for disabled, ANI-II failure, etc.) [(Official Sauce)](http://www.nanpa.com/number_resource_info/ani_ii_assignments.html)
* **ANI:** A ten digit number that identifies the actual phone line the call is being routed through. This always matches your phone number when you dial a number directly, but when dialling through some calling cards or other services that you place a call from, the ANI will match a generic call back number for that service instead.
* **CPN:** A ten digit number that is supposed to identify the phone line the call is being placed from, along with a marker as to whether the calling party wishes to remain anonymous to the caller. Will always match the ANI for directly dialled calls, but when the dialling through a calling card or other services you place a call from it will generally match your phone number even when the ANI doesn't. Caller ID is derived from the CPN. When the phone company of the person you call gets your CPN, they check if there is a privacy flag (from dialling *67 before the call), and if there is they just send private as the Caller ID, otherwise they send the number in the CPN. Because most calling cards have the feature of still displaying your Caller ID, they pass CPN unaffected, even if the outgoing ANI from said cards does not match your phone number anymore.
Caller ID spoofing usually works just like a regular calling card, except instead of passing your CPN to your target's phone company, it lets you control the CPN. Thus, you can spoof any number you want and it will show up on your target's Caller ID, along with the name that is registered for that number (more on using this to get the name for an unlisted number under backspoofing).

## Services ##


* Many caller ID spoofing services work a lot like a calling card, although some have slightly different implementations.
* Prices vary wildly from 1 cent per minute for Zenofon to 33 cents per minute for StealthCallRecorder.
* Spoofcard is the most famous spoofing service and they offer sweet bells and whistles such as call recording and voice changers, although they do charge over 14 cents per minute.
* Go with zenofon for no frills spoofing on the cheap, spoofcard or spoofninja if you need bells and whistles and don't mind being ripped off a bit.
* It is also possible to spoof caller ID yourself with an IP PBX, but this is too much trouble to go through unless your a super 1337 [phreak](/phreak).

## FREE CALLER ID SPOOFING ##

99% of the sites claiming to have free caller ID spoofing are in fact scams, however there are exceptions:

* **Zenofon gives away $0.30 credit with each new account, which at 1c/min totals a half hour of free spoofing.** You can sign up once with each phone number you have. **[CLICK HERE FOR FREE CALLER ID SPOOOOOFIN!!!!!!!!!!!!11111ONEONEONE](http://www.zenofon.com/?LPG9Z)**
* Spoofcard has a promotion where if you let them hijack your twitter account to post about how great they are, they give you a **5 min spoofcard free**. A good troll can register a twitter account every minute and thus get 5 hours of spoofing free from an hour of work until twitter IP bans you. You can use [mailinator](http://www.mailinator.com) to have the pins delivered to as many emails as you want. Warning: These cards expire after 4 months. [Teh linx](http://spoofcard.com/twitter?iframe)
* Several sites that offer paid spoofing have web initiated free trials that last a couple minutes.

## Legality ##

Caller ID spoofing itself as of right now is perfectly legal in most states, although [Captain Obvious](/Captain_Obvious) [X Y is X](/X_Y_is_X)
The Truth in Caller ID Act of <s>2007 2009 may [lie](/lie) pass by the year 2794, making spoofing without the concent of the called party a V&able offense.
You can use Google to figure out if caller ID spoofing is still legal as of the day you read this.

## Traceability ##

Caller ID spoofing is fairly safe, although not untraceable. Here are a few common methods of tracing calls and their results:

* **Target uses *69 post-call:** No use. *69 can sometimes (depending on the target's phone company) call back, or even read off your number despite having been blocked by *67. However *69 only uses CPN information, and because Caller ID spoofing falsifies CPN, the number returned by *69 will be whatever you spoofed.
* **Target looks at call history online or on paper bill:** No use. Call history is generated from Caller ID.
* **Target uses *57 post-call (or whatever the star code for the customer trace feature is):** Probably won't get you vanned, unless you were pulling serious shit. *57 will trap the ANI of the last caller. The target then has to contact the police and request further action; the police will then call the phone company and get the number faxed to them. The ANI will probably be that of spoofing service, and assuming you weren’t doing anything to serious, the cops will give up when the ANI isn't your number, and just go back to eating doughnuts and posting on /b/. Remember, the local cops are not hackers on steroids and if they don’t get your phone number from the trace, they will tell the target that the caller was "untraceable" or some bullshit and to call back if things escalate. If you did pull serious shit on the other hand, the local district attorney will file charges and subpoena your spoofing service for all your dox, and you'll get an express ticket to the Big Bubba Bumfuck-Fest.
* **Target is a super 1337 haxor on steroids and has their home phone forwarded to a personal toll free number:** Very very very unlikely, but watch the fuck out. They will then get the ANI of your spoofing service and after some social engineering, obtain all your dox and then rape your computers, shut off your phone service and post your dox on /b/.
* **You threatened the Grand Pooba of Lower Elbonia:** You're fucked, if you're using caller ID spoofing for really serious shit, you're going to get hunted down one way or another, unless you purchased the spoofing service from a security-camera-less internet cafe under a false name in a city on the other end of the country and then made the call from a payphone there before disposing of the payphone in a recycling plant and hiding out at the south pole for 75 years.
[TL;DR](/TL;DR): If you use it for harmless pranks/[battletoads](/battletoads)/generally fucking with people, you'll be fine and it's much safer than using *67. If you use it for [swatting](/swatting)/major threats/etc, you're gonna get V& [IRL](/IRL).

## Backspoofing ##

Because the name associated with a phone number will show up on Caller ID when you spoof that number, you can use caller ID spoofing to get the names associated with unlisted numbers. This doesn't work with cell phones because names are usually not registered to the CNAM database when a cell phone is purchased, but it almost always works with local landlines.
Heres how to do it:

* 1. Make sure you have a landline phone with caller ID name service.
* 2. Call the landline phone with the number you want the name of spoofed as the Caller ID
* 3. Get the person's name off Caller ID, whether its unlisted or not. (Unless its a cell)
* 4. ????
* 5. PROFIT!

## OMG OLD MEDIA KNOWS ABOUT CALLER ID SPOOFING!!!! ##


(If you get fooled by this shit, kill yourself, now.)

* CNN does a [Faux News](/Faux_News) [ZOMG](/ZOMG) [HACKERS ON STEROIDS](/HACKERS_ON_STEROIDS) style report about swatting and identity theft from Caller ID spoofing.
* [NBC New York Knows!](http://www.nbcnewyork.com/news/local-beat/Are-you-at-risk-of-getting-spoofed-67335977.html)
* [USA TODAY Knows!](http://www.usatoday.com/tech/news/2006-03-01-caller-id_x.htm)
* [EVEN ABC News Knows!](http://abcnews.go.com/Video/playerIndex?id=3307999)

## Uses that [Lie](/Lie) get you V& IRL ##


* [Battletoads](/Battletoads)ing
* Phone mobbing
* General prank calls
* Impersonating Joe Shmoe when calling Jane Shmoe
* General lulz via phone
* Calling [Alex Wuori](/Alex_Wuori), despite his mom's phone tracing system
* Calling any numbers posted on /b/
* Calling random people while spoofing your target's number in hopes of generating tons of callbacks to your target (Like a [DoS#Chicken_Noodle_DRDoS_-_Distributed_Reflection_Denial_of_Service](/DoS#Chicken_Noodle_DRDoS_-_Distributed_Reflection_Denial_of_Service) by phone)
* Ordering people lots and lots of pizza

## Uses that probably will get you V& IRL [and Put in Prison for 11 Years](http://www.mcclatchydc.com/homepage/story/79034.html) ##

**(<s>Don't do this shit under <s>any all circumstances)**

* Impersonating law enforcement
* [Calling law enforcement pretending to be at the home of the person you're spoofing the number of (SWATTING)](http://www.mcclatchydc.com/homepage/story/79034.html)
* Bomb threats
* Serious threats of personal injury
* Social engineering serious shit such as phone records
* Credit card fraud for over $100,000 and the secret service hauls ur ass off, lol.  Anything under $10,000 and no cop cares; happens nonstop on [eBay](/eBay).

## See Also ##


* [SWATing](/SWATing)
* [Alex Wuori](/Alex_Wuori)
* [Phreak](/Phreak)
* [Kevin Mitnick](/Kevin_Mitnick)
* [Hacker](/Hacker)
* [HACKERS ON STEROIDS](/HACKERS_ON_STEROIDS)
* [Proxy](/Proxy)
* [Troll](/Troll)
* [Prank Calls](/Prank_Calls)

## External Links ##


* [Link to Zenofon for a Free Half Hour of Spoofing](http://www.zenofon.com/?LPG9Z)

