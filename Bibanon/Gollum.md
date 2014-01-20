While it may seem like a strange choice, the Bibliotheca Anonoma uses Github's Gollum wiki engine due to it's special feature: The ability to use [Git Version Control](http://sixrevisions.com/web-development/introductory-guide-to-git-version-control-system/) to download the entire wiki and it's change history for offline view or rehosting. 

Gollum is not locked to Github. It can run as a [standalone Ruby on Rails server](), or on your own computer.

We chose to stick with Github due to it's scalable and autonomous infrastructure. Github combats spam, provides trusted authentication, and serves any amount of users at no cost; issues that have long been the Achilles' Heel of similar projects.

[More information can be found on the Gollum README.](http://github.com/github/gollum)

### Possible Successors to Github Gollum

Currently, the Bibliotheca Anonoma has become strongly associated with Github, especially on search results. Unfortunately, Gollum does have it's limitations, which hinges on the lack of plugins, Semantic Wiki, or Mediawiki-style templates.

A replacement would have to have:

* Simple wiki markup; either Markdown or Mediawiki
* Version Control support. Git strongly preferred.

Possible replacements include:

* **Private Gollum server on Openshift** - This allows us to use a modified version of Gollum with our own mods. The success of this method hinges on the creation of an independent authentication system for Gollum. It's been done before.
* [Jingo](https://npmjs.org/package/jingo) - Jingo is a Node.js webapp based on the same principles as Gollun; a Git-based repository of Markdown pages.
* Semantic Mediawiki - Good ol' Mediawiki augmented with semantic metadata databases. We would probably have use it only for a few interesting projects though, such as a copypasta database. 
* Ikiwiki - A Perl-based Git and Markdown wiki with a rich plugin ecosystem, but few compelling themes.