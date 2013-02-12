#!/usr/bin/env python3
# Copyright (c) 2010, Aaron DeVore
# Released under the Don't Be A Douchbag License.
# Use responsibly. Contribute changes if you feel like it. No CP!

import urllib.request, urllib.error
import os
import posixpath
import json
import time
from optparse import OptionParser
from bs4 import BeautifulSoup

options = OptionParser()
options.add_option("-b", "--board", dest="board",
    default='mlp', help="board name")
options.add_option("-o", "--overwrite-images", dest="overwrite_images",
   default=False, help="Overwrite non-empty images", action="store_true")
options.add_option("-u", "--update", dest="update", action="store_true",
    default=False, help="update the thread")
options.add_option("-p", "--pause-update", type="int", dest="pauseUpdate",
    default=100, help="Wait time between thread updates")
options.add_option("--pause-image", type="int", dest="pause_image",
    default=1, help="Wait time between image downloads")


class Post(object):
    def __init__(self):
        self.image_name = self.image_location = self.image_original = None

    @property
    def has_image(self):
        return self.image_name is not None

    def __repr__(self):
        if self.image_name:
            return "%(id)s by %(poster)s with %(image)s" % self.__dict__
        else:
            return "{id} by {poster} with no {image}".format(self.__dict__)


def get_soup(board, thread):
    url = "http://boards.4chan.org/%s/res/%s" % (board, thread)
    print("downloading thread %s for board %s at %s" % (thread, board, url))
    f = urllib.request.urlopen(url)
    soup = BeautifulSoup(f)
    f.close()
    return soup


def parse_posts(soup):
    image_count = 1  # OP has to have an image
    op = parse_post(soup.find(True, 'opContainer'))
    posts = [op]

    for reply_container in soup.find_all(True, 'replyContainer'):
        reply = parse_post(reply_container)
        if reply.image_name:
            image_count += 1
        posts.append(reply)
        
    print("found {} posts with {} images".format(len(posts), image_count))
    return posts


def parse_post(container):
    p = Post()
    # id, poster, subject
    p.id = int(container["id"][2:])
    p.poster = container.find('span', 'name').text.strip()
    p.subject = container.find(True, 'subject').text.strip()

    post_number_tag = container.find('span', 'postNum')
    p.utc = post_number_tag["data-utc"]
    p.timestamp = post_number_tag.text.strip()

    file_text_tag = container.find(True, 'fileText')
    if file_text_tag:
        location_tag = file_text_tag.a
        p.image_location = "http:" + location_tag["href"]
        p.image_name = location_tag.text.strip()
        p.image_original = file_text_tag.span.text.strip()

    post_message_tag = container.find('blockquote', 'postMessage')
    message = []
    for child in post_message_tag.children:
        if isinstance(child, str):
            message.append(child)
        elif child.name == 'br':
            message.append('\n')
    p.text = ''.join(message)

    return p
    

def download_images(posts, dest, overwrite_images, pause_image):
    image_dir = os.path.join(dest, "images")
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    print("pause time between image requests:", pause_image)
    for post in posts:
        if post.has_image:
            local_path = os.path.join(image_dir, post.image_name)
            if os.path.exists(local_path):
                if not overwrite_images and os.path.getsize(local_path) != 0:
                    print("Skip: image %s already exists" % post.image_name)
                    continue
            print("downloading %s to %s" % (post.image_location, post.image_name))
            with open(local_path, 'wb') as f:
                try:
                    remote = urllib.request.urlopen(post.image_location)
                except urllib.error.HTTPError as e:
                    if e.code == 404:
                        print("image 404ed")
                    raise
                f.write(remote.read())
            time.sleep(pause_image) # be nice to the servers


def write_data(thread, posts, dest):
   target = os.path.join(dest, "thread.js")
   json_posts = []
   json_code = {}
   json_code['id'] = thread
   json_code['posts'] = json_posts
   for post in posts:
       json_posts.append({
               'id': post.id,
               'poster': post.poster,
               'subject': post.subject,
               'image': {
                   'name': post.image_name,
                   'original': post.image_original,
                   },
               'timestamp': post.timestamp,
               'utc': post.utc,
               'text': post.text,
               })
       print("writing thread data for %s to %s" % (thread, target))
       with open(target, 'w') as f:
           json.dump(json_code, f, indent=4)


def main():
    opts, args = options.parse_args()
    if len(args) != 2:
        print(options.usage)
    thread = args[0]
    baseDest = args[1]
    board = opts.board
    overwrite_images = opts.overwrite_images
    if opts.update:
        updates = -1
    else:
        updates = 1
    dest = os.path.join(baseDest, "%s-%s" % (board, thread))
    if not os.path.exists(dest):
        os.makedirs(dest)
    try:
        while updates != 0:
            updates -= 1
            soup = get_soup(opts.board, thread)
            posts = parse_posts(soup)
            download_images(posts, dest, overwrite_images, opts.pause_image)
            write_data(thread, posts, dest)
            if updates != 0:
                print("waiting %i seconds for next update" % opts.pauseUpdate)
                print("-" * 40)
                time.sleep(opts.pauseUpdate)
    except KeyboardInterrupt:
        print("Keyboard Interrupt, ending archiving")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Thread or image 404ed")
        else:
            raise

if __name__ == "__main__":
    main()
