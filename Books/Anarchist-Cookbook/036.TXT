Phone Systems Tutorial part II                  by The Jolly Roger

Part II will deal with the various types of operators, office 
heirarchy, & switching equipment.

Operators
~~~~~~~~~

There are many types of operators in the network and the more 
common ones will be discussed.

TSPS Operator:

The TSPS [(Traffic Service Position System) ass opposed to This 
Shitty Phone Service] Operator is probably the bitch (or bastard, 
for the female libertationists out there) that most of us are used 
to having to deal with. Here are his/her responsibilities:

1) Obtaning billing information for calling card or third number 
calls

2) Identifying called customer on person-to-person calls.

3) Obtaining acceptance of charges on collect calls.

4) Identifying calling numbers. This only happens when the calling 
# is not automatically recorded by CAMA (Centralized Automatic 
Message Accounting) & forwarded from the local office. This could 
be caused by equipment failures (ANIF- Automatic Number 
Identification Failure) or if the office is not equipped for CAMA 
(ONI- Operator Number Identification).

<I once has an equipment failure happen to me & the TSPS operator 
came on and said, "What # are you calling FROM?" Out of curiosity, 
I gave her the number to my CO, she thanked me & then I was 
connected to a conversation that appeared to be between a frameman 
& his wife. Then it started ringing the party I wanted to 
originally call & everyone phreaked out (excuse the pun). I 
immediately dropped this dual line conference!

You should not mess with the TSPS operator since she KNOWS which 
number that you are calling from. Your number will show up on a 
10-digit LED read-out (ANI board). She also knows whether or not 
you are at a fortress phone & she can trace calls quite readily! 
Out of all of the operators, she is one of the MOST DANGEROUS.

INWARD operator:

This operator assists your local TSPS ("0") operatorin connecting 
calls. She will never question a call as long as the call is 
withing HER SERVICE AREA. She can only be reached via other 
operators or by a blue box. From a blue box, you would dial 
KP+NPA+121+ST for the INWARD operator that will help you connect 
any calls within that NPA only. (Blue Boxing will be discussed in 
a future file).

DIRECTORY ASSISTANCE Operator:

This is the operator that you are connected to when you dial: 411 
or NPA-555-1212. She does not readily know where you are calling 
from. She does not have access to unlisted numbers, but she DOES 
know if an unlisted # exists for a certain listing.

There is also a directory assistance operator for deaf people who 
use teletypewriters. If your modem can transfer BAUDOT [(45.5 
baud). One modem that I know of that will do this is the Apple Cat 
acoustic or the Atari 830 acoustic modem. Yea I know they are hard 
to find... but if you wanna do this.. look around!) then you can 
call him/her up and have an interesting conversation. The # is: 
800-855-1155. They use the standard Telex abbreviations such as GA 
for go ahead. they tend to be nicer and will talk longer than your 
regular operators. Also, they are more vulnerable into being 
talked out of information through the process of "social 
engineering" as Chesire Catalyst would put it. 

<Unfortunately, they do not have access to much. I once 
bullshitted with one of these operators a while back and I found 
out that there are 2 such DA offices that handle TTY. One is in 
Philadelphia and the other is in California. They have approx. 7 
operators each. most of the TTY operators think that their job is 
boring (based on an official "BIOC poll"). They also feel that 
they are under-paid. They actually call up a regular DA # to 
process your request (sorry, no fancy computers!)

Other operators have access to their own DA by dialing 
KP+NPA+131+ST (MF).

CN/A operators:

CN/A Operators are operators that do exactly the opposite of what 
directory assistance operators are for. In my experience, these 
operators know more than the DA op's do & they are more 
susceptable to "social engeneering." It is possible to bullshit a 
CN/A operator for the NON-PUB DA # (ie, you give them the name & 
they give you the unlisted number. See the article on unlisted 
numbers in this cookbook for more info about them.). This is due 
to the fact that they assume that you are a fellow company 
employee. Unfortunately, the AT&T breakup has resulted in the 
break-up of a few NON-PUB DA #'s and policy changes in CN/A

INTERCEPT Operator:

The intercept operator is the one that you are connected to when 
there are notenough recordings available to tell you that the # 
has been disconnected or changed. She usually says, "What # you 
callin'?" with a foreign accent. This is the lowest operator 
lifeform. Even though they don't know where you are calling from, 
it is a waste or your time to try to verbally abuse them since 
they usually understand very little English anyway.

Incidentally, a few area DO have intelligent INTERCEPT Operators.

OTHER Operators:

And then there are the: MObile, Ship-to-Shore, Conference, Marine 
Verify, "Leave Word and Call Back," Rout & Rate 
(KP+800+141+1212+ST), & other special operators who have one 
purpose or another in the network.

Problems with an Operator> Ask to speak to their supervisor... or 
better yet the Group Chief (who is the highest ranking official in 
any office) who is the equivalent of the Madame ina whorehouse.

By the way, some CO's that willallow you to dial a 0 or 1 as the 
4th digit, will also allow you to call special operators & other 
fun Tel. Co. #'s without a blue box. This is ver rare, though! For 
example,212-121-1111 will get you a NY Inward Operator.

Office Hierarchy
~~~~~~~~~~~~~~~~

Every switching office in North America (the NPA system), is 
assigned an office name and class. There are five classes of 
offices numbered 1 through 5. Your CO is most likely a class 5 or 
end office. All long-distance (Toll) calls are switched by a toll 
office which can be a class 4, 3, 2, or 1 office. There is also a 
class 4X office callen an intermediate point. The 4X office is a 
digital one that can have an unattended exchange attached to it 
(known as a Remote Switching Unit (RSU)).

The following chart will list the Office #, name, & how many of 
those office exist (to the best of my knowledge) in North America:

Class                 Name           Abb          # Existing
-----        ----------------------- ---      -----------------
> 1          Regional Center          RC                   12
> 2          Sectional Center         SC                   67
> 3          Primary Center           PC                  230
> 4          Toll Center              TC                1,300
> 4P         Toll Point               TP                 n/a
> 4X         Intermediate Point       IP                 n/a
> 5          End Office               EO               19,000
> 6          RSU                     RSU                 n/a

When connecting a call from one party to another, the switching 
equipment usually tries to find the shortest route between the 
class 5 end office of the caller & the class 5 end officeof the 
called party. If no inter-office trunks exist between the two 
parties, it will then move upward to the next highest office for 
servicing calls (Class 4). If the Class 4 office cannot handle the 
call by sending it to another Class 4 or 5 office, it will then be 
sent to the next highest office in the hierarchy (3). The 
switching equipment first uses the high-usage interoffice trunk 
groups, if they are busy then it goes to the fina; trunk groups on 
the next highest level. If the call cannot be connected, you will 
probably get a re-order [120 IPM (interruptions per minute) busy 
signal] signal. At this time, the guys at Network Operations are 
probably shitting in their pants and trying to avoid the dreaded 
Network Dreadlock (as seen on TV!).

It is also interesting to note that 9 connections in tandem is 
called ring-around-the-rosy and it has never occured in telephone 
history. This would cause an endless loop connection [a neat way 
to really screw up the network].

The 10 regional centers in the US & the 2 in Canada are all 
interconnected. they form the foundation of the entire telephone 
network. Since there are only 12 of them, they are listed below:

Class 1 Regional Office Location   NPA
--------------------------------   ---
Dallas 4 ESS                       214
Wayne, PA                          215
Denver 4T                          303
Regina No. 2SP1-4W (Canada)        306
St. Louis 4T                       314
Rockdale, GA                       404
Pittsburgh 4E                      412
Montreal No. 1 4AETS (Canada)      504

That's it for now! More info to come Future update to the 
Cookbook! Have fun!                        -Exodus-




