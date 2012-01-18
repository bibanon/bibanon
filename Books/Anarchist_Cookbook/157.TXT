The Infinity Transmitter                  courtesy of Exodus
                                          originally typed by:
                                                    <<<Ghost Wind>>>

                         FROM THE BOOK BUILD YOUR OWN
         LASER, PHASER, ION RAY GUN & OTHER WORKING SPACE-AGE PROJECTS
                       BY ROBERT IANNINI (TAB BOOKS INC)

Description:  Briefly, the Infinity Transmitter is a device which activates a
microphone via a phone call.  It is plugged into the phone line, and when the
phone rings, it  will immediately intercept the ring and broadcast into the
phone any sound that is in the room. This device was originally made by
Information Unlimited, and had a touch tone decoder to prevent all who did not
know the code from being able to use the phone in its normal way.  This
version, however, will activate the microphone for anyone who calls while it is
in operation.
NOTE:  It is illegal to use this device to try to bug someone. It is also
pretty stupid because they are fairly noticeable.
Parts List:
Pretend that uF means micro Farad, cap= capacitor

Part           #          Description
----           -          -----------
R1,4,8         3         390 k 1/4 watt resistor
R2             1         5.6 M 1/4 watt resistor
R3,5,6         3         6.8 k 1/4 watt resistor
R7/S1          1         5 k pot/switch
R9,16          2         100 k 1/4 watt resistor
R10            1         2.2 k 1/4 watt resistor
R13,18         2         1 k 1/4 watt resistor
R14            1         470 ohm 1/4 watt resistor
R15            1         10 k 1/4 watt resistor
R17            1         1 M 1/4 watt resistor
C1             1         .05 uF/25 V disc cap
C2,3,5,6,7     5         1 uF 50 V electrolytic cap or tant
                          (preferably non-polarized)
C4,11,12       3         .01 uF/50 V disc cap
C8,10          2         100 uF @ 25 V electrolytic cap
C9             1         5 uF @ 150 V electrolytic cap
C13            1         10 uF @ 25 V electrolytic cap
TM1            1         555 timer dip
A1             1         CA3018 amp array in can
Q1,2           2         PN2222 npn sil transistor
Q3             1         D4OD5 npn pwr tab transistor
D1,2           2         50 V 1 amp react. 1N4002
T1             1         1.5 k/500 matching transformer
M1             1         large crystal microphone
J1             1         Phono jack optional for sense output
WR3            (24")     #24 red and black hook up wire
WR4            (24")     #24 black hook up wire
CL3,4          2         Alligator clips
CL1,2          2         6" battery snap clips
PB1            1         1 3/4x4 1/2x.1 perfboard
CA1            1         5 1/4x3x2 1/8 grey enclosure fab
WR15           (12")     #24 buss wire
KN1            1         small plastic knob
BU1            1         small clamp bushing
B1,2           2         9 volt transistor battery or 9V ni-cad

Circuit Operation: Not being the most technical guy in the world, and not being
very good at electronics (yet),  I'm just repeating what Mr. Iannini's said
about the circuit operation.  The Transmitter consists of a high grain
amplifier fed into the telephone lines via transformer.  The circuit is
initiated by the action  of  a voltage transient pulse occurring across  the
phone line  at the instant the telephone circuit is made (the ring,  in other
words).  This transient immediately triggers a timer  whose output  pin  3 goes
positive, turning on transistors Q2 and  Q3. Timer TM1 now remains in this
state for a period depending on the values  of R17 and C13 (usually about 10
seconds for  the  values shown). When Q3 is turned on by the timer, a simulated
"off hook" condition is created by the switching action of Q3 connecting the
500  ohm  winding  of the transformer directly across  the  phone lines.
Simultaneously, Q2 clamps the ground of A1, amplifier, and Q1, output
transistor, to the negative return of B1,B2, therefore enabling this amplifier
section.  Note that B2 is always required by  supplying  quiescent power to TM1
during  normal conditions. System is off/on controlled by S1 (switch).
  A  crystal mike picks up the sounds that are fed to  the  first two
transistors of the A1 array connected as an emitter follower driving the
remaining  two  transistors  as  cascaded   common emitters. Output of the
array now drives Q1 capacitively coupled to  the  1500 ohm  winding of  T1.
R7  controls  the  pick  up sensitivity of the system.
  Diode  D1  is  forward biased at the instant of  connection  and essentially
applies a negative pulse at pin 2 of TM1,  initiating the cycle.   D2 clamps
any high positive pulses.   C9 dc-isolates and desensitizes the circuit. The
system described should operate when any incoming call is made without ringing
the phone.

Schematic Diagram:  Because this is text,  this doesn't look  too hot. Please
use  a little imagination!  I will hopefully get  a graphics drawing  of  this
out as soon as I  can  on  a  Fontrix graffile.

To be able to see what everything is, this character: | should appear as a
horizontal bar. I did this on a ][e using a ][e 80 column card, so I'm sorry if
it looks kinda weird to you.

Symbols:
 resistor: -/\/\/-            switch: _/ _
 battery:  -|!|!-             capacitor (electrolytic): -|(-
 capacitor (disc): -||-                   _    _
 transistor:(c)  > (e)        Transformer: )||(
              \_/                          )||(
               |(b)                       _)||(_
 diode: |<
 chip: ._____.
       !_____! (chips are easy to recognize!)

 Dots imply a connection between wires. NO DOT, NO CONNECTION.
ie.:  _!_ means a connection while _|_ means no connection.
----------------------------------------------------------------------------

.________________________to GREEN wire phone line
|
| .______________________to RED wire phone line
| |
| |     ._________(M1)______________.
| |     |                           |
| |     |           R1              |
| |     !__________/\/\/____________!
| |     |                          _!_ C1
| |     |this wire is the amp      ___
| |     |<=ground                   |                     R2
| |     |                           !___________________/\/\/_____________.
| |     |                   ._______!_______.                             |
| |     !___________________!4      9     11!_____________________________!
| |     |                   |               |                             |
| |     !___________________!7            12._____________________________!
| |     |                   |     A1        |              R3             |
| |     !___________________!10       ____*8!_______.____/\/\/____________! ^
| |     |                   |        /      |       |                     | |
| |     |    C4             |       /       |       \                     |2ma
| |     !____||______.      |      /        |       /R4                B1 +
| |     |    ||      |      |     /         |       \                    |!|!
| |     |     R7     |  C2  |    /          |       /                     |
| |     !____/\/\/___!__)|__!8*_/           |       |                 S1  |
| |     |     ^             |              6!_______!           neg<__/.__!
| |     |     |     C3      |               |       | C5       return     |
| |     |     !_____|(___.__!3              |       '-|(-|                |
| |     |                |  |       5      1!____________!                |
| |     |                \  !_______._______!            |             B2|!|!
| |     !________.    R8 /          |                    |                +
| |              |       \          |                    |      R6        |3ma
| |              |       !__________!____________________|_____/\/\/______! |
| |              |    R5            |                    |                | v
| |              !__/\/\/___________|____________________!                |
| |              |                  |                                     |
| |              |                  |                                     |
| |              |               C6 |                                     |
| |              |             |-)|-'             R9                      |
| |              |             !_________________/\/\/_______.            |
| |              |             |                             |            |
| |              |         Q1 _!_                            |   R10      |
| |              !____________/ \____________________________!__/\/\/_____!
| |              |                                           |            |
| |              |                                           |            |
| |              |          C8                               |            |
| |              !__________)|_______________________________|____________!
| |              !                                           |            |
| |             /                                            |            |
| |       -----|                                             |            |
| |       |     \                                            |            |
| |       |      >                                           |            |
| |       |      |                                           |            |
| |       |      |                                           |            |
| |       |      !_____________.                             |            |
| |       |                    |                             |            |
| |       !__________.         |                             |            |
| |                  |         |                             |            |
| !________.         |         |                       ._____!            |
|          |         |         |                       |                  |
|          |         |         |                       |                  |
|          |         |         |                       | C7               |
|          |         |         |                       '-|(-|             |
|          |_________|_________!_______.T1._________________|             |
|                    |         |  1500 )||( 500                           |
|                    |         |   ohm )||( ohm                           |
|                    |         !______.)||(.__.                           |
|                    |         |              |                           |
|                    |         |              |                           |
|                    |         |              >                           |
|                    |         |            |/                            |
|                    |         |       +----|   Q3                        |
|                    |         |       |    |\                            |
!____________________|_________|_______|______!__. D1   C9                |
                     |         |       |         '-|<---|(------|         |
      .______________!         |       |                        |         |
      |                        |       |                        |         |
      |       .________________!       |                        |         |
      |       |                        |                        |         |
      \       |       .________________!             C11        |         |
      /       |       |                       .___||____________!         |
  R13 \       |       |                       |   ||            |         |
      /       |       |                       |                 |         |
      \       !___.___|_______________________!                 |         |
      |       |   |   |                       |     R16         |    R15  |
      |       v   |   |                       !___/\/\/\________!___/\/\/_!
      |      neg  |   |                       |    D2           |         |
      |    return |   |                       !_____|<__________!         |
      |     B1,B2 |   \                       |                 |         |
      |           |   /                       |    .____________!_.       |
      |           |   \R14                    |C12 |   TM1      2 |       |
      |           |   /                       !_||_!5            4!_______!
      |           |   \                       | || |              |       |
      |           |   |                       !____!1            8!_______!
      |           |   |                       |    |     7 6   3  |       |
      |           |   |                       |    !_____._.____._!       |
      |           |   |                       |          | |    |         |
      |           |   |                       |   C13    | |    |   R17   |
      |           |   |                       !___)|_____!_!____|__/\/\/__!
      |           |   |                       |                 |         |
      !___________|___!_______________________|_________________!         |
                  |   |                       |                           |
                  |   \                       |          C10              |
                  |   /R18                    !__________)|_______________!
                  |   \
                  |   /
                  |   |
                  !___O J1
                    sense output

Construction notes: Because the damned book just gave a picture instead of step
by step instructions, and I'll try to give you as much help as possible. Note
that all the parts that you will be using are clearly labeled in the schematic.
The perfboard, knobs, 'gator clips, etc are optional. I do strongly suggest
that you do use the board!!! It will make wiring the components up much much
easier than if you don't use it.
 The knob you can use to control the pot (R7). R7 is used to tune the IT so
that is sounds ok over the phone. (You get to determine what sounds good) By
changing the value of C13, you can change the amount of time that the circuit
will stay open (it cannot detect a hang up, so it works on a timer.) A value of
100 micro Farads will increase the time by about 10 times.
 The switch (S1) determines whether or not the unit is operational. Closed is
on. Open is off. The negative return is the negative terminals of the battery!!
The batteries will look something like this when hooked up:

  <-v_____.   .______.    ._____.   .____->
          |   |      |    |     |   |
        __!___!__    |    |   __!___!__
        | +   - |    !_/ _!   | +   - |
        |       |  switch ^   |       |
        | 9volts|         |   | 9volts|
        !_______! neg return  !_______!

 To hook this up to the phone line, there are three ways, depending upon what
type of jack you have. If it is the old type (non modular) then you can just
open up the wall plate and connect the wires from the transmitter directly to
the terminals of the phone.
 If you have a modular jack with four prongs, attach the red to the negative
prong (don't ask me which is which! I don't have that type of jack... I've only
seen them in stores), and the green to the positive prong, and plug in. Try not
to shock yourself...
 If you have the clip-in type jack, get double male extension cord (one with a
clip on each end), and chop off one clip. Get a sharp knife and splice off the
grey protective material. You should see four wires, including one green and
one red. You attach the appropriate wires from the IT to these two, and plug
the other end into the wall.

Getting the IT to work: If you happen to have a problem, you should attempt to
do the following (these are common sense rules!!) Make sure that you have the
polarity of all the capacitors right (if you used polarized capacitors, that
is). Make sure that all the soldering is done well and has not short circuited
something accidently (like if you have a glob touching two wires which should
not be touching.) Check for other short circuits. Check to see if the battery
is in right. Check to make sure the switch is closed.
 If it still doesn't work, drop me a line on one of the Maryland or Virginia
BBSs and I'll try to help you out.

The sense output: Somehow or other, it is possible to hook something else up to
this and activate it by phone (like an alarm, flashing lights, etc.)

As of this writing, I have not tried to make one of these, but I will. If you
actually get it working, leave me a note somewhere.

I sure hope all you people appreciate this.


