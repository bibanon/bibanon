## Long Paragraphs

Historically, typewriters and text editors do not use visual word wrapping, and thus writers were forced to add hard line breaks for the same sentence. Even today, most text editors leave visual line wrapping disabled.

Since Markdown was designed to support writing in plain text files that have line wrap disabled, such as Windows Notepad, it has a special syntax for paragraphs. 

This causes Markdown to exhibit unexpected behavior. Here's an example:

```
This sentence has
line breaks in it
but it still will
be formatted as
one sentence by
Markdown
```

Markdown will ignore the line breaks within a paragraph, as shown below:

---

This sentence has
line breaks in it
but it still will
be formatted as
one sentence by
Markdown

---

On the other hand, paragraphs with one empty line between them will be left alone.

```
The two sentences
in this paragraph
will be wrapped.
Including this one.

But that paragraph
will be kept seperate
from this one.
```

Notice that the two paragraphs stay distinct in the example below:

---

The two sentences
in this paragraph
will be wrapped.
Including this one.

But that paragraph
will be kept seperate
from this one.

---

So what do you do if you want to prevent this behavior? One way is to divide the sentences to split into two paragraphs by adding a blank line between them. But that might not always be visually appropriate.

Instead, you can create your own line breaks with Markdown by adding two spaces `  ` at the end of the lines you want to seperate.

```
This paragraph has 
a line break here ->.  
That way it will not
collide with this
sentence.

Alternatively, in this  
paragraph, each line  
has line breaks created  
by placing two spaces at  
the end of each line  
```

Notice that the two sentences are kept in seperate lines by Markdown, because of the addition of two spaces `  ` at the end of the first sentence.

---

This paragraph has 
a line break here ->.  
That way it will not
collide with this
sentence.

Alternatively,  
in this paragraph  
all the line have  
line breaks created  
by two spaces at the  
end of each line  

---

While the BASC does not agree with Markdown's odd solution for an archaic problem, we have to follow this syntax rule to maintain compatibility with Markdown parsers.

## 4chan Transcription Guide

For greater readability, the BASC converts 4chan posts into Markdown format. These are some standards for transforming 4chan content into Markdown syntax.

### 4chan Quotes/Backlinks

On 4chan, when users reply to each other, they use backlinks which are then interpreted as URLs to the post ID. They look like this:

    >>1444444

However, these backlinks can get misinterpreted by Markdown as quotes. You must escape them with backslashes `\>\>`, and add two spaces at the end of the line `  ` to create a line break (so that Markdown doesn't smash it together with the next paragraph).

    \>\>1444444  

### 4chan Greentext

4chan Greentext stories are created due to `>` quote character producing green text for a certain line. Originally, they were designed to signify a vertabrim quote from another user. However, since post number references do a much better job, they are rarely used for this purpose.

Unfortunately, Github Flavored Markdown and most Markdown parsers don't allow colored text, and the `>` can be mistaken for an actual quote. Also, Markdown parsers typically treat any paragraph as one single line Therefore, all greentext stories will follow this standard format:

Here is a plain greentext story:

```markdown
>plain greentext story
>normally this text would be green
>greentext is a compromise between bullets and complete sentences
>they typically have no periods or capitalization.
```

That text will be garbled, shown like this in Markdown.

>plain greentext story
>normally this text would be green
>greentext is a compromise between bullets and complete sentences
>they typically have no periods or capitalization.

Instead, use this syntax: adding a `> \` to the beginning and two spaces `  ` at the end of each line.

```markdown
> \>plain greentext story  
> \>normally this text would be green  
> \>greentext is a compromise between bullets and complete sentences  
> \>they typically have no periods or capitalization.  
```

The `> ` syntax puts the line in a quotebox. The two spaces creates an elegantly invisible line break. The greentext's important `>` is escaped with a backslash `\>` so that Markdown will not interpret it as a quote.

Now the greentext will look far better:

> \>plain greentext story  
> \>normally this text would be green  
> \>greentext is a compromise between bullets and complete sentences  
> \>they typically have no periods or capitalization.  

### Spoiler Tags

