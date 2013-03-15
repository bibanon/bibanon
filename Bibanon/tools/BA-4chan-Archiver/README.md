A quick and dirty python-based image downloader using the 4chan API for better, faster, and machine parsable 4chan thread archives.

Supports Mac OS X and Linux (make sure that Python 2.x is installed.)

Dependencies: Python 2.x, Bash

* [The Chandler - PyQt4 GUI interface for downloading images.](https://github.com/Dhole/4chan-image-dl.git)
* [img-downloader.py - Command line script.](https://github.com/socketubs/4chandownloader.git)
* grab-thread.sh - Just repeats the command:
    curl http://api.4chan.org/$boardid/res/$tnumber.json | python2 -mjson.tool > b-$tnumber.json

## Improvements:

* Windows version (by integrating into Chandler?)
* Integrate thread json grabber into The Chandler
* Create a json to html viewer for json posts, using Yotsuba CSS
