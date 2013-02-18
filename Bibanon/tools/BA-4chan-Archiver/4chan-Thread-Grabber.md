With the introduction of 4chan's JSON API, archiving threads has never been easier!

## How to archive threads by hand

If you're on Linux, See "Getting Prettified JSON". This will give you the raw thread in JSON format, which can then be transformed into other things. 

Hopefully, we will be able to convert previously saved html into the new JSON format.

*[Adevore's 4chan Archiver](https://github.com/adevore/4chan-archiver) offers the best solution, using BeautifulSoup to save threads and images. Just install `python3-bs4` on debian/ubuntu. It, however, is now a roundabout solution with the advent of the 4chan API.

## Automatic archiver

If Fuuka is too big for you, here is a smaller chan-archiver made in PHP:

https://github.com/emoose/chan-archiver/

Here is a python wrapper for the 4chan API:

https://github.com/e000/py-4chan

### Saving images

The JSON also gives an MD5 hash for every image, in case the original was not saved and needs to be retrieved.

## Format

The format basically corresponds to the conventional 4chan link, with the addition of `.json` at the end and the `api` subdomain in the beginning.

In the examples below, subsitute the `<board>` tag with the board acronym (ex. `lit` for Literature) and the `<thread-id>` tag with the id of the OP post, which can be found in the original HTML link.

Conventional html link:

    http://boards.4chan.org/<board>/res/<thread-id>

JSON API link:
    
    http://api.4chan.org/<board>/res/<thread-id>.json

## Getting Prettified JSON

Using python:

    curl http://api.4chan.org/<board>/res/<thread-id>.json | python -mjson.tool

Using perl:

    curl http://api.4chan.org/<board>/res/<thread-id>.json | json_pp
    
## Converting JSON to Markdown

## Saving Images

Here is a node.js script to gather full images from a certain thread until it is no longer reachable.

https://github.com/ypocat/4chan

The best python script for image grabbing. Also takes in times.

https://github.com/crypt3lx2k/4chan-Image-Scraper

Here is an equivalent python script that also watches, and is extensible to any chan:

https://github.com/lunanoko/4chan-image-downloader
