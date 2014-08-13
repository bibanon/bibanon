
# What is an Operator #

An operator is a command which tell your PC exactly what you want it to do.  This is not to be confused with a operand, an operand is an arguement for the operator.

# Input/Output Operators #


## > ##

Write program output to a file, is used as follows:
    echo hello world > helloworld
this writes anything that the command "echo hello world" says into the file "helloworld."  Will overwrite the contents of helloworld if the file already exists.

## >> ##

Append all output to a file, is used as follows:
    echo hello world >> helloworld
this appends any data output from the command "echo hello world" into the file "helloworld." All information will be placed at the end of the file and no information from "helloworld" will be overwritten

## < ##

Fill the input stream of a program with the content of a file (usually the input stream is connected to the commandline)
    someprogram < somefile
will work as if you started 'someprogram' and typed the content of 'somefile' into the program's commandline by your own hands

## | ##

Write the output stream of a program to the input stream of another program
Using this operator (usually called 'pipe') you can build a chain of over9000 programs using the output of the previous program as input and doing magic with it


# Job Control Operators #


## & ##

Start a program in background, so you can continue using the shell while it's running. Whenever you start a program with the '&' operator appended, it will be assigned a job number which is displayed in square brackets. You can use this job number to bring the program back into foreground by invoking 'fg jobnumber'. To get the job into background again, you can use 'Ctrl-Z' to interrupt the program and 'bg jobnumber' to continue in background.

# Logical Operators #

In unix systems, the two possible values of boolean logic, TRUE and FALSE, are represented by 0 for TRUE and any other number than 0 for FALSE. This can be useful since every program has a return value which indicates, if the program ran successful or not. The return value of a successfully ran program will always be 0 which also means TRUE. Knowing this, we can for example use the success or fail of a program to determine if we want to run another program automatically.

## && ##

The AND operand is true, if values on both right and left side are true. Since both values must be TRUE to make this operand return TRUE, the 2nd value won't be considered anymore, if the first one already was FALSE. So we can use this poerator to start a 2nd program only if the 1st one we started ran successful:
    program1 && program2
will start 'program2' only if program1 runs successful.
To start a 2nd program after the 1st one no matter, if it was successful, we can use ';' as delimiter between the commands.
    program1 ; program2
will run 'program1' and 'program2' after 'program1' finished.
