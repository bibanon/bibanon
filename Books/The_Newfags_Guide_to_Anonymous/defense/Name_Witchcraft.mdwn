This article will go over a method of hiding shit in a folder with two levels of protection. 

# Windows Easter Eggs #

In windows, there are several odd behaviors displayed when you use certain file/folder names. By combining these, you can pretty safely store files.

## Con ##

If you try to make a file/folder named con, you will get an error. This is because it is a file name reserved from DOS. However, you can get around this by creating it with a network path: "\\.\c:\full\path\name\con"

## Control Panel ##

Another trick in windows, is that if you make a folder and change the extension to {21EC2020-3AEA-1069-A2DD-08002B30309D}, then when you click on it you see the control panel (and the ext is hidden). You can also toggle back and forth with command prompt.
_Update: Because of heavy fail at Microsoft Corporation, this trick does not work on Windows Vista. A solution/workaround is [Name_Witchcraft#vista](/Name_Witchcraft#vista)._

# The Trick #

What this file-hiding-hack does is explained here.

## How-To ##

Make a directory, and fill it with shit. Then, move it to this path (rename it) "\\.\c:\windows\system32\con.{21EC2020-3AEA-1069-A2DD-08002B30309D}". It acts like the control panel, lives in the system32 directory (a logical place for the control panel), and is unrenamable. You can't search within it, can't delete it, etc.

## Script ##

There is a premade script for this, courtesy of pseudolobster.
     @echo off
     if exist con.{21EC2020-3AEA-1069-A2DD-08002B30309D}\nul goto toggleoff
     if exist porn\nul goto toggleon
     md "\\.\%cd%\con.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
     goto end
     :toggleoff
     move "\\.\%cd%\con.{21EC2020-3AEA-1069-A2DD-08002B30309D}" porn>nul
     goto end
     :toggleon
     move porn "\\.\%cd%\con.{21EC2020-3AEA-1069-A2DD-08002B30309D}">nul
     :end
Just put in the system32 directory, and run it to toggle between hidden and normal mode.

# Vista #

For all of you that have vista, Microsoft decided that they were going to no longer allow you to use {21EC2020-3AEA-1069-A2DD-08002B30309D} to disguise that folder as a link to the control panel.  What they didn't do was disabled this for any other folder type.  So we can take any other folder type and use that instead of the control panel.  If you have the balls to pick a folder for yourself the list is in the registry located at:
     My Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\explorer\FolderDescriptions\
When selecting a type, you do not want to use the key's name.  Instead use the value of ParsingName (without the double colons)
For everyone who is lazy, here is a few I grabbed for you:
     Printers: {2227A280-3AEA-1069-A2DE-08002B30309D}
     History: {FF393560-C2A7-11CF-bff4-444553540000}
     Network Connections: {992CFFA0-F557-101A-88EC-00DD010CCC48}
Simple replace {21EC2020-3AEA-1069-A2DD-08002B30309D} with a folder type of your choice.  I would recommend the Network Connections folder type.  This way you can say "con" is a shortened name.

# Problems #

Depending on the person, using "con" can set off red flags to your investigator.
The first dead giveaway is the fact that your "shortcut" to printers is not named "Printers" like default, instead it will be named con.  This cause three problems.
     One: If the person knows what "con" is, they are going to know exactly how to get around it.  Also you batch file is also a big giveaway.
     Two: If the person don't know what con is and you aren't able to pass it off for a shortened version of "Network Connections," a simple Google search 
     will give it away
     Three: If your computer is seized by the FBI, that's the first thing they are going to look for.
If you decide to name it "Printers.{2227A280-3AEA-1069-A2DE-08002B30309D}" instead of "con.{2227A280-3AEA-1069-A2DE-08002B30309D}" because of the reasons above then you have another problem.  It is now renamable, deletable, and you can still search within it.  If a file is found in it a simple right-click-->open containing folder will reveal all that is in your folder.
"con.{...}" is more protected but more suspicious.
"Printers.{...}" is less suspicious but less protected.
