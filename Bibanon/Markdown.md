This page details the usage of the Markdown markup language.

Markdown is a commonly used markup language across the internet, used in blogs, Reddit, and some README files.

If it's too much to remember, note that there are buttons in the web interface that automatically place markup tags in the page.

## Markdown Basics

### Paragraphs

Paragraphs are blocks of text seperated by one or two lines. 

    This is a paragraph. It has two lines.

    Here is another paragraph.

Blocks of text without seperating lines will be combined into one paragraph.

    This is a paragraph. It has three lines.
    This line will be part of the same paragraph.

    Here is another paragraph.

### Italics

    *Italic*
    _Italic_

Either of these will produce _Italic_ *text*.

### Bold

    **Bold**
    __Bold__

Either of these will produce __Bold__ **text**

### Code

To insert code, indent lines by 4 spaces. Without this, the wiki might screw up the text.

    line 1 of code
    line 2 of code
    line 3 of code

### Lists

    * An item in a bulleted (unordered) list
	* A subitem, indented with 4 spaces
    * Another item in a bulleted list

    1. An item in a numbered (ordered) list
    2. Another item in an numbered list

### Headings

To make an HTML heading (titles for sections), put some hashes in front of the title. Hashes can also be placed after the text if wanted.

    ## Second-level heading

    #### Fourth-level heading

    ## Heading with extra hashes ##

Alternatively, this syntax can also be used for more readable headings.

    First-level Headings
    ====================

    Second-level Headings
    ---------------------

### Blockquotes

    > "This entire paragraph of text will be enclosed in an HTML blockquote element.
    Blockquote elements are reflowable. You may arbitrarily
    wrap the text (place line breaks) to your liking, and 
    it will all be parsed into a single blockquote element."

    > Blockquotes are like quoted text in email replies
    >> And, they can be nested

### Horizonal lines

Horizontal rules are created by placing three or more hyphens, asterisks, or underscores on a line by themselves. You may use spaces between the hyphens or asterisks.

    * * *
    ***
    *****
    - - -
    ---------------------------------------

### External links

To make a http address clickable, just add <> tags.

    <http://example-page.com/page>

To use alternate text, use this syntax.

    [Alternate hyperlink text](http://example-page.com/page)

### Wikilinks, Embedded images and File links

These functions are specific to Gollum and usable in all markup languages, so read [[Gollum Markup]] for more info on them.

## Extended Markdown

Gollum uses RDiscount for Markdown, which gives extended syntax.

### Centering

You can center text by surrounding it with arrows (-> and <-).

  ->this will be centered<-

### Tables

Simple tables can be made with dashes and pipes.

    aaa  | bbbb
    -----|------
    hello|sailor
    next | line

It's also possible to control horizonal alignment. A colon on the left will force left alignment (the default). A colon on the right will force right alignment. A colon on both sides will center the column.

      aaa  | bbbb | cccc
      :----|:----:|-----:
      hello|sailor|pirate
      next | line | third

If you want to get fancy, pipes can also be placed on the sides of the tables for a cleaner look.

    | aaa  | bbbb | cccc |
    |:---- |:----:|-----:|
    | hello|sailor|pirate|
    | next | line | third|

## Sources

* [[Wikipedia Article on Markdown|https://en.wikipedia.org/wiki/Markdown]]
* [[Markdown Cheat Sheet|http://warpedvisions.org/projects/markdown-cheat-sheet/]]
* [[Tedwise blog post on Markdown|http://tedwise.com/markdown/]]