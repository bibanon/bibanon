## File Formats

Because we will be archiving a variety of formatted materials which MUST stay readable and easily convertible in the near future, we'll make a preliminary list of what formats need to be used on the wiki.

### Documents

* Wiki Markup Language: **[[Markdown]]**
  * Markdown is an easily readable markup language that helps makes text files not only readable, but parsable. Since it's the most common non-html markup, all articles should be converted to this format.
* General text: **.md, .txt**
  * It's strongly recommended that all general text files (READMEs, Pastebin dump) be in the Markdown format, so that they can easily read and parsed as wikipages on this wiki. The file extension should be .txt outside the wiki (for Windows compatibility), and .md within the wiki.
* Office Documents: **OpenDocument**
  * All office documents need to be in the Open Document Format, an ISO standard for Office Applications. This format is more portable than .DOCX , and would probably be well-supported into the future, unlike .DOC. Microsoft Office supports reading and writing to this format easily, with only a few imperfections.
* Document Exchange: **PDF**
  * The majority of our source documents are in PDF format, which is not the easiest thing to work with. PDF is usually used for research papers or essays, which might use graphs or pictures in conjunction with text.
* Ebook: **EPUB**
  * A container format using web formats, optimized for e-books to be read on e-readers, rather than computers. It's quite portable and can be easily be generated from markdown with [[Pandoc]]. All books formatted for distribution MUST be in this format.

### Image formats

* Lossy compression: **JPEG**
  * Lossy compression is used for real-life pictures that do not need as much info for the eye. This includes anything that came out of a camera.
* Lossless compression: **PNG**
  * For any images with text, lines, computer screenshots, or vector graphics. It's preferable to get Anime drawings in this format. Should also be used when transparency is needed.
* Animations: **GIF**
  * The current standard for animated images. It's getting very old and has a limited color palette, and was already replaced by PNG in static images.
  * Alternative: **APNG**
    * An addon to the PNG format that gives animation abilities in addition the the existing abilities of GIF. It's supported well in Firefox, but not at all in other browsers or image viewers.
    * If we implement this [APNG compatibility library](https://github.com/davidmz/apng-canvas) in [[Gollum]], the images will animate fine in IE9, Chrome, and Safari. 

### Audio

* Lossy compression: **OGG**
  * A common [[Copyleft]] MP3 alternative that has built-in support in all browsers (with the exception of IE, which needs VLC installed). Should be used with music  or other recordings. 
    * We strongly recommend avoiding MP3, as it is a patented format with lawyers actively pursuing royalties for it's use. Also, OGG is 
  * To convert from mp3/wma to OGG, you can use [[http://media.io/|Media.io]], or use [Audacity](http://audacity.sourceforge.net/) to take in mp3 and export as OGG. To convert it back, import the OGG and export as MP3. Since both formats are lossy, there will be a marginal difference in sound quality going back and forth.
* Lossless compression: **FLAC**
  * A common [[Copyleft]] WAV alternative that reduces file size without compromising audio quality.