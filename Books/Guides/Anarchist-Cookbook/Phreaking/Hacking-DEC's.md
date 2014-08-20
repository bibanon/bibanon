Hacking DEC's                                 by the Jolly Roger

In this article you will learn how to log in to dec's, logging out, and all
the fun stuff to do in-between.  All of this information is based on a
standard dec system.
Since there are dec systems 10 and 20, and I favor, the dec 20,
there will be more info on them in this article.  It just so happens
that the dec 20 is also the more common of the two, and is used by much
more interesting people (if you know what I mean...) Ok, the first thing
you want to do when you are receiving carrier from a dec system is to find
out the format of login names.  You can do this by looking at who is on the
system.
Dec=> `  (the 'exec' level prompt)
you=> sy
sy is short for sy(stat) and shows you the system status.
You should see the format of login names...
A systat usually comes up in this form:
job  line  program  user
job:  the job number (not important unless you want to log them off later)
line:  what line they are on (used to talk to them...)
These are both two or three digit numbers.
Program:  what program are they running under?  If it says 'exec'
they aren't doing anything at all...
User:  ahhhahhhh!  This is the user name they are logged in under...
Copy the format, and hack yourself outa working code... Login format is as
such:
dec=> `
you=> login username password
username is the username in the format you saw above in the systat.
After you hit the space after your username, it will stop echoing
characters back to your screen.  This is the password you are typing in...
Remember, people  usually use their name, their dog's name, the name of a
favorite character in a book, or something like this. A few clever
people have it set to a key cluster (qwerty or asdfg).  Pw's can be from 1
to 8 characters long, anything after that is ignored. You are finally in...
It would be nice to have a little help, wouldn't it?  Just type a ? Or the
word help, and it will give you a whole list of topics...
Some handy characters for you to know would be the control keys,
wouldn't it? Backspace on a dec 20 is rub which is 255 on your ascii chart.
On the dec 10 it is cntrl-h. To abort a long listing or a program,
cntrl-c works fine.  Use cntrl-o to stop long output to the terminal.
This is handy when playing a game, but you don't want to cntrl-c out.
Cntrl-t for the time. Cntrl-u will kill the whole line you are typing at
the moment.  You may accidently run a program where the only way out is
a cntrl-x, so keep that in reserve. Cntrl-s to stop listing, cntrl-q to
continue on both systems. Is your terminal having trouble??
Like, it pauses for no reason, or it doesn't backspace right?  This is
because both systems support many terminals, and you haven't told it what
yours is yet... You are using a vt05
so you need to tell it you are one.
Dec=> `
you=> information terminal
or...
You=> info
this shows you what your terminal is set up as...
Dec=>all sorts of shit, then the `
you=> set ter vt05 this sets your terminal
type to vt05.
Now let's see what is in the account (here after abbreviated acct.)
that you have hacked onto... Say
=> dir
short for directory, it shows
you what the user of the code has save to the disk.  There should be a format
like this:    xxxxx.Oooxxxxx is the file name, from 1 to 20 characters
long.  Ooo is the file type, one of: exe, txt, dat, bas, cmd   and a few
others that are system dependant.
Exe is a compiled program that can be run (just by typing its name at the `).
Txt is a text file, which you can see by
typing=>
type xxxxx.Txt
Do not try to=>
type xxxxx.Exe this is very bad for your terminal and will tell you
absolutly nothing.
Dat is data they have saved.
Bas is a basic program, you can have it typed out for you.
Cmd is a command type file, a little too
complicated to go into here.
Try =>
take xxxxx.Cmd
By the way, there are other users out there who may have files you can use
(gee, why else am I here?).
Type => dir <*.*> (Dec 20)
     => dir [*,*]   (dec 10)
* is a wildcard, and will allow you to access the files on other accounts
if the user has it set for public access. If it isn't set for public access,
then you won't see it. To run that program:
dec=> `
you=> username program-name
username is the directory you saw the
file listed under, and file name was
what else but the file name?
**  You are not alone  **
remember, you said (at the very start) sy  short for systat,
and how we said this showed the other users on the system?  Well, you
can talk to them, or at least send a message to anyone you see listed in a
systat.  You can do this by:
dec=> the user list (from your systat)
you=> talkusername (dec 20)
      send username (dec 10)
talk allows you and them immediate transmission of whatever you/they type
to be sent to the other.  Send only allow you one message to be sent, and
send, they will send back to you, with talk you can just keep going. By the
way, you may be noticing with the talk command that what you type is still
acted upon by the parser (control program).  To avoid the constant error
messages type either:
you=>  ;your message
you=>  rem your message
the semi-colon tells the parser that what follows is just a comment.  Rem
is short for 'remark' and ignores you from then on until you type a cntrl-z
or cntrl-c, at which point it puts you back in the exec mode. To break the
connection from a talk command type:
you=>  break priv's:
if you happen to have privs, you can do all sorts of things. 
First of all, you have to activate those privs.
You=> enable
this gives you a $ prompt, and allows you to do this:
whatever you can do to your own directory you can now do to any
other directory. To create a new acct. Using your privs, just type
=>build username
if username is old, you can edit it, if it is new, you can
define it to be whatever you wish. Privacy means nothing to a user with
privs.  By the way, there are various levels of privs:  operator, wheel,
cia.
wheel is the most powerful, being that he can log in from anywhere and
have his powers.
Operators have their power because they are at a special terminal
allowing them the privs.  Cia is short for 'confidential information
access', which allows you a low level amount of privs. 
Not to worry though, since you can read the system log file, which also
has the passwords to all the other accounts.
To de-activate your privs, type
you=> disable
when you have played your greedy heart out, you can finally leave the
system with the command=>
logout
this logs the job you are using off the system (there may be varients
of this such as kjob, or killjob).

                                ----------------Exodus---------------


