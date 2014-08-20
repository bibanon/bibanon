_courtesy of the Jolly Roger_

Just about everyone i talk to these days about ess seems to be scared
witless about the 2600hz detector. i don't know who thought this one up,
but it simply does not exist. so many of you people whine about this so
-called phreak catching device for no reason. 
someone with at&t said they had it to catch phreakers.  this was just to
scare the blue-boxers enough to make them quit boxing free calls.
i'm not saying ess is without its hang-ups, either. one thing that ess can
detect readily is the kick-back that the trunk circuitry sends back to the
ess machine when your little 2600hz tone resets the toll trunk. after an
ess detects a kickback it turns an m-f detector on and recordes any m-f
tones x-mitted.

## DEFEATING THE KICK-BACK DETECTOR

As mentioned in my previous note, kick-back detection can be a serious
nuisance to anyone interested in gaining control of a trunk line.
the easiest way to by-pass this detection circuitry is not really
by-passing it at all, it is just letting the kick-back get detected on
some other line. this other line is your local mci, sprint, or other long
distance carrier (except at&t).  the only catch is that the service 
you use must not disconnect the line when you hit the 2600hz tone.
this is how you do it:  call up your local extender, put in the code,
and dial a number in the 601 area code and the 644 exchange. lots of other
exchanges work across the country, i'm sure, but this is the only one
that i have found so far.  anyway, when it starts ringing, simply hit
2600hz and you'll hear the kick-back, (ka-chirp, or whatever). then you are
ready to dial whoever you want (conferences, inward, route and rate,
overseas, etc.) from the trunk line in operator tones! since blowing
2600hz doesn't make you you a phreaker until the toll equipment resets
the line, kickback detection is the method at&t chooses (for now)
this information comes as a result of my experiments & experience and
has been verified by local at&t employees i have as acquaintances.
they could only say that this is true for my area, but were pretty sure
that the same idea is implemented across the country.

=======================================

Now that you know how to access a trunk line or as operators say a loop, i
will tell you the many things you can do with it.
here is a list of at&t services accessible to you by using a blue box.

* A/C+101    TOLL SWITCHING
* A/C+121    INWARD OPERATOR
* A/C+131    INFORMATION
* A/C+141    ROUTE & RATE OP.
* A/C+11501  MOBILE OPERATOR
* A/C+11521  MOBILE OPERATOR

## STARTING CONFERENCES

This is one the most useful attributes of blue boxing. now the confs.
are up 24 hours/day and 7 days/week and the billing lines are being
billed.
since i beleive the above is true (about the billing lines being billed)
i would recommend that you never let your # show up on the conf. if you
started it, put it on a loop and then call the loop. enough
bullshit!!!!! to start the conf. dial one of these three numbers in
m-f while you are on the trunk.

    213+080+XXXX
    XXXX=1050,3050
    SPECIAL XXXX=1000,1100,1200,1500,2200,2500.

THESE #S ARE IN L.A. AND ARE THE MOST WATCHED, I DO NOT ADVISE USING THIS
NPA.

    312+001+1050 OR 3050
    914+042+1050 OR 1100,1200 ECT..

UPDATE: I BELEIVE ONLY 914 WORKS AT THE MOMENT

Once connected with one of these you will either hear a re-order,
busy, or cherp. when you hear the cherp enter the billing line in m-f.
i use the conf. dial- up.

A BILLING LINE EXAMPLE: KP312+001+1050ST

You will then hear two tutes and a recording asking you for the # of
conferrees including yourself.  enter a # between 20 and 30.
if you ever get over 30 people on a conferance all you will hear is
jumbled voices.  after the it says
"YOUR CONFERANCE SIZE IS XX" Then hit # sign.  add your favorite loop
on and hit 6 to transfer control to it. after it says control will be
transfered hang up and call the other side of the loop,
hit # sign and follow the instructions. a bonus for conf. is to add an
international # dial 1+011+CC+NUMBER PRETTY COOL EHHH.

### a few extra notes.

do not add #s that you will want to hang up, add these through mci or
sprint. you cannot blow anyone off w/2600hz unless they are in an
old x-bar or older system.
many d.a. operators will stay on after you abuse them; you may have to
start another or at least don't say any numbers.
never add the tone side of a loop onto a conf.
never add more than one mci node on your conf.

ROUTE & RATE:
-------------

Note route & rate and rqs perform the same service.
r&r simply tells you route and rate info which is very valuble, ex.
such as the inward routing for an exchange in an area code.  
an inward routing will let you call her and she can do an emergency
interupt for you. she can tell you how to get international operators,ect.
here are the terms you are required to use:
international,

- OPERATOR ROUTE FOR [COUNTRY, CITY]. *GIVES YOU INWARD OP.
- DIRECTORY ROUTE FOR [COUNTRY, CITY]. *GIVES YOU DIRECTORY ASS.
- CITY ROUTE FOR [COUNTRY, CITY]. *GIVES YOU COUNTRY AND CITY CODE.

Operator route for [A/C]+ [EXCHANGE] *gives you inward op. ROUTE
EX. [A/C]+ OR [A/C]+0XX+ When she says plus she means plus 121.
numbers route for [STATE, CITY] *gives you A/C.
Place name [A/C]+[EXCHANGE] *gives you city/state for that a/c and
exchange.

INTERNATIONAL CALLS:
--------------------

to call international over cable simply access a trunk and dial
KP011XXXST wait for sender tone, KPXXXCC-NUMBERST
XXX - A 3 digit country code, It may not be 3 digits so just put
1 or 2 0's in front of it. cc - is the city code
to go by satellite:
DIAL KP18XST    X - NUMBERS 2-8 Wait for sender tone then
KPXXXCCNUMBERST

A favorite in the CookBookIV!
Exodus-.