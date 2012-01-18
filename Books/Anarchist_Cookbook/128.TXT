

                                ==Phrack Inc.==
 
                     Volume Three, Issue 30, File #3 of 12
 
               [-][-] [-][-] [-][-] [-][-] [-][-] [-][-] [-][-]
               [-]                                          [-]
               [-]             Hacking & Tymnet             [-]
               [-]                                          [-]
               [-]                    by                    [-]
               [-]                                          [-]
               [-]                Synthecide                [-]
               [-]                                          [-]
               [-][-] [-][-] [-][-] [-][-] [-][-] [-][-] [-][-]
 
 
There are literally hundreds of systems connected to some of these larger
networks, like Tymnet and Telenet.  Navigation around these networks is very
simple, and usually well explained in their on-line documentation.
Furthermore, some systems will actually tell you what is connected and how to
get to it.  In the case of Tymnet, after dialing in, at the log in prompt, type
"information" for the on-line documentation.
 
Accessing systems through networks is as simple as providing an address for it
to connect to.  The best way to learn about the addresses and how to do things
on a network is to read "A Novice's Guide to Hacking (1989 Edition)" which was
in Issue 22, File 4 of 12, Volume Two (December 23, 1988).  Some points are
re-iterated here.
 
Once on a network, you provide the NUA (network user address) of the system you
wish to connect to.  NUAs are strings of 15 digits, broken up in to 3 fields,
the NETWORK ADDRESS, the AREA PREFIX, and the DNIC.  Each field has 5 digits,
and are left padded with 0's where necessary.
 
The DNIC determines which network to take the address from.  Tymnet, for
example, is 03106. 03110 is Telenet.
 
The AREA PREFIX and NETWORK ADDRESS determine the connection point.  By
providing the address of the system that you wish to connect to, you will be
accessing it through the net... as if you were calling it directly.  Obviously,
then, this provides one more level of security for access.
 
By connecting to an outdial, you can increase again the level of security you
enjoy, by using the outdial in that area to connect to the remote system.
 
Addendum -- Accessing Tymnet Over Local Packet Networks
 
This is just another way to get that extra step and/or bypass other routes.
This table is copied from Tymnet's on-line information.  As said earlier, it's
a great resource, this on-line information!
 
                                 BELL ATLANTIC
 
  NODE    CITY                  STATE           SPEED    ACCESS NUMBER  NTWK
  ----   -------------------    --------------  ------   ------------   ----
  03526   DOVER                 DELAWARE        300/2400 302/734-9465   @PDN
  03526   GEORGETOWN            DELAWARE        300/2400 302/856-7055   @PDN
  03526   NEWARK                DELAWARE        300/2400 302/366-0800   @PDN
  03526   WILMINGTON            DELAWARE        300/1200 302/428-0030   @PDN
  03526   WILMINGTON            DELAWARE        2400     302/655-1144   @PDN
 
 
  06254   WASHINGTON            DIST. OF COL.   300/1200 202/479-7214   @PDN
  06254   WASHINGTON (MIDTOWN)  DIST. OF COL.   2400     202/785-1688   @PDN
  06254   WASHINGTON (DOWNTOWN) DIST. OF COL.   300/1200 202/393-6003   @PDN
  06254   WASHINGTON (MIDTOWN)  DIST. OF COL.   300/1200 202/293-4641   @PDN
  06254   WASHINGTON            DIST. OF COL.   300/1200 202/546-5549   @PDN
  06254   WASHINGTON            DIST. OF COL.   300/1200 202/328-0619   @PDN
 
  06254   BETHESDA              MARYLAND        300/1200  301/986-9942  @PDN
  06254   COLESVILLE            MARYLAND        300/2400  301/989-9324  @PDN
  06254   HYATTSVILLE           MARYLAND        300/1200  301/779-9935  @PDN
  06254   LAUREL                MARYLAND        300/2400  301/490-9971  @PDN
  06254   ROCKVILLE             MARYLAND        300/1200  301/340-9903  @PDN
  06254   SILVER SPRING         MARYLAND        300/1200  301/495-9911  @PDN
 
 
  07771   BERNARDSVILLE         NEW JERSEY      300/2400 201/766-7138   @PDN
  07771   CLINTON               NEW JERSEY      300-1200 201/730-8693   @PDN
  07771   DOVER                 NEW JERSEY      300/2400 201/361-9211   @PDN
  07771   EATONTOWN/RED BANK    NEW JERSEY      300/2400 201/758-8000   @PDN
  07771   ELIZABETH             NEW JERSEY      300/2400 201/289-5100   @PDN
  07771   ENGLEWOOD             NEW JERSEY      300/2400 201/871-3000   @PDN
  07771   FREEHOLD              NEW JERSEY      300/2400 201/780-8890   @PDN
  07771   HACKENSACK            NEW JERSEY      300/2400 201/343-9200   @PDN
  07771   JERSEY CITY           NEW JERSEY      300/2400 201/659-3800   @PDN
  07771   LIVINGSTON            NEW JERSEY      300/2400 201/533-0561   @PDN
  07771   LONG BRANCH/RED BANK  NEW JERSEY      300/2400 201/758-8000   @PDN
  07771   MADISON               NEW JERSEY      300/2400 201/593-0004   @PDN
  07771   METUCHEN              NEW JERSEY      300/2400 201/906-9500   @PDN
  07771   MIDDLETOWN            NEW JERSEY      300/2400 201/957-9000   @PDN
  07771   MORRISTOWN            NEW JERSEY      300/2400 201/455-0437   @PDN
  07771   NEWARK                NEW JERSEY      300/2400 201/623-0083   @PDN
  07771   NEW BRUNSWICK         NEW JERSEY      300/2400 201/247-2700   @PDN
  07771   NEW FOUNDLAND         NEW JERSEY      300/2400 201/697-9380   @PDN
  07771   PASSAIC               NEW JERSEY      300/2400 201/473-6200   @PDN
  07771   PATERSON              NEW JERSEY      300/2400 201/345-7700   @PDN
  07771   PHILLIPSBURG          NEW JERSEY      300/2400 201/454-9270   @PDN
  07771   POMPTON LAKES         NEW JERSEY      300/2400 201/835-8400   @PDN
  07771   RED BANK              NEW JERSEY      300/2400 201/758-8000   @PDN
  07771   RIDGEWOOD             NEW JERSEY      300/2400 201/445-4800   @PDN
  07771   SOMERVILLE            NEW JERSEY      300/2400 201/218-1200   @PDN
  07771   SOUTH RIVER           NEW JERSEY      300/2400 201/390-9100   @PDN
  07771   SPRING LAKE           NEW JERSEY      300/2400 201/974-0850   @PDN
  07771   TOMS RIVER            NEW JERSEY      300/2400 201/286-3800   @PDN
  07771   WASHINGTON            NEW JERSEY      300/2400 201/689-6894   @PDN
  07771   WAYNE/PATERSON        NEW JERSEY      300/2400 201/345-7700   @PDN
 
 
  03526   ALLENTOWN             PENNSYLVANIA    300/1200 215/435-0266   @PDN
  11301   ALTOONA               PENNSYLVANIA    300/1200 814/946-8639   @PDN
  11301   ALTOONA               PENNSYLVANIA    2400     814/949-0505   @PDN
  03526   AMBLER                PENNSYLVANIA    300/1200 215/283-2170   @PDN
  10672   AMBRIDGE              PENNSYLVANIA    300/1200 412/266-9610   @PDN
  10672   CARNEGIE              PENNSYLVANIA    300/1200 412/276-1882   @PDN
  10672   CHARLEROI             PENNSYLVANIA    300/1200 412/483-9100   @PDN
  03526   CHESTER HEIGHTS       PENNSYLVANIA    300/1200 215/358-0820   @PDN
  03526   COATESVILLE           PENNSYLVANIA    300/1200 215/383-7212   @PDN
  10672   CONNELLSVILLE         PENNSYLVANIA    300/1200 412/628-7560   @PDN
  03526   DOWNINGTON/COATES.    PENNSYLVANIA    300/1200 215/383-7212   @PDN
  03562   DOYLESTOWN            PENNSYLVANIA    300/1200 215/340-0052   @PDN
  03562   GERMANTOWN            PENNSYLVANIA    300/1200 215-843-4075   @PDN
  10672   GLENSHAW              PENNSYLVANIA    300/1200 412/487-6868   @PDN
  10672   GREENSBURG            PENNSYLVANIA    300/1200 412/836-7840   @PDN
  11301   HARRISBURG            PENNSYLVANIA    300/1200 717/236-3274   @PDN
  11301   HARRISBURG            PENNSYLVANIA    2400     717/238-0450   @PDN
  10672   INDIANA               PENNSYLVANIA    300/1200 412/465-7210   @PDN
  03526   KING OF PRUSSIA       PENNSYLVANIA    300/1200 215/270-2970   @PDN
  03526   KIRKLYN               PENNSYLVANIA    300/1200 215/789-5650   @PDN
  03526   LANSDOWNE             PENNSYLVANIA    300/1200 215/626-9001   @PDN
  10672   LATROBE               PENNSYLVANIA    300/1200 412/537-0340   @PDN
  11301   LEMOYNE/HARRISBURG    PENNSYLVANIA    300/1200 717/236-3274   @PDN
  10672   MCKEESPORT            PENNSYLVANIA    300/1200 412/673-6200   @PDN
  10672   NEW CASTLE            PENNSYLVANIA    300/1200 412/658-5982   @PDN
  10672   NEW KENSINGTON        PENNSYLVANIA    300/1200 412/337-0510   @PDN
  03526   NORRISTOWN            PENNSYLVANIA    300/1200 215/270-2970   @PDN
  03526   PAOLI                 PENNSYLVANIA    300/1200 215/648-0010   @PDN
  03562   PHILADELPHIA          PENNSYLVANIA    300/1200 215/923-7792   @PDN
  03562   PHILADELPHIA          PENNSYLVANIA    300/1200 215/557-0659   @PDN
  03562   PHILADELPHIA          PENNSYLVANIA    300/1200 215/545-7886   @PDN
  03562   PHILADELPHIA          PENNSYLVANIA    300/1200 215/677-0321   @PDN
  03562   PHILADELPHIA          PENNSYLVANIA    2400     215/625-0770   @PDN
  10672   PITTSBURGH            PENNSYLVANIA    300/1200 412/281-8950   @PDN
  10672   PITTSBURGH            PENNSYLVANIA    300/1200 412-687-4131   @PDN
  10672   PITTSBURGH            PENNSYLVANIA    2400     412/261-9732   @PDN
  10672   POTTSTOWN             PENNSYLVANIA    300/1200 215/327-8032   @PDN
  03526   QUAKERTOWN            PENNSYLVANIA    300/1200 215/538-7032   @PDN
  03526   READING               PENNSYLVANIA    300/1200 215/375-7570   @PDN
  10672   ROCHESTER             PENNSYLVANIA    300/1200 412/728-9770   @PDN
  03526   SCRANTON              PENNSYLVANIA    300/1200 717/348-1123   @PDN
  03526   SCRANTON              PENNSYLVANIA    2400     717/341-1860   @PDN
  10672   SHARON                PENNSYLVANIA    300/1200 412/342-1681   @PDN
  03526   TULLYTOWN             PENNSYLVANIA    300/1200 215/547-3300   @PDN
  10672   UNIONTOWN             PENNSYLVANIA    300/1200 412/437-5640   @PDN
  03562   VALLEY FORGE          PENNSYLVANIA    300/1200 215/270-2970   @PDN
  10672   WASHINGTON            PENNSYLVANIA    300/1200 412/223-9090   @PDN
  03526   WAYNE                 PENNSYLVANIA    300/1200 215/341-9605   @PDN
  10672   WILKINSBURG           PENNSYLVANIA    300/1200 412/241-1006   @PDN
 
 
  06254   ALEXANDRIA            VIRGINIA        300/1200  703/683-6710  @PDN
  06254   ARLINGTON             VIRGINIA        300/1200  703/524-8961  @PDN
  06254   FAIRFAX               VIRGINIA        300/1200  703/385-1343  @PDN
  06254   MCLEAN                VIRGINIA        300/1200  703/848-2941  @PDN
 
 
    @PDN BELL ATLANTIC - NETWORK NAME IS PUBLIC DATA NETWORK (PDN)
 
 
             (CONNECT MESSAGE)
             . _. _. _< _C _R _> _            (SYNCHRONIZES DATA SPEEDS)
 
             WELCOME TO THE BPA/DST PDN
 
             *. _T _  _< _C _R _> _           (TYMNET ADDRESS)
 
 
             131069             (ADDRESS CONFIRMATION - TYMNET DNIC)
             COM                (CONFIRMATION OF CALL SET-UP)
 
             -GWY 0XXXX- TYMNET: PLEASE LOG IN:  (HOST # WITHIN DASHES)
 
 
                                  BELL SOUTH
 
  NODE    CITY                  STATE           DENSITY  ACCESS NUMBER MODEM
  -----   --------------------  --------------  ------   ------------  -----
  10207   ATLANTA               GEORGIA         300/1200 404/261-4633  @PLSK
  10207   ATHENS                GEORGIA         300/1200 404/354-0614  @PLSK
  10207   COLUMBUS              GEORGIA         300/1200 404/324-5771  @PLSK
  10207   ROME                  GEORGIA         300/1200 404/234/7542  @PLSK
 
 
    @PLSK  BELLSOUTH - NETWORK NAME IS PULSELINK
 
 
             (CONNECT MESSAGE)
 
             . _. _. _  _< _C _R _> _           (SYNCHRONIZES DATA SPEEDS)
                                (DOES NOT ECHO TO THE TERMINAL)
             CONNECTED
             PULSELINK
 
             1 _3 _1 _0 _6 _              (TYMNET ADDRESS)
                                (DOES NOT ECHO TO THE TERMINAL)
 
             PULSELINK: CALL CONNECTED TO 1 3106
 
             -GWY 0XXXX- TYMNET: PLEASE LOG IN:  (HOST # WITHIN DASHES)
 
 
                                 PACIFIC BELL
 
  NODE    CITY                  STATE           DENSITY  ACCESS NUMBER  NTWK
  -----   -------------------   --------------  ------   ------------   ----
  03306   BERKELEY              CALIFORNIA      300/1200 415-548-2121   @PPS
  06272   EL SEGUNDO            CALIFORNIA      300/1200 213-640-8548   @PPS
  06272   FULLERTON             CALIFORNIA      300/1200 714-441-2777   @PPS
  06272   INGLEWOOD             CALIFORNIA      300/1200 213-216-7667   @PPS
  06272   LOS ANGELES(DOWNTOWN) CALIFORNIA      300/1200 213-687-3727   @PPS
  06272   LOS ANGELES           CALIFORNIA      300/1200 213-480-1677   @PPS
  03306   MOUNTAIN VIEW         CALIFORNIA      300/1200 415-960-3363   @PPS
  03306   OAKLAND               CALIFORNIA      300/1200 415-893-9889   @PPS
  03306   PALO ALTO             CALIFORNIA      300/1200 415-325-4666   @PPS
  06272   PASADENA              CALIFORNIA      300/1200 818-356-0780   @PPS
  03306   SAN FRANCISCO         CALIFORNIA      300/1200 415-543-8275   @PPS
  03306   SAN FRANCISCO         CALIFORNIA      300/1200 415-626-5380   @PPS
  03306   SAN FRANCISCO         CALIFORNIA      300/1200 415-362-2280   @PPS
  03306   SAN JOSE              CALIFORNIA      300/1200 408-920-0888   @PPS
  06272   SANTA ANNA            CALIFORNIA      300/1200 714-972-9844   @PPS
  06272   VAN NUYS              CALIFORNIA      300/1200 818-780-1066   @PPS
 
 
    @PPS   PACIFIC BELL - NETWORK NAME IS PUBLIC PACKET SWITCHING (PPS)
 
             (CONNECT MESSAGE)
 
             . _. _. _< _C _R _             (SYNCHRONIZES DATA SPEEDS)>
                                (DOES NOT ECHO TO THE TERMINAL)
 
             ONLINE 1200
             WELCOME TO PPS:  415-XXX-XXXX
             1 _3 _1 _0 _6 _9 _             (TYMNET ADDRESS)
                                (DOES NOT ECHO UNTIL TYMNET RESPONDS)
 
         -GWY 0XXXX- TYMNET: PLEASE LOG IN:  (HOST # WITHIN DASHES)
 
                               SOUTHWESTERN BELL
 
  NODE    CITY                  STATE           DENSITY  ACCESS NUMBERS NWRK
  -----   --------------------  --------------  -------  ------------   -----
  05443   KANSAS CITY           KANSAS          300/1200 316/225-9951   @MRLK
  05443   HAYS                  KANSAS          300/1200 913/625-8100   @MRLK
  05443   HUTCHINSON            KANSAS          300/1200 316/669-1052   @MRLK
  05443   LAWRENCE              KANSAS          300/1200 913/841-5580   @MRLK
  05443   MANHATTAN             KANSAS          300/1200 913/539-9291   @MRLK
  05443   PARSONS               KANSAS          300/1200 316/421-0620   @MRLK
  05443   SALINA                KANSAS          300/1200 913/825-4547   @MRLK
  05443   TOPEKA                KANSAS          300/1200 913/235-1909   @MRLK
  05443   WICHITA               KANSAS          300/1200 316/269-1996   @MRLK
 
 
  04766   BRIDGETON/ST. LOUIS   MISSOURI        300/1200 314/622-0900   @MRLK
  04766   ST. LOUIS             MISSOURI        300/1200 314/622-0900   @MRLK
 
 
  06510   ADA                   OKLAHOMA        300/1200 405/4


On a side note, the recent book The Cuckoo's Egg provides some interesting
information (in the form of a story, however) on a Tymnet hacker.  Remember
that he was into BIG things, and hence he was cracked down upon.  If you keep a
low profile, networks should provide a good access method.
 
If you can find a system that is connected to the Internet that you can get on
from Tymnet, you are doing well.
_______________________________________________________________________________


-- Exodus --  '94