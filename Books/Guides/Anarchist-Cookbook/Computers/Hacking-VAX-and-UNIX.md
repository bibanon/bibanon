_by the Jolly Roger_

Unix is a trademark of At&t (and you know what that means)

In this article, we discuss the unix system that runs on
the various vax systems.  If you are on another unix-type system, some
commands may differ, but since it is licenced to bell, they can't make many
changes.

Hacking onto a unix system is very difficult, and in this case, we advise
having an inside source, if possible. The reason it is difficult to hack a
vax is this:  Many vax, after you get a carrier from them, respond=>

    Login:

They give you no chance to see what the login name format is.  Most commonly
used are single words, under 8 digits, usually the person's name.  There is
a way around this:  Most vax have an acct. called 'suggest' for people to
use to make a suggestion to the system root terminal.  This is usually watched
by the system operator, but at late he is probably at home sleeping or
screwing someone's brains out.  So we can write a program to send at the
vax this type of a message:

A screen freeze (Cntrl-s), screen clear (system dependant), about 255
garbage characters, and then a command to create a login acct., after which
you clear the screen again, then unfreeze the terminal.  What this does:
When the terminal is frozen, it keeps a buffer of what is sent.  well, the
buffer is about 127 characters long. so you overflow it with trash, and then
you send a command line to create an acct. (System dependant).  after this
you clear the buffer and screen again, then unfreeze the terminal.  This is
a bad way to do it, and it is much nicer if you just send a command to
the terminal to shut the system down, or whatever you are after...
There is always, *Always* an acct. called root, the most powerful acct.
to be on, since it has all of the system files on it.  If you hack your
way onto this one, then everything is easy from here on...

On the unix system, the abort key is the Cntrl-d key.  watch how many times
you hit this, since it is also a way to log off the system!

A little about unix architechture: The root directory, called root, is
where the system resides.  After this come a few 'sub' root directories,
usually to group things (stats here, priv stuff here, the user log here...).
Under this comes the superuser (the operator of the system), and then
finally the normal users.  In the unix 'Shell' everything is treated the same.

By this we mean:  You can access a program the same way you access a user
directory, and so on.  The way the unix system was written, everything,
users included, are just programs belonging to the root directory.  Those
of you who hacked onto the root, smile, since you can screw everything...
the main level (exec level) prompt on the unix system is the $, and if you
are on the root, you have a # (superuser prompt).
Ok, a few basics for the system... To see where you are, and what paths
are active in regards to your user account, then type

    => pwd

This shows your acct. seperated by a slash with another pathname (acct.),
possibly many times. To connect through to another path,
or many paths, you would type:

    You=> path1/path2/path3

and then you are connected all the way from path1 to path3.  You can
run the programs on all the paths you are connected to.  If it does
not allow you to connect to a path, then you have insufficient privs, or
the path is closed and archived onto tape.  You can run programs this way
also:

    you=> path1/path2/path3/program-name

Unix treats everything as a program, and thus there a few commands to
learn...

To see what you have access to in the end path, type=>
    ls

for list.  this show the programs you can run.  You can connect to
the root directory and run it's programs with=>

    /root

By the way, most unix systems have their log file on the root, so you
can set up a watch on the file, waiting for people to log in and snatch their
password as it passes thru the file. To connect to a directory, use the
command:

    => cd pathname

This allows you to do what you want
with that directory.  You may be asked for a password, but this is a good
ay of finding other user names to hack onto.
The wildcard character in unix, if you want to search down a path for
a game or such, is the *.

    => ls /*

Should show you what you can access. The file types are the same as they
are on a dec, so refer to that section when examining file.  To see what is
in a file, use the

    => pr

filename command, for print file.

We advise playing with pathnames to get the hang of the concept.  There
is on-line help available on most systems with a 'help' or a '?'.
We advise you look thru the help files and pay attention to anything
they give you on pathnames, or the commands for the system.
You can, as a user, create or destroy directories on the tree beneath you.
This means that root can kill everything but root, and you can kill any
that are below you.  These are the

    => mkdir pathname
    => rmdir pathname

commands.

Once again, you are not alone on the system... type=> 

    who

to see what other users are logged in to the system at the time.  If you
want to talk to them=>

    write username 

Will allow you to chat at the same time, without having to worry
about the parser.  To send mail to a user, say

    => mail

And enter the mail sub-system. To send a message to all the users
on the system, say

    => wall

Which stands for 'write all'. By the way, on a few systems,
all you have to do is hit the <return> key to end the message,
but on others you must hit the cntrl-d key.
To send a single message to a user, say

    => write username

this is very handy again!  If you send the sequence of characters discussed
at the very beginning of this article, you can have the super-user terminal do
tricks for you again. 

## Privs:

If you want superuser privs, you can either log in as root, or edit your
acct. so it can say

    => su

this now gives you the # prompt, and allows you to completely by-pass the
protection.  The wonderful security conscious developers at bell made it
very difficult to do much without privs, but once you have them, there
is absolutely nothing stopping you from doing anything you want to.
To bring down a unix system:

    => chdir /bin
    => rm *

this wipes out the pathname bin, where all the system maintenance files are.

Or try:

    => r -r

This recursively removes everything from the system except the remove
command itself.

Or try:

    => kill -1,1
    => sync

This wipes out the system devices from operation.

When you are finally sick and tired from hacking on the vax systems, just
hit your cntrl-d and repeat key, and you will eventually be logged out.

The reason this file seems to be very sketchy is the fact that bell has 7
licenced versions of unix out in the public domain, and these commands are
those common to all of them.  I recommend you hack onto the root or
bin directory, since they have the highest levels of privs, and there
is really not much you can do (except develop software) without them.

## Tutorial on hacking through a UNIX system
 
In the following file, all references made to the name Unix, may also be 
substituted to the Xenix operating system. 
 
Brief history:  Back in the early sixties, during the development of 
third generation computers at MIT, a group of programmers studying the 
potential of computers, discovered their ability of performing two or 
more tasks simultaneously.  Bell Labs, taking notice of this discovery, 
provided funds for their developmental scientists to investigate into this 
new frontier.  After about 2 years of developmental research, they produced 
an operating system they called "Unix".

Sixties to Current:  During this time Bell Systems installed the Unix system 
to provide their computer operators with the ability to multitask so that 
they could become more productive, and efficient.  One of the systems they
put on the Unix system was called "Elmos". Through Elmos many tasks (i.e.
billing,and installation records) could be done by many people using the same 
mainframe. 
 
Note: Cosmos is accessed through the Elmos system. 
 
Current:  Today, with the development of micro computers, such multitasking 
can be achieved by a scaled down version of Unix (but just as 
powerful).  Microsoft,seeing this development, opted to develop their own 
Unix like system for the IBM line of PC/XT's.  Their result they called 
Xenix (pronounced zee-nicks).  Both Unix and Xenix can be easily installed 
on IBM PC's and offer the same function (just 2 different vendors). 
 
Note: Due to the many different versions of Unix (Berkley Unix, 
Bell System III, and System V the most popular) many commands 
following may/may not work. I have written them in System V routines. 
Unix/Xenix operating systems will be considered identical systems below. 
 
How to tell if/if not you are on a Unix system:  Unix systems are quite 
common systems across the country. Their security appears as such: 
 
    Login;     (or login;) 
    password: 
 
When hacking on a Unix system it is best to use lowercase because the Unix 
system commands are all done in lower- case. Login; is a 1-8 character field. It is 
usually the name (i.e. joe or fred) of the user, or initials (i.e. j.jones 
or f.wilson).  Hints for login names can be found trashing the location of 
the dial-up (use your CN/A to find where the computer is). Password: is a 1-8 character password assigned by the sysop or chosen by the user. 
   
     Common default logins 
     -------------------------- 
     login;       Password: 
     root         root,system,etc.. 
     sys          sys,system 
     daemon       daemon 
     uucp         uucp 
     tty          tty 
     test         test 
     unix         unix 
     bin          bin 
     adm          adm 
     who          who 
     learn        learn 
     uuhost       uuhost 
     nuucp        nuucp 
 
If you guess a login name and you are not asked for a password, and have 
accessed to the system, then you have what is known as a non-gifted account. 
If you guess a correct login and pass- word, then you have a user account. 
And, if you get the root p/w you have a "super-user" account. 
All Unix systems have the following installed to their system: 
root, sys, bin, daemon, uucp, adm Once you are in the system, you will 
get a prompt. Common prompts are: 
 
    $ 
    %
    # 
 
But can be just about anything the sysop or user wants it to be. 
 
Things to do when you are in: Some of the commands that you may want to 
try follow below: 
 
* who is on  (shows who is currently logged on the system.) 
* write name (name is the person you wish to chat with) 
To exit chat mode try ctrl-D. 
* EOT=End of Transfer. 
* ls -a      (list all files in current   directory.) 
* du -a      (checks amount of memory  your files use;disk usage) 
* cd\name    (name is the name of the sub-directory you choose) 
* cd\        (brings your home directory  to current use) 
* cat name   (name is a filename either  a program or documentation  your username has written) 

Most Unix programs are written  in the C language or Pascal 
since Unix is a programmers'  environment. One of the first things done on the system is print up or capture (in a buffer) the file containing all user names and accounts. This can be done by doing the following command: 
 
    cat /etc/passwd 
 
If you are successful you will see a list of all accounts on the system.  It 
should look like this:

    root:hvnsdcf:0:0:root dir:/: joe:majdnfd:1:1:Joe Cool:/bin:/bin/joe hal::1:2:Hal Smith:/bin:/bin/hal 
 
The "root" line tells the following info : 

    login name=root 
    hvnsdcf   = encrypted password 
    0         = user group number 
    0         = user number 
    root dir  = name of user 
    /         = root directory 
 
In the Joe login, the last part "/bin/joe " tells us which directory 
is his home directory (joe) is. In the "hal" example the login name is 
followed by 2 colons, that means that there is no password needed to get in 
using his name. 
 
Conclusion:  I hope that this file will help other novice Unix hackers 
obtain access to the Unix/Xenix systems that they may find.
