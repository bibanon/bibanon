OK you guys, so basically the first thing you should know about the C programming language is that it is fucked beyond belief. It was designed in the late 60s, when computers were fucking slow as hell, and half the programmers were high ALL THE TIME. Dennis Ritchie, one of the inventors of C, definitely had to be high most of the time. Seriously, just like, go fucking read some of the shit he wrote back then. He tries to sound like he's all mysterious and wizardly, but really he's just a fucking pothead or something. Maybe. I dunno. Anyway, enjoy fucking around with header files, buffer overflows, and various other shit that only a 40-year-old, almost-assembly programming language can offer. yeah, I heard C is "fast" and shit, so maybe that's good. Whatever, do whatever the fuck you want.  
The above being said, C is still pretty much the common language amongst programmers, and despite its faults is beloved amongst them. C is taught in every single computer science major, all computer scientists know C, most exploits are published in C, and therefore reading it will be of great use if you have any intention of doing more serious programming.  
**The main aim of this tutorial is to provide you with the knowledge needed to not only write your own programs, but also to correct errors in others' programs.**  
  
# Compilers #  
  
**A compiler is a program which converts source code into machine code. Humans cannot read machine code and computers cannot read C. Think of it as a translator between you and someone else that doesn't speak your language.**  
_Any other operating systems will be added on demand._  
The first step will be to acquire the tools required for programming and compiling. There are many different ways to do this; but since it's likely this is your first experience of C, I'll go with the simplest.  
  
## Microsoft Windows ##  
  
Windows C compilers are ubiquitous and many of them do the exact same job. Unfortunately, most of them cost assloads of cash for the full version. Here's a listing of integrated development environments that support C on Windows, along with download links for the free ones.  
  
* [Microsoft Visual Studio Express](http://anonym.to/http://www.microsoft.com/express/download/#webInstall) - you want the C++ version.  
* [Dev-C++](http://anonym.to/http://prdownloads.sourceforge.net/dev-cpp/devcpp-4.9.9.2_setup.exe) - GNU free, it uses an ancient version of GCC, so beware.  
* [wxDev-C++](http://anonym.to/http://wxdsgn.sourceforge.net/) - GNU free, like Dev-C++ but you can use any compiler you want (i.e. a more modern version of GCC).  
* [Code::Blocks](http://anonym.to/http://www.codeblocks.org/) - GNU free, supports plugins.  
* [Eclipse](http://anonym.to/http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/europa/winter/eclipse-cpp-europa-winter-win32.zip) - Eclipse handles more than just C/C++ through its extensive plugins system.  
* [MonoDevelop](http://anonym.to/ftp://www.go-mono.com/archive/1.9/windows-installer/4/mono-1.9-gtksharp-2.10.4-win32-4.exe) also provides supports .Net frameworks. <-- b0rked, there's no username/password to the ftp  
* [NetBeans](http://anonym.to/http://www.netbeans.org/features/cpp/index.html) - it isn't just for Java anymore.  
My recommendation would probably be to go with MonoDevelop, which supports the full .Net stack without shelling out for Visual Studio. That said, Visual Studio does have its perks, particularly when you're using functions listed in Windows.h (which, generally speaking, you shouldn't do).  
  
## Unix/Linux/BSD ##  
  
It's likely that you already have a compiler such as gcc installed. To be sure, go to the command line and type "gcc" (minus the quotes of course). If you get the response "no input files", you're good. If you do get an error then I suggest you install it now from <http://gcc.gnu.org/> or your distribution's package manager. The latter course of action is preferable, because compiling it takes forever--it took 4 hours on a first generation MacBook. For Ubuntu users, use 'sudo apt-get install build-essential', as this will give you everything you need to compile C.  
The majority of Unix and Linux programmers don't use an IDE, but rather prefer the text-based interfaces provided by the GNU utilities, which are included with most Unix/Linux operating systems. Emacs can also be set up with [CC mode](http://anonym.to/http://cc-mode.sourceforge.net/) which will help with editing and compiling C and C-like languages with all the power (and confusion) of emacs! Of course, if you're not gay and have no interest in learning Lisp to learn C, vi/vim works just as well without the overhead.  
You can also get Anjuta IDE, get it from Add/Remove programs or sudo apt-get install anjuta or yum install anjuta. This particular IDE is fully integrated with GNU's Autotools, and will produce source tarballs that Unix users expect. The environment is fully integrated with the GNOME desktop, and thus will look like shit on KDE. It'll also let you configure a graphical front-end that will look and feel like it belongs in GNOME/Xfce.  
For KDE users, there is KDevelop, which is made by the KDE people. It'll look better in KDE than Anjuta, and provides a similar feature set, but with support for Qt based graphical interfaces instead of Glade/GTK2 graphics.  
Lastly, MonoDevelop, NetBeans, and Eclipse are available on Unix-like systems as well, and work exactly the same as they do on Windows. These should all be available through your operating system's package management system.  
  
## Macintosh ##  
  
Mac OSX includes Xcode (the installation will install gcc and all your libs) on the operating system DVD. It's pretty easy to set up a C project. Open Xcode, File->New Project. Of course, you can always follow the *nix tutorial. It should work as Mac OS X is essentially BSD with a pretty frontend.  
Be warned: Apple's GCC is ass. While it will take forever to build and install on your Mac, you should probably install the gcc out of Fink after installing the development tools. It's a more vanilla version of GCC, and unlike Apple's GCC, will not be broken. For those that do not want to use Xcode, the Smultron text editor is really nice.  
Whatever you do, don't use the beta of Xcode 3.1 right now. It's debugger is seriously borked, and the -g options on GCC don't work worth shit, either. I guess that's what you get for trusting Apple.   
  
# Get started #  
  
Now that we all have a compiler I suppose we can get started right? Well first of all I have a few things to say:  
  
* You may find similarities between this and other tutorials. Since we're teaching you the same thing (except I'm going very deep) this should be expected.  
* It won't happen overnight, be patient, if you feel yourself getting frustrated, take a break. Go for a walk, smoke a bowl or whatever you do to relax. This isn't the easiest thing you'll do in your life but I assure you that if you stick with it, you'll be thankful you put the work in.  
* Use your new found knowledge! There's no point learning a language and not doing anything else. Write (useful) programs, help others and generally help the community.  
* **Download the Kernighan and Ritchie C book**: [Link](http://www.51cnnet.com/ebook/660-the-c-programming-language) -- This will teach you all you need to know to code in C.  
* You can find more books on C, C++ and C# at <http://www.51cnnet.com/>  
* Ask for help in /pr/ on [99Chan](http://99chan.org/pr) and /halp/ on [7Chan](http://7chan.org/halp)  
  
# C# #  
  
This is the .NET version of C. It runs in a visual environment similar to Visual Basic.  
  
# Ancient Tradition #  
  
       #include <stdio.h>  
       int main(int argc, char** argv)  
       {  
           printf("Goodbye, cruel world!");  
           return 0;  
       }  
That's the basic emo version of "Hello World", as shown in K&R's The C Programming Language. If you're really interested in C, that book is a must have. It'll explain a lot that this tutorial will gloss over. Now, let us explain everything in this code selection.  
Line 1: #include <stdio.h> This is a preprocessor command telling the compiler that we're going to use some standard IO functions. These functions allow us to print things to the command line and read in information from the keyboard.  
Line 2: int main(int argc, char** argv) This line starts the "main" function, which is the primary entry point into your program. This function is common to all programs, and usually consists of calls to other functions and subroutines that actually do the work of the program. The word "int" here at the beginning refers to the fact that the main function returns an integer, usually 0. Other return values can be useful if your C code is intended to be used as a part of a shell script. The stuff inside the parentheses are the arguments for the main function, which are taken from the command line. The first argument here is an integer (hence the 'int') called "argc", and it tells us how many words were on the command line when the program was called. The second argument is the list of words called argv. argv[0] is the name of the program itself, as all lists in C start with 0 because system engineers and language writers back in the day were lazy. This program doesn't use this information, but others do.  
Line 3: The open curly brace here opens the primary code block for the main function. That's all it does.  
Line 4: printf() prints shit to the screen through a terminal emulator. The arguments it takes consist of a string in double quotes with special symbols for variables, followed by the list of variables in the order they're used. A full explanation of the function can be found [here](http://anonym.to/http://www.cplusplus.com/reference/clibrary/cstdio/printf.html).  
Line 5: Here, we return the integer that the main function expects, namely 0.  
Line 6: The closed curly brace here closes the primary code block for the main function.  
All lines of actual program code must end in a semicolon. Preprocessor lines don't need it, neither do the opening lines of function definitions nor curly brace lines. This is because the semicolon is about the most useless key on the keyboard when you're programming, so it got used for denoting the end of a command.  
Now, you might want to put some shit below the other, in two different lines. You might be thinking "That shit's easy, dawg, you'll make another printf() command, so we would have something like this:  
       #include <stdio.h>  
       int main(int argc, char** argv)  
       {  
           printf("Goodbye, cruel world!");  
           printf("brb suicide");  
           return 0;  
       }  
Thing is, when you try to compile the program with that, you will end up with shit like this:  
Goodbye, cruel world!brb suicide  
Which is, well, not exactly what we're looking for.   
But why does this shit happen? It's because that after the end of a command, it positions an "invisible" cursor at the end of the text, and that's why it writes right after finishing the first line. We solve this with a new line, or "\n", that makes the cursor go into the next line. We will have something like this:  
       #include <stdio.h>  
       int main(int argc, char** argv)  
       {  
           printf("Goodbye, cruel world!\n");  
           printf("brb suicide");  
           return 0;  
       }  
And finally we'll end up with this:  
Goodbye, cruel world!<br>brb suicide  
Victoly.  
If you wanna clear up the screen, simply use the command clrscr()  
  
  
