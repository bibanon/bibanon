Perl is a dynamic programming language created by Larry Wall and was first released in 1987. Perl borrows features from a variety of other languages including [C](/C), shell scripting (sh), AWK, sed and [Lisp](/Lisp).  

Perl is usually good for searching for data and matching variables. Structurally, most people believe that Perl is a brainfuck comparable to that of [brainfuck](/brainfuck).  

For moar info, see <http://anonym.to/http://en.wikipedia.org/wiki/Perl> 

Some of the tools the Insurgency uses, such as mt_pulse.pl, use Perl. [Linux](/Linux) and BSD distros usually include Perl as a default package. Windows users should get Strawberry Perl and Macfags should get ActivePerl from the link below. 

## How to get Perl #


### Windows

1. Download the Strawberry Perl installer from [here](http://strawberryperl.com/)
2. Run the program and follow the instructions 
3. Open Command prompt and run "perl -v", You should see "The is perl.." This means Perl is installed properly. 

### Linux

On Ubuntu/Debian you can simply use the "apt-get" command 

    sudo apt-get install perl 

On Redhat/fedora 

    yum install perl 

on suse 

    yast install perl 

on Arch Linux 

    pacman -S perl 

on Gentoo 

    emerge -av perl 

## Post Installation : 

     # perl -MCPAN -e shell 
2. Just Follow step by step. Use all the Default Answer.
ii.  install Bundle::CPAN
iii. install Bundle::LWP
iv.  install Bundle::DBI
v.   install DBD::mysql

To test the install run. 

    perl -v 

or 

    GET -ed www.yahoo.com

## Learning Perl #

Though there are several books available to someone wanting to learn perl, O'Reilly's "Learning Perl" is widely considered to be the best book for newcomers to Perl.
It is available, along with the rest of O'Reilly's books on Perl [here](http://lulzcats.org/files/perl-bookshelf4.rar).