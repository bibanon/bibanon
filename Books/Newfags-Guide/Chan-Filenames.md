## You probably never cared about this, but too bad!

Here's some fun info kids!  Well, fun for autistic kids!  OK, only fun for a very specific type of autistic kid...

4chan, 2chan, and all the others use unix timestamps for file names with three additional numbers tacked onto the end in order to avoid collisions (two threads started with the same image).  It would require a couple hundred images posted in the //same second// to break things.  I'm sure there's a little <del>genius</del> bastard that's now going to attempt to exploit it someday...

> Note: It has been brought to my attention since the first draft of this article that the last three digits may either be a checksum with a particular relation to the image OR the unix timestamp out to milliseconds.  Either possibility should not be important to you. __Talk to girls and get a life please__.

A unix timestamp (as you should all have been forced to learn from senile old college professors who wrote SysV while on cocaine in the '80s) is time measured in seconds from midnight, 1 January 1970 (with specific quirks outside the scope of this project).  Thus you can determine the posting date/time of any 4chan image (or perhaps fake one) given you have the file name (like this one I made up):  1310998213744.jpg, for instance. 

To determine the time it was posed from the filename, you'd remove the last three digits and get:  **1310998213**.  The autistic kids would do the math.  For the rest of you, I'd suggest a nice converter, say [[http://www.onlineconversion.com/unix_time.htm|the first result off of Google]].

But since this is for posterity and I'm bored at the moment: 
1310998213 = 21849970.21666667 //minutes// since 1 Jan 1970 = 364166.1702777778 //hours// since 1 Jan 1970 = 15173.59042824074 //days// since 1 Jan 1970 = 41.5714806253171 **years** since 1 Jan 1970 = 2011, .5x puts us halfway through the year, .5714 puts us in July, and all the rest puts us at 18 July 2011, sometime in the afternoon, UTC (as long as we overlook a few technical details and I choose to do this because I've already exceeded the attention span of //all// of my readers even the severely OCD ones).  Don't like my math?  Then you need a hobby!

## So what the fuck does that mean to you?
Well, this actualy means very little to you as a reasonable person.  What this means to weird obsessive creeps like myself is that every image that's posted is timed and traceable in three ways but also fucked over in //one// unique way.  As for the traceable part, it goes like this:

  - Server time from the filename
  - Adjusted by lag from to post time due to mysql @$&!^$! (if applicable, otherwise //just// lag) as logged on their side and what you see as the post time (slightly important if screenshots are involved)
  - And if you choose to save an image, then lag between when you saw it and when you saved it as recorded by //your// file system

Now for the fucked over bit:
  - Since every *chan uses this system, you cannot differentiate the source of the image unless you have a proper two-way chain of information.  It could come from //any// one of these sites (2chan, 4chan, and the other hangers-on) given you have only the final image saved on an end-user's computer.

And now you know one more thing you never needed to know!