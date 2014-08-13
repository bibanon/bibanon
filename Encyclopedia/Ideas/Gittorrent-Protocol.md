This protocol specification was written by Jonas Fonseca. The original can be retrieved [here](http://jonas.nitro.dk/gittorrent/rfc.html).

### Abstract

This document describes the GitTorrent Protocol version 1.0 referred to
as "GTP/1.0". The GitTorrent Protocol (GTP) is a protocol for
collaborative git repository distribution across the Internet. It is
best classified as a peer-to-peer (P2P) protocol, although it also
contains highly centralized elements.

Git is a decentralized version control system (VCS) created in the
begining of 2005 by Linus Torvalds. To date only client-server based
distribution has been supported. Although git is able to densly exchange
updates between repositories and thereby minimize the overall resource
requirements for distributing git repositories distribution will
occationally involve clients cloning a complete repository. This poses
much strain on sites hosting many git repositories in terms of
request-processing and sheer bandwidth. It is the goal of GTP to
facilitate such hosting services in reducing resource demands.

Normally a client does not use their upload capacity while downloading a
repository. The GTP approach The GTP approach capitalizes on this fact
by having clients upload bits of the repository data to each other. In
comparison to the original client-server distribution this adds huge
scalability and cost-management advantages.

\

* * * * *

### Table of Contents

[1.](#anchor1) Introduction\
 [1.1](#anchor2) Audience\
 [1.2](#anchor3) Terminology\
 [1.3](#anchor5) Overall Operation\
 [2.](#anchor6) Bencoding \
 [2.1](#anchor7) Scalar Types\
 [2.2](#anchor8) Compound Types\
 [3.](#peers) Discovering Peers\
 [4.](#references) Repository References\
 [5.](#anchor9) Objects and Blocks\
 [5.1](#anchor10) Objects\
 [5.2](#anchor11) Blocks\
 [6.](#anchor12) The Metainfo File\
 [6.1](#anchor13) The Structure of the Metainfo File\
 [7.](#anchor14) The Tracker HTTP Protocol\
 [7.1](#anchor15) Request\
 [7.2](#anchor16) Response\
 [8.](#anchor17) The Peer Wire Protocol\
 [8.1](#peer-wire-guidelines) Peer Wire Guidelines\
 [8.2](#anchor18) Handshaking\
 [8.3](#anchor19) Message Communication\
 [8.3.1](#anchor20) Peer States\
 [8.4](#anchor21) Peer Wire Messages\
 [8.5](#anchor22) State-oriented Messages\
 [8.5.1](#anchor23) Choke\
 [8.5.2](#anchor24) Unchoke\
 [8.5.3](#anchor25) Interested\
 [8.5.4](#anchor26) Uninterested\
 [8.5.5](#anchor27) Peers\
 [8.5.6](#anchor28) References\
 [8.5.7](#anchor29) Packs\
 [8.5.8](#anchor30) Index\
 [8.6](#anchor31) Data-oriented Messages\
 [8.6.1](#anchor32) Request\
 [8.6.2](#anchor33) Block\
 [8.6.3](#anchor34) Cancel\
 [8.7](#anchor35) The End Game\
 [8.8](#anchor36) Object Selection Strategy\
 [8.9](#peer-selection-strategy) Peer Selection Strategy\
 [9.](#security-considerations) Security Consideration\
 [9.1](#anchor37) Tracker HTTP Protocol Issues\
 [9.2](#anchor38) Denial of Service Attacks on Trackers\
 [9.3](#anchor39) Peer Identity Issues\
 [9.4](#anchor40) DNS Spoofing\
 [9.5](#anchor41) Issues with File and Directory Names\
 [9.6](#anchor42) Validating the Integrity of Data Exchanged Between
Peers\
 [9.7](#anchor43) Transfer of Sensitive Information\
 [10.](#IANA) IANA Considerations\
 [11.](#rfc.references1) References\
 [§](#rfc.authors) Author's Address\

\
 \

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 1. Introduction

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC 2119Bradner, S., Key
words for use in RFCs to Indicate Requirement Levels, March
1997.](#RFC2119)[3].

The existing distribution protocols provides secure and reliable
transmission of large git repositories over the Internet. However, its
highly centralized client-server approach also means, it is inadequate
for mass publication of files, where a single point may expect to be
requested by a critically large number of clients simultaneously. To
remedy this situation many organizations either implement a cap on the
number of simultaneous requests, or spread the load on multiple mirror
servers. Needless to say both approaches have their drawbacks, and a
solution that addresses these problems is highly needed.

The approach in GitTorrent Protocol (GTP) is to spread the load not on
mirror servers, but to the clients themselves by having them upload bits
of the file to each other while downloading it. Since the clients
usually do not utilize their upload capacity while fetching a file, this
approach does not put the clients in any disadvantage. This has the
added advantage that even small organizations with limited resources can
publish large files on the Internet without having to invest in costly
infrastructure.

#### 1.1 Audience

This document is aimed at developers who wish to implement GTP for a
particular platform. Also, system administrators and architects may use
this document to fully understand the implications of installing an
implementation of GTP. In particular, it is advised to study the
security implications in more detail, before installing an
implementation on a machine that also contains sensitive data. Security
implications are discussed in [Section 9Security
Consideration](#security-considerations).

It is assumed that the developers are familiar with the layout of the
git repository and the design of the object store. This includes the use
of pack files and how to validate signed tag objects.

#### 1.2 Terminology

> Peer:
>   ~ A peer is a node in a network participating in repository sharing.
>     It can simultaneously act both as a server and a client to other
>     nodes on the network.
> Neighboring peers:
>   ~ Peers to which a client has an active point to point TCP
>     connection.
> Client:
>   ~ A client is a user agent (UA) that acts as a peer on behalf of a
>     user.
> Torrent:
>   ~ A torrent is the term for the group of branches the client is
>     downloading.
> Swarm:
>   ~ A network of peers that actively operate on a given torrent.
> Seeder:
>   ~ A peer that has a complete copy of a torrent.
> Tracker:
>   ~ A tracker is a centralized server that holds information about one
>     or more torrents and associated swarms. It functions as a gateway
>     for peers into a swarm.
> Metainfo file:
>   ~ A text file that holds information about the torrent, e.g. the URL
>     of the tracker. It usually has the extension .gittorrent.
> Peer ID:
>   ~ A 20-byte string that identifies the peer. How the peer ID is
>     obtained is outside the scope of this document, but a peer must
>     make sure that the peer ID it uses has a very high probability of
>     being unique in the swarm.
> Repo hash:
>   ~ A SHA1 hash that uniquely identifies the torrent. It is calculated
>     from data in the metainfo file.

#### 1.3 Overall Operation

GTP consists of two logically distinct protocols, namely the Tracker
HTTP Protocol (THP), and the Peer Wire Protocol (PWP). THP defines a
method for contacting a tracker for the purposes of joining a swarm,
reporting progress etc. PWP defines a mechanism for communication
between peers, and is thus responsible for carrying out the actual
download and upload of the torrent.

In order for a client to download a torrent the following steps must be
carried through:

1.  A metainfo file must be retrieved.
2.  Instructions that will allow the client to contact other peers must
    be periodically requested from the tracker using THP.
3.  The torrent must be downloaded by connecting to peers in the swarm
    and trading objects using PWP. \
     \

To publish a torrent the following steps must be taken:

1.  A tracker must be set up.
2.  A metainfo file pointing to the tracker and containing information
    on the structure of the torrent must be produced and published.
3.  At least one seeder with access to the complete torrent must be set
    up.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 2. Bencoding

Bencoding encodes data in a platform independent way. In GTP/1.0 the
metainfo file and all responses from the tracker are encoded in the
bencoding format. The format specifies two scalar types (integers and
strings) and two compound types (lists and dictionaries).

The [Augmented BNF syntaxCrocker, D., Ed. and P. Overell, Augmented BNF
for Syntax Specifications: ABNF, November 1997.](#RFC2234)[5] for
bencoding format is:

       dictionary = "d" 1*(string anytype) "e" ; non-empty dictionary
       list       = "l" 1*anytype "e"          ; non-empty list
       integer    = "i" signumber "e" 
       string     = number ":" <number long sequence of any CHAR>
       anytype    = dictionary / list / integer / string
       signumber  = "-" number / number
       number     = 1*DIGIT
       CHAR       = %x00-FF                    ; any 8-bit character
       DIGIT      = "0" / "1" / "2" / "3" / "4" /
                    "5" / "6" / "7" / "8" / "9"

#### 2.1 Scalar Types

Integers are encoded by prefixing a string containing the base ten
representation of the integer with the letter "i" and postfixing it with
the letter "e". E.g. the integer 123 is encoded as i123e.

Strings are encoded by prefixing the string content with the length of
the string followed by a colon. E.g. the string "announce" is encoded as
"8:announce".

#### 2.2 Compound Types

The compound types provides a mean to structure elements of any
bencoding type.

Lists are an arbitrary number of bencoded elements prefixed with the
letter "l" and postfixed with the letter "e". It follows that lists can
contain nested lists and dictionaries. For instance "li2e3:fooe" defines
a list containing the integer "2" and the string "foo".

Dictionaries are an arbitrary number of key/value pairs delimited by the
letter "d" at the beginning and the letter "e" at the end. All keys are
bencoded strings while the associated value can be any bencoded element.
E.g. "d5:monthi4e4:name5:aprile" defines a dictionary holding the
associations: "month" =\> "4" and "name" =\> "april". All dictionary
keys MUST be sorted alphabetically.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 3. Discovering Peers

Two methods exist for discovering other peers in the swarm. Either peer
information can be requested from the tracker, or it can be requested
from a neighboring peer. A tracker can be used as the initial method for
seeding the peer's list of other peers in the swarm, after which the
peer should prefer to discover peers through its neighboring peer to
reduce resource demands on the tracker.

A peer should continously discover new peers while it is connected to
the swarm to find peers that provide better download rates than its
current neightboring peers. Peer rating and selection is discussed in
[Section 8.9Peer Selection Strategy](#peer-selection-strategy).
Periodically connecting to new peers ill also be ensured that updates
are distributed through-out the swarm faster.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 4. Repository References

New tags and branch updates are announced using reference lists, that
contain information about what git commit SHA-1 each branch is at and
the name and SHA-1 of available tags. The reference list enables a peer
to know which revision history to trust and consequently which objects
to request. Since references may be distributed using both THP and PWP,
trust is ensured by requiring that all reference information distributed
in the swarm is signed so that the peer may verify the signature using a
public key available in the metainfo file.

Repository references are distributed in a signed tag object. Each new
repository reference tag should refer to its successor to indicate the
relation between a newer and older reference object. However, when a
peer does not have all reference objects it should should use the
creation date indicated in the tag object to infer a relation between
two reference objects. How to verify the signed git tag is beyond the
scope of this document.

The format of data embedded in the tag object is the same as the format
of the .git/info/refs file. It is line-oriented, where each line
contains a SHA-1 and reference name separated by a tab. Details on how
peers should interpret the reference names are beyond the scope of this
document. Following is an example:

    bd562ca1ef05b91e6dbcddf3ace0c897ef76567e    HEAD
    bd562ca1ef05b91e6dbcddf3ace0c897ef76567e    refs/heads/master
    bd562ca1ef05b91e6dbcddf3ace0c897ef76567e    refs/heads/origin
    7113a59591aab60f979c6993bffa4cdd66236fdf    refs/tags/initial
    8dec84bb6b5eb7eb8831582dfd7ebbadb0403474    refs/tags/initial^{}
    8567d6dfb446364b823190b9e6c988f0ba72e1ba    refs/tags/review-0.1
    bdb69c0458215a761d5ae36c143a8b37cf20e103    refs/tags/review-0.1^{}
    f41e03ffa9b0d46f466bb73408c7562e49fcb435    refs/tags/review-0.2
    094308b52456b21dd00988f5fc3ee3e5cb1d5a75    refs/tags/review-0.2^{}

The references object may be partial in that not all tags or branches
are listed in it. The entity in charge of signing the references objects
must make decisions regarding how to best distribute the repository
references. For repositories with many branches or tags it may be
necessary to split up the list of references so as not to require big
objects to be exchanged over the wire. The same applies for repositories
with frequent updates, in that partial and smaller reference lists can
help to reduce the overhead of of exchanging many reference objects.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 5. Objects and Blocks

This section describes how a torrent is organized in objects, and
blocks. The torrent is divided into one or more objects. Each object is
named using a SHA-1 hash which allows the peer to verify the contents of
a single object. Using the repository references as the starting point
and walking all downloaded objects according to the git object hierarchy
the peer is able to verify the complete object store. When distributing
data over PWP objects are divided into one or more blocks.

#### 5.1 Objects

An object is either a single git object or a group of git objects
compressed into a pack object. All objects are uniquely identified by a
SHA-1, derived from the object content. Pack objects are special in that
they are accompanied by an index object listing the git objects in the
pack. Peers can exchange information about what objects they have by
first requesting the list of pack objects a neighboring peer makes
available and afterwards requesting the index files for each pack.
Although git objects may be distributed one by one, it is recommended
that peers primarily use packs for downloading to improve overall
bandwidth utilization.

The size of the individual pack objects is implementation depend. As a
guideline a peer should not provide packs with a size that is greater
than the resulting pack index object can be sent in its entirety over
the wire. Also, git objects may be packed in a variety of different
packs resulting in the peer having many different possible overlapping
packs depending on how the download history of the peer. This reduces
changes that a pack object will be available from multiple peers.
Keeping the size of the pack objects down ensures that a peer will have
a greater change at being able to both request and complete the download
of the pack from one neighboring peer.

#### 5.2 Blocks

The size of a block is an implementation defined value that is not
dependant on the fixed piece size. Once a fixed size is defined, the
number of blocks per objects can be calculated using the formula:

            number_of_blocks = (object_size / fixed_block_size)
                             + !!(object_size % fixed_block_size)

where "%" denotes the modulus operator, and "!" the negation operator.
The negation operator is used to ensure that the last factor only adds a
value of 0 or 1 to the sum. Given the start offset of the block its
index within a piece can be calculated using the formula:

            block_index = block_offset % fixed_block_size

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 6. The Metainfo File

The metainfo file provides the client with information on the tracker
location as well as the torrent to be downloaded. Besides listing which
branches will result from downloading the torrent, it also provides the
client with a mean to verify branches.

In order for a client to recognize the metainfo file it SHOULD have the
extension .gittorrent and the associated the media type
"application/x-gitttorrent". How the client retrieves the metainfo file
is beyond the scope of this document, however, the most user-friendly
approach is for a client to find the file on a web page, click on it,
and start the download immediately. This way, the apparent complexity of
GTP as opposed to FTP or HTTP transfer is transparent to the user.

#### 6.1 The Structure of the Metainfo File

The metainfo file contains a bencoded dictionary with the following
structure. A key below is REQUIRED unless otherwise noted.

> 'comment':
>   ~ This is an OPTIONAL string value that may contain any comment by
>     the author of the torrent.
> 'created by':
>   ~ This is an optional string value and may contain the name and
>     version of the program used to create the metainfo file.
> 'creation date':
>   ~ This is an OPTIONAL string value. It contains the creation time of
>     the torrent in standard Unix epoch format.
> 'pubkey':
>   ~ This is a string value. It must contain the public key that is
>     used by GTP/1.0 to verify each update to a branch head.
> 'repo':
>   ~ This is a list containing a description of each branch offered in
>     the torrent.
>
>     > 'branches':
>     >   ~ This key points to a dictionary that contains information
>     >     about the branches to download.
>     >
>     >     > 'name':
>     >     >   ~ This is a string value. It contains the name of the
>     >     >     branch.
>     >     > 'pubkey':
>     >     >   ~ This is an OPTIONAL string value. It must contain the
>     >     >     public key that is used by GTP/1.0 to verify each
>     >     >     update to a branch head. If no key is supplied the
>     >     >     global "pubkey" value will be used for verification
>     >     >     branch updates.
>     >     > 'alternatives':
>     >     >   ~ This is an OPTIONAL list of string value. It may
>     >     >     contain repo hashes for repositories that can be used
>     >     >     as an alternative object source for this branch. This
>     >     >     tells clients when the object store of a repository
>     >     >     can be shared between different torrents.
>     >
>     > 'description':
>     >   ~ This is an OPTIONAL string value that may contain a
>     >     description of the repository. It may simply be the content
>     >     from the description file in the git repository.
>
> 'trackers':
>   ~ This is a list of string values. Each value is a URL pointing to a
>     tracker.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 7. The Tracker HTTP Protocol

The Tracker HTTP Protocol (THP) is a simple mechanism for introducing
peers to each other. A tracker is a HTTP service that must be contacted
by a peer in order to join a swarm. As such the tracker constitutes the
only centralized element in GTP/1.0. A tracker does not by itself
provide access to any downloadable data. A tracker relies on peers
sending regular requests. It may assume that a peer is dead if it misses
a request.

#### 7.1 Request

To contact the tracker a peer MUST send a standard HTTP GET request
using an URL from the "trackers" entry of the metainfo file. If one of
the tracker URLs are not available another one may be tried. The GET
request must be parametrized as specified in the HTTP protocol. The
following parameters must be present in the request:

> 'repo\_hash':
>   ~ This is a REQUIRED 20-byte SHA1 hash value. In order to obtain
>     this value the peer must calculate the SHA1 of the value of the
>     "branches" key in the metainfo file.
> 'peer\_id':
>   ~ This is a REQUIRED string and must contain the 20-byte
>     self-designated ID of the peer.
> 'port':
>   ~ the port number that the peer is listening to for incoming
>     connections from other peers. gtp/1.0 does not specify a standard
>     port number, nor a port range to be used. this key is required.
> 'uploaded':
>   ~ This is a base ten integer value. It denotes the total amount of
>     bytes that the peer has uploaded in the swarm since it sent the
>     "started" event to the tracker. This key is REQUIRED.
> 'downloaded':
>   ~ This is a base ten integer value. It denotes the total amount of
>     bytes that the peer has downloaded in the swarm since it sent the
>     "started" event to the tracker. This key is REQUIRED.
> 'completed':
>   ~ This is a base ten integer value. The value must be 0 if the peer
>     does not have the complete torrent and 1 if it has the complete
>     torrent.
> 'ip':
>   ~ This is an OPTIONAL value, and if present should indicate the
>     true, Internet-wide address of the peer, either in dotted quad
>     IPv4 format, hexadecimal IPv6 format, or a DNS name. When not
>     present the tracker will derive the IP address from the request
>     connection.
> 'peers':
>   ~ This is an OPTIONAL value. If present, it should indicate the
>     number of peers that the local peer wants to receive from the
>     tracker. If not present, the tracker uses an implementation
>     defined value.
> 'references':
>   ~ This is an OPTIONAL value. If present, it should indicate the
>     number of references that the local peer wants to receive from the
>     tracker. If not present, the tracker uses an implementation
>     defined value.
> 'event':
>   ~ This parameter is OPTIONAL. If not specified, the request is taken
>     to be a regular periodic request. Otherwise, it MUST have one of
>     the three following values:
>
>     > 'started':
>     >   ~ The first HTTP GET request sent to the tracker MUST have
>     >     this value in the "event" parameter.
>     > 'stopped':
>     >   ~ This value SHOULD be sent to the tracker when the peer is
>     >     shutting down gracefully.
>
#### 7.2 Response

Upon receiving the HTTP GET request, the tracker MUST respond with a
document having the "application/x-gittorrent" MIME type. This document
MUST contain a bencoded dictionary with the following keys:

> 'failure reason':
>   ~ This key is OPTIONAL. If present, the dictionary MUST NOT contain
>     any other keys. The peer should interpret this as if the attempt
>     to join the torrent failed. The value is a human readable string
>     containing an error message with the failure reason.
> 'interval':
>   ~ A peer must send regular HTTP GET requests to the tracker to
>     obtain an updated list of peers and update the tracker of its
>     status. The value of this key indicated the amount of time that a
>     peer should wait between to consecutive regular requests. This key
>     is REQUIRED.
> 'complete':
>   ~ This is an integer that indicates the number of seeders. This key
>     is OPTIONAL.
> 'incomplete':
>   ~ This is an integer that indicates the number of peers downloading
>     the torrent. This key is OPTIONAL.
> 'peers':
>   ~ This is a bencoded list of dictionaries containing information
>     about the peers in the swarm. This key is REQUIRED. It has the
>     following structure:
>
>     > 'peer id':
>     >   ~ This is a REQUIRED string value containing the
>     >     self-designated ID of the peer.
>     > 'ip':
>     >   ~ This is a REQUIRED string value indicating the IP address of
>     >     the peer. This may be given as a dotted quad IPv4 format,
>     >     hexadecimal IPv6 format or DNS name.
>     > 'port':
>     >   ~ This is an integer value. It must contain the
>     >     self-designated port number of the peer. This key is
>     >     REQUIRED.
>
> 'references':
>   ~ This is a string value containing information about the references
>     in the repository. The value can be sent to neighboring peers over
>     the wire using the References message. See [Section 4Repository
>     References](#references) for instructions on how to interpret the
>     string.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 8. The Peer Wire Protocol

The aim of the PWP, is to facilitate communication between neighboring
peers for the purpose of sharing the content of a git repository. PWP
describes the steps taken by a peer after it has read in a metainfo file
and contacted a tracker to gather information about other peers it may
communicate with. PWP is layered on top of TCP and handles all its
communication using asynchronous messages.

#### 8.1 Peer Wire Guidelines

PWP does not specify a standard algorithm for selecting elements from a
clients neighboring peers with whom to share pieces, although the
following guidelines are expected to be observed by any such algorithm:

-   The algorithm should not be constructed with the goal in mind to
    reduce the amount of data uploaded compared to downloaded. At the
    very least a peer should upload the same amount that it has
    downloaded.
-   The algorithm should not use a strict tit-for-tat schema when
    dealing with remote peers that have just joined the swarm and thus
    have no objects to offer.
-   The algorithm should make good use of both download and upload
    bandwidth by putting a cap on the number of simultaneous connection
    that actively send or receive data. By reducing the number of active
    connections, TCP congestion can be avoided.
-   The algorithm should pipeline data requests in order so saturate
    active connections.
-   The algorithm should be able to cooperate with peers that implement
    a different algorithm.

#### 8.2 Handshaking

The local peer opens a port on which to listen for incoming connections
from remote peers. This port is then reported to the tracker. As GTP/1.0
does not specify any standard port for listening, it is the sole
responsibility of the implementation to select a port.

Any remote peer wishing to communicate with the local peer must open a
TCP connection to this port and perform a handshake operation. The
handshake operation MUST be carried out before any other data is sent
from the remote peer. The local peer MUST NOT send any data back to the
remote peer before a well constructed handshake has been recognized
according to the rules below. If the handshake in any way violates these
rules the local peer MUST close the connection with the remote peer.

A handshake is a string of bytes with the following structure:

    -----------------------------------------------------------------------
    | Name Length | Protocol Name | Extension Flags | Repo Hash | Peer ID |
    -----------------------------------------------------------------------

> Name Length:
>   ~ The unsigned value of the first byte indicates the length of a
>     character string containing the protocol name. In GTP/1.0 this
>     number is 19. The local peer knows its own protocol name and hence
>     also the length of it. If this length is different than the value
>     of this first byte, then the connection MUST be dropped.
> Protocol Name:
>   ~ This is a character string which MUST contain the exact name of
>     the protocol in ASCII and have the same length as given in the
>     Name Length field. The protocol name is used to identify to the
>     local peer which version of GTP the remote peer uses. In GTP/1.0
>     the name is 'GitTorrent protocol'. If this string is different
>     from the local peers own protocol name, then the connection is to
>     be dropped.
> Extension Flags:
>   ~ The next 8 bytes in the string are reserved for future extensions,
>     so that peers can exchange information about what optional
>     features they implement. Peers should interpret it according to
>     what extensions they support else it should be read without
>     interpretation.
> Repo Hash:
>   ~ The next 20 bytes in the string are to be interpreted as a 20-byte
>     SHA1 of the info key in the metainfo file. Presumably, since both
>     the local and the remote peer contacted the tracker as a result of
>     reading in the same .torrent file, the local peer will recognize
>     the repo hash value and will be able to serve the remote peer. If
>     this is not the case, then the connection MUST be dropped. This
>     situation can arise if the local peer decides to no longer serve
>     the file in question for some reason. The branches hash may be
>     used to enable the client to serve multiple torrents on the same
>     port.
>   ~ At this stage, if the connection has not been dropped, then the
>     local peer MUST send its own handshake back, which includes the
>     last step:
> Peer ID:
>   ~ The last 20 bytes of the handshake are to be interpreted as the
>     self-designated name of the peer. The local peer must use this
>     name to identify the connection hereafter. Thus, if this name
>     matches the local peers own ID name, the connection MUST be
>     dropped. Also, if any other peer has already identified itself to
>     the local peer using that same peer ID, the connection MUST be
>     dropped.

In GTP/1.0 the handshake has a total of 68 bytes.

#### 8.3 Message Communication

Following the PWP handshake both ends of the TCP channel may send
messages to each other in a completely asynchronous fashion. PWP
messages have the dual purpose of updating the state of neighboring
peers with regard to changes in the local peer, as well as transferring
data blocks between neighboring peers.

PWP Messages fall into two different categories:

> State-oriented messages:
>   ~ These messages serve the sole purpose of informing peers of
>     changes in the state of neighboring peers. A message of this type
>     MUST be sent whenever a change occurs in a peer's state,
>     regardless of the state of other peers. The following messages
>     fall into this category: Interested, Uninterested, Choked,
>     Unchoked, References, Packs, Index, and Peers.
> Data-oriented messages:
>   ~ These messages handle the requesting and sending of data portions.
>     The following messages fall into this category: Request, Cancel
>     and Piece.

#### 8.3.1 Peer States

For each end of a connection, a peer must maintain the following two
state flags:

> Choked:
>   ~ When true, this flag means that the choked peer is not allowed to
>     request data.
> Interested:
>   ~ When true, this flag means a peer is interested in requesting data
>     from another peer. This indicates that the peer will start
>     requesting blocks if it is unchoked.

A choked peer MUST not send any data-oriented messages, but is free to
send any other message to the peer that has choked it. If a peer chokes
a remote peer, it MUST also discard any unanswered requests for blocks
previously received from the remote peer.

An unchoked peer is allowed to send data-oriented messages to the remote
peer. It is left to the implementation how many peers any given peer may
choose to choke or unchoke, and in what fashion. This is done
deliberately to allow peers to use different heuristics for peer
selection.

An interested peer indicates to the remote peer that it must expect to
receive data-oriented messages as soon as it unchokes the interested
peer. It must be noted, that a peer must not assume a remote peer is
interested solely because it has pieces that the remote peer is lacking.
There may be valid reasons why a peer is not interested in another peer
other than data-based ones.

#### 8.4 Peer Wire Messages

All integer members in PWP messages are encoded as a 4-byte big-endian
number. Furthermore, all object block specific offset members in PWP
messages are zero-based.

A PWP message has the following structure:

    -----------------------------------------
    | Message Length | Message ID | Payload |
    -----------------------------------------

> Message Length:
>   ~ This is an integer which denotes the length of the message,
>     excluding the length part itself. If a message has no payload, its
>     size is 1. Messages of size 0 MAY be sent periodically as
>     keep-alive messages. Apart from the limit that the four bytes
>     impose on the message length, GTP does not specify a maximum limit
>     on this value. Thus an implementation MAY choose to specify a
>     different limit, and for instance disconnect a remote peer that
>     wishes to communicate using a message length that would put too
>     much strain on the local peer's resources.
> Message ID:
>   ~ This is a one byte value, indicating the type of the message.
>     GTP/1.0 specifies 9 different messages, as can be seen further
>     below.
> Payload:
>   ~ The payload is a variable length stream of bytes.

If an incoming message in any way violates this structure then the
connection SHOULD be dropped. In particular the receiver SHOULD make
sure the message ID constitutes a valid message, and the payload matches
the the expected payload, as given below.

For the purpose of compatibility with future protocol extensions the
client SHOULD ignore unknown messages. There may arise situations in
which a client may choose to drop a connection after receiving an
unknown message, either for security reasons, or because discarding
large unknown messages may be viewed as excessive waste.

Following, are the messages specified in GTP/1.0.

#### 8.5 State-oriented Messages

#### 8.5.1 Choke

This message has ID 0 and no payload. A peer sends this message to a
remote peer to inform the remote peer that it is being choked.

#### 8.5.2 Unchoke

This message has ID 1 and no payload. A peer sends this message to a
remote peer to inform the remote peer that it is no longer being choked.

#### 8.5.3 Interested

This message has ID 2 and no payload. A peer sends this message to a
remote peer to inform the remote peer of its desire to request data.

#### 8.5.4 Uninterested

This message has ID 3 and no payload. A peer sends this message to a
remote peer to inform it that it is not interested in any pieces from
the remote peer.

#### 8.5.5 Peers

This message has ID 4 and a variable payload length. The payload is a
list of peers each with their self-designated peer ID, port number, and
the IP address of the peer. This may be given as a dotted quad IPv4
format, hexadecimal IPv6 format or DNS name. A peer can send this
message with no payload to requesting the references from the remote
peer. See [Section 3Discovering Peers](#peers) for guidelines for using
Peers messages.

    -----------------------------------------------------------
    | Peer SHA-1 | Peer Port | Peer IP Length | Peer IP | ... |
    -----------------------------------------------------------

#### 8.5.6 References

This message has ID 5 and a variable payload. To request references from
the remote peer, a peer can send this message with no payload. To
announce to the other peer that it has a new reference object available
it can send this message with a reference SHA-1 and an empty object. A
peer should newer send its current reference object unless it has
requested using this method. This reduces the impact of new reference
object being flooded in the network.

The reference object is similar to the "references" string returned in
the tracker response. A peer receiving this message must validate the
resulting object using the public key from the metainfo file and drop
the connection if the object has a false signature. See [Section
4Repository References](#references) for more instructions on how to
interpret the reference object.

    ----------------------------------------------
    | Reference Object SHA-1 | References Object |
    ----------------------------------------------

#### 8.5.7 Packs

This message has ID 6 and a variable payload length. The payload is a
list of pack objects that the sender has successfully downloaded,
validated, and is offering. Each pack file is listed with a SHA-1
uniquely identifying it, a 8-byte big-endian number telling the size of
the pack file, and finally a 1-byte flag field. In all, 29 bytes per
embedded pack object. A peer can send this message with no payload to
requesting the references from the remote peer.

The flag member holds information about what type of git objects are in
the pack. This can be used by peers to fetch the various objects in a
specific order, such as first downloading all commit objects. The
following bit flags are defined: 0-bit is tag objects, 1-bit is commit
objects, 2-bit is tree objects, and 3-bit is blob objects. The flag byte
is interpreted in MSB-order. If no flags are set the pack object may
contain any combination of objects.

A peer receiving this message SHOULD send an index message to the sender
to keep it informed of any new objects the remote peer has downloaded.

    ---------------------------------------------
    | Pack SHA-1 | Pack size | Pack Flags | ... |
    ---------------------------------------------

#### 8.5.8 Index

This message has ID 7 and a variable payload. The payload always
contains a pack SHA-1. If no index data is sent the receiving peer
should interpret it as a request for the pack index, otherwise the data
of the pack index object follows. The recipient MUST only send index
object messages to a sender that has already requested the index object.
A peer receiving this message MUST send an interested message to the
sender if indeed it lacks any of the objects that are announced.
Further, it MAY also send a request for that pack or object. The payload
has the following structure:

    ---------------------------
    | Pack SHA-1 | Index Data |
    ---------------------------

#### 8.6 Data-oriented Messages

#### 8.6.1 Request

This message has ID 8 and a payload of length 28. The payload is first
an object SHA-1 and two integers indicating a block within an object
that the sender is interested in downloading from the recipient. The
recipient MUST only send object messages to a sender that has already
requested it, and only in accordance to the rules given above about the
choke and interested states. The payload has the following structure:

    ----------------------------------------------
    | Object SHA-1 | Block Offset | Block Length |
    ----------------------------------------------

#### 8.6.2 Block

This message has ID 9 and a variable length payload. The payload holds
an object SHA-1 and an integer indicating from which object and with
what offset the block data in the 3rd member is derived. Note, the data
length is implicit and can be calculated from the total message length.
The payload has the following structure:

    --------------------------------------------
    | Object SHA-1 | Block Offset | Block Data |
    --------------------------------------------

#### 8.6.3 Cancel

This message has ID 10 and a payload of length 28. The payload is one
object SHA-1 nad two integer values indicating a block within an object
that the sender has requested, but is no longer interested in. The
recipient MUST erase the request information upon receiving this
messages. The payload has the following structure:

    ----------------------------------------------
    | Object SHA-1 | Block Offset | Block Length |
    ----------------------------------------------

#### 8.7 The End Game

Towards the end of a download session, it may speed up the download to
send request messages for the remaining objects to all the neighboring
peers. A client must issue cancel messages to all pending requests sent
to neighboring peers as soon as an object is downloaded successfully.
This is referred to as the end game.

A client usually sends requests for blocks in stages; sending requests
for newer blocks as replies for earlier requests are received. The
client enters the end game, when all remaining objects have been
requested.

#### 8.8 Object Selection Strategy

GTP/1.0 does not force a particular order for selecting which objects to
download. However, experience shows that downloading in rarest-first
order seems to lessen the wait time for objects. To find the rarest
objects a client must calculate for each commit object the number of
times this index is true in the commit bitfield vectors of all the
neighboring peers. The object with the lowest sum is then selected for
requesting.

#### 8.9 Peer Selection Strategy

This section describes the choking algorithm recommended for selecting
neighboring peers with whom to exchange objects. Implementations are
free to implement any strategy as long as the guidelines in [Section
8.1Peer Wire Guidelines](#peer-wire-guidelines) are observed.

After the initial handshake both ends of a connection set the Choked
flag to true and the Interested flag to false.

All connections are periodically rated in terms of their ability to
provide the client with a better download rate. The rating may take into
account factors such as the remote peers willingness to maintain an
unchoked connection with the client over a certain period of time, the
remote peers upload rate to the client and other implementation defined
criteria.

The peers are sorted according to their rating with regard to the above
mentioned scheme. Assume only 5 peers are allowed to download at the
same time. The peer selection algorithm will now unchoke as many of the
best rated peers as necessary so that exactly 5 of these are interested.
If one of the top rated peers at a later stage becomes interested, then
the peer selection algorithm will choke the the worst unchoked peer.
Notice that the worst unchoked peer is always interested.

The only lacking element from the above algorithm is the capability to
ensure that new peers can have a fair chance of downloading a object,
even though they would evaluate poorly in the above schema. A simple
method is to make sure that a random peer is selected periodically
regardless of how it evaluates. Since this process is repeated in a
round robin manner, it ensures that ultimately even new peers will have
a chance of being unchoked.

\

* * * * *

  -------------
  [TOC](#toc)
  -------------

### 9. Security Consideration

This section examines security considerations for GTP/1.0.The discussion
does not include definitive solutions to the problems revealed, though
it does make some suggestions for reducing security risks.

#### 9.1 Tracker HTTP Protocol Issues

The use of the HTTP protocol for communication between the tracker and
the client makes GTP/1.0 vulnerable to the attacks mentioned in the
security consideration section of [RFC 2616Fielding, R., Gettys, J.,
Mogul, J., Frystyk, H., Masinter, L., Leach, P. and T. Berners-Lee,
Hypertext Transfer Protocol -- HTTP/1.1, June 1999.](#RFC2616)[6].

#### 9.2 Denial of Service Attacks on Trackers

The nature of the tracker is to serve many clients. By mounting a denial
of service attack against the tracker the swarm attached to the tracker
can be starved. This type of attack is hard to defend against, however,
the metainfo file allows for multiple trackers to be specified, making
it possible to spread the load on a number of trackers, and thus
containing such an attack.

#### 9.3 Peer Identity Issues

There is no strong authentication of clients when they contact the
tracker. The main option for trackers is to check peer ID and the IP
address of the client. The lack of authentication can be used to mount
an attack where a client can shut down another client if the two clients
are running on the same host and thus are sharing the same IP address.
In addition, a rogue peer may masquerade its identity by using multiple
peer IDs. Clients should there refrain from taking the peer ID at face
value.

#### 9.4 DNS Spoofing

Clients using GTP/1.0 rely heavily on the Domain Name Service, which can
be used for both specifying the URI of the tracker and how to contact a
peer. Clients are thus generally prone to security attacks based on the
deliberate mis-association of IP addresses and DNS names. Clients need
to be cautious in assuming the continuing validity of an IP address/DNS
name association.

In particular, GTP/1.0 clients SHOULD rely on their name resolver for
confirmation of an IP number/DNS name association, rather than caching
the result of previous host name lookups. If clients cache the results
of host name lookups in order to achieve a performance improvement, they
MUST observe the TTL information reported by DNS.

If clients do not observe this rule, they could be spoofed when a
previously-accessed peers or trackers IP address changes. As network
renumbering is expected to become increasingly common according to [RFC
1900Carpenter, B. and Y. Rekhter, Renumbering Needs Work, February
1996.](#RFC1900)[2], the possibility of this form of attack will grow.
Observing this requirement reduces this potential security
vulnerability.

#### 9.5 Issues with File and Directory Names

The metainfo file provides a way to suggest a name of the downloaded
branches for torrents. GTP clients SHOULD verify that the suggested file
names in the metainfo file do not compromise services on the local
system when translated to a path in the repository structure.

Using UNIX as an example, some hazards would be:

-   Creating startup files (e.g., ".login").
-   Creating or overwriting system files (e.g., "/etc/passwd").
-   Overwriting any existing file.

It is very important to note that this is not an exhaustive list; it is
intended as a small set of examples only. Implementers must be alert to
the potential hazards on their target systems. In general, the GTP
client SHOULD NOT name or place files such that they will get
interpreted or executed without the user explicitly initiating the
action.

#### 9.6 Validating the Integrity of Data Exchanged Between Peers

By default, all content served to the client from other peers should be
considered tainted and the client SHOULD validate the integrity of the
data before accepting it. The metainfo file contains information for
checking both individual objects using SHA1, and optionally individual
files using MD5. SHA1, being the strongest of the two, is preferred.
Furthermore, sole reliance on whole-file checking can potentially render
otherwise valid objects invalid, and should only be considered for small
files, to limit the amount of data being discarded.

Trusting the validity of the resulting repository ends up being a matter
of trusting the content of the metainfo file and branch updates from the
tracker. Ensuring the validity of the metainfo file is beyond the scope
of this document.

#### 9.7 Transfer of Sensitive Information

Some clients include information about themselves when generating the
peer ID string. Clients should be aware that this information can
potentially be used to determine whether a specific client has a
exploitable security hole.

### 10. IANA Considerations

This document makes no request of IANA.

### 11 References

  [1]   Postel, J. and J. Reynolds, "[File Transfer Protocol](ftp://ftp.isi.edu/in-notes/rfc959.txt)", STD 9, RFC 959, October 1985.
  [2]   [Carpenter, B.](mailto:brian@dxcoms.cern.ch) and [Y. Rekhter](mailto:yakov@cisco.com), "[Renumbering Needs Work](ftp://ftp.isi.edu/in-notes/rfc1900.txt)", RFC 1900, February 1996.
  [3]   [Bradner, S.](mailto:sob@harvard.edu), "[Key words for use in RFCs to Indicate Requirement Levels](ftp://ftp.isi.edu/in-notes/rfc2119.txt)", BCP 14, RFC 2119, March 1997 ([TXT](ftp://ftp.isi.edu/in-notes/rfc2119.txt), [HTML](http://xml.resource.org/public/rfc/html/rfc2119.html), [XML](http://xml.resource.org/public/rfc/xml/rfc2119.xml)).
  [4]   [Troost, R.](mailto:rens@century.com), [Dorner, S.](mailto:sdorner@qualcomm.com) and [K. Moore](mailto:moore@cs.utk.edu), "[Communicating Presentation Information in Internet Messages: The Content-Disposition Header Field](ftp://ftp.isi.edu/in-notes/rfc2183.txt)", RFC 2183, August 1997 ([TXT](ftp://ftp.isi.edu/in-notes/rfc2183.txt), [HTML](http://xml.resource.org/public/rfc/html/rfc2183.html), [XML](http://xml.resource.org/public/rfc/xml/rfc2183.xml)).
  [5]   [Crocker, D., Ed.](mailto:dcrocker@imc.org) and [P. Overell](mailto:paulo@turnpike.com), "[Augmented BNF for Syntax Specifications: ABNF](ftp://ftp.isi.edu/in-notes/rfc2234.txt)", RFC 2234, November 1997 ([TXT](ftp://ftp.isi.edu/in-notes/rfc2234.txt), [HTML](http://xml.resource.org/public/rfc/html/rfc2234.html), [XML](http://xml.resource.org/public/rfc/xml/rfc2234.xml)).
  [6]   [Fielding, R.](mailto:fielding@ics.uci.edu), [Gettys, J.](mailto:jg@w3.org), [Mogul, J.](mailto:mogul@wrl.dec.com), [Frystyk, H.](mailto:frystyk@w3.org), [Masinter, L.](mailto:masinter@parc.xerox.com), [Leach, P.](mailto:paulle@microsoft.com) and [T. Berners-Lee](mailto:timbl@w3.org), "[Hypertext Transfer Protocol -- HTTP/1.1](ftp://ftp.isi.edu/in-notes/rfc2616.txt)", RFC 2616, June 1999 ([TXT](ftp://ftp.isi.edu/in-notes/rfc2616.txt), [PS](ftp://ftp.isi.edu/in-notes/rfc2616.ps), [PDF](ftp://ftp.isi.edu/in-notes/rfc2616.pdf), [HTML](http://xml.resource.org/public/rfc/html/rfc2616.html), [XML](http://xml.resource.org/public/rfc/xml/rfc2616.xml)).