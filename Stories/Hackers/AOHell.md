[[AOHell.jpg|float|width=300px|height=200px]]

*From the Something Awful Forums, author "iceaim"*

This thread has been inspired by the "Anyone remember AOHell and similiar programs?" thread in SH/SC. Well personally I was never into that AOHell shit. Way too amateur. I do admit that I did start out with AOHell but quickly outgrew it.

I used various methods to crack employee "internal" accounts and volunteer "overhead" and "community leader" accounts which were used by GUIDES and other AOL volunteers.

## Special AOL Accounts

Below is a description of some of the "special" AOL accounts that were around.

1. Overhead - This is a special account which is not billed any monthly fees. Many Guides and other volunteers initially had these accounts. Also certain corporations also had these kind of accounts for their employees too. Namely ones which had "content" on AOL.

Some of the cool features of this account were the ability to IM people who had their IMs off, the ability to scroll in the chat room like a madman without being booted off, and also gaining access to some restricted keywords. This was a great account for punting people (since you could IM people who had their IMs off). Also good way to fuck up a chat room too. Good account for lifting tokens too.

You could IM TOSadvisor with it, and even have a conversation with him. He's a nice guy (or guys since it seemed TOSadvistor was on 24/7), unless of course he came into a chat room because you're stirring up trouble (More on this later).

2. Community Leader Account - This is one of the shittiest special accounts you could find. AOL decided to move most of their volunteer accounts (except for Guides) to this account type. It can't break through disabled IMs nor can it scroll. All it could take is access the same restricted keywords that an OH account can. It's good for lifting tokens, and fairly common so it's easy to hijack.

3. Guide (Overhead) account - This is special OH account used by Guides. I'm sure you former AOL users remember these assholes trolling the chatrooms. They always ruined the fun because when they were around you couldn't use foul language without getting an OSW (On Screen Warning) which resulted in getting your account knocked offline and a nice TOS violation mark on your record. Three OSW reports and your AOL account is insta canned. Guides were pretty much fags who worked for free and did it for the free AOL and the power trip. 

Guide accounts can do everything that regular OH accounts do plus offer the ability to do an OSW (Great way to smoke accounts) and the timed gag.

The timed gag is a neat little chat command that allows you to prevent someone from chatting. Now unless you announce to the person that they were gagged, they would never realize it because to them it looks like the chat text is showing up fine but no one else can see it. Guides will announce to the chatter that they've been gagged, but I never did since it's more fun that way. Timed gags were logged so I used them sparingly (Until I got CRIS access). Once the timed gag is applied the chatter will be gagged for X minutes (set by the guide) and there is no way to chat until the time limit was up.

4. Rainman - These accounts could publish and modify keywords. That's about it. For some reason a lot of lamers thought that could do more.

5. Internal - Internal accounts are given to employees and are a lot of fun to use. They can do everything an OH can do plus access ALL restricted keywords. Furthermore they can do untimed gags which prevented the chatter from but only while they were in the chat room. Once they left and re-entered the chat room the gag no longer applied. Despite this limitation, these gags were a lot of fun to use when unannounced and they weren't logged like timed gags.

Internal accounts could also access CRIS (now Merlin) which is a member database containing details of every AOL account made. You kill accounts, perma ban accounts, change name and address, reset the account's password, and do a bunch of other things. 

Unfortunately CRIS was firewalled so the only way you could only access it is if you were inside one of AOL's buildings or had a special piece of hardware that looked like a calculator called a SecurID. CRIS looked like it would impossible to break into at first, but AOL didn't take into account the stupidity of their employees....

## Breaking in

While guides and many AOL volunteers are obvious due to their restricted names, "internal" employee accounts are less obvious. In fact I found the employee list while token scanning.

What is token scanning you might ask? Well they are similar to "invokes" from master AOL. In fact an "invoke" is a type of token (U1 I believe). Invokes in most cases (but not all) are for old keywords that are usually abandoned. Token ranges on the other hand may be actively used. All keywords have a token assigned to it. Almost like every domain has an ip address.

Now certain keywords on AOL are restricted like keyword ARC. If you access it from a normal account it will behave like it doesn't exist (viewruling). However if accessed from a overhead or internal account the keyword will work. Once accessed from a special account, its token can be lifted so that it can be accessed from a regular account. Funny thing is you can get around the viewrule by accessing the token rather than the keyword directly.

So how do you access tokens. You need an add on application called Rainman Tool. It adds on to your copy of AOL much in the same manner that Master AOL did but it gave you many more menu options. In addition to using it to token scan, it can also be used to design new keywords. It used a scripting language called FDO which is like a propriatory version of HTML. While anyone can design keywords, only special rainman aol accounts can "publish" new keywords. Rainman accounts have been jacked in the past and keywords have actually been vandalized sort of how we see html pages defaced these days. While you may not be able to upload new keyword pages, they can run on your local machine and can interface with AOL. Very nice for exploits (More on this later).

Oh and FYI many lamers thought "rainman tool" was used to create overhead accounts thus causing many to download fake "rainman tool" apps online which did nothing but steal their password. :keke:

So anyway I made a simple VB program that used API to control the AOL client. This allowed me to create a token scanner that scanned for tokens with rainman and record any interesting ones I found. I used the keyword ARC token as my "base" and used it to dig up other restricted AOL employee or volunteer areas. After a bit of scanning I hit the jackpot! I found an employee area with a sexy text document that contained a list of AOL employee accounts!!! With this list I was guaranteed to gain access to several employee accounts.

The way I cracked accounts was via a password cracker I made. First version was slow because it actually send the commands to the AOL client, but eventually I made a winsock based version which was much faster and didn't require the AOL client. AOL's login protocol was similar to pop3. 

Anyway you'd be surprised what dumb passwords these geniuses picked. I've seen everything from "dildo" and "bacon" to password spelled backwards :lol:.

In addition to cracking, I also wrote a sweet little password sniffer. First version mailed out the password via the AOL mail form and used a screen capture and forced the curser into an hourglass to mask itself while my more advanced version used winsock to mail out the password via an open relay. 

When using a sniffer, I usually converted the EXE into .SHS (scrapbook file) by pasting the EXE into wordpad and dragged the pasted EXE into my desktop. For some reason it converted it into a .SHS file but it acted just like an exe! Most idiots figured .SHS was some sort of image format. 

When using the sniffer I would make friends with the internal I wanted to "hack". My friendship would usually last for months so that I could gain their trust, and usually I made several friends at once. Eventually I would go "Hey Bob you got a pic?". Usually "Bob" would go "Oh yeah!" and we swapped pics. My "pic" was of course an SHS file. When executed it showed a real pic of "me" for realism before activating the sniffer.

## Exploits

Some exploits I found (none of them work today). There were more but I forgot them, these really stood out to me:

1. I found a token that was some sort of ad for some shitty camera AOL was pushing. What was interesting about it is if you pushed the order button it showed a prefilled form with YOUR full name, address, and credit card info!!! 

Essentially any stolen AOL account turned into a credit card. I used a few to card porn site membership, but got bored of that fast. Also using stolen credit cards even behind proxys made me a little uncomfortable as did causing some innocent individual financial loss (I later found out that in the end the merchant gets fucked not the individual).

2. In the "AOHell" thread some of you mentioned those restricted screen names like "Guide", "Help", and "Host". Well normally you can't make these, but after AOL trains a Guide candidate they reserve a screen name for them. While that screenname on reserve anyone who knows about it can take it. In the ideal situation only the Guide and AOL know about it.

I knew about it too after reading some documentation I found while token scanning.

So I wrote another VB app that scanned for open restricted screen names. You entered a prefix into it like "Guide", "Host", "AOLtech", etc. It would then rapidly run through sufixes like "Guide AAA, Guide AAB, etc" until it found a valid non restricted screen name. This application was not winsock based and used the AOL client to do this.

3. With Rainman tool and VPD (IIRC) you could access the source code of any AOL form. Well after downloading the source to the "Create a screen name" form I figured out how to modify the source to allow me to make any restricted screen name! I don't remember the exact details today on what I did but when viewing the modified form with rainman it allowed any restricted name I desired. This exploit died pretty fast.

4. Not really an exploit but I found a document that detailed about a new keyword called toxic im. The allowed any community leader account to file a special toxic IM tos report. As deadly as OSW and worked with all comunity leader accounts. Unlike "normal" aol account TOS reports, toxic IM smoked the offending account in seconds.

Toxic IM was added because a lot of punters were punting volunteer hosts who were trying to help members or something like that. When accessing the keyword you pasted the offending punter HTML so that AOL could research it. Of course it was easy to forge that too and smoke somebody's account who you really hated.

Unfortunately more than one person found out about this and it was abused and eventually killed.

5. Not really an exploit but as a Guide you can issue an OSW report. Each OSW will bump the account user offline and three will terminate the account for good. You are supposed to send an email to "Deadvolvo" or "GrandpaZ3" (These screen names may be wrong since I'm pulling this from the top of my head) with the proper OSW format and the bot reading the report would execute the OSW.

Those stupid Guides didn't delete their sent email so I lifted the OSW format and wrote a VB app that automated the OSW process and even announced to the chat room which user was about to lose their AOL account. 

I made a "stealth mode" option too which announced the kill on a "normal" AOL account while the Guide account initiated the kill. This prevented my target from claiming that a Guide account was compromised when calling AOL. Instead they would blame some normal account account causing the rep on the phone to go ":lol: sure kid". 

6. I figured out how to get around the firewall that protected the CRIS database. With some help from a more advanced programmer friend I made a special proxy server which bounced my packets through an AOL employee's workstation. After making friends with an AOL employee and sending them my "pic" I was in business.

I modified my TCP/IP CCL login script so that instead of connecting to do the default tcp "Bring your own access" server it connected to the compromised AOL workstation machine which redirected the packet to the default tcp server. This caused the tcp server see an ip address that was in one of AOL's offices and call centers. 

When logging in with an internal account and going to keyword CRIS I had complete access to CRIS from an internal account! This allowed me to do almost anything I damn pleased except view someone's password. This was bad because since all CRIS activity is logged, I didn't want them to realize I was resetting Guide accounts. I also didn't want to do any direct malicious activity with CRIS because AOL thought it was "impossible" and I didn't want them to know about that security hole. I really wanted to save this exploit so I wanted to be conservative.

Well I found another exploit that allowed me to view passwords! (See Below)

7. When AOL released AIM they allowed any AOL account to be converted to AIM. The converted AIM account would have the same password as the AOL account. So what I did was convert the AOL account to AIM and then selected the "forgot password" option. The forgot password form would email out the forgotten password of the AIM account to the AOL email address it was converted from. You see after the AIM account was made, it was semi independant of the AOL account. Meaning you could change the password of the AIM account while keeping the AOL password the same.

So before resetting the password I would do the above. Once reset, I logged in and check the account's email, pulled up the "Forgotten Password" email and went to keyword "password" to change the password back to its original.

This allowed me to access every Guide account I desired. That way if I wanted to term someone, rather than doing it via CRIS I did it indirectly with the Guide account via OSW. 

The CRIS exploit lasted a long time, but eventually someone else did the same thing I did and wasn't as conservative as me. This caused a huge panic at AOL and they fixed that hole by requiring to everyone to use their SecurID device even while inside the AOL building. Hopefully they were also smart enough to modify their firewall so that unauthorized servers could not be run on employee workstations :lol:.

8. This was the last major exploit I did after my CRIS exploit died. This might not seem like a big exploit but it make me a lot of money (more on this later). I figured out a way that prevented my AOL account from getting terminated if I was caught with a "unacceptable" profile. Normally when AOL found an unacceptable profile they would delete it and note a TOS violation on your AOL account. After three TOS violations your account is toast.

Well I found out that after my profile was deleted, if I went on my master screen name and deleted the screen name with the deleted profile and then used the "restore" feature to restore my deleted screen name that the profile would also be restored! Not only that but if AOL caught the vulgar profile again they would delete it but it wouldn't count as a TOS violation!!!! So at worst, my screen name would only have 1 violation and it wouldn't die.

After about 1 year and a half AOL found out, but I made a lot of money with it. This exploit was my transition from being a loser "hacker" to businessman since it gave me seed money to start a legit enterprise.

## What I did

Some things I did while being an angsty AOL "hacker":

1. There was this teen chat room that I hated. It was one of those special moderated conference rooms which held more than 24 people. People talked about the gayest shit and the moderators were equally gay. So I hopped on an internal account and gagged the entire room including moderators. This made the chat room way better. For 5 minutes no one spoke and the stupid mods knew something was up. Finally TOSadvisor came in the room and one of the mods IMed me saying something lame like "So it was you!!! You are in big trouble now!!". Then TOSadvisor IMed me and asked for my supervisor. I replied with "Steve Case". This caused my account to be bumped offline with the password reset.

2. I hated "proggie" rooms. Talk about gay. Everyone and their mother thought they were some sort of hacker because they could push a few buttons. Wow what a rough crowd. I would annouce to the room who I would be booting/terming and I would personally IM them too. They would laugh it off and call me a lamer until they got bumped. When they came back online they were all "WuT HoW DId u dO dAt?? WaNa B PreZ of Mi HaCkeR GreWp?". I liked to toy with them at that point. I would sometimes tell them that I am going to terminate their account. They would shit their pants and beg me not to or their moms would kill them. Of course I did anyway. God I was such a dick, even if they were just AOL pups who made a scriptkiddie look smart.

3. I loved to goto the Black and Asian rooms and asked them if it was okay to hang out there even though I was white. If the room welcomed me in open arms I do nothing and be cool. If they replied with some racial slur it would be payback. Most of the aZn chat rooms were cool with me although some notibly the "PinoY" rooms for some reason did not like a whiteboy coming into their rooms. They would "step up" and tell me they'd "fuck me up" if I didn't leave.

You can guess what happened. I sniped their accounts one by one till they were all gone.

Yes it was a real dickhead thing to do even if they were pricks. I had a lot of Asian friends though (since they were computer nerds like me) and they thought it was funny. :)

4. AOL had these special "tech support" rooms where you could get one on one help with an "AOLTech" rep. If you used AOL for a while you probably know what I'm talking about. Well with an AOLTech account I could access these rooms too on the tech support side! They were password protected with a special PIN but these smarty man reps sometimes had the PIN in their mailbox! I would simply keep CRISing accounts till I found one that had a PIN. 

With PIN in hand I accessed the tech support chat room and started "helping" people. No matter what question the AOLer had I would "solve" their problem by instructing them how to "deltree" themselves in a DOS console window. Some caught on, but *most* didn't. You'd think they'd be suspicious typing "deltreee". 

As soon as the victim said "HEY WHY ARE MY FILES BEING DELETED!!!!!!" I would kick them off so I could "help" the next person.

God I was such a prick! Talk about angst.

## Going Gold

When I turned 15 I finally realized that "hacking" AOL was gay as hell and a waste of time. I decided to use my skills for profit rather than fucking around AOL.

My first for profit venture was botting. I noticed there were a lot of chat spam bots on AOL. They were all intrusive and gay. They pushed all sort of adult websites which these bots were earning commission on via an affiliate program. 

Now I was smart enough to realize that unless you had a backdoor deal, there was no way to get away with spamming links in the chat rooms. In fact I've seen many of those idiot chat bots get their affiliate link codes disabled.

Well during this time I read about a public "exploit" that allowed you to have links in your profile that could link to any website. Normally only AOL homepage links were linkable on your profile. Well I used this link exploit to link to a porn site I made with various adult sites that I was advertising. My profile had naughty words on it that make me look like a "cam girl" and lured the AOL surfer to the adult site.

I realized that if I just idled in a cybersex chat room under a sexy screen like like "Sxy Hot 18 Cindy" that tons of people would access my profile and check out my site. I didn't even chat or anything, I just idled. So I didn't annoy anyone nor did I spam so my sponsor never got any complaints.

Unfortunately AOL *DID* get complaints from asshole fucks who were pissed that I was indling in "their" chat room. This got me TOSed, but led to my discovery of exploit number 8.

By this time I had setup a S-corporaiton with the help of my parents and a special business account with AOL. You see normally you are limited to the amount of pay AOL account you could create per credit card. I think the limit was five, but I needed 100. The solution was AOL's business service. This was for any business who needed to make many AOL accounts for their employees and was stupid enough to think AOL is a good way for their employees to access the Internet. Rather than billing your credit card, AOL mailed out an invoice that was supposed to be paid every month. This setup was perfect so I made 100 accounts for my "employees" and controlled AOL like the mafia controlled Vegas. It was a pretty sweet setup, I had my very own personal account rep and everything.

This AOL bot method made a pretty penny too. I was pulling in over 13 grand a month when I was 17.

This "partnership lasted for about one and a half years. AOL charged me $14.95 per month for each account so they made out real good out of this deal. Well after 1.5 years they finally figured out what was going on and killed exploit #8. Not only that but they reset all my passwords and continued to send me an invoice anyway. So after 2 months of getting billed for dead accounts I called my rep.

I was real pissed, I called my account rep who very rudely told me "Ameria Online is not interested in your kind of business.". I told him "Okay well I would like a refund for the past 2 months since I couldn't access my accounts". He replied with "I'm sorry sir but you still have to pay the entire balance due". I replied back with "I'm sorry but I refuse to pay the balance and I think both you and AOL can go suck a dick!". After he heard that he sounded pretty shocked as if nobody ever said anything like that to him "Well sir.....I uh....think this conversation is over."

This really pissed me off at the time and it ment war. I fucking paid $1495 a month for AOL ACCESS to advertise adult services in CYBER SEX chat rooms in a low key manner and this is how they fucking treat me? Fine fuck it. No more Mr. Nice Guy.

Since I couldn't advertise on AOL in a semi-legit and low key fashion I went with a more invasive and even less legit fashion. I started to email spam. By this time I had a good rep with my sponsors and I too setup some backdoor spam deals.

I was determined to milk AOL for all its worth and punish them by causing them as much grief as possible via spam complaints their members filed. I wasn't the only guy spamming AOL though, there were other AOL spammers too. All of them morons. Sure there were spammers making a SHITLOAD of money but rather than investing their money into legit business ventures they blew it on drugs and who knows what else. I knew this because I lurked in a AOL email spammer forum.

When I was doing the bot thing and the spam thing I was very conservative with my money. Since I didn't drink or do drugs I was able to wisely invest my money into various legit ventures. Some are still around today while others failed miserably. I was always thinking of new business ventures and still am today. 

I never spammed non AOL users. I figured if someone was dumb enough to use AOL they deserved to be spammed. Besides I didn't know how to harvesnt quality non AOL lists (I figured email addresses harvested from search engines were shit anyway and hammered to death by other spammers).

I don't do email spamming anymore and I kind of regret doing it in a way. Nothing forced me to continue milking AOL. I was already making a killing also exploiting the search engines at the same time by getting the top listings on major porn related keywords.

Well I don't spam anymore and never plan on doing it in the future. It was sleazy but hey I was young. I figure if Steve Jobs make his seed money selling Blue Boxes, I would make mine this way.

It's been a fun ride going from loser "hacker" to legitimate businessman. My business is constantly expanding. Right now I have 5 new business ventures that that I thought up and are on the "drawing boards" in addition to my current ventures. I have 8 full time programmers now in the Ukraine and am an IT major now (My parents pushed me to goto college "just in case").

So that's my story. Any comments and questions? Flames? Feel free to post your computer experiences relating to AOL or the Internet too. Well it's late, time for me to goto bed. Take care everyone!

Sorry if I pissed anyone off with this thread. I was an angsty teen I guess.

## Sources

* [Shii's archive of this story](http://shii.org/knows/From_AOL_Hacker_to_Businessman)