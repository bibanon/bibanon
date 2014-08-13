The Bash shell is the default shell you see every time you start a terminal in a Unix-like system (GNU/Linux, Mac OS X, BSD, Solaris, etc). Developed by the GNU project as a pillar of their userspace, it is now the most popular shell.

The big strength of Bash is in it's ability to set alias and scripts in the bash configuration files. Alias are powerful and make macros for commands that would otherwise take a long time to type. Bash functions can also be set here, although for complex ones it might be better to make the function an independent script. Next are the variables, setting things like the default editor. You can also edit the prompt to have colors or look insanely different. Finally, you can start programs every time bash is launched, such as a fortune.

## Config files  ##

There are four bash configuration files:

* **/etc/bash.bashrc**

  * This is the master bash config. It should **never** be edited, as it would break other shells that depend on it.
* **/etc/skel/.bashrc**

  * This is the bash config that is given to each new user when their home directory is created. Edit this if you want certain settings to be given to each new user.
* **/root/.bashrc**

  * This is the root user's bash config. Edits made here only affect the root user.
* **~/.bashrc**

  * This is your personal bash config. Edits made here only affect you.
We've included quite a few in Cherimoya, and they can be reviewed below.

## Shell Variables  ##

These variables control which programs are used and other nice options in the bash shell. They are normally prefixed with a $ symbol to distinguish them from normal text.

### $EDITOR  ###

```bash
export EDITOR=nano
export VISUAL=nano
```

The $EDITOR variable is probably the most important shell variable of them all. It controls the editor used in `git`, `ccr`, `packer`, `visudo`, and other programs. $EDITOR is normally set to Vi in most linux distributions, causing no end of pain to noobs using the command line. 
Vi is an extremely powerful editor, but few know how to control that freedom. Since those that use Vi would already know how to change the `.bashrc`, we've made the default editor `nano` to make it easier on those who are uninitiated. Nano is a basic command-line editor that works in the same way as a normal GUI notepad, so noobs will instantly understand it.
I have not seen the $VISUAL variable in use before, but I also set it to `nano` just in case.

## Alias  ##

Alias change the actions of commands inputted into Bash. They can turn long strings of commands into two character macros, or make existing commands run differently.

### ls class  ###

```bash
alias ls='ls --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias ll='ls -l --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias la='ls -la --group-directories-first --time-style=+"%d.%m.%Y %H:%M" --color=auto -F'
alias lm='ls -al | less'
```

These alias set the commands 

* **ls** to have color 
* **ll** as a macro for `ls -l`, which displays more information about each file
* **la** as a macro for `ls -a` which displays all files, hidden or not
* **lm** as a macro for `ls -al | less`, which combines the `-l` and `-a` options and pipes the output to the command-line reader "less".

### cd class  ###

```bash
alias ..='cd ..'
alias ...='cd ../..'
```

These are two simple alias for `cd` (change directory). The `..` is a bash variable for the directory right above, so `cd ..` goes to it. Rather than type `cd`, typing `..` will be all you need. `cd ../..` tells bash to go two directories above, so we've simplified it to `...`
In summary:

* **..** sends you to the directory above your current one.
* **...** sends you two directories above.

### File management class  ###

```bash
alias rm='rm -i'	                  # asks you what to remove
alias cp='cp -i'
alias mv='mv -i'
```

These alias force the commands to ask before deleting/overwriting each file (interactive mode). You can override them by using the option `-f`.

### Misc. class  ###

```bash
alias grep='grep --color=tty -d skip'
alias du='du -kh'
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
```

These are miscellaneous commands that can be quite helpful, as reading their raw output can be quite painful for anyone.

### Pacman class  ###

```bash
alias pacman='sudo pacman'
alias ccr='sudo ccr'
alias vp='vim PKGBUILD'
alias vs='vim SPLITBUILD'
alias np='nano PKGBUILD'
alias ns='nano SPLITBUILD'
```

The first set of alias make the commands `pacman` and `ccr` ask for the password with `sudo` upon use. This saves a lot of keystrokes, as you're going to have to get root permissions anyway.
The second set is useful when building from the [User Repositories#CCR](/User_Repositories#CCR) or [User Repositories#AUR](/User_Repositories#AUR) manually using `makepkg`. Every single source package in an Arch-based system uses a `PKGBUILD` or `SPLITBUILD` file to store instructions for building the package automatically, so these alias can save you a lot of keystrokes and time. One pair is for `Vim` (not a noob editor), and the other is for `nano` (more initutive editor).

* **vp** tells vim to search for the file `PKGBUILD` in the current directory and edit it.
* **np** does the same with nano.
* **vs** tells vim to search for the file `SPLITBUILD` in the current directory and edit it.
* **ns** is the same, but using nano.

## Functions  ##

Functions in the bash configuration files are tiny bash scripts that can be called as if they were in the `/usr/bin/` directory. A few useful ones are defined here.

## ex  ##

ex uses every possible extractor program on the specified archive to extract it. Using this, you don't have to remember the command to extract a specific archive, such as "tar -xzvf" or something else. Just use ex and it works.
```bash
# usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
```
## Login prompt  ##

The login prompt is the stuff that displays right before your cursor in Bash. In our .bashrc, we've simply added colors to the original to distinguish between a user and the root user.
![Fig 1.1 - A terminal with colored prompts activated](File:terminal.png)
```bash
# user's green-colored prompt
PS1='\[\e[1;32m\][\u@\h \W]\$\[\e[0m\] '
```
As shown in the figure to the right, it is green to symbolize "safety".
```bash
# root's red colored prompt
PS1='\[\e[1;31m\][\u@\h \W]\$\[\e[0m\] '
```
This prompt is red to clash with the user's green and symbolize "danger". It also looks cooler, IMHO.

## Programs  ##

Programs can also be set to run right before each instance of bash.
```bash   
# Fortune + cowsay in every terminal
/usr/bin/fortune | cowsay -f tux -n
```
Here, the `fortune` program is piped through `cowsay` to show a penguin saying a funny quote. If you don't like them, just comment it out (put a "#" symbol before the code)
