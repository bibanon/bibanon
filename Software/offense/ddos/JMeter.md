
## Ingredients  ##

1. If you don't have Java, get it [here](http://anonym.to/https://cds.sun.com/is-bin/INTERSHOP.enfinity/WFS/CDS-CDS_Developer-Site/en_US/-/USD/ViewProductDetail-Start?ProductRef=jre-6u4-b-oth-JPR@CDS-CDS_Developer)
1. Get JMeter from one of the links below (Doesn't matter which)

  1. [jakarta-jmeter-2.3.1.zip](http://anonym.to/http://apache.dataphone.se/jakarta/jmeter/binaries/jakarta-jmeter-2.3.1.zip) 404
  1. [jakarta-jmeter-2.3.1.zip](http://anonym.to/http://www.smudge-it.co.uk/pub/apache/jakarta/jmeter/binaries/jakarta-jmeter-2.3.1.zip)
1. Unzip it
1. Unzip it
1. Get [link](http://anonym.to/http://rapidshare.de/files/38417667/scientology.jmx.html) [Mirror](http://www.mediafire.com/?5taq9vvn33z)
1. Go into the 'bin' folder and run 'jmeter.bat' (.sh for linux/macfags)
1. Go to File -> Open, and select the scientology.JMX file
1. Go to Run -> Start
1. Raep!
1. Watch results on the 'Aggregate Report' screen if you want.
1. ???
1. PROFIT!!!
tl;dr: It's designed to "stress test" a server, we're using the stress and not the test part. When a raid uses JMeter look for a pre-prepared "test plan" file. [Download here!](http://anonym.to/http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi)

## OMG IT'S ANON SOFTWARE, WILL NOT RUN ##

JMeter is a freely available, open-source application written and maintained by the Apache Software Foundation. These people are also the maintainers of the Apache web server, as used by 70% of webservers, including /b/. This shit is legit, clean and free of spyware. If you're paranoid, build your own sources.
Running and using JMeter is not a crime and the software/usage is entirely legit. Effects (Denial of Service) may not be if misused (say, by anon)

## Performance   ##

If you have more memory than 512 MB you can increase the heap size JMeter uses to increase performance.
Open the jmeter.bat (Windows users) or jmeter file (NOT the JAR- Linux users), and find the line that looks like this:

* set HEAP=-Xms256m -Xmx256m (Windows Users)
* HEAP="-Xms256m -Xmx256m" (Linux Users)
Now, just edit where it says '256' to whatever you want it to be- say, 512, or 768 (1024 if you've got 2 gigs of RAM and not much else open). Restart JMeter if it's running already using your new startup file and off it goes.

## Tutorials   ##

Along with the other resource raep tools in our arsenal, this can be of great use to put stress on any larger targets who need extra raep to take down.
To use any JMX (Test Plan) files, you need JMeter itself. It's Java-based and therefore works on all platforms.

* [Download, includes manual- you want the '2.3.1.zip' file (Binary)](http://anonym.to/http://jakarta.apache.org/site/downloads/downloads_jmeter.cgi)
Creating your own test plans, when done well, is the best way to go about attacking, or alternatively you can use an already existing test plan file.
Start up JMeter using the jmeter.sh or jmeter.bat script and navigate to the 'test plan' element in the treeview. This treeview displays the layout of the plan, which is hierarchal.
A basic rape script will use a **Thread Group** to control the number of system processes running a set of **Samplers**, and these will report to a **Monitor**.

### Thread Groups   ###

Right click on the test plan and add a Thread Group to the plan.
A thread group has three parameters you need to worry about. Number of Threads controls how many users you'll be emulating once the plan is running at full capacity. On most computers, 250 is a good maximum, though higher spec machines with faster connections can run up to 1000. OS limitations may also apply. Ramp-Up Period is just how fast you get to the number above. 30 seconds is usually good, but if you're going for, say, 1000, spend 5 minutes ramping up. Loop Count- check the 'forever' checkbox.

### HTTP and TCP Samplers   ###

You now need to identify a target and add samplers to suit. Right click the Thread Group and add either a HTTP or TCP sampler.

#### HTTP Sampler   ####

HTTP samplers need a web server IP or address/hostname, port number (80) and a HTTP request.
You can ignore the GET/POST request setting unless you want to spam, say, a search form.
The 'Optional Tasks' panel includes an option to Retrieve All Embedded Resources from HTML Files. If you're selecting a webpage with images on and you want to get everything, images and all, check this. If not, leave it- it'll slow things up a bit.
Disable the 'Redirect Automatically' field so it'll ignore any 302 redirect instructions from the server, which is sometimes used for stopping bandwidth-based attacks.
Disable the 'Use KeepAlive' option to do more opening and closing of requests, unless you're going for BW rape rather than connect/disconnect SYN/ACK rape.

#### TCP Sampler   ####

Insert server name and IP, throw a port in, disable the 'Re-Use Connection' option, and check 'Set NoDelay'. Send some Text. Use a low, low timeout.

### Monitoring   ###

Add a 'Summary Report' pane to the plan, underneath the thread group, below the sampler.

### Running   ###

Press Run -> Start in the menus and watch the top right corner for startup info

## Distributed Testing   ##

JMeter supports distributed testing systems, and if you have a network of high-bandwidth or even smaller machines you want to combine with a singular control interface you can use this method. Pretty much just follow the docs on the JMeter website for setting this up and then use a normal testplan.

## JMeter Test Files   ##

 - paste from the website into a .jmx file (plaintext) and load into JMeter for instant blaze-of-glory attacking.

