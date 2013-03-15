With the introduction of 4chan's JSON API, archiving threads has never been easier!

## How to archive threads by hand

If you're on Linux, See "Getting Prettified JSON". This will give you the raw thread in JSON format, which can then be transformed into other things. 

Hopefully, we will be able to convert previously saved html into the new JSON format.

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