Ukiyo-e is a proposed wiki engine for the Bibliotheca Anonoma. It has the following goals:

* p2p distribution (perhaps using [[Gittorrent]])
* Git DVCS (or alternatively, Optomistic Replication from [[Wooki]]'s WOOT algorithm)
* Based off of or [[Gollum]]-compatible
* Cross platform
* Extensions (like ikiwiki plugins or Mediawiki templates)

## Forerunners

### Wikis

* ikiwiki - The first git-based wiki compiler, created by Joey Hess and based on Perl. Used by many free software projects, such as GNU and Debian. The Bibliotheca Anonoma wass originally designed to use this wiki.
* sputnik - a lua wiki engine that stores static files, possibly in git repositories.
* dokuwiki - another wiki similar to sputnik with static pages
* [[gollum]] - Github's git-based static file wiki engine. This is what we are currently using.

### Backends

* [[git]] - A commonly-used DVCS, allowing anyone to easily jump through the history of any file inside the repository. It also forks
* [[gittorrent]] - A possible extension to the Git DVCS that would end it's current dependency on central servers on the internet, and make it fully distributed using p2p methodologies. If made, Gittorrent could have implications beyond software versioning; it might just change the whole way we work with websites and software projects. 
* [[Hg-Freenet]] - A working project similar to [[gittorrent]], except that it uses Mercurial and Freenet. Users can clone and push mercurial repos anonymously through the Freenet network, where those repos are spread across the hard disks of it's nodes.

### Research on implications

The creation of a distributed wiki, website, or even a p2p DVCS could have massive implications on how we work on the internet. These papers explore the effects such innovations could have on internet decentralization, anonymous collaboration, and cryptoanarchy.

* [[Gittorrent]] - The article for Gittorrnet
