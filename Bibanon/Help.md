This wiki needs some help to succeed.

## URGENTLY NEEDED

### A server to host this wiki

The Bibliotheca Anonoma is "decentralized" in the sense of version control, rather than in distribution like Bittorrent.  Because [[Gittorrent]] and [[Hg-Freenet]] are not ready yet, we currently have to depend on central servers and mirrors to host the content.

If you want to make a mirror, please see [[Setup]].

## Importing data

*Things that anyone can easily do with a few basic skills and a bit of determination.*

### Fix our wiki pages

Some of our wiki pages were automatically converted from Mediawiki to [[Markdown]] in a failed attempt to make them work with ikiwiki. Unfortunately, the script we used is imperfect, and broke all the wikilinks.

So, if you see this in the source code of any page:

  [An Article](/An_Article)

It needs to be changed to this:

  [[An Article]]

(It would help a lot if someone could make a sed command or a bash script that automatically does this...)

### Help refine our history pages

If you know anything about internet history, we need you to write up some stuff [[History|here]]. Don't let our communities, websites, and glories be forgotten.

### Find more cool stuff

Got a good story, perhaps from Reddit or 4chan? Find it and put it on here.

I'm looking at RomeSweetRome, for starters.

### Turn the pictures in the [[Information Library]] into wiki pages

The [[Information Library]] is a big repository of interesting images from 4chan. The majority of them contain very useful guides inside. To make them editable and take up less space, we need to turn them into text that can be put into the wiki.

### Add more recipes to [[The Big Book of Anonymous Recipes]]

[[The Big Book of Anonymous Recipes]] is pretty big right now, but not nearly big enough. Add some good stuff to it. Like green curry. I do love my curries.

### Import these sites

Cool sites are everywhere. These are the best of them:

#### Personal Sites

* [[http://shii.org/knows/|Everything Shii Knows]] - The quintessinal Personal Wiki. Made by [[Shii]], an important force in the evolution of early 4chan, Anonymous, and anonymous forums in general.
* [[http://www.gwern.net|gwern's site]] - While we have absolutely no clue who this guy is, he is a big contributor to Wikipedia and writes very, very good articles.
* [[http://www.platypuscomix.net/|Platypus Comix]] - It's the place to go if you want to know anything about the 80s and 90s, with commentaries galore about movies, comix, and TV Shows. The author's father was obsessive in his archival of every single TV show that existed at the time. While he had gone totally bonkers, he was right, because in most cases the originals have not been well maintained.

#### Wikis

* [[http://web.archive.org/web/20080125233301/http://www.wikichan.org/index.php/Main_Page|Wikichan]] - One of the first great 4chan wikis. Was totally lost due to bad administration. Still, a majority of the best articles from there can be easily gleaned from the Internet Archive.
* [[LURKMOAR Wiki]] - The last remaining definitive wiki about early 4chan and Anonymous, with a bunch of histories of raids. It's grinding to a halt, so we need to save it fast.
* [[Tanasinn.info|http://tanasinn.info]] - A wiki for 4-ch.net's DQN, and creation of Halcy, a Wikichan and ED sysop. There's a lot of random stuff here that may or may not be useful.

#### Misc.

* [[http://www.fsmitha.com/|MacroHistory]] - Frank Smitha dumps all his knowledge about all of human history into the timelines and commentaries here. The timelines are so conclusive, important events are still being saved there to this day.

## Make the wiki better

### We need more servers and mirrors

Because for most people, it's usually easier to edit from the browser rather than within a Git repository, we need some Perl CGI servers to host our ikiwiki on.

Currently we use a static site on Github (which means no automatic update or browser edits), this is really important.

See [[Setup]] for more info on this.

## Scripts

*Some scripts that would be nice to have for the wiki.*

### [[4chan2Markdown]]

A script that would strip the fat and CSS from 4chan threads, download all the images, and convert the whole format to Markdown code, making it clean and easy to archive. It shouldn't be too hard to make.

### [[Reddit2Markdown]]

A script that would use Reddit's API to grab an entire thread and convert it to Markdown code. Should take in comment permalinks and output

## Programming

### Gittorrent/Hg-Freenet

Implementing [[Gittorrent]] or [[Hg-Freenet]] into our wiki would finally make it truly decentralized, in distribution and data management. Rather than relying on central servers, users could just clone the entire wiki's git repo with a trackerless torrent hash.

### Mediawiki Templates for Gollum

To the best of our knowledge, Gollum does not support Mediawiki-style templates. It would be a nice thing to have, as it would repost redundant portions, tag a page for fixing or other problems, and make variables that could change at any time.