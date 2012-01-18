[[!meta title="Help"]]

This wiki needs some help to succeed.

## URGENTLY NEEDED

### A server to host this wiki

Sometimes, people just want to click a button in their browser to make a quick edit, rather than having to load up [[Slitaz|Bibanon_SDK]] or learn to use [[Git]]. If someone could host this wiki, we would be 

## Importing data

*Things that anyone can easily do with a few basic skills and a bit of determination.*

### Fix our wiki pages

Some of our wiki pages were automatically converted from Mediawiki to [[Markdown]]. Unfortunately, [[the_script_that_we_used|Mediawiki2Markdown]] cannot convert wikilinks or tags (Categories in Mediawiki).

So, if you see this in the source code of any page:

  [An Article](/An_Article)

It needs to be changed to this:

  [[An_Article]]

(It would help a lot if someone could make a sed command or a bash script that automatically does this...)

### Help refine our history pages

If you know anything about internet history, we need you to write up some stuff [[here|Encyclopedia_Anonoma]]. Don't let our communities, websites, and glories be forgotten.

### Find more cool stuff

Got a good story, perhaps from Reddit or 4chan? Find it and put it on here.

I'm looking at RomeSweetRome, for starters.

### Turn the pictures in the [[Information_Library]] into wiki pages

The [[Information_Library]] is a big repository of interesting images from 4chan. The majority of them contain very useful guides inside. To make them editable and take up less space, we need to turn them into text that can be put into the wiki.

### Add more recipes to [[The_Big_Book_of_Anonymous_Recipes]]

[[The_Big_Book_of_Anonymous_Recipes]] is pretty big right now, but not nearly big enough. Add some good stuff to it. Like green curry. I do love my curries.

### Import these sites

Cool sites are everywhere. These are the best of them:

#### Personal Sites

* [[Everything Shii Knows|http://shii.org/knows/]] - The quintessinal Personal Wiki. Made by [[Shii]], an important force in the evolution of early 4chan, Anonymous, and anonymous forums in general.
* [[gwern's site|http://www.gwern.net]] - While we have absolutely no clue who this guy is, he is a big contributor to Wikipedia and writes very, very good articles.
* [[Platypus Comix|http://www.platypuscomix.net/]] - It's the place to go if you want to know anything about the 80s and 90s, with commentaries galore about movies, comix, and TV Shows. The author's father was obsessive in his archival of every single TV show that existed at the time. While he had gone totally bonkers, he was right, because in most cases the originals have not been well maintained.

#### Wikis

* [[Wikichan|http://web.archive.org/web/20080125233301/http://www.wikichan.org/index.php/Main_Page]] - One of the first great 4chan wikis. Was totally lost due to bad administration. Still, a majority of the best articles from there can be easily gleaned from the Internet Archive.
* [[LURKMOAR_Wiki|]] - The last remaining definitive wiki about early 4chan and Anonymous, with a bunch of histories of raids. It's grinding to a halt, so we need to save it fast.
* [[Tanasinn.info|http://tanasinn.info]] - A wiki for 4-ch.net's DQN, and a creation of Halcy, a Wikichan and ED sysop. There's a lot of random stuff here that may or may not be useful.

#### Misc.

* [[MacroHistory|http://www.fsmitha.com/]] - Frank Smitha dumps all his knowledge about all of human history into the timelines and commentaries here. The timelines are so conclusive, important events are still being saved there to this day.

## Make the wiki better

### We need more servers and mirrors

Because for most people, it's usually easier to edit from the browser rather than within a Git repository, we need some Perl CGI servers to host our ikiwiki on.

Currently we use a static site on Github (which means no automatic update or browser edits), this is really important.

See [[Setup]] for more info on this.

### Better CSS and page templates

We basically just took the CSS from the [Tails Website](http://tails.boum.org) and changed the name. While it's a massive improvement over This format leaves much to be desired:

* There's not enough space for the articles. The sidebar, as you can plainly see, eats up a third of the article area. We need to at least move the sidebar to the margins in the side.
* The settings (Edit, RecentChanges, History, etc) hide themselves automatically. Because we're supposed to be a community-editable wiki, we need to disable that feature so that it's clear that this is fully editable.
* There's a lot of stuff in the CSS that we don't need.

### We need our own logo on the banner

[[logo-7.png]]

This is what the TAILS banner logo looks like. We want our own, though.

The logo's size must be 980x192, and it should not include the text (it's already inserted by the banner).

## Programming

*Advanced stuff that would be nice to have.*

### Portable Ikiwiki



* [[tools/Retext-Ikiwiki]] - This is a PyQt markdown reader that is able to make instant previews of text files. This will be useful for people who want to read and edit the source wiki on their USB drives.

Since ikiwiki has little chance of ever working on Windows, we will need to mod this reader to parse the Ikiwiki Markdown dialect, and extend it to resolve wikilinks, display inlined pages, and possibly implement some wiki features inside it.

### A better Mediawiki to Ikiwiki importer

