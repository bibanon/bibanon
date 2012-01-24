The **mIRC scripting language** is the scripting language embedded in mIRC, a popular [IRC](/IRC) client for Windows.

## Primary uses ##


* Channel and personal protection against any types of attacks (flooding, spamming, CTCP floods, etc)
* Dialog windows can be created in mIRC to better serve user-compatibility.

  * Popular mIRC dialog extensions include MDX (**M**irc **D**ialog **Ex**tension) and DCX (**D**ialog **C**ontrol **Ex**tension) There are also a few versions of mdx.dll and dcx.dll modded by irc hackers.
* Bots that provide automated IRC channel management, trivia or other games, and other desired functions for chatters
* Commands that save typing or otherwise simplify life on IRC (such as automatically identifying as the owner of a nickname)

## Script storage ##

Scripts are stored as either plain text files, usually with a .mrc file extension, or as INI files. They however can be stored with any extension. It can be: .exe, .script, etc.
Multiple script files can be loaded at one time, although in some cases, one script will conflict with another and cause one or both of them to no longer work properly.

## Language features ##

mIRC scripting involves a peculiar nomenclature that is not entirely consistent with most of the rest of the programming world. (Most notably, the term identifier—which in most languages refers to the name of a variable or function (whether it returns a value or not)—in mIRC refers specifically to a value returning function.)

* Built-in functions are termed **commands** or, if they return a value, **identifiers**.
* Custom scripted functions are called **aliases**.  Aliases that return a value are known as **custom identifiers**. Both are called from the command line or other parts of a script in the same ways as built-in commands and identifiers (and can even supersede them).
* **Popups** are scripted context menu items.  Popups are called when they are selected by the user. The term originally referred to the menus—which pop up upon a right click. It is still used this way in the manual. But the user community (who tend not to read scripting manuals) took to calling the individual items popups—perhaps thinking of the colourful novelty actions that are popular with many users as pages of a popup book.
* Remotes are event-handling scripts.  Remotes are called when the event they handle occurs.
* All variables are dynamically typed.
* mIRC scripts make use of sigils.  Identifiers (whether custom or built-in) are preceded by _$_, binary variables are preceded by _&_, and other variables (whether local or global) are preceded by _%_.  Commands and aliases are not preceded by any particular character (although when entered from a window's command line they must be preceded by the command prefix, usually _/_).

### File handling ###


* Scripts can read from and write to files [_$read(file,[args])_ | _/write_ ]
The above is intended for singular access to the file. Because each time you issue `$read` or _/write_ you open and close the file for access.
Multiple accesses, during a loop for instance, is best handled through _/fopen_, _/fwrite_ and _/fclose_. Since this opens the file only once. In some cases _/filter_ and _/savebuf_ is an even more efficient (non scripted loop) method.

* Scripts can also copy and delete files. [_/copy_ | _/remove_]

### Binary variables ###


* Contain unlimited (8192 bytes prior to mIRC 6.1) raw data
* Globally accessible via commands and identifiers
* Automatically unset when script returns control to mIRC (and not to another part of a script)
* Prefixed with _&_ (eg. _&Variable_)
* Cannot be accessed other than by _/bread_ and _/bwrite_, so these variables cannot be passed onto other parts of the script

### Hash tables ###


* May contain unlimited binary data or up to 4,143 (941 prior to mIRC 6.32) bytes of plain text. This limit is imposed by mIRC's scripting parser's own line length limitation (unless assigning a binary variable)
* Globally accessible via commands and identifiers
* Automatically unset when exiting mIRC
* Not prefixed
* Faster than accessing from a variable or INI file, as hash tables are stored in memory rather than the hard disk
* Can be saved for later use
* Size limited only by the computer's memory limits. Each table defaults with a size to hold 1000 different items, but this may be enlarged to potentially unlimited sizes
* The default size of an hash table created using /hmake table name is actually 100 and not 1000 items

### Global variables ###


* May contain up to 4,147 (946 prior to mIRC 6.32) bytes of data (however due to line-length limitations in mIRC's scripting parser, a maximum of 4,144 bytes can be assigned explicitly — this number decreasing as the variable's name grows longer)
* Cannot store NUL (ASCII 0) or trailing spaces
* Globally accessible
* Do not automatically unset (stored automatically in a mIRC initialization file)
* Prefixed with _%_ (eg. _%Variable_)
* Created using the _set_ command or _var -g_ or _%Variable = value_ notation

### Local variables ###


* May contain up to 4,147 (946 prior to mIRC 6.32) bytes of data (however due to line-length limitations in mIRC's scripting parser, a maximum of 4,144 bytes can be assigned explicitly — this number decreasing as the variable's name grows longer)
* Can store NUL (ASCII 0) or trailing spaces
* Accessible only within the scope that created them
* Prefixed with _%_ (eg. _%Variable_)
* Created using the _var_ command. _var_ is merely an internal alias for _set -l_ but _var_ poses the means to declare multiple local variables on a single line.

## Limitations ##


* mIRC's scripting parser only supports a maximum of 4,147 (947 prior to mIRC 6.32) characters per line (not including newlines or indentation).
* Strings are not syntactically enclosed, creating ambiguities in code where characters meant as literal strings are treated as part of the language's syntax.
* Each line of code is broken down into a set of space-delimited tokens. As mIRC's parser does not support null tokens and the language doesn't provide a syntax to clearly differentiate literal strings from code; Prior to mIRC version 6.2 it was impossible to pass multiple consecutive spaces to any command or alias. However, this was fixed with the introduction of the returnex command which allows the preservation of spaces.

## Code examples ##

The code below is in the remote scripts format. If placed into an alias file, the command names should not be preceded by the word "_alias_". Test Comments include the common _/* comment */_ and _;comment_.
Here is an example of a Hello World alias:
    ;Defines the alias 'hello' in the remote script
    ;Note: if this is placed in an alias script, the 'alias' part must be removed (result: hello {)
    ;Usage: /hello
    alias hello {
      ;Displays(/echo) 'Hello World!' into the active window(-a)
      echo -a Hello World!
    }
Counting to 10:
    alias ten {
      ;'%i' is locally set as 1
      var %i = 1
      ;The while loop continues until '%i' is greater than 10, then stops.
      while (%i <= 10) {
        ;Displays(/echo) '[value of %i]' into the active window(-a)
        ;'[value of %i]' will be 1 at the beginning of the execution.
        echo -a %i
        ;To continue the while loop, '%i' must be increased, or you'll
        ;have yourself an infinite loop (can be breaked with Ctrl+Pause/Break)
        inc %i
        ;Don't forget to close the while loop scope.
      }
    }
A remote script event handler:
    ;Placed in a remote script.
    ;Literally: when any user joins #IRCHelp, message to the channel: Hello [nickname that joined]
    on *:JOIN:#IRChelp: { msg $chan Hello $nick }
    ;To do this for any channel, the code would be:
    on *:JOIN:#: { msg $chan Hello $nick }
A remote script to automatically respond to certain text
    ;Placed in a remote script
    ;When a user types Hello! in a channel, you answer back: Hello, [nickname]!
    on *:TEXT:Hello!:#:{ msg $chan Hello, $nick $+ ! }
    ;When a user types Hello! in a private message, you answer back: Hello, [nickname]!
    on *:TEXT:Hello!:?: { msg $nick Hello, $nick $+ ! }
Here is an example of picture windows:
    alias cir {
    ;Create a picture (-p) window (@cir)
    window -pek @cir
    ;Draw a circle (on window @cir) with color 4 (red), size of 50 at coordinates (200,200)
    drawdot @cir 4 50 200 200

## See also ##


* [IRC](/IRC)

## External links ##


* [Official mIRC website](http://www.mirc.com/)
* [mIRC scripting links](http://www.mirc.com/links.html)
* [mircscripts.org](http://www.mircscripts.org/)
* [mircscripts.com](http://www.mircscripts.com/)
* [mircscripts.us](http://www.mircscripts.us/)
* [mIRC Online Manual](http://wi-fizzle.com/mircdocs/) — documentation in single-page HTML format


