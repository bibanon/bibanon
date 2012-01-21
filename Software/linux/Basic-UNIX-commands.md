The list of commands, used in UNIX shell (sh, bash, etc).

# Basic File Operations  #


## man  ##

If you don't know smth - RTFM! _man_ stands for **man**ual. And what you were thinking of?
Type
    $ man <command>
If you want to have information about <command>.
Example:
    $ man ls
    LS(1)                   NetBSD General Commands Manual                   LS(1)
    NAME
         ls -- list directory contents
    SYNOPSIS
         ls [-AaBbCcdFfghikLlmnopqRrSsTtuWwx1] [file ...]
    DESCRIPTION
         For each operand that names a file of a type other than directory, ls
         displays its name as well as any requested, associated information.  For
         each operand that names a file of type directory, ls displays the names
         of files contained within that directory, as well as any requested, asso-
         ciated information. 
         If no operands are given, the contents of the current directory are dis-
         played.  If more than one operand is given, non-directory operands are
         displayed first; directory and non-directory operands are sorted sepa-
         rately and in lexicographical order.
         The following options are available:
    ...

## cd  ##

Change Directory
Use is very simple, and just like use of `cd` in DOS
    cd ~/l33t/h4x/
Note that ~ is your home directory, if you need to see where you are (if your prompt doesn't display it, use:
    pwd

## mv  ##

MoVe or rename a file
    mv oldname.dix newname.dix
    mv ~/olddirectory/file ~/newdirectory/file
Note that on *nix, moving and renaming files is essentially the same thing, as the entire path is considered part of the file name

## cp  ##

Captian Planet. I mean... CoPy
    cp ~/old ~/new

### Options  ###

    cp -R
Copies everything in a directory and subdirectories

## scp  ##

SFTP CoPy
Like cp, but allows copying from one machine to another.
    scp user@remote.machine.com:~/list.txt ./
If you wanted to copy an entire directory:
    scp -r user@remote.machine.com:~/cake ./cake
Note that **./** is the current directory.

## cat, more etc  ##

**Note, that you can use [Unix_operands](/Unix_operands) with this commands**

### cat  ###

Printing the whole file to teh screen.
    $ cat some.file
    i am faggot hhahahah
    gsgffsdf
    agfsd.. (file content)
Now, try this:
    $ cat faggot.txt >> copypasta.txt
This appends the content of _faggot.txt_ to _copypasta.txt_

### head  ###

Showing the begining of the file
    $ head ussr.txt
    Союз нерушимый
    республик свободных
    сплотила на веки великая Русь!

### tail  ###

OMG, works like _head_, but in opposit way!
    ~/vk% tail album.pl                                                     
                           unless $response->is_success or $response->code == 302;
                   print "Success.\n";
                   $response = $ua->get("$url\?gid=$gid");
                   $_ = $response->content;
                   @_ = /\"photos.php\?act=album&id=(\d+)\"/gm;
                   # return album ID
                   return $_[$#_];
           }

### more & less  ###

Useful for working with big txt files. With this tool you can scroll the content.
    $ more big.fil3

## ls  ##

Just listing file in current dirrectory
       ~% ls                                                             
       Mail            codes           mail            mbox            vk
       centericq.core  dead.letter     mails           public_html     zed

### Options  ###

Note, that options can be combined.
ls <dir>
Listing files in <dir> directory.
       ~% ls vk         
       album.pl     graffiti.pl  img
ls -a
Listing ALL files (include hidden).
       ~% ls -a                                                                
       .               .emacs.d        .ssh            codes           vk
       ..              .irssi          .subversion     dead.letter     zed
       .bash_history   .libetpan       .vifm           mail
       .bash_profile   .links          .zshrc          mails
       .elinks         .mc             Mail            mbox
       .elm            .pinerc         centericq.core  public_html
ls -l
Showing items in nice list format.
       ~% ls -l                                                               
       total 4292
       drwx------  2 dany  users      512 Apr  3  2007 Mail
       -rw-------  1 dany  users  2138112 Oct 29  2007 centericq.core
       drwxr-xr-x  3 dany  users      512 Sep  1 17:54 codes
       -rw-------  1 dany  users        1 May  2  2007 dead.letter
       drwx------  2 dany  users      512 Apr  9  2007 mail
       drwxr-xr-x  2 dany  users      512 Apr  2  2007 mails
       -rw-------  1 dany  users    16926 Oct 29  2007 mbox
       drwxrwxrwx  5 dany  users      512 Sep 10 16:20 public_html
       drwxr-xr-x  3 dany  users      512 Jun 26 20:14 vk
       -rwxrwxrwx  1 dany  users     1408 Jan 26  1999 zed

# See also  #


* [Batch](/Batch)
* [Unix_operands](/Unix_operands)
