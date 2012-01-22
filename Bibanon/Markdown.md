## PAGE LINKS

To link to another Gollum wiki page, use the Gollum Page Link Tag.

    [[Frodo Baggins]]

The above tag will create a link to the corresponding page file named
`Frodo-Baggins.ext` where `ext` may be any of the allowed extension types. The
conversion is as follows:

  1. Replace any spaces (U+0020) with dashes (U+002D)
  2. Replace any slashes (U+002F) with dashes (U+002D)

If you'd like the link text to be something that doesn't map directly to the
page name, you can specify the actual page name after a pipe:

    [[Frodo|Frodo Baggins]]

The above tag will link to `Frodo-Baggins.ext` using "Frodo" as the link text.

The page file may exist anywhere in the directory structure of the repository.
Gollum does a breadth first search and uses the first match that it finds.

Here are a few more examples:

    [[J. R. R. Tolkien]] -> J.-R.-R.-Tolkien.ext
    [[Movies / The Hobbit]] -> Movies---The-Hobbit.ext
    [[モルドール]] -> モルドール.ext

## OTHER TAGS

A variety of Gollum tags use a double bracket syntax. For example:

    [[Link]]

Some tags will accept attributes which are separated by pipe symbols. For
example:

    [[Link|Page Title]]

In all cases, the first thing in the link is what is displayed on the page.
So, if the tag is an internal wiki link, the first thing in the tag will be
the link text displayed on the page. If the tag is an embedded image, the
first thing in the tag will be a path to an image file. Use this trick to
easily remember which order things should appear in tags.

Some formats, such as MediaWiki, support the opposite syntax:

    [[Page Title|Link]] 
