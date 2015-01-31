#!/usr/bin/env python
# encoding: utf-8


"""
imguralbum.py - Download a whole imgur album in one go.

Provides both a class and a command line utility in a single script
to download Imgur albums.

MIT License
Copyright Alex Gisby <alex@solution10.com>
"""


import sys
import re
import urllib.request, urllib.parse, urllib.error
import os
import math


help_message = """
Quickly and easily download an album from Imgur.

Format:
    $ python imguralbum.py [album URL] [destination folder]

Example:
    $ python imguralbum.py http://imgur.com/a/uOOju#6 /Users/alex/images

If you omit the dest folder name, the utility will create one with the same name
as the album 
(for example for http://imgur.com/a/uOOju it'll create uOOju/ in the cwd)
"""


class ImgurAlbumException(Exception):
    def __init__(self, msg=False):
        self.msg = msg


class ImgurAlbumDownloader:
    def __init__(self, album_url):
        """
        Constructor. Pass in the album_url that you want to download.
        """
        self.album_url = album_url

        # Callback members:
        self.image_callbacks = []
        self.complete_callbacks = []

        # Check the URL is actually imgur:
        match = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/a/([a-zA-Z0-9]+)(#[0-9]+)?", album_url)
        if not match:
            raise ImgurAlbumException("URL must be a valid Imgur Album")

        self.protocol = match.group(1)
        self.album_key = match.group(3)

        # Read the no-script version of the page for all the images:
        noscriptURL = "http://imgur.com/a/" + self.album_key + "/noscript"

        try:
            self.response = urllib.request.urlopen(url=noscriptURL)
            response_code = self.response.getcode()
        except Exception as e:
            self.response = False
            response_code = e.code
        
        if not self.response or self.response.getcode() != 200:
            raise ImgurAlbumException("Error reading Imgur: Error Code %d" % response_code)

        # Read in the images now so we can get stats and stuff:
        html = self.response.read().decode('utf-8')
        self.images = re.findall('<img src="(\/\/i\.imgur\.com\/([a-zA-Z0-9]+\.(jpg|jpeg|png|gif)))(\?[0-9]+)?"', html)


    def num_images(self):
        """
        Returns the number of images that are present in this album.
        """
        return len(self.images)


    def album_key(self):
        """
        Returns the key of this album. Helpful if you plan on generating your own
        folder names.
        """
        return self.album_key


    def on_image_download(self, callback):
        """
        Allows you to bind a function that will be called just before an image is
        about to be downloaded. You'll be given the 1-indexed position of the image, it's URL 
        and it's destination file in the callback like so:
            my_awesome_callback(1, "http://i.imgur.com/fGWX0.jpg", "~/Downloads/1-fGWX0.jpg")
        """
        self.image_callbacks.append(callback)


    def on_complete(self, callback):
        """
        Allows you to bind onto the end of the process, displaying any lovely messages
        to your users, or carrying on with the rest of the program. Whichever.
        """
        self.complete_callbacks.append(callback)


    def save_images(self, foldername=False):
        """
        Saves the images from the album into a folder given by foldername.
        If no foldername is given, it'll use the cwd and the album key.
        And if the folder doesn't exist, it'll try and create it.
        """
        # Try and create the album folder:
        if foldername:
            albumFolder = foldername
        else:
            albumFolder = self.album_key

        if not os.path.exists(albumFolder):
            os.makedirs(albumFolder)

        # And finally loop through and save the images:
        for (counter, image) in enumerate(self.images, start=1):
            image_url = "%s:%s" % (self.protocol, image[0])

            # Fetch hi-res images (Fixes https://github.com/alexgisby/imgur-album-downloader/issues/5)
            image_url = re.sub(r"([a-zA-Z0-9]+)(h)\.(jpg|jpeg|png|gif)$", r"\1.\3", image_url)

            prefix = "%0*d-" % (
                int(math.ceil(math.log(len(self.images) + 1, 10))),
                counter
            )
            path = os.path.join(albumFolder, prefix + image[1])

            # Run the callbacks:
            for fn in self.image_callbacks:
                fn(counter, image_url, path)

            # Actually download the thing
            if os.path.isfile(path):
                print ("Skipping, already exists.")
            else:
                try:
                    urllib.request.urlretrieve(image_url, path)
                except:
                    print ("Download failed.")

        # Run the complete callbacks:
        for fn in self.complete_callbacks:
            fn()


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 1:
        # Print out the help message and exit:
        print (help_message)
        exit()

    try:
        # Fire up the class:
        downloader = ImgurAlbumDownloader(args[1])
        print(("Found {0} images in album".format(downloader.num_images())))

        # Called when an image is about to download:
        def print_image_progress(index, url, dest):
            print(("Downloading Image %d" % index))
            print(("    %s >> %s" % (url, dest)))
        downloader.on_image_download(print_image_progress)

        # Called when the downloads are all done.
        def all_done():
            print ("")
            print ("Done!")
        downloader.on_complete(all_done)

        # Work out if we have a foldername or not:
        if len(args) == 3:
            albumFolder = args[2]
        else:
            albumFolder = False

        # Enough talk, let's save!
        downloader.save_images(albumFolder)
        exit()

    except ImgurAlbumException as e:
        print(("Error: " + e.msg))
        print ("")
        print ("How to use")
        print ("=============")
        print (help_message)
        exit(1)
