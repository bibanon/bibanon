QBASIC is a simple text interface programming language developed by Microsoft. It is intended to design programs for Microsoft Disc Operating System, or MS-DOS. It can be downloaded from Microsoft with this link:
<http://download.microsoft.com/download/win95upg/tool_s/1.0/w95/en-us/olddos.exe>

## History #

Here is a brief history of QBASIC

### Early History ##

Many new programs were being developed back in the late sixties and early seventies. Mostly, they were for early calculators, word processors, and other such electronic devices. One major language was BASIC. 

### Late History ##

Most major computer systems and home video game consoles ran on their own modified version of BASIC. Microsoft was founded when Bill Gates and several of his colleagues at Harvard developed a version of BASIC that could run on the Commodore, called Commodore BASIC. As Microsoft expanded they began releasing their own operating systems, which required their own version of BASIC. The BASIC that was developed was referred to as quick BASIC, or QBASIC. To enhance sales, it came free with any copy of MS-DOS.

## Tutorial #

In this tutorial, I will teach you the more simple commands and show you how to make a number game using them.

## Commands ##

### REM:

REM stands for "remark." The computer ignores the REM command. Like a string tied to your finger, it is there to remind you what your program is or what it is supposed to do. For example, programmers frequently use the REM command at the beginning of a program to give the program a name, and tell instructions for the program.
Notice on the last line of the program, that there is a '. The apostrophe stands for the REM command, but looks better, and is more common on QBASIC programs. Most programs will be documented with apostrophes rather than REM commands.
Remember: Anything following REM, or ' the computer will ignore. It stops reading the line at that command.

### CLS:

CLS is a command used to clear the screen. It makes the screen completely black. (Notice how the first letters of "clear" and "screen" are in the command.) This command is not required for text, because text will just put text on the top of the screen off and put the new text on the bottom. However, when you run your program without clearing the screen before it starts, it shows the remains of the program run previously. If you clear the screen at the beginning of the program, (and in longer programs, during it) the program looks much neater.

### Variables:

Notice the INPUT nm$ line directly following the PRINT "What is your name" statement on the third line of the program? Before I explain what print does (which is pretty self explanatory), I have to tell you what INPUT nm$ means. Before I tell you that, you'll have to understand what variables are. Here you go:

Computers have thousands of little cubby holes in which you can store commands and information. Before you can store commands in a cubbyhole, however, you need to give the cubbyhole a name. Variables are these cubbyholes. In math class, you learned that variables are unknowns. You can't do anything else with them. For example, in math class, x * x = x squared, and x + x = 2x. You don't know what they are.

Computer variables always have a definite value. If you don't have anything in a cubbyhole, what's in it? Nothing. Nothing is equal to zero. Therefore, before you tell the computer what the variable equals, it always is equal to zero. After you tell the computer what a variable is equal to, (or before) you can use it in math problems, display it on the screen, and many other things. Variables look like this: a, a$, a%, a! Those are the four types of variables that QBASIC can handle. I'll tell you what each type means later.

I guess I should tell you what the commands mean in order, so keep this thought in your head while you read the next section.

### Math Operands:

Math is very important to QBASIC programs. You must be able to use math in programs you write to make any half decent programs. Well... you can make some half decent programs, but not many. So let's get to it!

* Add: `+`
* Multiply: `*`
* Subtract: `-`
* Divide: `/`
* Exponents: `^`
* Square Root: `SQR`
* Make an Integer: `INT`
* Order of Operations: `( )`

There are more of them, but these are the most important. Use them the same way that you would in math class. There's only one more catch. You have to say that a variable is equal to a math problem,. or to PRINT the math problem, or assign it to do something else. You can't just leave a math problem without telling the computer what to do with it.

I'll tell you how to use the last four mat operands mean, because they're not so obvious. The ^ for exponents makes the number(s) directly following the carat the exponents of the number proceeding it. You must have a number before and after the exponent sign. The SQR for square root finds the square root for number in parenthesis directly following it. For example, SQR(16) finds the square root of 16, which is 4. Integers are whole numbers. They can be positive or negative. What INT does is make the expression in parenthesis directly following the INT command into an integer. The INT function rounds the number to the nearest whole number. Order of Operations is very easy, but is a tough concept to understand. Say you wanted to multiply X by what the difference of Y and Z. How would you do it? Well, first, you would subtract Z from Y, and then multiply the difference by X. You write this as X(Y-Z), but in QBASIC, you would have to add an asterisk between the X and the first parenthesis. So it would look like this: X*(Y-Z). What the computer does is solve this problem from the inside out. It starts in the middle of the parenthesis, combining Y and negative Z, then multiplying this by X. If you don't understand this, read about it in your math book.

### PRINT:

PRINT puts text on the screen. Anything that you want PRINTed you must put in quotes, or be a variable. The Syntax of PRINT is: PRINT [expression list] [{,;}]. If you just type in "PRINT", a blank line will be PRINTed. Anything that is PRINTed must be put in quotes (""), or be in variable form. If you wanted to print Ahoy, there! on the screen, the statement would look like this: PRINT "Ahoy, there!". All ASCII characters can be PRINTed on the screen except for quotes ("). The answer to math problems can also be PRINTed by just writing the math problem after a PRINT statement. Also, if you put a variable after a PRINT statement, the variable's contents will be PRINTed on the screen. (Not the Variable's name!)

All this is fine except for the fact that you want to PRINT variables and regular text in one line. You do this by putting semicolons between separate things you want. If you wanted to PRINT "There are [The value of X] people in this class, and if you add ten people to the total number of people, there would be [X+10] people."? The code for it would look like: PRINT "There are";X;"people in this class, and if you add ten people to the total number of people, there would be";X+10;"people." Does that make sense? Just break everything up into separate parts. First, you want to write "There are" on the screen. So put your PRINT statement there, and type in "There are". Put your semicolon there to tell the computer that you are writing the next thing to be PRINTed. Now put X down because you want that to be PRINTed next. Now add another semicolon because you want to write another thing on the screen. Now type in the next set of text and your semicolon. Now you want to write the value of X+10 on the screen, so you write it followed by a semicolon. Now write "people." and you're done with that line of code! (A lot of work, eh? Don't worry, you'll get used to it...)

You could also do this by typing PRINT, and one expression followed by a semi colon, and it would display the same thing on the screen. For example, on one line, you type PRINT Hello, "; and on the next line, you type PRINT abc$. The following will be displayed: Hello, [value of abc$]. This brings us to another thing. Notice how after the Hello in the PRINT "Hello "; line I left a space? When you PRINT variables that keep track of numbers or math problems on the screen, there is a space put on both the left and the write of the character(s). When you PRINT string variables (variables that store text) on the screen, no spaces are put around the contents of the variable. To make it look nicer and easier to understand, you have to PRINT spaces on both sides of the variable. So you put a space after the end of Hello so that you don't have "wall to wall letters". If you want to print two string variables in a row, you must PRINT " " in between them to keep them separated. It would look something like this: "PRINT a$;" ";z$ ". 

#### Recap:

* If you type PRINT without any variables or text after it, it will PRINT a blank line.
* Text that you want PRINTed must be in quotes. (")
* Variables can be PRINTed by adding the variables title after the PRINT command.
* Math problems can also be PRINTed.
* More than one thing can be PRINTed on a line by adding semicolons between separate things you want PRINTed.
* You must PRINT spaces between string variables and other things you want PRINTed.
* If a semicolon follows a PRINT statement, the next thing PRINTed will be on the same line.

> **NOTE:** _The PRINT Command can be used to write to sequential files, and "PRINT USING" can be used to PRINT formatted text. These are not important for you to know now._

### INPUT:

INPUT is a command that takes information from the user of the program. The person types in information, and it is assigned to a variable. You INPUT like this: INPUT [Variable name]. This PRINTs a question mark (?) and puts a cursor on the screen where you should begin to type. After all desired information is INPUTted, press enter, and it is saved in the array specified by the INPUT command. String and numeric variables can be written with this command, but if you type characters other than numbers for numeric variables, the computer will not accept the information, and will write "Redo from start", and you will be given a second chance to INPUT the information.

Now you're wondering how to get rid of that darn question mark aren't you? Well, if you make your PRINT and INPUT statements one, you don't have to look at that stupid question marks. This is how you do it: Say you wanted to write "Type in your birthday:", and right after the colon, have the user type in their birthday. The code for that would look like this: INPUT "Type in your birthday", bday$ .

#### Recap:

* INPUT can write either string or numeric variables.
* When you type INPUT, a question mark is displayed to tell the user to type in information.
* If you don't want the question mark shown, make the INPUT statement into an INPUT/PRINT statement like this: INPUT "Write Number Here:", A$
* When you write characters other than numbers onto a numeric variable, a "Redo from start" message will appear, and you can retype the variables data.

### LET:

LET actually isn't a QBASIC command. It's a command left over from BASIC that Microsoft decided to get rid of in QBASIC. Why do you tell me about, you ask? Well, because what it does, or used to, is very, very important. LET allows the computer to change variable values without direct input from the user. For example, if you wanted to create a program that counts the number of times you've shot a cannon, you wouldn't want to have to have the player type in how many times they have shot. They might cheat, and it would get EXTREMELY annoying! So, you can have the computer change numeric variables value.

You do this by saying the a variable is equal to something. It would look like this: `ZUM=A+(34*56.8)`. This makes the variable ZUM equal to the value of A plus 34*56.8 . String variables are exactly the same, but what they're equal to must be another variable, or something in quotes. Understand? It's quite easy, and very important! 
#### Recap:

* The LET command is not required. Don't use it! It's a waste of time and of three good bytes!
* With this command, you assign the values of numeric and string variables.
* String variables can be equal to numeric variables, but numeric variables can't be equal to strings.
* If you say that a string variable is equal to something, it must be enclosed in quotes. `("")`

### Line Numbers:

Line numbers are a way to name certain portions of your program. These are essential for the computer to change positions in the program using GOTO or GOSUB statements.
What they are are numbers or words that are located at the beginning of a line or section of code. Numeric line numbers are sort of generic. They aren't customizable. Text line labels can be whatever you want, but they must be followed by a colon (:). Line numbers were required in older version of BASIC on each line of code, but now they're optional. Put them in front important sections of code so that you can send the computer to read that part of the program. In a program, they look like this: 126 PRINT "Hello, world!". The 126 on that line was the line number. Here's another example. goldfish: IF g$="gold" AND s$="fish" THEN PRINT "I like fish!" The goldfish: was the line label.

One more thing about word line labels: the line's name is not the word followed by a colon. It is just the word. This prevents QBASIC from thinking that a line number is actually a CALL statement. You don' need to know about these yet, just remember that the name of a line does not include the colon. It only needs it if it is the actual line number at the actual point in the program that is named by that line number. 

#### Recap:

Line numbers can be words or numbers.

Word line numbers require a colon after them. The colon is not part of the name.

### GOTO:

GOTO is a command that tells the computer to go to another place in the program, and continue executing the statements. GOTO tells the computer to find a line number or label, and start reading from there. It's pretty simple. All you have to do is type in GOTO and a line number or label, and the computer will resume the program there. It looks like this: GOTO funfunsillywilly . This tells the computer to find the line "funfunsillywilly", and continue reading from there.

#### Recap:

* GOTO tell the computer to find another line in the program, and continue reading from there.

The Syntax is: `GOTO [line label or number]`

### IF...THEN

`IF...THEN` asks computers yes or no questions only. You ask the computer if a variable is equal to what you asked about, it does what is after the THEN command. If the answer to the question is no, the computer ignores anything beyond the THEN command. The syntax for IF...THEN is IF [variable] [=, <, >, <>] [variable or expression] THEN [do whatever is beyond this point]. You can ask if an expression is equal to, less than, greater than, or not equal to.

The first IF...THEN statement in the program was on the 11th line, which is IF g<>n THEN 300. It asks the computer if your guess, g is not equal to the number, n. If your number is not equal to the computer's number, the computer goes down to line 300. If they are equal, the computer continues reading on the next line, ignoring the THEN command.

Pretty easy, right? Well, there are still a couple more things you should know about this command. You can use the AND, OR and the ELSE command. You can probably figure out how to use them - they're not hard. However, I'll show you how just because I'm nice.

`AND` is a command that you put in the IF part of the command. You put this there to ask two questions, and if both are true (have yes for an answer), the command(s) after the THEN are executed. The commands after the THEN are only executed if both are true. Here's what it would look like: IF x=18 and m$="Hello, Dude!" THEN PRINT "Hello!".

`OR` works almost the same way as AND. It does what is after the THEN statement if any of the statements are true. It would look like this: IF a$="abcdefg" OR qwert=8 (88 + 9.2) OR B$="Up, up and away!" THEN PRINT "!Ay Carumba!".

ELSE is a command that follows the THEN command. If the statement is false, the computer skips what is after the THEN command and does what is after the ELSE command. It looks like this: IF hi$="Here comes RICHARD SIMMONS!" THEN 100 ELSE 200.

When you ask questions about string (text) variables, you must write the expression that the variable will equal if the question is true in quotes.
One more thing: after THEN and ELSE commands, if you want to use a GOTO command, just write the line number. The GOTO command is not required, so skip it :)

#### Recap:

`IF...THEN` asks only yes or no questions. It's either true or false.
If the statement is true, the command(s) after the THEN are executed.
If the statement is false, the command(s) after the THEN command are skipped.

AND and OR can make IF...THEN commands more powerful by making the command ask more questions.

Answers to questions asked about string variables must be in quotes. (_")_

The ELSE command follows the THEN command, and is executed if the IF...THEN question is false.

### FOR...NEXT

FOR...NEXT is your first loop. Loops are bits of a program that tell the computer to repeat itself - to do a section of a program over again. Loops were invented because programmers are extremely lazy, and instead of wasting time and space writing PRINT "hello!" ten times, they just write FOR t=1 TO 10 : PRINT "hello!" : NEXT t . I'll explain what the FOR...NEXT loop means (and does) now.

What FOR does is name a variable and set it equal to the number before the TO, and tell the computer to repeat the part of the program up to the NEXT that many times. Simple, right? Well, there's more. You can also set the STEP for a FOR...NEXT loop. The STEP is the number that the variable adds to itself everytime it goes by the FOR command. The STEP is not required, and is by default set at one. The NEXT command does not have to have a variable following it, but it's nice to have one there so that you know what FOR loop you're returning to. The computer figures that when it hits a NEXT, it should return to the most recent FOR.

#### Recap:

* The FOR...NEXT loop repeats a part of a program a specified number of times.
* The syntax of this loop is: FOR [numeric variable (name of a variable)] = [numeric value (the value of the numeric variable)] TO [numeric value (The number that the loop should end on.)] (STEP [number (the number to be added to the variable each time around]) NEXT can be left without a variable or with one.
* Anything you want can be put in between FOR...NEXT loops, even other FOR...NEXT loops.
* STEP is not required, and is automatically set at one if omitted.

### END:

The END command tells the computer that the program is over, and it should stop reading lines. It's as simple as that. When the computer reads the end command, it stops reading lines, and PRINTs "Press any Key to Continue." It returns power to the system. The syntax for END is - you guessed it - END.

The END command is not required to end the program unless there is more of the program listed below where you want it to END. If the program runs out of lines to read, it assumes the program is over, and stops it. 

#### Recap:

* The END statement tells the computer to stop reading and executing the program.
* The END command's syntax is: END.

### RND:

RND chooses a random number between zero and one. Not very impressive, eh? Well, it isn't, but if you multiply that really small number by a big one, it becomes a big, random number!

Notice the fifth line down in the program? It has the following code: N=INT(RND*19)+1 . You might understand it, but it might look Greek to you. I'll explain it step by step. First of all, this is a LET command, without the LET. (You know why LET is omitted.) This line makes the variable N a random integer between 1 and 20. Now the hard part - the math problem. Remember how computers solve math problems backwards with order of operations? Well, this problem is no different. The computer starts out with the RND command. The computer sees this and picks a random number between one and zero. Next, it multiplies the random number by 19. Now the parenthesis are gone. Next, the computer adds one to the number, so that the number is between one and twenty. You see, RND can choose a number so small that if you multiply it by twenty, still is less than one. So, to make the number that's less than one equal to it, you add one. However, then, if you multiplied the number by 20, the number would be between 1 and 21. Well, that's not right, so you have to multiply the RND by 19. Finally, the INT command rounds the number to the nearest whole number. It may be a complicated way to get a number, but you'll get used to it.

There's one more problem with QBASIC and RND's, however. IT ALWAYS PICKS THE SAME ONES! They're not random, which is why you use RANDOMIZE TIMER in front of your RND statements if you want them to be truly random. Put a apostrophe in front of the RANDOMIZE TIMER line to REM it out, and then run the program. Play the game until you win once, and then exit.

I bet you that the answer was 15. I don't know why RND doesn't work right, but the RANDOMIZE TIMER statement fixes that problem. You don't need to know what it means - just remember to put it in front of your RND statements. When you're more advanced you can learn those commands, but don't worry about it now.
#### Recap:

* The RND command picks a random number between zero and one.
* Multiply RNDs to get larger random numbers.
* Always put RANDOMIZE TIMER statements above RND statements.

### Variable Types:

There are two basic types of variables - numeric and string. String variables are ones that can hold all ASCII characters. They can not be used in math problems. When asking questions about them, or changing their content, the expressions must be in quotes. String variables are letters and numbers followed by a dollar sign. ($) String names must have a letter as the first character, but everything else is up to you.

There are three types of numeric variables. The first type is called floating point. They are regular number variables. They can be any number, it doesn't matter. Variables with a percent sign on the end are integers. They automatically round themselves off to the nearest whole number. I have no idea what the ones with exclamation points are. As far as I can tell, they do the same thing as floating point variables. I've only seen them used once or twice.

#### Recap:

* Variables with dollar signs on the end are called strings, and can hold any ASCII character.
* Variables without any sign on the end are floating point variables. They hold numbers.
* Variables with a percent sign are integers. They automatically round to the nearest whole number.

## Formatting Text ##

### COLOR (FAGGOT WAY)

COLOR lets you change the color of text you put on the screen. It's very simple to understand. The syntax is: COLOR [foreground color] , [background color] , [border color] . Foreground is the color that the text is. Background is the color that the area around the letter is. Border color is supposed to set the border to the screen, but doesn't do anything that I can see! if you put COLOR in the program, it changes the color of all of the text printed until the next COLOR statement.
For example, if you typed "COLOR 1, 4", it would PRINT blue text with a red background. If you typed "COLOR 2, 9", it would PRINT green text with a light green background. Understand? It's pretty easy. Now you need to know the basic fifteen color codes. Well, guess what? They're right here:

    0 - Black
    1 - Blue
    2 - Green
    3 - Light Blue
    4 - Red
    5 - Purple
    6 - Brown
    7 - Light Grey
    8 - Dark Grey
    9 - Light Blue (A little darker than #3)
    10 - Light Green
    11 - Turquoise
    12 - Light Red
    13 - Light Purple
    14 - Yellow
    15 - WhiteZ

After you use these colors for a while, you memorize them.

### !! COLOR (BADASS WAY) !!

you can have up to 250,000 colors if you only write "screen 12" at some of the first lines.

the formula is C = R + (G * 256) + (B * 65536) as in C = color, R = red, G = green and B = blue.

then use "palette 1, C" to change the color 1 (see faggot way) to some new exciting shit BWAHAHAWDHA

#### Recap:

* COLOR changes the color of text that you PRINT on the screen.
* The syntax is COLOR [foreground color] , [background color] Foreground is the actual text color and background is the background color. A comma must always separate the two numbers.
* COLOR changes the text color until the end of the program or until the next COLOR statement.

### LEFT$

LEFT$ is the first of the three string splitter-uppers. It takes a string expression and breaks it into seperate parts. The syntax is LEFT$ (stringexpression$, number of characters) . Stringexpression$ is the string variable or the text that you want part of. The number of characters is the number of characters you want left of the first character in the expression returned. It takes the characters starting with the furthest left character and going right the number of characters specified and returning them. LEFT$ can be used in PRINT statements and in LET statements.
Here's what it looks like: PRINT LEFT$ ("Take a bite out of crime", 9) This writes the first nine characters from the first character, which is "Take a bi". That's what's written on the screen. LEFT$ can also look like this: "MA$ = LEFT$ (dod$, 5)". This makes the variable MA$ equal to the first five characters of the variable dod$. That's the LEFT$ command.

#### Recap:

* LEFT$ splits up strings from the leftmost character on.
* The syntax is LEFT$ is LEFT$ (stringexpression, number of characters) stringexpression is either a string variable or an expression in quotes. Number of characters is the number of characters you want the computer to read from the left of the expression.
* This comand can be used with PRINT statements or LET statements.

### RIGHT$

We won't go into this one as much as we did with the LEFT$ command. It's basically the same thing, just backwards. It's syntax is RIGHT$ (stringexpression, number of characters) . Stringexpression is a string or expression and number of characters is the number of characters you want the computer to read and return.

It looks like this: PRINT RIGHT$ ("Oh my God! They killed Kenny!", 13) "killed Kenny is PRINTed. 

#### Recap:

RIGHT$ Splits up words from the rightmost character on.
This is exactly the same as LEFT$, it just starts from the right side.
This works with the PRINT and LET statements.

### MID$

MID$ reads string variables. starting midway through a string or expression, and continues until a specified point to stop. This is a lot like LEFT$ and RIGHT$, but a little more complicated. The syntax is: MID$ (stringexpression$, start%, length%) . Stringexpression$ is either a string variable or an expression in quotes. Start% is the charachter number that the computer should begin reading on. Length% is the amount of charachters you want the computer to read (going from left to right). MID$ can be used with PRINT or LET statements.

It would look something like this: PRINT MID$ ("Green Grow The Rushes Ho!", 7, 8). That line would PRINT "Grow The". It started reading on the seventh character, the G on Grow and continued reading until the e on The, which was eight characters away. This line: A$=MID$ ("Huzzah!", 3, 2) would store "zz" in A$.

#### Recap:

MID$ reads part of a variable and writes it to a variable or displays.
The syntax is: MID$ (stringexpression$, start%, lenght%). Stringexpression$ stands for a string variable or an expression in quotes. Start% is the character number that you tell the computer to start reading on. Length% is the amount of characters you want the computer to read for.
MID$ can be used with LET or PRINT statements.

### LOCATE

LOCATE lets you put text at a certain place on the screen. Imagine the screen as a grid with a whole bunch of places that you can put letters. When you use a PRINT statement to write text on the screen, it, by default, starts on the first open space on the screen - usually the top left corner. You can't decide exactly what place on that grid to put your character without a whole bunch of PRINT statements and spaces - unless you use the LOCATE command. The syntax is: LOCATE [row%] , [column%] , [cursor%] , [start%] , [stop%] . The most important parts are row% and column%. They tell the computer what space on the imaginary grid to start putting the text at. Cursor% tells the computer if you want the cursor shown after the text you PRINT. If you put a one there, it is shown, and a zero makes it not-shown.
LOCATE looks like this while in a program: LOCATE 10, 12 . It doesn't do anything unless followed by a PRINT statement. If that LOCATE statement was put in front of a PRINT statement, the next thing PRINTed would be LOCATEd at that place on the screen. If this line: LOCATE 18, 24 : PRINT "I want Pringles!" was in a program, the computer would go to the eighteenth row down, and then go to the twenty - fourth space over and PRINT I want Pringles! Don't worry about the other three attributes - I've only needed to use one of them in one of my program once. NOTE: There are different numbers of rows and columns depending on the screen mode. You'll learn about screens in tutorial five.

#### Recap:

* LOCATE PRINTs text on the screen at a certain point on an imaginary grid.
* The syntax is: LOCATE row%, column%. There are other attributes - you [probably] won't need them.
* The next PRINT command after the LOCATE command is PRINTed at the specified location.
* The number of rows and columns varies with screen mode.

### UCASE$

UCASE$ makes any string or expression have only capital letters. This takes any lower case letter (askii characters 97 to 122) equal to their capital form (askii character 65 to 90). This is very useful for reading input which may be inputted in capitals, lowercase, or mixed. LCASE$ is almost the same, it just does the opposite.

The syntax for UCASE$ is: UCASE$ (stringexpression). Pretty simple, right. UCASE$ ("Happy Happy Joy Joy!"). Would return "HAPPY HAPPY JOY JOY!". UCASE$, like LEFT$, MID$ and RIGHT$ must be used with a PRINT or LET statement.

#### Recap:

UCASE$ makes any string variable or expression completely capital.
The syntax is: UCASE$ (stringexpression) Variableexpression must be in parenthesis and must be a string variable or a text expression.

### LCASE$

LCASE$ is exactly the same as UCASE$, just changes the letters to lowercase instead of uppercase. This takes any uppercase letter (askii character 65 to 90) equal to their lowercase form (askii characters 97 to 122). This is very useful for reading input which may be inputted in capitals, lowercase, or mixed.

The syntax for LCASE$ is: LCASE$ (stringexpression). Pretty simple, right? LCASE$ ("Happy Happy Joy Joy!"). Would return "happy happy joy joy!". LCASE$, like LEFT$, MID$ and RIGHT$ must be used with a PRINT or LET statement. 

#### Recap:

* LCASE$ makes any string variable or expression completely lowercase.
* The syntax is: LCASE$ (stringexpression) Variableexpression must be in parenthesis and must be a string variable or a text expression.

### TAB

TAB is a command meant to be used with the PRINT command. It is a primitive form of LOCATE. It moves the starting PRINTing point over a few spaces (columns). It is put between PRINT and the expression you want PRINTed.

It looks like this: PRINT TAB(25); "Rugga-Rugga!". This PRINTs Rugga-Rugga! twenty five spaces to the right. It's very easy to understand. Just change the expression and the number of spaces in that statement and you're set!

#### Recap:

TAB is used with the PRINT statement to PRINT text a specified number of columns to the right.
The syntax is: PRINT TAB(number%); [stringexpression]

## Advanced Commands ##

### INKEY$

INKEY$ is an extremely useful command. Basically what it does is check the keyboard to see if you are pressing a key, and if so what is it? It's pretty simple, but easy. INKEY$'s syntax is INKEY$. What you do with it is treat it like a string variable. You can use it in IF...THEN statements, LET statements, PRINT statements - anything you could normally use with a string variable or text in quotations.

Here is what INKEY$ would look like in a program: "IF INKEY$="a" THEN GOTO 100" That line of code will check to see if the key that is being pressed is "a", and if it is, goes to line #100. Simple as that. You could also use it like this: "a$ = "INKEY$" or "PRINT INKEY$". Just think of it as a string variable, and it will be easy to understand.

There is another trick to INKEY$. If you are checking for a standard key (a letter or number), it will be read as a one byte letter. That's simple. For extended keys (arrow keys, function keys, escape, enter, etc.) a "null" character and an ascii scan code. What that means is that if you want to check and see if the up arrow is being pressed, the code would look like: IF key$=CHR$(0) + "H". (For some more of these "codes", check my tutorials section. There is a tutorial that has all of the keyboard scancodes.) You don't know the CHR$ command, but it is the fourth heading down from here, so go head and read it if you want to know it ahead of time.

One more thing: If you check what key is being pressed, there is a very good chance that the user is not pressing that key at that specific nano second. What are you going to do? Well, the most logical answer is to check and see if the user presses it the next nano second. If they aren't pressing a key, you should check it again. Over and over until something is being pressed. If something is being pressed,. go off into a branch of your program depending on what is being pressed.

#### RECAP:

INKEY$ checks to see what key is being pressed at the exact time that the command is being executed.

It is a good idea to check what key is being pressed with INKEY$ many times in a row because there is a big chance that the user will not be pressing that key at that time.

The syntax for INKEY$ is INKEY$, but it is used as a string variable. This command can't be used without a "helping" command.
Extended keys use "codes" instead of the exact letter or number.

### INPUT$

INPUT$ is basically a cross between INKEY$ and INPUT. It is used to take a certain number of keypresses from the keyboard without displaying them on the screen. It is also used to read from OPENed data files, but you won't be getting in to that for a while.

The syntax for INPUT$ is "INPUT$ (Number of expressions you want read)". Simple as that. This command must be used with a "helping" command that is normally used with a string variable. (Commands like "LET", "PRINT", "IF...THEN", etc.) Use it just like INKEY$, just realize that it will store or read more than one character.

#### RECAP:

INPUT$ reads or stores (depending on the command it's used with) a specified number of characters.
The syntax for INPUT$ is: INPUT$. It must be used with a "helping" command.

### DO...LOOP

DO...LOOP is, as far as I'm concerned, the most useful loop. It is very useful for main loops of games, and can even do the same functions as IF...THEN if you put an adding statement in the middle. Okay, enough talk. DO...LOOP is a command that DOes something forever, or until you tell it to stop. In older versions of BASIC, this was a major problem, because if you ran your program, and did not provide an "exit" from the loop, it would continue forever. The programmer would have to turn off their computer and would lose all of the programming they had done from the last time they saved. Now, though, you can just use CTRL + Break
Here's how to use DO...LOOP: "DO : 'execute commands here : LOOP" simple as that. This code doesn't do anything because in between the DO and LOOP I don't have any commands except for a REM command. If there was other code in between, say, "PRINT "hello!", "hello" would be PRINTed over and over again - forever or until you press CTRL + Break or turn off your computer.

DO...LOOP already is pretty useful, but back when Microsoft developed QBASIC, they decided to make a couple more functions you could use to end the LOOP, thus making programming easier. These commands are, among others UNTIL and WHILE. UNTIL keeps on going through the LOOP UNTIL some variable equals something. It looks like this: "DO : x=x+1 : LOOP UNTIL x=1783" This simple program LOOPs around until x=1783, adding one to itself every time it goes through. UNTIL can be used with both DO and LOOP in the same manner. WHILE works pretty much the same. WHILE makes the LOOP continue until the variable after it does not equal itself. This command usually is used with greater than or less than signs, but can be used with an equal sign. It looks like this: "x=400 : DO WHILE x > 10: x=x-1 : LOOP" This program makes x=400, then subtracts one from it every single time it LOOPs until x=10. Once again, this command can be used with the DO or the LOOP.

#### RECAP:

* DO...LOOP is a loop that continues forever until it is stopped. 
Any commands can be put between the DO and the LOOP that you want done over again later.
* WHILE and UNTIL can be used with either the DO or the LOOP to stop the loop if somthing equals the expression or variable following the WHILE or UNTIL.
* WHILE checks if something is equal or not equal to something WHILE the loop is running.
* UNTIL makes the LOOP continue UNTIL a variable equals the variable or expression following the UNTIL command.
* This is useful for main loops of programs.

### CHR$

CHR$ is a command that converts ascii code numbers into ascii characters. It takes a character (a letter or a number) and converts it to an ascii number code. It can be used with any command that can be used with any command that supports string variables. The syntax is: CHR$, but always needs a "helping" command to be used. Here is what it looks like: "PRINT CHR$(150)" will PRINT the ascii character corresponding with 150, which is "û".

#### RECAP:

* CHR$ converts numbers into ascii characters.
* The syntax is CHR$, but must be used with a "helping" command that is normally used with a string variable or expression.

### ASC

ASC is a command that ascii characters numbers into ascii number codes. It takes an ascii number code and converts it to a character (a letter or a number). It can be used with any command that can be used with any command that supports number variables. The syntax is: ASC, but always needs a "helping" command to be used. Here is what it looks like: "PRINT ASC(û)" will PRINT the ascii number corresponding with û, which is 150.

#### RECAP:

* ASC converts ASCII Characters into Ascii number codes.
* The syntax is ASC, but must be used with a "helping" command that is normally used with a number or a number variable.

### SLEEP

SLEEP is a command that makes the computer sleep for a certain amount seconds or until a key is pressed. It is universal, so SLEEP will cause the same delay on all computers - 286 to P800. Here's how it works: "SLEEP 5". This line of code will make the computer delay for exactly five seconds, then resume the program with the lines of code after it. It's very simple. There are some problems with SLEEP, though. If the computer is "SLEEPing", and you press a key, it skips from wherever it is in the current second to the beginning of the next one. Also, you can't use decimals with SLEEP - only whole numbers.

SLEEP has one more function. If you type in just "SLEEP", the computer will stop and wait for a key to be pressed.

#### RECAP:

SLEEP makes the computer stall for a specified number of seconds or waits for a key to be pressed.

The syntax of SLEEP is: SLEEP [number of seconds to stall] . If no number of seconds is given, the computer waits for a key press.

SLEEP can not support decimals and if the computer is stalling for a specified number of seconds, and a key is pressed during a second, it goes to the beginning of the next second. 

### Sub Routines

Sub Routines are small programs that are in a bigger program. They can be CALLed upon to perform a specific task any time during the course of a program. They are very useful in big programs that perform multiple functions, or games.

Here's an easier way to think of a sub routine. Think of the main program as your brain and involuntary organs (heary, lubgs, etc.). Your arms, hands, legs and feet are subroutines to the main program. Say that you wanted to walk across the room, pick up a baseball and throw it out the window. Now it would be very hard for you to go across the room and throw the ball without using your arms or legs - your subroutines. Now, you could do it using your main program, but it would be way too hard for you to go across the room, pick up the ball and get it out the window without using your arms or legs. If you had those subroutines, you could do it very simply. It's the same thing with subroutines on a main program. Subroutines make the program size much smaller, much simpler to use, faster, and makes much less work for the programmer.

Lets say that you have two subroutines on your main program - one for your legs and one for your arms. The one for your legs takes a message from the main program that says "stand up and walk to the other side of the room." The legs do this task and return control to the main program. The main program says to the arm subroutine "pick up the ball and throw it out the window." The arms throw the ball out the window and return control to the main program.

Okay, enough talk about arm subroutines and throwing baseballs. Subroutines are little tiny programs that do one simple task whenever you want that to happen and can do it differently to fit different needs (variables). They can be on the main "page" of your program, or side "pages". By "page", I mean place where code is displayed for you to edit it. A program can be one long, complex page that has all subs included, reachable with a GOSUB statement, or they can be on seperate pages and be reached by CALL statements.

All my rambling isn't really helping you much, so we'll just get started with the coding process and you should catch on.

### GOSUB

GOSUB basically means "go to a sub routine". This only goes to a sub on the main "page" of the program. It is almost like GOTO, but has a cool built-in feature. When the subb is done with, it RETURNs to the place where it was called. So if you call it anywhere in a program, it will return to the same place that it was called from.
The syntax for GOSUB is "GOSUB [line number or name]". That's all it is. It goes to the line number that the sub begins on, goes through the sub and RETURNs to the next command after the line where it was called. This is what it would look like in a program: "GOSUB 1080". This statement would send the computer to line 1080 to execute the commands in the sub routine until it is told to RETURN to the line where it came from.

#### RECAP:

GOSUB sends the computer to another part of the program and executes the statements there until it is told to RETURN.
The syntax for GOSUB is: GOSUB [line number or name]

### RETURN

RETURN is a command used to RETURN to the place in a program where the last GOSUB command was executed. This command is put at the end of subroutines on the main "page" of a program.

The syntax for RETURN is just plain old RETURN. There are no variables or expressions you have to fill in. It's very simple.

#### RECAP:

RETURN is used to RETURN to the place in a program where the last GOSUB command was executed.

The syntax for RETURN is just plain old RETURN. No bells and whistles with this one.

Since you might not be completely clear on subroutines and usage of GOSUB and RETURN, I've written a small program to better explain it here:

#### Program using a GOSUB/RETURN subroutine

    PRINT "Cool! We're goinng to demonstrate how to use suboutines!"
    PRINT "Press a key to continue..."
    SLEEP
    GOSUB hello                 'Goes to a subroutine beginning on the line "hello"
    PRINT                           'After the subroutine ends, you are sent here.
    PRINT "Wow! That subroutine ran and RETURNed us to the same place in the program! Neato!"
    PRINT "Press a key to continue..."
    SLEEP
    CLS
    PRINT "Now, to prove that we didn't cheat, I'll run that sub again!"
    GOSUB hello                 'calls upon the subroutine again.
    PRINT "Groovy!"
    END                             'The End!
    hello:                            'The line label that this subroutine begins on.
    FOR t=1 to 10               'starts a loop to PRINT some words ten times.
    PRINT "This loop is in a subroutine! This will be printed ten times!" 'PRINT's some crap
    NEXT t                         
    RETURN                       'RETURNs to where this sub was called from via GOSUB

### Seperate "Page" Subroutines

Okay, you know how to make a subroutine on the same "page" of program as the main loop, but what if you want your program on a different "page" of program? Well, QBASIC has that incorporated into it. Now to get you started, I'll type out step by step instructions for you to follow to start your very first subroutine. First, (this is in QBASIC, mind you), click on "Edit" on the heading row of the  screen. After the drop down menu is opened, go down to "New Sub". Click it. Now a pop up window will appear. Next to name, type in the name that you want to give your sub. For this example, I'll call the sub "myfirstsub". After you have that typed in, click on OK or press enter (whatever you prefer.) Now three things will happen. Where the name of your file is displayed, it will show [subname]:[filename]. In this case, "myfirstsub : Untitled". The main program screen will have disappeared, and in the screen is the following text: "SUB [subname], (NEXT LINE) END SUB". What does this mean? Well, END SUB is just like RETURN. It just returns the computer to the same spot on the previous page, not to a different spot in the program. The SUB [subname] line identifies the sub for both you and teh computer. That's about it. No executable commands can be put before these two lines of code, but any command you want can be put in between.

### DECLARE

DECLARE is a command that tells the computer that there is a seperate page subroutine, and what variables are associated with it. Think of DECLARE as a REM statement for the computer. It tells the computer that there is a subroutine on a seperate page in the program, and when you run the program, what the variables supplied by the main loop mean in the subroutine. The computer puts this statement in for you after you save the program and load it again, or you can type them in yourself. It must always be at the top of the main page of your program, and be before executable statements.

The syntax for DECLARE is: "DECLARE SUB [subroutine name](parameter list)". The subroutine name is hust that - the name of the subroutine that you are declaring. The parameter list is a list of variables that you supply when you CALL the subroutine that are going to be used in the subroutine. These varaibles are listed, seperated by a comma. This is what DECLARE would look like in a program: "DECLARE SUB shop(itemname$, price%, money%)". This declares the sub "shop", and makes the variables itemname$, price% and money% variables that must be supplied every time the sub is CALLed. When you CALL teh sub, you just supply what those variables are equal to in that particular case.

#### Recap:

DECLARE is a command that tells the computer that there is a subroutine on another page, and supplies parameter names that are to be supplied when the sub is CALLed for use in the sub.

The syntax is DECLARE SUB [subroutine name](parameters seperated by commas)

If you don't type in this statement, the computer puts it in for you the next time the program is loaded.

DECLARE must always proceed executable statements.

### CALL

CALL runs a subroutine on a different page of a program. It can be located in any sub or on the main page (but if you CALL too many subs out of subs, you run out of stack space.) It must contain all parameters that are DECLAREd with the subroutine.
The syntax for CALL is "CALL [sub name](parameters)". The sub name is the name of the sub. Parameters are the variables DECLAREd with the DECLARE statement in the exact order that they were originally written, and seperated by commas. Here is what CALL would look like in a program: "CALL oogabooga("abracadabra", 17, "Hello!")" This CALLs the sub oogabooga and supplies variables with information to store for use in the sub.

CALL has one more cool feature. You can omit the word CALL, and CALL a sub with just it's name. It would look like this: "moveplayer". If the sub has parameters, You must omit the parenthesis around them. It would look like this: "CALL wagtail "wagging...", 83.7, "Wag completed!", 104.98" Simple, eh?

#### RECAP:

* CALL runs a subroutine on a seperate "page" than the current one.
* The syntax for CALL is "CALL [sub name](parameters seperated by commas)
* The CALL can be omited, but if omited, parenthesis must be omited too.

### COMMON SHARED

Ever notice how variables that are used in the main program are reset when they are used in subs? COMMON SHARED is the command(s) that you can use to solve this problem until you learn DIM. COMMON SHARED tells the computer not to reset certain variables in subroutines. The syntax for COMMON SHARED is "COMMON SHARED [parameters seperated by commas]" Very simple. It would look like this in a program: "COMMON SHARED name$, HP, MP, weapon$". This code tells the computer not to reset the variables name$, HP, MP and weapon$ when they are used in subroutines. COMMON and SHARED have different meanings, but you don't need to know them now. Also, COMMON should be located at the top of the main page of a program.

#### RECAP:

* COMMON SHARED tells the computer not to reset certain variables when they are used in subroutines.
* The syntax is "COMMON SHARED [parameters]
* COMMON SHARED should be located towards the top of the main page of a program.

### EXIT SUB

EXIT SUB is a command to end the subroutine in the middle of it and return to the place where the sub was called from. It performs the same funtion as END SUB, but it does it in the middle of a sub, as END SUB must be the last command in a subroutine. The syntax for EXIT SUB is EXIT SUB. Nothing special about it. You would probably use this with IF...THEN statements if certain variables are equal.

#### RECAP:

EXIT SUB exits a subroutine and returns the computer to the plave where the subroutine was CALLed from before the END SUB command.

The syntax for EXIT SUB is EXIT SUB.

## Algorithms

Algorithms are plans for a program that you should make before you begin coding it. Somtimes you would write this out, sometimes you would just visualize it in your head, but anyway, this is how you think up how a program works, and how to code it.
Algorithms are made up of many simple steps (commands) and go in an order. They ask yes or no questions (IF...THEN) to decide what to do next. Here is the algorithm for a simple shooting game:

1. Move target a little bit.
2. Get input from player.
3. If no input is given, repeat from #1.
4. If INPUT is a press from the spacebar, shoot bullet.
5. If INPUT is from escape key, end the program.
6. Move bullet forward, move target a little bit.
7. Repeat #6 until bullet is off the screen or hits the target.
8. If the bullet hits the target, add one to target hits.
9. If target hits equals 5, tell the player that they one. If not, repeat from #1.

Understand? Converting this into a program would be much easier than writing it from scratch. Now that you are going to be maiking more complicated programs, algorithms (plans) for your programs will be very helpful.

## Sample Game ##

Here is the code for a simple game using the commands you learned above:

    REM ***Guess The Number***
    CLS
    PRINT "What is your name";:INPUT nm$
    110 RANDOMIZE TIMER
    N=INT(RND*19)+1
    PRINT
    PRINT nm$;", I'm thinking of a"
    PRINT "number between 1 and 20."
    138 PRINT
    PRINT "What is my number";:input g
    IF g<>n THEN 300
    PRINT
    PRINT "Hurray, ";nm$;"!"
    PRINT "You Guessed my number!"
    FOR t=1 to 10000:NEXT t
    200 PRINT
    PRINT nm$;", Do you want to"
    PRINT "play again";:INPUT a$
    IF a$="Y" OR a$="y" or a$="YES" or a$="yes" THEN 110
    IF a$<>"N" or a$<>"n" or a$<>"NO" or a$<>"no" THEN 200
    PRINT:END
    300 PRINT
    IF g>n THEN 350
    PRINT "Sorry, ";NM$;". Too Small!"
    GOTO 138
    350 PRINT "Sorry, ";nm$;". Too Big!"
    GOTO 138
    'This is the end of the program!

### Sample Game Outcome ###

Here is how the game should play out (assuming you guessed the numbers this way)

    Computer: Ready
    You: Shift + F5
    Computer: What is your name?
    You: Anonymous
    Computer: I'm thinking of a number between 1 and 20.     What is my number?
    You: 10
    Computer: Sorry, Anonymous. Too small! What is my number?
    You: 17
    Computer: Sorry, Marvin. Too big!        What is my number?
    You: 15
    Computer: Hurray, Anonymous! You guessed my number!
    ---Slight Pause---
    Computer: Do you want to play again?
    You: No
    Computer: Press any key to continue.