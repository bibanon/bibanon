Black Box Plans                                 by The Jolly Roger

Introduction:
------------
At any given time, the voltage running through your phone is about 20
Volts. When someone calls you, this voltage goes up to 48 Volts and rings
the bell. When you answer, the voltage goes down to about 10 Volts.
The phone company pays attention to this. When the voltage drops to 10,
they start billing the person who called you.

Function:
--------
The Black Box keeps the voltage going through your phone at 36 Volts,
so that it never reaches 10 Volts. The phone company is thus fooled
into thinking you never answered the phone and does not bill the caller.
However, after about a half hour the phone company will get suspicious
and disconnect your line for about 10 seconds.

Materials:
---------
1 1.8K 1/2 Watt Resistor
1 1.5V LED
1 SPST Switch

Procedure:
---------
(1) Open your phone by loosening the two screws on the bottom and
lifting the case off.
(2) There should be three wires: Red, Green, and Yellow. We'll be working
with the Red Wire.
(3) Connect the following in parallel:
     A. The Resistor and LED.
     B. The SPST Switch.
In other words, you should end up with this:
              (Red Wire)
           !---/\/\/\--O--!
(Line)-----!              !-----(Phone)
           !-----_/_------!
          /\/\/\ = Resistor
          O      = LED
          _/_    = SPST

Use:
---
The SPST Switch is the On/Off Switch of the Black Box. When the box is off,
your phone behaves normally. When the box is on and your phone rings,
the LED flashes. When you answer, the LED stays on and the voltage
is kept at 36V, so the calling party doesn't get charged. When the box
is on, you will not get a dial tone and thus cannot make calls.
Also remember that calls are limited to half an hour.

                                      ------------Exodus

p.s. Due to new Fone Company switching systems & the like, this 
may or may not work in your area. If you live in bumfuck Kentucky, 
then try this out. I make no guarantees! (I never do...) ----Ex.


