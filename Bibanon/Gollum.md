gollum -- A wiki built on top of Git
====================================

## DESCRIPTION

Gollum is a simple wiki system built on top of Git that powers GitHub Wikis.

Gollum wikis are simply Git repositories that adhere to a specific format.
Gollum pages may be written in a variety of formats and can be edited in a
number of ways depending on your needs. You can edit your wiki locally:

* With your favorite text editor or IDE (changes will be visible after committing).
* With the built-in web interface.
* With the Gollum Ruby API.

Gollum follows the rules of [Semantic Versioning](http://semver.org/) and uses
[TomDoc](http://tomdoc.org/) for inline documentation.


## INSTALLATION

The best way to install Gollum is with RubyGems:

    $ [sudo] gem install gollum

If you're installing from source, you can use [Bundler][bundler] to pick up all the
gems:

    $ bundle install # ([more info](http://gembundler.com/bundle_install.html))

In order to use the various formats that Gollum supports, you will need to
separately install the necessary dependencies for each format. You only need
to install the dependencies for the formats that you plan to use.

* [ASCIIDoc](http://www.methods.co.nz/asciidoc/) -- `brew install asciidoc`
* [Creole](http://wikicreole.org/) -- `gem install creole`
* [Markdown](http://daringfireball.net/projects/markdown/) -- `gem install rdiscount`
* [Org](http://orgmode.org/) -- `gem install org-ruby`
* [Pod](http://search.cpan.org/dist/perl/pod/perlpod.pod) -- `Pod::Simple::HTML` comes with Perl >= 5.10. Lower versions should install Pod::Simple from CPAN.
* [RDoc](http://rdoc.sourceforge.net/)
* [ReStructuredText](http://docutils.sourceforge.net/rst.html) -- `easy_install docutils`
* [Textile](http://www.textism.com/tools/textile/) -- `gem install RedCloth`
* [MediaWiki](http://www.mediawiki.org/wiki/Help:Formatting) -- `gem install wikicloth`

[bundler]: http://gembundler.com/

## RUNNING

To view and edit your Gollum repository locally via the built in web
interface, simply install the Gollum gem, navigate to your repository via the
command line, and run the executable:

    $ gollum

This will start up a web server running the Gollum frontend and you can view
and edit your wiki at http://localhost:4567. To get help on the command line
utility, you can run it like so:

    $ gollum --help


## REPO STRUCTURE

A Gollum repository's contents are designed to be human editable. Page content
is written in `page files` and may be organized into directories any way you
choose. Special footers can be created in `footer files`. Other content
(images, PDFs, etc) may also be present and organized in the same way.


## PAGE FILES

Page files may be written in any format supported by
[GitHub-Markup](http://github.com/github/markup) (except roff). The
current list of formats and allowed extensions is:

* ASCIIDoc: .asciidoc
* Creole: .creole
* Markdown: .markdown, .mdown, .mkdn, .mkd, .md
* Org Mode: .org
* Pod: .pod
* RDoc: .rdoc
* ReStructuredText: .rest.txt, .rst.txt, .rest, .rst
* Textile: .textile
* MediaWiki: .mediawiki, .wiki

Gollum detects the page file format via the extension, so files must have one
of the supported extensions in order to be converted.

Page file names may contain any printable UTF-8 character except space
(U+0020) and forward slash (U+002F). If you commit a page file with any of
these characters in the name it will not be accessible via the web interface.

Even though page files may be placed in any directory, there is still only a
single namespace for page names, so all page files should have globally unique
names regardless of where they are located in the repository.

The special page file `Home.ext` (where the extension is one of the supported
formats) will be used as the entrance page to your wiki. If it is missing, an
automatically generated table of contents will be shown instead.

## SIDEBAR FILES

Sidebar files allow you to add a simple sidebar to your wiki.  Sidebar files
are named `_Sidebar.ext` where the extension is one of the supported formats.
Sidebars affect all pages in their directory and any subdirectories that do not
have a sidebar file of their own.

## FOOTER FILES

Footer files allow you to add a simple footer to your wiki. Footer files must
be named `_Footer.ext` where the extension is one of the supported formats.
Like sidebars, footers affect all pages in their directory and any
subdirectories that do not have a footer file of their own.

## SYNTAX

See [[Gollum Markup]].

## API DOCUMENTATION

The Gollum API allows you to retrieve raw or formatted wiki content from a Git
repository, write new content to the repository, and collect various meta data
about the wiki as a whole.

Initialize the Gollum::Repo object:

    # Require rubygems if necessary
    require 'rubygems'

    # Require the Gollum library
    require 'gollum'

    # Create a new Gollum::Wiki object by initializing it with the path to the
    # Git repository.
    wiki = Gollum::Wiki.new("my-gollum-repo.git")
    # => <Gollum::Wiki>

By default, internal wiki links are all absolute from the root. To specify a different base path, you can specify the `:base_path` option:

    wiki = Gollum::Wiki.new("my-gollum-repo.git", :base_path => "/wiki")

Get the latest version of the given human or canonical page name:

    page = wiki.page('page-name')
    # => <Gollum::Page>

    page.raw_data
    # => "# My wiki page"

    page.formatted_data
    # => "<h1>My wiki page</h1>"

    page.format
    # => :markdown

    vsn = page.version
    # => <Grit::Commit>

    vsn.id
    # => '3ca43e12377ea1e32ea5c9ce5992ec8bf266e3e5'

Get the footer (if any) for a given page:

    page.footer
    # => <Gollum::Page>

Get a list of versions for a given page:

    vsns = wiki.page('page-name').versions
    # => [<Grit::Commit, <Grit::Commit, <Grit::Commit>]

    vsns.first.id
    # => '3ca43e12377ea1e32ea5c9ce5992ec8bf266e3e5'

    vsns.first.authored_date
    # => Sun Mar 28 19:11:21 -0700 2010

Get a specific version of a given canonical page file:

    wiki.page('page-name', '5ec521178e0eec4dc39741a8978a2ba6616d0f0a')

Get the latest version of a given static file:

    file = wiki.file('asset.js')
    # => <Gollum::File>

    file.raw_data
    # => "alert('hello');"

    file.version
    # => <Grit::Commit>

Get a specific version of a given static file:

    wiki.file('asset.js', '5ec521178e0eec4dc39741a8978a2ba6616d0f0a')

Get an in-memory Page preview (useful for generating previews for web
interfaces):

    preview = wiki.preview_page("My Page", "# Contents", :markdown)
    preview.formatted_data
    # => "<h1>Contents</h1>"

Methods that write to the repository require a Hash of commit data that takes
the following form:

    commit = { :message => 'commit message',
               :name => 'Tom Preston-Werner',
               :email => 'tom@github.com' }

Write a new version of a page (the file will be created if it does not already
exist) and commit the change. The file will be written at the repo root.

    wiki.write_page('Page Name', :markdown, 'Page contents', commit)

Update an existing page. If the format is different than the page's current
format, the file name will be changed to reflect the new format.

    page = wiki.page('Page Name')
    wiki.update_page(page, page.name, page.format, 'Page contents', commit)

To delete a page and commit the change:

    wiki.delete_page(page, commit)


## CONTRIBUTE

If you'd like to hack on Gollum, start by forking my repo on GitHub:

http://github.com/github/gollum

To get all of the dependencies, install the gem first. The best way to get
your changes merged back into core is as follows:

1. Clone down your fork
1. Create a thoughtfully named topic branch to contain your change
1. Hack away
1. Add tests and make sure everything still passes by running `rake`
1. If you are adding new functionality, document it in the README
1. Do not change the version number, I will do that on my end
1. If necessary, rebase your commits into logical chunks, without errors
1. Push the branch up to GitHub
1. Send a pull request to the github/gollum project.

