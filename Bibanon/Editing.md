This wiki is based on Gollum, an open-source wiki built by Github, and uses a git repository with .md files to store wiki pages.

You will need a Github account to edit the wiki.

## [[Content Policy]]

We would prefer going without restrictions on what can be posted (it would be difficult to enforce anyway), but in the spirit of common decency, please follow the [[Content Policy]] while adding data to the wiki.

## Using the web interface

The web interface works just like any other wiki. Just click links to jump around, and click edit page to edit. Notice that some wikis may need accounts to be editable.

To find websites with this feature, simply check the [[Mirrorlist]].

## Manual Install

To manually download the whole wiki, just install [[Git]]. After that, run this command:

  git clone git://git@github.com/treeofsephiroth/bibanon-wiki.git bibanon

You will have a copy of the entire wiki in the "bibanon" folder.

If you want to edit through a web interface, you'll also need to set up [[Gollum]], and run it in the folder.

## Wiki markup

When you click "edit" at the top of any wiki page, you'll be sent to a page showing the wiki's source code. Rather than spitting out some html code, it gives you a text format that is easier to read, and one that you may be familiar with, along with some buttons.

On this wiki, we allow only two markup languages: [[Markdown]] and [[Mediawiki]]. Click the links to learn how to read them. Markdown is strongly recommended for new pages, while Mediawiki is only used for compatibility reasons.

## Upload Files

(TODO: There is no way to upload files through Gollum's web interface, so we will need to [[make a mod|Upload Files]] to do so. I'm guessing extension and size restrictions like with ikiwiki...)

### File Linking

Files can be easily linked to 

See [[File Links|Gollum Markup#File Links]] for more information about linking to files.

### Git

You'll need to clone the whole wiki with [[Git]] first. Then, put your files in any directory. Finally, link to it the pages where it's needed, and if it's an image, it will be displayed.

### File policy

For some reason, Gollum does not use a single namespace when dealing with files. (why pages and not files?) 

Therefore, all files must be in the same directory as the file it links to, or otherwise it won't be linked.