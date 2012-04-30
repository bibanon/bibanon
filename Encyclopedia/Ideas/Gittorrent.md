Gittorrent is a proposal for making Git truly distributed by combining the p2p distribution of Bittorrent, the DVCS of Git, and the trust circle of GPG together. 

> The implications of a truly distributed revision control system are
> truly staggering: unrestricted software freedom; the playing field is
> levelled in so many ways, as "the web site" no longer becomes the
> central choke-point of control. This article will explain more fully
> some of these implications, not only from a technical perspective but
> also including the political implications for Software Freedom.

While there hasn't been much going on with the project, they've made complete [[design|Gittorrent_Design]] and [[protocol|Gittorrent_Protocol]] specifications for anyone that feels like making it tangible. They also have also made a basic implementation of it called [[MirrorSync]].

# [GitTorrent, The Movie](http://www.advogato.org/article/994.html)

- Written by [lkcl](http://www.advogato.org/person/lkcl/) on [advogato](http://www.advogato.org/article/994.html).

[Git](http://en.wikipedia.org/wiki/Git_(software)) promises to be a
distributed software management tool, where a repository *can* be
distributed. Yet, the mechanisms used to date to actually "distribute",
such as rsync, http and ssh, are very much "single path" and
centralised.

[GitTorrent](http://code.google.com/p/gittorrent/) makes Git *truly*
distributed. The initial plans are for reducing mirror loading, however
the full plans include totally distributed development: no central
mirrors whatsoever. PGP signing and other web-of-trust-based mechanisms
will take over from protocols on ports (e.g. ssh) as the access control
"clearing house".

## What is GitTorrent?

From the [gittorrent page](http://code.google.com/p/gittorrent/): *The
[[GitTorrent_Protocol]] (GTP) is a protocol for collaborative git repository
distribution across the Internet.*

Straight from the homepage, as it's put so succinctly:

> GitTorrent is a first step towards applying decentralizing Peer to
> Peer concepts to Git. If you decentralize the download layer, it's
> just another small step before you decentralize the push rights and
> tie it to a web of trust such as PGP, and then you don't actually need
> discrete mirror sites. Every mirror can track the git repositories the
> owners want it to carry, and those authorized to sign updates can make
> signed updates to push the cloud forward. Your local mirror can become
> a one-stop git push and pull stop depot, and the source code is
> preserved in many more places, increasing resilience, availability and
> download performance for all.

(`Hurrah. Wouldn't it be nice if money and real goods could be
 exchanged and distributed as easily, we'd be living in paradise...`)

## Why is GitTorrent so important?

The possibilities that GitTorrent opens up are just mind-blowing. Here
are a few:

-   Imagine that an entire project - its web site, documentation, wiki,
    bug-tracker, source code and binaries are all managed and stored in
    a peer-to-peer distributed git repository.
    -   To view the web site, you either go to the main site,
        http://web-site.org, or, if you are offline or want faster
        access, you go to the locally checked out copy.
    -   To read the documentation, you likewise either go to the main
        site or you go the locally checked out copy.
    -   To contribute to the wiki, you either go the main web site, or
        you edit the local pages and git push them to the cloud.
    -   To report a bug, you either go to the main web site, or you run
        your own local web server that duplicates the bug database, and,
        once you've reported it, the submit ends up with the bugreport
        being in the locally checked out git repository which, on a
        push, gets uploaded into the cloud - and ends up on the main web
        site.
    -   To contribute to the project's source, you already understand
        that you do local edits and then git push them.
    -   To upgrade to the latest release, you do a git checkout (of the
        binaries). They're digitally signed; they're pulled not from "a
        mirror", they're pulled from gittorrent peers. Only the
        components that you don't already have will be pulled.
        Documentation need not be separately included with the binary
        distribution because that can already be obtained direct from
        the source repository.

-   Imagine that you want to fork a project, but you feel intimidated
    doing so because of the "centralisation". You have no control over
    the "central web site".
    -   With GitTorrent-distributed projects, there *is* no "central"
        web site: the PGP keys are far more important.
    -   Abandoned projects can easily be revived, through a simple
        process of a new developer announcing their PGP public key
        identity, and for Users to start pulling in code that's tagged
        with that PGP key.
    -   Users will be able to decide whom to trust based on who
        contributes, not on who controls the project's web site.

-   Imagine what would happen if you made a git-based filesystem on top
    of a distributed GitTracker repository, and a Linux Distribution was
    actually placed into the Git Repository.
    -   In combination with automount, there would be no more
        "downloading" and "installing" you would simply endeavour to run
        an application and, on finding that the application did not
        exist, the git-based filesystem would automatically go hunting,
        through the GPG-Digitally-signed peer-to-peer cloud, looking for
        the binary.
    -   Upgrades would be a matter of "git checkout -b debian-testing;
        git pull"

Here's the very strange thing about all of these idea: they are not new;
they are all in development, or exist in one form or another - they just
haven't been tied in behind GitTorrent. yet.

## GPG-signed distributed distribution

[git tag](http://www.kernel.org/pub/software/scm/git/docs/git-tag.html)
provides the means to digitally-sign a release. It's therefore possible
to make GitTorrent aware of this by specifying whose GPG keys you trust,
as part of the "pull" process.
[update-hook](http://jonas.nitro.dk/gittorrent/tracker/update-hook) in
[tracker](http://jonas.nitro.dk/gittorrent/tracker/) shows the principle
(using the cogito command, cg tag).

## Keynote for advanced trust infrastructure management

[KeyNote](http://www1.cs.columbia.edu/~angelos/keynote.html), aka
RFC2704, allows access control rules to be digitally signed. Integration
of KeyNote into git would provide a formal language for pulling git
repositories from people that you trust - or, specifically from groups
of people that are trusted.

GPG signatures go onto git tags in an RFC922-compliant fashion: there
can thus be multiple such signatures: the initial person who created the
patch; the lieutenant who signed it off; Linus himself; the Distribution
maintainer and finally the package maintainer. At each stage, the use of
a KeyNote formally-specified "gateway", written into a file that itself
is digitally signed, is an automated double-check on where the source
code, the wiki content, the bug and the binaries will end up being
pulled or pushed, across the cloud.

The alternative is to have shell-scripts, as git hooks, that hard-code
the people who must GPG sign a tag before it can be distributed: that
just gets messy, and it should be clear that KeyNote is a much better
tool for the job.

## Distributed Wiki

[IkiWiki](http://ikiwiki.info/rcs/git/) is a Wiki where the original
wiki content is stored in a repository, and, in the case of git, hooks
can be executed to turn the wiki pages into HTML. That's all very
well-known.

What happens when GitTorrent is thrown into the mix is very exciting:
Wiki-based documentation becomes decentralised. Imagine if Wikipedia
could be mirrored locally, run on a *local* mirror, where content was
pushed and pulled, GPG-Digitally-signed; content shared via peer-to-peer
instead of overloading the Wikipedia servers.

## Distributed Bugtracker

[dist-bugs](http://dist-bugs.kitenet.net/) is a project to design a
worldwide globally-useable format (strictly: microformat) for bug
tracking. The underlying transport is *not* part of the specification,
as the microformat is generic enough to be transferred over anything.

Imagine dist-bugs being stored in a GitTorrent-backed distributed wiki
or other web server. In this way, the bug database could be used for
offline work as well as online work. And, thanks to the combination of
dist-bugs and GitTorrent, bugs would be world-wide globally unique,
GPG-Digitally-signed, version-trackable (one distro has the bug listed
as fixed and another independent linux distro has it as still open) -
it's just an incredibly powerful combination.

## Distributed Linux Distribution

[vcs-pkg](http://vcs-pkg.org/) has as its goal:

> The aim of the vcs-pkg project is to investigate the use of version
> control for distro package maintenance. We bring together people
> interested in taking the next step in distro package maintenance: the
> proper integration of version control into the package maintenance
> workflow.

An earlier advogato article, [Distributed Debian Distribution
Development](http://advogato.org/article/972.html) discusses how
debian's packages can be peer-to-peer distributed, and vcs-pkg is a
generalisation of the issues involved.

It goes without saying that the binary distribution is not the only part
that needs to be distributed, but it is a big part of the picture.

Whilst DDDD advocated that projects such as debtorrent and
[apt-p2p](http://www.camrdale.org/apt-p2p/) would help with debian
binary package distribution, vcs-pkg with GitTorrent as the underlying
transport would be much more powerful, as it would allow *anyone* to
create their own Linux - or FreeBSD - or other software - distribution,
based on top of existing packages.

## Branching a distribution: git checkout -b ubuntu-8.1-custom

Suddenly, creating a major overnight runaway successful distribution no
longer needs the resources of a corporate-backed RedHat or even the
charity-backed Debian: anyone could start a distribution themselves, and
it would automatically be peer-to-peer replicated.

If the GitTorrent-backed Debian Distribution concept had existed at the
time, ubuntu would not need to have forked and copied the entire debian
codebase / repository at the time. Debian users who wanted to try out
Ubuntu could have done so with a single command such as "git checkout -b
ubuntu".

## Root-mounted Git Filesystem

[GitFS](http://www.sfgoth.com/~mitch/linux/gitfs/) is a FUSE (File
System in User Space) plugin that allows a Git repository to be accessed
as a mounted filesystem. Although it is read-only at present, that is
*more* than enough for the required purpose.

Imagine running an entire Linux (or FreeBSD) distribution off of a
GPG-digitally signed GitTorrent peer-to-peer distributed binary
repository. That's a long sentence with a hell of a lot of buzzwords.
The implications are that there would no longer need to be binary
mirrors, and, as long as one person in the swarm still has an
application that's needed locally, everyone else can automatically get
it, too.

## Distributed automated Backups

Many developers check their home directory into a git repository, using
it as a backup mechanism. Imagine what then happens when GitTorrent is
added to the mix: a group of developers could set up a peering
arrangement where they make automated distributed backups of each
others' computers.

An entirely old business model becomes new and easy: providing backups
for linux n00bs and linux gurus alike becomes a matter of doing regular
git pulls onto Amazon EC2 cloud machines...

## Political and Free Software Freedom implications

It's worth explicitly spelling out the significance of the use of
GitTorrent for Free Software development, as outlined above.

-   **Freedom from political interference**. A government or an
    organisation decides that it doesn't want free software to be used,
    as it undermines their ability to exert "control". By going fully
    distributed, the only way for a government or an organisation -
    covert or otherwise - to exert any influence or "control" is, just
    like anyone else, through the GPG-digitally-signed web of trust
    (such as the Debian one). In this way, the only influences that can
    be exerted are publically accountable influences. Democracy with
    mathematically backed teeth.
-   **Freedom from project maintainer manipulation**. If a project
    maintainer becomes manipulative or is manipulated, to exert a
    negative influence on a project, users can simply shunt them aside,
    by setting up a new list of GPG keys from whom they will trust to
    receive patches and updates. Even the web site content can be
    forked. The only thing that *can't* be forked is the web site domain
    name - *but*, as has been [mentioned
    previously](http://advogato.org/article/919.html), [distributed peer
    to peer
    dns](http://www.google.co.uk/search?hl=en&q=distributed+peer+to+peer+dns)
    takes care even of that. There's even [an
    implementation](http://distributeddns.sourceforge.net/) of a
    distributed dns system.
-   **Freedom for Governments to fork entire distributions**. Many
    governments - especially those in emerging markets and the third
    world - find it difficult to adopt a particular linux distribution,
    on the basis that they find the corporate sponsors (Redhat, Novell)
    distasteful and untrustworthy. Whilst some free software developers
    may find this to be upsetting, being upset about it doesn't make the
    problem go away. However, allowing a country to fork an entire
    distribution *does* make the problem go away, as it allows that
    country - that government - to issue their own GPG keys for their
    own distribution. The other nice thing is that their contributions
    *should* (unless special effort is made to ensure that they don't)
    automatically find their way back into the GitTorrent cloud,
    digitally-signed and easily identifiable, just like everyone else's.
-   **Freedom from resource limitations**. As the entire free software
    development process - documentation, ideas, source, bugs and
    binaries - is distributed, suddenly the only limitation on the
    distribution and deployment on a useful idea is ... well... it's
    hard to think of one. Even network bandwidth should not be a
    problem, as entire repositories could be git-cloned onto CDs, DVDs
    or memory sticks and communicated by postal service to a location
    with better bandwidth.
-   **Freedom from SPAM**. With the entire infrastructure GPG signed,
    the possibility of individuals posting GPG-signed SPAM becomes...
    somewhat moot. If it were to happen (to an otherwise trusted user),
    it would indicate that a user's computer had been compromised, and
    that they were stupid enough to not keep their GPG private key
    physically separated (USB key) from their computer. Slapped wrists
    all round, but nothing *remotely* like the present situation.

## Flies in the ointment

Here is a list of technical challenges that need to be overcome - to get
from here to there:

-   GitTorrent needs attention - and time and money are the ways to do
    that!
-   Git tagging in a single git repository is a "global" operation. For
    GitTorrent to work as a binary distribution mechanism, as things
    stand at present there are a couple of options.
    -   One is to split packages down into separate git repositories -
        one GitTorrent repository per package, and then have a "top
        level" git which lists the seeds/trackers from which individual
        packages can be found. In "debian / apt" terminology, there
        would be one git repository containing Releases.gz and
        Packages.gz etc.
    -   Another option is for git itself to be enhanced so that it can
        "tag" *portions* of a tree, not the entire tree.

-   dist-bugs is a protocol with (as best can be determined) no released
    implementation, as of yet. However, there are some perfectly good
    distributed bug tracking systems - all of which can use git:
    -   [distract](http://www.distract.wellquite.org/)
    -   [ditrack](http://ditrack.org/)
    -   [ditz](http://ditz.rubyforge.org/)

-   GitTorrent - and BitTorrent - do not have "search" mechanisms,
    unlike eMule and mlDonkey. the eMule protocol provides a DHT-based
    search mechanism as part of the peer-to-peer distribution:
    bittorrent completely lacks such mechanisms, and so searching
    through packages or source code would require downloading of the
    entire codebase or package base (somewhere). This *has* to be
    properly addressed, by augmenting GitTorrent. Versions of BitTorrent
    from [bittorrent.com](http://bittorrent.com) have been enhanced, as
    can be seen in the [full source
    code](http://download.bittorrent.com/dl/), to include a DHT search
    algorithm.

## Conclusion

From a simple, simple project that is suffering from an inexplicable
near complete lack of attention from the free software community comes a
revolutionary change in the way that free software is developed and
distributed. [A previous article](http://advogato.org/article/972.html)
made it clear the scale of the issues that just Debian on its own faces,
and if Linux ever takes off from its current market share to mainstream,
much of the infrastructure that's currently taken for granted is going
to collapse.

GitTorrent isn't a complete panacea; it isn't a completely utopian
idealistic piece of non-existent airhead software, either, because it's
*real*. It's been developed "because it can be". It's just that the
implications of its deployment really haven't been fully uncovered.
Those that have been discussed here are pretty monumental.

Piece by piece, free software is inexorably getting its act together.
[GitTorrent](http://code.google.com/p/gittorrent/) is just another bit
of the puzzle...

## Sources

* [Gittorrent, the Movie](http://www.advogato.org/article/994.html)
* [Gittorrent Project on Google Code](https://code.google.com/p/gittorrent/)
* [Jonas Fonesca's Gittorrent Design Specification](https://gittorrent.googlecode.com/files/Fonseca-2006.pdf)
* [Gittorrent Protocol Specification](http://jonas.nitro.dk/gittorrent/rfc.html)