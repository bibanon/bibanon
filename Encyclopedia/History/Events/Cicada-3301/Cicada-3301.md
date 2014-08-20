#### [ClevCode](http://www.clevcode.org/ "Home") My life as a hacker

-   [Home](http://www.clevcode.org/ "Home")
-   [3301](http://www.clevcode.org/cicada-3301/)
-   [GCHQ](http://www.clevcode.org/canyoucrackit-co-uk-gchq-challenge-solution/)
-   [pCTF](http://www.clevcode.org/pctf/)
-   [About](http://www.clevcode.org/about/)

3301
----

On January 5th 2012, an image was uploaded to various image boards,
possibly originating at the infamous /b/ board at 4chan. When I came
across it, I didn’t think much of it at first, but still decided to look
into it just in case it turned out to be interesting. I have always had
a hard time resisting a challenge. This is the image that was posted:

![image](http://www.clevcode.org/wp-content/uploads/2012/01/3301.jpg)

My first thought was that it used steganography to hide a message, and
since it was a JPEG image I tried using stegdetect by Niels Provos in
case one of the detectable schemes was used. Since stegdetect have not
been updated in almost 7 years, I didn’t really get my hopes up that
high though, but it is always worth a try. ;) The result can be seen
below:

    je@isis:~/3301/stage_1$ stegdetect 3301.jpg
    3301.jpg : appended(61)<[nonrandom][ASCII text][TIBERIVS CLAVDIV]>

It did not detect any of the common steganographic schemes, but notified
me of 61 appended bytes of ASCII text. Since my next move would have
been to use “strings”, I would have discovered this anyway, but
stegdetect was kind enough to tell me directly instead. :) So, let’s see
what we have:

    je@isis:~/3301/stage_1$ tail -61c 3301.jpg
    TIBERIVS CLAVDIVS CAESAR says "lxxt>33m2mqkyv2gsq3q=w]O2ntk"

This is quite obviously a shift cipher of some sort (also known as a
Caesar cipher), with “lxxt\>33″ being the ciphered version of “http://”.
A shift cipher replaces each letter in the plaintext with a letter (or
in this case, arbitrary ASCII character) with a letter a certain number
of positions down the alphabet. So, let’s compare the ASCII values for
the cipher text with the ASCII value of the supposed plaintext to see
what the shift value is:

    je@isis:~/3301/stage_1$ perl -e 'print ord("h")-ord("l"),chr(10)'
    -4

In this particular case, this might have been a bit overkill, since we
could just as well have manually counted the distance between h and l in
the alphabet. ;) It is probably not a coincidence that Claudius happens
to be the 4th Emperor of the Roman Empire, and the shift value happens
to be 4, either. To decipher this, a perl oneliner is enough:

    je@isis:~/3301/stage_1$ echo "lxxt>33m2mqkyv2gsq3q=w]O2ntk" | perl -pne 'chomp;s{(.)}{chr(ord($1)-4)}sgex;$_.=chr(10)'

    http://i.imgur.com/m9sYK.jpg

The image at the URL above can be seen below:

![image](http://www.clevcode.org/wp-content/uploads/2012/01/duck.jpg)

It seems like the challenge is a bit harder than a caesar cipher after
all. Note that the message contains the words “out” and “guess” though,
which could be a hint that we are actually supposed to use the old
OutGuess tool to extract the hidden message. Incidentally, OutGuess is
also developed by Niels Provos and is available for download from the
same site as stegdetect
([http://www.outguess.org/](http://www.outguess.org/)). Unfortunately,
it seems like stegdetect is only able to detect when the older OutGuess
0.13b has been used and not OutGuess 0.2 (from 2001!). :D

Using outguess 0.2 with the -r option immediately reveals the hidden
message in the original image:

    je@isis:~/3301/stage_1$ outguess -r 3301.jpg 3301.txt
    Reading 3301.jpg....
    Extracting usable bits:   29049 bits
    Steg retrieve: seed: 228, len: 535

The hidden message can be found
[here](http://www.clevcode.org/wp-content/uploads/2012/01/3301.txt).

* * * * *

Now things are actually getting interesting. Although the challenge have
not been required any particularly advanced skills yet, someone has
obviously been putting some work into it. The hidden message says that
we should go to the following URL:
[http://www.reddit.com/r/a2e7j6ic78h0j/](http://www.reddit.com/r/a2e7j6ic78h0j/)

The hidden message also includes a so called book code, consisting of a
number of lines with two digits separated by a colon on each. The book
and more information should be found at the URL above. Book ciphers are
ciphers that use a book or a text of some sort as the key to encode a
secret message. Traditionally, they worked by replacing words in the
plaintext with the locations of words from a book, but in this case it
seems more likely that the two digits separated by a colon in the code
refers to a line and column number.

When visiting the Reddit page, we can make a number of observations.
Most notably, there are a number of posts by the pseudonym
CageThrottleUs that seem to consist of encoded text, which we can assume
to be the book. It looks like an ordinary Caesar cipher may have been
used, but on a closer look no shift value results in readable text. It
seems most likely that a key of some sort is required to decode the
text.

Looking closer on the page, we can see that the title is
“a2e7j6ic78h0j7eiejd0120″. The URL itself is a truncated version of
this. To the right, below the “subscribe” button, the title text is
repeated and “Verify: 7A35090F” is written underneath. We can also see
pictures of some mayan numbers on the top of the page. Mayan numbers are
quite logical, at least from 0-19. A dot equals one, and a vertical line
equals five. Two lines thus equals ten, one line with two dots equals
seven (5 + 2) and so on. There is also a symbol resembling a rugby ball
that equals zero. :)

The number sequence that is written using mayan numbers is as follows:\
 10 2 14 7 19 6 18 12 7 8 17 0 19

Comparing this with the a2e7j6ic78h0j7eiejd0120 in the title, we can see
that numbers below 10 in the sequence above is also found in this
string, at the same positions. Also note that instead of 10 we have “a”,
instead of 14 we have “e”, and so on up to “j” being 19. Since the title
of the page contains 23 characters and there were only 13 mayan numbers
is is quite likely that we are supposed to continue converting
characters from the title to numbers. This gives us:

10 2 14 7 19 6 18 12 7 8 17 0 19 7 14 18 14 19 13 0 1 2 0

This could very well be the key required to decode the text. Regarding
the “Verify: 7A35090F”, it may refer to any number of things. A PGP key
ID is, however, a good assumption since it consists of a 32 bit value
normally encoded as eight hex characters and since PGP keys can be used
to verify the signature, and thus the authenticity, of messages signed
with a PGP key. This could be quite handy, in case the challenge goes on
and in case people decide to drop false leads to the people working on
it. So, let’s try to import the public key with the ID in question from
one of the common PGP key servers:

    je@isis:~$ gpg --recv-keys 7A35090F
    gpg: requesting key 7A35090F from hkp server keys.gnupg.net
    gpg: key 7A35090F: public key "Cicada 3301 (845145127)" imported
    gpg: Total number processed: 1
    gpg:               imported: 1  (RSA: 1)

The comment for the key mentions 3301, which was used as the signature
in the original image. It also includes the word “cicada” and the number
845145127, which may turn out to be significant at a later stage. Note,
for instance, that cicadas emerge from their hideouts under earth every
13 or 17 years depending on which kind. By emerging every N:th year,
where N happens to be a prime number, cicadas actually minimize the
possibility of scynchronizing with the life cycles of birds and other
animals that prey on them. Also note that 3301 is a prime, and that
845145127 has 3301, 509 and 503 as its prime factors.

    je@isis:~$ factor 3301
    3301: 3301
    je@isis:~$ factor 845145127
    845145127: 503 509 3301

When taking a closer look at the lines of encoded text posted to the
reddit page, we also find two images. One named
[Welcome](http://www.clevcode.org/wp-content/uploads/2012/01/welcome.jpg)
and the other one
[Problems?](http://www.clevcode.org/wp-content/uploads/2012/01/problems.jpg).
By using OutGuess again, we find another couple of hidden messages:

    je@isis:~/3301/stage_2$ outguess -r welcome.jpg welcome.txt
    Reading welcome.jpg....
    Extracting usable bits:   326276 bits
    Steg retrieve: seed: 58, len: 1089
    je@isis:~/3301/stage_2$ cat welcome.txt
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    - From here on out, we will cryptographically sign all messages with this key.

    It is available on the mit keyservers.  Key ID 7A35090F, as posted in a2e7j6ic78h0j.

    Patience is a virtue.

    Good luck.

    3301
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (GNU/Linux)

    iQIcBAEBAgAGBQJPBRz7AAoJEBgfAeV6NQkP1UIQALFcO8DyZkecTK5pAIcGez7k
    ewjGBoCfjfO2NlRROuQm5CteXiH3Te5G+5ebsdRmGWVcah8QzN4UjxpKcTQRPB9e
    /ehVI5BiBJq8GlOnaSRZpzsYobwKH6Jy6haAr3kPFK1lOXXyHSiNnQbydGw9BFRI
    fSr//DY86BUILE8sGJR6FA8Vzjiifcv6mmXkk3ICrT8z0qY7m/wFOYjgiSohvYpg
    x5biG6TBwxfmXQOaITdO5rO8+4mtLnP//qN7E9zjTYj4Z4gBhdf6hPSuOqjh1s+6
    /C6IehRChpx8gwpdhIlNf1coz/ZiggPiqdj75Tyqg88lEr66fVVB2d7PGObSyYSp
    HJl8llrt8Gnk1UaZUS6/eCjnBniV/BLfZPVD2VFKH2Vvvty8sL+S8hCxsuLCjydh
    skpshcjMVV9xPIEYzwSEaqBq0ZMdNFEPxJzC0XISlWSfxROm85r3NYvbrx9lwVbP
    mUpLKFn8ZcMbf7UX18frgOtujmqqUvDQ2dQhmCUywPdtsKHFLc1xIqdrnRWUS3CD
    eejUzGYDB5lSflujTjLPgGvtlCBW5ap00cfIHUZPOzmJWoEzgFgdNc9iIkcUUlke
    e2WbYwCCuwSlLsdQRMA//PJN+a1h2ZMSzzMbZsr/YXQDUWvEaYI8MckmXEkZmDoA
    RL0xkbHEFVGBmoMPVzeC
    =fRcg
    -----END PGP SIGNATURE-----
    je@isis:~/3301/stage_2$ gpg --verify welcome.txt
    gpg: Signature made Thu 05 Jan 2012 04:46:03 AM CET using RSA key ID 7A35090F
    gpg: Good signature from "Cicada 3301 (845145127)"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 6D85 4CD7 9333 22A6 01C3  286D 181F 01E5 7A35 090F
    je@isis:~/3301/stage_2$ outguess -r problems.jpg problems.txt
    Reading problems.jpg....
    Extracting usable bits:   256999 bits
    Steg retrieve: seed: 194, len: 1041
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    The key has always been right in front of your eyes.

    This isn't the quest for the Holy Grail.  Stop making
    it more difficult than it is. 

    Good luck.

    3301
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (GNU/Linux)

    iQIcBAEBAgAGBQJPCBl3AAoJEBgfAeV6NQkPo6EQAKghp7ZKYxmsYM96iNQu5GZV
    fbjUHsEL164ZLctGkgZx2H1HyYFEc6FGvcfzqs43vV/IzN4mK0SMy2qFPfjuG2JJ
    tv3x2QfHMM3M2+dwX30bUD12UorMZNrLo8HjTpanYD9hL8WglbSIBJhnLE5CPlUS
    BZRSx0yh1U+wbnlTQBxQI0xLkPIz+xCMBwSKl5BaCb006z43/HJt7NwynqWXJmVV
    KScmkpFC3ISEBcYKhHHWv1IPQnFqMdW4dExXdRqWuwCshXpGXwDoOXfKVp5NW7Ix
    9kCyfC7XC4iWXymGgd+/h4ccFFVm+WWOczOq/zeME+0vJhJqvj+fN2MZtvckpZbc
    CMfLjn1z4w4d7mkbEpVjgVIU8/+KClNFPSf4asqjBKdrcCEMAl80vZorElG6OVIH
    aLV4XwqiSu0LEF1ESCqbxkEmqp7U7CHl2VW6qv0h0Gxy+/UT0W1NoLJTzLBFiOzy
    QIqqpgVg0dAFs74SlIf3oUTxt6IUpQX5+uo8kszMHTJQRP7K22/A3cc/VS/2Ydg4
    o6OfN54Wcq+8IMZxEx+vxtmRJCUROVpHTTQ5unmyG9zQATxn8byD9Us070FAg6/v
    jGjo1VVUxn6HX9HKxdx4wYGMP5grmD8k4jQdF1Z7GtbcqzDsxP65XCaOYmray1Jy
    FG5OlgFyOflmjBXHsNad
    =SqLP
    -----END PGP SIGNATURE-----
    je@isis:~/3301/stage_2$ gpg --verify problems.txt
    gpg: Signature made Sat 07 Jan 2012 11:07:51 AM CET using RSA key ID 7A35090F
    gpg: Good signature from "Cicada 3301 (845145127)"
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: 6D85 4CD7 9333 22A6 01C3  286D 181F 01E5 7A35 090F

The messages verifies both our assumptions, since they are indeed signed
using the key ID 7A35090F and since the second one specifically says
that the key “has always been right in front of your eyes”. In other
words, it is likely to consist of the numbers we discovered being
encoded as characters in the title of the page. The first message also
specifically states that all messages from now on will be signed using
the PGP key with ID 7A35090F.

All that remains now is to figure out which encoding scheme has been
used so that we can apply the key to the text. Since a shift cipher was
used in the original image (although it was used as a decoy), perhaps
the numbers are different shift values. In other words, for each line of
text, shift/rotate the first letter ten steps in the alphabet, rotate
the second letter two steps, the third letter 14 steps, and so on, to
get the plaintext. Implementing this in C results in the following:

    je@isis:~/3301/stage_2$ cat decipher.c
    #include <stdio.h>
    #include <ctype.h>

    int main(void)
    {
            unsigned char key[] = {
                    10, 2, 14, 7, 19, 6, 18, 12,
                    7, 8, 17, 0, 19, 7, 14, 18,
                    14, 19, 13, 0, 1, 2, 0
            };
            int c, i = 0;

            while ((c = getchar()) != EOF) {
                    if (isalpha(c)) {
                            int base, off;
                            if (isupper(c))
                                    base = 'A';
                            else
                                    base = 'a';

                            off = c - base - key[i++ % sizeof(key)];
                            if (off < 0)
                                    off += 26;

                            c = base + off;
                    } else if (c == '\n')
                            i = 0;

                    putchar(c);
            }

            return 0;
    }
    je@isis:~/3301/stage_2$ gcc -o decipher decipher.c -O -Wall -ansi -pedantic
    je@isis:~/3301/stage_2$ head -3 reddit.txt
    Ukbn Txltbz nal hh Uoxelmgox wdvg Akw; hvu ogl rsm ar sbv ix jwz
    mjotukj; mul nimo vaa prrf Qwkkb aak kau ww Ukpsf, ogq Kzpox vvl luf
    yh Qsrjfa, hvu Ktp hzs lbn ph Kipsy; ttv Sdmehpfjsf tad igr
    je@isis:~/3301/stage_2$ ./decipher < reddit.txt | head -3
    King Arthur was at Caerlleon upon Usk; and one day he sat in his
    chamber; and with him were Owain the son of Urien, and Kynon the son
    of Clydno, and Kai the son of Kyner; and Gwenhwyvar and her

The file "reddit.txt" consists of the lines posted to the reddit page so
far, in the order that they have been posted. Note that this is not in
the exact order that they are shown on the reddit page. As you can see,
our assumption was correct and we can now decipher every line of text
that has been posted, and try to apply the book code that we got in the
message hidden in the original image.

Using a small bash script, we can apply the book code to the text from
reddit to retreive yet another hidden message:

    je@isis:~/3301/stage_2$ ./decipher < reddit.txt > reddit-deciphered.txt
    je@isis:~/3301/stage_2$ cat reddit-decode.sh
    #!/bin/bash

    while read line; do
            row=`echo $line | cut -d: -f1`
            col=`echo $line | cut -d: -f2`
            head -n$row reddit-deciphered.txt | tail -n1 | head -${col}c | tail -1c
    done < bookcode.txt
    echo
    je@isis:~/3301/stage_2$ ./reddit-decode.sh
    Call us at us tele phone oumBer two one four thsee nine oi nine si  oh  ihht

Although we can easily see which phone number is being refered to, it's
obvious that the output is a bit garbled. For the sake of completeness,
let's look into what the cause might be. The first letter that is
garbled is the "n" in number that has been turned into an "o", then the
"r" in three which have been turned into an "s" and so on. The upper
case "B" may have been intended though, although it seems a bit off.
There is actually a lower case "b" on the same line that is used for
encoding the upper case "B", but the upper case one comes first.

When looking at the line corresponding to the "n" turning into an "o"
(line 26, column 65), we can see that there is actually an "n" right
before the "o" at column 65 (from the name "Kynon"). Looking further
down, at the line corresponding to the "r" turning into an "s" (line 48,
column 43), we can see that the expected "r" is right before "s" on this
line as well (from the word "daggers").

Another thing in common for these particular lines of text is that they
include a period somewhere before the character that has been decoded
incorrectly. If we assume that periods, which end sentences, should
count as two characters instead of one when applying the book code we
get this, which looks a bit neater:

    je@isis:~/3301/stage_2$ perl -i -pne 's/\./. /g' reddit-deciphered.txt
    je@isis:~/3301/stage_2$ ./reddit-decode.sh
    Call us at us tele phone numBer two one four three nine oh nine six oh eight

So, to continue the challenge we need to call the (214) 390-9608, a
Texas based phone number. Whoever is behind this challenge, they have
obviously put some effort into it. :)

When calling the number, one is (or rather, was, the number has now been
deactivated) greeted by the following message:\
 "Very good. You have done well. There are three prime numbers
associated with the original final.jpg image. 3301 is one of them. You
will have to find the other two. Multiply all three of these numbers
together and add a .com to find the next step. Good luck. Goodbye."

When examining the PGP key, we already noted that it included the number
845145127 in the description, and that this is the product of 3301, 503
and 509. When looking at the metadata for the original image, we also
note this:

    je@isis:~/3301/stage_1$ exiftool 3301.jpg | grep 50[39]
    Image Width                     : 509
    Image Height                    : 503
    Image Size                      : 509x503

Seems like we've solved this stage as well, now let's head to
http://845145127.com/ to find the next part of the challenge. :) When I
first arrived at the http://845145127.com/ site, it just displayed an
image of a cicada and a countdown. Using OutGuess again, the following
signed message could be extracted from the cicada image:

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    You have done well to come this far.

    Patience is a virtue.

    Check back at 17:00 on Monday, 9 January 2012 UTC.

    3301
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (GNU/Linux)

    iQIcBAEBAgAGBQJPCKDUAAoJEBgfAeV6NQkPf9kP/19tbTFEy+ol/vaSJ97A549+
    E713DyFAuxJMh2AY2y5ksiqDRJdACBdvVNJqlaKHKTfihiYW75VHb+RuAbMhM2nN
    C78eh+xd6c4UCwpQ9vSU4i1Jzn6+T74pMKkhyssaHhQWfPs8K7eKQxOJzSjpDFCS
    FG7oHx6doPEk/xgLaJRCt/IJjNCZ9l2kYinmOm7c0QdRqJ+VbV7Px41tP1dITQIH
    /+JnETExUzWbE9fMf/eJl/zACF+gYii7d9ZdU8RHGi14jA2pRjc7SQArwqJOIyKQ
    IFrW7zuicCYYT/GDmVSyILM03VXkNyAMBhG90edm17sxliyS0pA06MeOCjhDGUIw
    QzBwsSZQJUsMJcXEUOpHPWrduP/zN5qHp/uUNNGj3vxLrnB+wcjhF8ZOiDF6zk7+
    ZVkdjk8dAYQr62EsEpfxMT2dv5bJ0YBaQGZHyjTEYnkiukZiDfExQZM2/uqhYOj3
    yK0J+kJNt7QvZQM2enMV7jbaLTfU3VZGqJ6TSPqsfeiuGyxtlGLgJvd6kmiZkBB8
    Jj0Rgx/h9Tc4m9xnVQanaPqbGQN4vZF3kOp/jAN5YjsRfCDb7iGvuEcFh4oRgpaB
    3D2/+Qo9i3+CdAq1LMeM4WgCcYj2K5mtL0QhpNoeJ/s0KzwnXA+mxBKoZ0S8dUX/
    ZXCkbOLoMWCUfqBn8QkQ
    =zn1y
    -----END PGP SIGNATURE-----

Just like before, the message is signed using the Cicada 3301 key. The
challenge so far have been a quite fun, and rather different, experience
and I'm looking forward to see what comes next.

* * * * *

When the countdown was finished, at 17:00 UTC January 9 2012, it was
replaced by strings of digits resembling GPS coordinates. Also, the
image of the cicada now contained another signed text containing the
same GPS coordinates as on the web page, except for two that were only
on the webpage (37.577070, 126.813122 and 36.0665472222222,
-94.1726416666667):

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    52.216802, 21.018334
    48.85057059876962, 2.406892329454422
    48.85030144151387,2.407538741827011
    47.664196,  -122.313301
    47.637520, -122.346277
    47.622993, -122.312576
    37.5196666666667, 126.995
    33.966808, -117.650488
    29.909098706850486 -89.99312818050384
    25.684702, -80.441289
    21.584069, -158.104211
    - -33.90281, 151.18421
    3301
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (GNU/Linux)

    iQIcBAEBAgAGBQJPChn7AAoJEBgfAeV6NQkPZxMP/05D9TkSpwRaBXPqYthuyqxx
    uo+ZDyr/yVIlAdurTBiWb3aGxKJjtWg/vlcHcatK0TGL2qaHwB/FFZQAaqOyU7Zf
    DXdpWr8PWoWhpWNYUK8IrOaYu1SmWlJnkTdUSzGrX0lbwjwMmJJoPNS7CJuO6MaA
    2GIwpv2G7lYqnH3xeX3kzGlPMsVb/wucKRjobsbdbreh1SNuQuRnhfe4s+oHTTqs
    XjtGL/VhBI0DUAdfLqW7z4C+Gvbx6okC8x5Sj2N2UTJOiyMYXz5+QyHoA6fo9g5V
    6zodNpx/RvxuZP2Ssc9TqERgTo5FjRBpON1vjDalHgg0H2Fus2LK3gh+NZfj1i5b
    Oqa4Cqd9epI2pe+glXn86j9crS+2BEAr1cguqAFepvI9sdFEornDja4VXwDtUdM8
    9hMVkU5NiTUYfvxZbL6W7rHIF7wxjGUwpe1ViuixG+cKNfv0enrt60PrtDByBOWI
    9LLIUE0cB5HDT1xrczZ/55CtuM3Zf07/l0nLFdmgR0oa8KUA9gWcPs6S1EpBa185
    VcyOTqbpIPiT8neiJEkXarbJeFk15m1P73Fr8XZxdj7EHK0aOwGYcc8e4PmW/dSh
    gcrSNXiePCbcRVRD2n9L47C0LkNyRpoBkmjvtpcRyp5ISe+0xcx/QI+gc1lkSijC
    89qV+ymCHae1RiSDxVbd
    =ZJ37
    -----END PGP SIGNATURE-----

Using Google Maps (maps.google.com) I could search for each of these
locations, and in most cases even get a street view. The locations were
spread out around the world without any obvious connection (USA, Poland,
France, South Korea and Australia), except for perhaps each of them
being home to some talented hackers. At this point I thought it would be
the end of the game for me, since I am far away from all of these
locations.

I was still very curious on how the challenge would continue though, and
found that there are groups of people working on this from all over the
world. One of these groups had set up an IRC channel at n0v4.com, and
managed to get people to check out the locations at the specified GPS
coordinates. What they found was notes attached to lightpoles, with the
cicada image and a QR code. When scanning the QR code, they got image
URLs with a black and white image of a cicada and the text "everywhere"
and "3301". Each image also contained a hidden image, with a signed
message. Even though there were 14 locations, only two different
messages were used though.

One of them had with the following text at the top of the message (full
message
[here](http://www.clevcode.org/wp-content/uploads/2012/01/3301-msg1.txt)):

    In twenty-nine volumes, knowledge was once contained.
    How many lines of the code remained when the Mabinogion paused?
    Go that far in from the beginning and find my first name.

The other one had this text (full message here
[here](http://www.clevcode.org/wp-content/uploads/2012/01/3301-msg2.txt)):

    A poem of fading death, named for a king
    Meant to be read only once and vanish
    Alas, it could not remain unseen.

They both also included a 22 line book code. Both of them included the
text "the product of the first two primes" at line 3 and 15, and one of
them also included the text "the first prime" at line 8. This probably
means that the characters on these positions should be replaced with the
numbers described. Note that the definition of a prime number is a
natural number greater than 1, with no positive divisors other than 1
and itself. This means that the first two prime numbers are two and
three.

The three lines of text in each message seemed likely to be a hint to
which book/text to use as the key for the included book code. By
googling for some keywords in the second message (poem fading death read
only once vanish), the Wikipedia entry for a 300-line poem by William
Gibson is among the first hits. The poem is called Agrippa (a book of
the dead) and according to Wikipedia "Its principal notoriety arose from
the fact that the poem, stored on a 3.5" floppy disk, was programmed to
erase itself after a single use; similarly, the pages of the artist's
book were treated with photosensitive chemicals, effecting the gradual
fading of the words and images from the book's first exposure to
light.". This fits the description perfectly.

When googling for william gibson agrippa, the first hit is
[http://www.williamgibsonbooks.com/source/agrippa.asp](http://www.williamgibsonbooks.com/source/agrippa.asp).
Taking this text, including line breaks, as the key for the book code
results in the following:

    je@isis:~/3301/stage_3$ cat agrippa-decode.sh
    #!/bin/bash

    while read line; do
            if [ "$line" = "the product of the first two primes" ]; then
                    echo -n 6
            else
                    row=`echo $line | cut -d: -f1`
                    col=`echo $line | cut -d: -f2`
                    head -n$row agrippa.txt | tail -n1 | head -${col}c | tail -1c
            fi
    done < agrippa-code.txt
    echo
    je@isis:~/3301/stage_3$ ./agrippa-decode.sh
    sq6wmgv2zcsrix6t.onion

Judging by the ".onion" at the end of the string, this is actually an
anonymous hidden service in the Tor network. Unfortunately, by the time
I arrived at this stage the Tor service was not available anymore. 3301
had concluded the last couple of messages with "You've shared too much
to this point. We want the best, not the followers. Thus, the first few
there will receive the prize.", so it was probably first come first
served. The ones who were lucky enough to arrive in time (most of which
did not solve much or any of this challenge themselves, since people
were sharing their solutions) got to enter their e-mail addresses and
were informed that they would be contacted in few days.

* * * * *

By this time, someone noticed that the DNS entry for 845145127.com had
been removed. By using the IP (75.119.203.244) it was found that the
page that recently had GPS coordinates had changed yet again, to a
seemingly empty page. On a closer look it turned out to consist entirely
of spaces, tabs and linebreaks. Since every line contained a multiple of
eight spaces/tabs, it seemed likely to be a plain binary code. This was
confirmed by:

    je@isis:~/3301$ wget -q -O- http://75.119.203.244/ > 3301.html
    je@isis:~/3301$ perl -pne 's/[^\s]//g;s/\t/0/g;s/ /1/g;s{([01]{8})}{chr(oct("0b$1)"))}sgex' < 3301.html

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    162667212858
    414974253863
    598852142735
    876873892385
    935691396441
    316744223127
    427566844663
    644169769482
    889296759263
    963846244281
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.11 (GNU/Linux)

    iQIcBAEBAgAGBQJPDRkvAAoJEBgfAeV6NQkPVuMP/3ZyAgwsko/B2T9Ew1yqAKVy
    K9//wIWCRvMyZ4k79ApqvOJAlezgHTsAM8XG/I71bAG+2wMOXNJfTj/SFONEEbS5
    BOp9UP7LHn1j3NKoESrDzsKd+u3oHoNnhs628aLrc8uDqbn/6DNUnObu5Tn3unu0
    zZ3NjSs/A5QQX8O56RsK81eSJ2fifbr4NYfHBeUTeVe17nsr48WQI7qc9UVWlPsM
    91FWsvhX+WohX8DyFWJmtz0lLvmh3jN+oE8WFPTVbcVCM+eiDt0TqkUNlmq/fxbd
    X2Sbs8zMxDXNQWrw58TcSC6oLfXSXZnjh8uTMwrQ0tNdRXHDndgPiurXz62XjVjf
    4AhSXBoXF9CHTOyGGEqvfNvFMKyz968iMZDXDNBrM8pkxx1xBHhAnoEznVpeMhII
    +IfBTnV8x9lSNgFhmham5eEZlWvqRidqes8EAriqGA6uZokCq7X1IeMHo52ACWmP
    2bJsCV5wZDc52c3JnwKe+cAcbsA4OWCNEH29lAsgFw5079BP8lkpY3AH2+8kqs0X
    QvqsaMuUq5ZHEaZMgdD0VKYlRrKdhOiDjtJVxoXk1b7YBOV8dZZBXJbEIbTvaof4
    yhgUObovx/VFGmsenp+j3nBCxgEO22SgNW3B3pN0yuIMCqccWEZ1nME/QOwLa85n
    HOmElIXvK13Q9m545RtP
    =Q1Fy
    -----END PGP SIGNATURE-----

The message simply contains ten different 12 digit numbers. As it turns
out, each of these correspond to image URLs such as:
http://75.119.203.244/NUMBER.jpg

Each of these images contains a hidden message that can be extracted
with outguess, and it turns out that it's the same messages that could
be extracted from the images found through QR codes on notes at the
GPS-coordinates mentioned earlier. Turns out we didn't have to be at one
of those locations after all. :)

Regarding the remaining code, it is very likely to refer to the same
.onion site as before. Just to be sure, and not to leave out any piece
of the puzzle, it would be nice to solve that one too though.

My thoughts so far are these:

"In twenty-nine volumes, knowledge was once contained" may refer to the
11th edition of Encyclopedia Britannica, which consisted of exactly 29
volumes and that is now in the public domain and available for download
since it was released back in 1910-1911.

Regarding "How many lines of the code remained when the Mabinogion
paused?", note that the text posted to the reddit page is from "The Lady
of the Fountain", which is the first out of eleven stories from medieval
Welsh manuscripts in the collection called the Mabinogion. Also note
that there was a pause for about 24 hours after the 65:th encoded line
of text was posted to the reddit page. After that, new encoded lines
have been posted about every 6th or 7th hour.

Assuming the code will continue until "The Lady of the Fountain" is
finished, we will need to figure out the total number of lines in that
story. To do that, we need to find the text that 3301 uses as their
source, so that line breaks are placed on the same positions. After a
bit of searching around it turns out that the source that 3301 uses is
from Project Gutenberg
([here](http://www.gutenberg.org/cache/epub/5160/pg5160.txt)). Blank
lines are discarded, and lines with only one word on them are being
appended to the preceding line. Applying those rules to the entire text
of "The Lady of the Fountain" results in a total of 833 lines. Thus, the
number of lines of code that remained when the Mabinogion paused is 833
- 65 = 768 (which also happens to be 512+256, but I guess that may be a
mere coincidence after all).

Finally we have "Go that far in from the beginning and find my first
name", which could mean a number of things. My guess is that we should
go 768 words, sentences, word definitions, characters or pages into the
11th edition of Encyclopedia Britannica. Question is where we are
supposed to go from there, since it ends with "and find my first name".
By this, I assume we should only find a certain name at this particular
position, and then from this name find the actual text to use as the key
for the book code.

I also noticed that the code for this part only use 27 lines, with
columns ranging from 1-66 and many columns being above 30-40. This rules
out most poems, that usually don't have long lines. It could very well
be a text straight from the Encyclopedia Britannica, however. Due to the
large number of possibilities I have not looked into it much further
than this, and so far I don't think anyone have come up with the
solution for this particular puzzle. So, anyone up for it? :)

### 16 Responses

1.  ![image](http://0.gravatar.com/avatar/c4fe2d6eea66808cd352cbb49c5f46d1?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Jean**

    Contact me :)

    2012-01-14 at 11:11 \

    [Reply](/cicada-3301/?replytocom=363#respond)

2.  ![image](http://0.gravatar.com/avatar/a21f04b7cd9ba93211b0e1254fedd370?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **The Doctor**

    Im working on it….

    2012-01-16 at 21:15 \

    [Reply](/cicada-3301/?replytocom=374#respond)

3.  ![image](http://0.gravatar.com/avatar/aa7d2c561fe557690fae5ebd0de6d69e?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **boss**

    I love your work.\
     [boss@tormail.net](mailto:boss@tormail.net)

    2012-01-19 at 10:15 \

    [Reply](/cicada-3301/?replytocom=390#respond)

4.  ![image](http://1.gravatar.com/avatar/7f2b79cd5329a2c04562a873211e5d16?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **vander**

    I have no clue about anything, but I just came up here and I want to
    congratulate you on your shocking skills and intelligence. Great
    work, sir.

    (do not suspect, this comment is not a hint xD )

    2012-01-19 at 10:38 \

    [Reply](/cicada-3301/?replytocom=391#respond)

5.  ![image](http://0.gravatar.com/avatar/22890a8a34b7fab6dc14de65a1220456?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **marty**

    if there is anything i can do to help please let me know, it would
    be a shame not to see this through seeing how much effort you have
    put i

    2012-01-19 at 13:42 \

    [Reply](/cicada-3301/?replytocom=392#respond)

6.  ![image](http://0.gravatar.com/avatar/e093d5d19a92a06c7dbbfa183e76fe9b?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Janus**

    It´s sad that this requires Internet/Coding skills, the search for
    highly intelligent people should not be limited for those which have
    this skills, but for everyone.\
     But maybe they search that kind of people, who ever “they” are.\
     My guess is that they are from 4Chan,Reddit or something similar.\
     Irc Channels, Coding and things set up at different places on the
    earth which is kind of easy if you ask the right people on the
    internet:\
     Anyway it kind of motivates me, i will try to solve it even without
    greater knowlege this matter.

    2012-01-19 at 14:13 \

    [Reply](/cicada-3301/?replytocom=393#respond)

    -   ![image](http://1.gravatar.com/avatar/1aaa3a069df4873cfc2f23cf20cd0aec?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

        **[Marcus Wanner](http://marcus.wanners.net/)**

        Janus, every thing here can be done by hand (aside from the PGP
        verification and outguess). Je’s use of UNIX utilities to solve
        this is a convenience, not a necessity. The same can be done
        with almost any file; manipulating text in a shell is one of the
        most fun and easy ways to do so.

        Now I will concede that later in the puzzle, things do get more
        technical. To the point at which this narrative terminates,
        however, there is little need of the skills you mention.

        2012-01-25 at 00:09 \

        [Reply](/cicada-3301/?replytocom=407#respond)

7.  ![image](http://0.gravatar.com/avatar/0a7409515085e54e7e7b0041278ff325?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Procyon**

    “Thus, the number of lines of code that remained when the Mabinogion
    paused is 833 – 65 = 768″

    Don’t know if it’s important, but the first edition of Encyclopedia
    Britannica was published in 1768. So maybe we shouldn’t be looking
    at 11th edition, but first. The question – where to find it? :D\
     I just found out about this today, so I still haven’t worked
    anything up.

    2012-01-24 at 04:30 \

    [Reply](/cicada-3301/?replytocom=404#respond)

8.  ![image](http://0.gravatar.com/avatar/0a7409515085e54e7e7b0041278ff325?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Procyon**

    In the preface of the first edition, in the place of 768th word is a
    sign for repetition, since the essay was written by the same author
    as the previous one. The name of the author is Charles Alston. Don’t
    know if I’m helping or spamming, tho.

    2012-01-24 at 04:57 \

    [Reply](/cicada-3301/?replytocom=405#respond)

9.  ![image](http://1.gravatar.com/avatar/955af39e5548ced23fcfaf216b0212ff?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **kala**

    Will you update this post if you find out more about this? Who do
    you think are “they”?

    2012-01-25 at 00:49 \

    [Reply](/cicada-3301/?replytocom=409#respond)

10. ![image](http://1.gravatar.com/avatar/7ad62bb77e7cadf471856f17fb1bb0ed?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Maria**

    Do you know anything about what happened from the point the e-mails
    have been sent on? The few people who got to the Tor site on time
    and submitted their addresses got an RSA encrypted message to
    decrypt. After that, I read there was a midi file with a hidden
    message to report back. What about after that? People suddenly got
    so secretive about sharing info. It’s like it’s really serious
    business. What the hell?

    2012-01-25 at 05:08 \

    [Reply](/cicada-3301/?replytocom=411#respond)

11. ![image](http://1.gravatar.com/avatar/fe5c101af51c004a38949bbff864736d?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Shizznit**

    It is likely a government or Anonymous recruiting…. personally i
    would let go.

    [WORDPRESS HASHCASH] The poster sent us ’0 which is not a hashcash
    value.

    2012-01-30 at 14:29 \

    [Reply](/cicada-3301/?replytocom=446#respond)

12. ![image](http://1.gravatar.com/avatar/fb67054491b38856e97900cf9539fa53?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **Kieran**

    You havnt heard anything more because the people who reported
    receiving those emails have dropped out of view/do not want to
    participate.

    It’s pretty suspicious of you ask me, there was one guy who was
    posting non stop about his progress, received the said email, and
    was never heard from again.

    It’s been speculated that it’s a hiring process for a highly funded
    hacker program that plans to permanent destroy Facebook…..they must
    have been paid a lot If they kept their mouths shut

    2012-02-01 at 14:30 \

    [Reply](/cicada-3301/?replytocom=457#respond)

13. ![image](http://1.gravatar.com/avatar/d0882f81f57ba6b4ff6a81bbb11c9523?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **frop**

    Any update on this? What about the midi file?\
     I was able to place my email on the 2nd TOR site after the first
    one was shut down…i never received an email tho :(

    2012-02-06 at 16:18 \

    [Reply](/cicada-3301/?replytocom=481#respond)

14. ![image](http://1.gravatar.com/avatar/165c8ee15062bb74cb334e91ced4fc86?s=75&d=http%3A%2F%2F1.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **noone**

    To those who have followed this game as I have from the beginning, I
    just wanted to take a moment and let you know that the “game” is
    over. Those who have made it in the end have received their final
    emails, which are confidential (however, if you search pastebin, you
    might just find some people who like to break the rules).

    As one of the players in this game, this has been an exciting
    experience. Now on to other things…

    2012-02-07 at 22:11 \

    [Reply](/cicada-3301/?replytocom=488#respond)

15. ![image](http://0.gravatar.com/avatar/8ce772bf731e8e8e694d0491dd382ffc?s=75&d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D75&r=G)

    **...Am...**

    Is there anyone who can post a link to proof or speculation of where
    this originated?

    2012-02-22 at 03:55 \

    [Reply](/cicada-3301/?replytocom=539#respond)
