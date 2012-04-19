
                                ==Phrack Inc.==
 
                     Volume Three, Issue 28, File #5 of 12
 
                  /////////////////////\\\\\\\\\\\\\\\\\\\\\
                 ||                                        ||
                 || A Real Functioning PEARL BOX Schematic ||
                 ||                                        ||
                 ||        Written, Tested, and Used       ||
                 ||                                        ||
                 ||               by Dispater              ||
                 ||                                        ||
                 ||              July 1, 1989              ||
                 ||                                        ||
                  \\\\\\\\\\\\\\\\\\\\\/////////////////////
 
 
Introduction:  After reading the earlier renditions of schematics for the Pearl
               Box, I decided that there was an easier and cheaper way of doing
               the same thing with an IC and parts you probably have just
               laying around the house.
 
 
What Is A Pearl Box and Why Do I Want One?
 
     A Pearl Box is a tone generating device that is used to make a wide range
     of single tones.  Therefore, it would be very easy to modify this basic
     design to make a Blue Box by making 2 Pearl Boxes and joining them
     together in some fashion.
 
     A Pearl Box can be used to create any tone you wish that other boxes may
     not.  It also has a tone sweep option that can be used for numerous things
     like detecting different types of phone tapping devices.
 
 
Parts List:
 
        CD4049 RCA integrated circuit
        .1 uF disk capacitor
        1 uF 16V electrolitic capacitor
        1K resistor
        10M resistor
        1meg pot
        1N914 diode
        Some SPST momentary push-button switches
        1 SPDT toggle switch
        9 Volt battery & clip
        and miscellaneous stuff you should have laying around the house.
 
 
State-of-the-Art-Text Schematic:
                                       +  16V  1uF -
              _______________________________||_____
             |        !     !                ||     |           _
             |   _______________________            |__________| |/| 8ohms
         ____|__|_____:__|__:__|_       |            __________| | |
        | 9 10 11 12 13 14 15 16 |      |           |          |_|\|
        |        CD4049UBE       |      |           |
        |_1__2__3__4__5__6__7__8_|      :           |          _
          |  |  |__|  |__|  |  |____________________|_________[-]
          |  |  !           !           :                     [b]
          |  |__________________________|                     [a]
          |     :           :           |                     [t]
          |     !    1N914  !           !                     [t]
          |___________|/|_____________________________________[+]
                :     |\|   :           :
                |           |           |
                |    10M    |           |
                |___/\/\/\__|           |
                |           |           |
                |_____||____|           |  <-- These 2 wires to the center pole
                      ||    |           |      of switch.
                 .1uF   50V |           |
                            |           |
     _______________________|           |_____________________________
    |                   ___[Toggle Switch]____________                |
    |                  |                              |          ___  |
    |                  |                              |          o o  |
    |                  |                              | /\/\/\___| |__|
    |_/\/\/\____/\/\/\ |                              |    ^          |
        1K         ^   |                              |____|     ___  |
                   |___|                              |          o o  |
                                                      | /\/\/\___| |__|
          (pAakala                 Administrator:  Gary W. Krumbine
Gen Directorate Of Post &                   AT&T Information Systems
Phone:  35806921730                         Lincroft, NJ  07738
                                            Phone:  +1 201 576 2658
 
MHS Gateway:  mhs!telemail                  MHS Gateway:  mhs
Administrator:  Jim Kelsay                  Administrator:  AT&T Mail MHS
GTE Telenet Comm Corp                                       Gateway
Reston, VA  22096                           AT&T
Phone:  +1 703 689 6034                     Lincroft, NJ  08838
                                            Phone:  +1 800 624 5672
 
CMR
~~~
Previously known as Intermail, the Commercial Mail Relay (CMR) Service is a
mail relay service between the Internet and three commercial electronic mail
systems:  US Sprint/Telenet, MCI-Mail, and DIALCOM systems (i.e. Compmail,
NSFMAIL, and USDA-MAIL).
 
An important note:  The only requirement for using this mail gateway is that
the work conducted

- Exodus -