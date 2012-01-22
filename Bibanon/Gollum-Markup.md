Gollum has it's own function syntax, which can be used along with any other markup language.

## Page Links

To link to another Gollum wiki page, use the Gollum Page Link Tag.

    [[Frodo Baggins]]

The above tag will create a link to the corresponding page file named
`Frodo-Baggins.ext` where `ext` may be any of the allowed extension types.  Spaces will be converted to dashes, and slashes to 3 dashes.

If you'd like the link text to be something other than the existing page name, you can specify the actual page name after a pipe:

    [[Frodo|Frodo Baggins]]

The above tag will link to `Frodo-Baggins.ext` using "Frodo" as the link text.

Note that some formats, such as Mediawiki, support the opposite syntax:

    [[Frodo Baggins|Frodo]] 

The page file may exist anywhere in the directory structure of the repository.
Gollum will search all directories and use the first match that it finds.

Here are a few more examples:

    [[J. R. R. Tolkien]] -> J.-R.-R.-Tolkien.ext
    [[Movies / The Hobbit]] -> Movies---The-Hobbit.ext
    [[モルドール]] -> モルドール.ext

## External Links

As a convenience, simple external links can be placed within brackets and they will be linked to the given URL with the URL as the link text. For example:

    [[http://example.com]]

External links must begin with either "http://" or "https://". If you need
something more flexible, you can resort to the link syntax in the page's
underlying markup format.

## Images, Files, and other media

### File Links

To link to static files that are contained in the Gollum repository you should
use the Gollum File Link Tag.

    [[Gollum|gollum.pdf]]

The first part of the tag is the link text. The path to the file appears after
the pipe.

### Images

To display images that are contained in the Gollum repository you should use
the Gollum Image Tag. This will display the actual image on the page.

    [[gollum.png]]

In addition to the simple format, there are a variety of options that you
can specify between pipe delimiters.

To specify alt text, use the `alt=` option. Default is no alt text.

    [[gollum.png|alt=Gollum and his precious wiki]]

To place the image in a frame, use the `frame` option. When combined with the
`alt=` option, the alt text will be used as a caption as well. Default is no
frame.

    [[gollum.png|frame|alt=Gollum and his precious wiki]]

To specify the alignment of the image on the page, use the `align=` option.
Possible values are `left`, `center`, and `right`. Default is `left`.

    [[gollum.png|align=center]]

To float an image so that text flows around it, use the `float` option. When
`float` is specified, only `left` and `right` are valid `align` options.
Default is not floating. When floating is activated but no alignment is
specified, default alignment is `left`.

    [[gollum.png|float]]

To specify a max-width, use the `width=` option. Units must be specified in
either `px` or `em`.

    [[gollum.png|width=400px]]

To specify a max-height, use the `height=` option. Units must be specified in
either `px` or `em`.

    [[gollum.png|height=300px]]

Any of these options may be composed together by simply separating them with
pipes.

## ESCAPING GOLLUM TAGS

If you need the literal text of a wiki or static link to show up in your final
wiki page, simply preface the link with a single quote (like in LISP):

    '[[Page Link]]
    '[[File Link|file.pdf]]
    '[[image.jpg]]

This is useful for writing about the link syntax in your wiki pages.

## HTML

Sometimes, markup languages are not enough, so a few HTML tags can be used inside wiki pages.

For security and compatibility reasons Gollum wikis may not contain custom CSS or JavaScript. These tags will be stripped from the converted HTML. See [[Sanitization]] for more details on what tags and attributes are allowed.

## SYNTAX HIGHLIGHTING

In page files you can get automatic syntax highlighting for a wide range of
languages (courtesy of [Pygments](http://pygments.org/) - must install
separately) by using the following syntax:

    ```ruby
      def foo
        puts 'bar'
      end
    ```

The block must start with three backticks (as the first characters on the
line). After that comes the name of the language that is contained by the
block. The language must be one of the `short name` lexer strings supported by
Pygments. See the [list of lexers](http://pygments.org/docs/lexers/) for valid
options.

If the block contents are indented two spaces or one tab, then that whitespace
will be ignored (this makes the blocks easier to read in plaintext).

The block must end with three backticks as the first characters on a
line.

## MATHEMATICAL EQUATIONS

Page files may contain mathematic equations in TeX syntax that will be nicely
typeset into the expected output. A block-style equation is delimited by `\[`
and `\]`. For example:

    \[ P(E) = {n \choose k} p^k (1-p)^{ n-k} \]

Inline equations are delimited by `\(` and `\)`. These equations will appear
inline with regular text. For example:

    The Pythagorean theorem is \( a^2 + b^2 = c^2 \).