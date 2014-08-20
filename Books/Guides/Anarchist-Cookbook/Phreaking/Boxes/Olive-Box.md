Olive Box Plans                        Courtesy of Exodus

    This is a relatively new box, and all it basically does is serve as a phone
ringer. You have two choices for ringers, a piezoelectric transducer (ringer),
or a standard 8 ohm speaker. The speaker has a more pleasant tone to it, but
either will do fine. This circuit can also be used in conjunction with a rust
box to control an external something or other when the phone rings. Just connect
the 8 ohm speaker output to the inputs on the rust box, and control the pot to
tune it to light the light (which can be replaced by a relay for external
controlling) when the phone rings.

             ______________
            |              |        ^
       NC --|-- 5      4 --|-----/\/\/------->G
            |              |      / R2
G<----)|----|-- 6      3 --|-- NC
    | C3    |      U1      |
     -------|-- 7      2 --|---------- --- -- - > TO RINGER
            |              |
        ----|-- 8      1 --|--
       |    |______________|  |
       |                       ---/\/\/----|(----- L1
       |                           R1      C1
        ------------------------------------------ L2

                  a. Main ringer TTL circuit

(>::::::::::::::::::::::::::::::::::::::::::::::::::::::::<)

                                   _
FROM PIN 2 < - -- --- ----------| |_| |------------->G
                                    P1

                  b. Peizoelectric transducer

(>::::::::::::::::::::::::::::::::::::::::::::::::::::::::<)

                                                      __  /|
FROM PIN 2 < - -- --- ---------|(---------.  .-------|  |/ |
                                          >||<       |S1|  |
                                          >||<     --|  |  |
                                          >||<    |  |__|\ |
                              G<---------.>||<.---        \|
                                           T1
                c. Elctro magnetic transducer
Parts List
----------

U1 - Texas Instruments TCM1506
T1 - 4000:8 ohm audio transfomer
S1 - 8 ohm speaker
R1 - 2.2k resistor
R2 - External variable resistor; adjusts timing frequency
C1 - .47uF capacitor
C2 - .1uF capacitor
C3 - 10uF capacitor
L1 - Tip
L2 - Ring
     L1 and L2 are the phone line.


Shift Rate:
-----------

  This is the formula for determining the shift rate:

                   1                   1
    SR = --------------------- = ------------ = 6.25 Hz
         (DSR(1/f1)+DSR(1/f2))    128     128
                                 ----  + ----
                                 1714    1500


              DSR = Shift Devider Rate ratio = 128
                f1 = High Output Frequency = 1714
               f2 = Low Output Frequency = 1500



