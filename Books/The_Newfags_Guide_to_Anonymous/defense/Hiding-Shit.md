When storing tools and such (read: porn), and you live with other people, it may be necessary to hide your shit. There are several ways to do this.

## Hiding in JPEGs ##

![](RAR_Guide.png)

### Intro  ###

Basically, in the header of a jpeg it specifies where the data for the picture ends, so you can safely append binary data (like rar archives) to the end of jpeg images, and the image will still work.

### Details  ###

Details and scripts can be found in the [Fusion](/Fusion) article.

### How to do it  ###

Drusepth wrote a sweet ass guide on how to do this madness.  Check it out: <http://drusepth.wordpress.com/2007/08/28/hiding-files-in-images/>

## Windows file name witchcraft  ##


### Intro  ###

Straight from the pits of /tech/ comes the combination of a few well known windows easter-eggs, that translates to you craftily hiding porn in the open.

### Details  ###

Details and scripts can be found in the [Name Witchcraft](/Name_Witchcraft) article.

## Truecrypt  ##


### Intro  ###


* 
  * A MUST USE FOR SECRET-SQUIRREL CP**
Truecrypt is an app for Windows and Linux which lets you use strong encryption on data.

### Details  ###

More info can be found at the [Truecrypt](/Truecrypt) article.

## Toucan  ##


### Intro  ###

Toucan is a multi-platform (and flash drive portable) open source app that can encrypt any file (think .rar) using Rijndeal or Blowfish encryption. Shit hard to crack, it renders any file unusable without the program and the password.

### Links  ###

<http://portableapps.com/apps/utilities/toucan/>


## Hide it in plain sight  ##


### Intro  ###

Store your shit inside a game folder, and rename all your shit from "DICKBUTTGAY.MOV" to stuff like "SaveGame" or something like that. Easy if you don't have too much pr0n.
Edit: If you do have a lot of files in one folder you can make a batch script to rename them all in one go and one to rename them back when you are finished. To rename them open a text editor and on the first line put 'rename *.mov *.whatever' (extensions are changable) and save file as a .bat. The rename back to .mov is just the same in reverse.

## Locked Archives (RAR or 7z)  ##


### Intro  ###

Locked archives are strong and very slow to crack due to the method in which passwords are tested. WinRAR and 7zip use powerful encryption (AES-128 and AES-256 respectively). 7zip is particularly annoying to crack because of the better encryption and some extra shit that makes guessing passwords really slow.

### Details  ###

Just lock the stupid archives. When you make a RAR or 7z there are options to put a password on it. Put a good password on it: something longer than 7 or 8 characters, using capital and lower-case letters, numbers, and special characters like @ or &. 
**Don't** use: simple words/names/sites/etc, passwords under 5 characters, or things that can be guessed or determined through social engineering or data mining (shit like your birthday, address, whatever).
Archives don't need to be encrypted with 3rd party programs, they can encrypt themselves. Make sure, if possible, to hit the option to scramble the file names in the archive. A locked RAR isn't very useful if people can read "CP_1.jpg".

## Using linux root  ##

If you are reading this, chances are that you are the only one to know the root password of the computer. Just create a folder and set the visibility to "root only". Newfag-protip: in Newbuntu you open the terminal, type "gksudo nautilus" (or "kdesu konqueror" if you run Kubuntu), and there's your nice graphical root thing: drag and drop your stuff to satefy.

