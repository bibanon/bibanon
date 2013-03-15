#!/usr/bin/env python
# coding: utf-8

#
# Initial release Nov. 5, 2009
# v6 release Jan. 20, 2009
# http://cal.freeshell.org
#
# Refactor, update and Python package
# by Socketubs (http://socketubs.net/)
# 09-08-12
#

import os
import time
import json
from docopt import docopt
import requests

doc = """4chandownloader.py, download 4chan thread images.

Usage:
  4chandownloader.py <url> <path> [--delay=<int>] [--thumbs]
  4chandownloader.py -h | --help
  4chandownloader.py -v | --version

Options:
  --thumbs            Download thumbnails
  --delay=<int>       Delay between thread checks [default: 20]
  -h --help           Show help
  -v --version        Show version
"""

def main(args):
    thread = args.get('<url>').split('/')[5]
    board  = args.get('<url>').split('/')[3]
    path   = args.get('<path>')
    thumbs = args.get('--thumbs', False)
    delay  = args.get('--delay')

    #Start
    while 1:
        r = requests.get('https://api.4chan.org/%s/res/%s.json' % (board, thread))

        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(os.path.join(path, board)):
            os.makedirs(os.path.join(path, board))
        if not os.path.exists(os.path.join(path, board, thread)):
            os.makedirs(os.path.join(path, board, thread))
        if thumbs:
            if not os.path.exists(os.path.join(path, board, thread, 'thumbs')):
                os.makedirs(os.path.join(path, board, thread, 'thumbs'))

        print(' :: Board: %s' % board)
        print(' :: Thread: %s' % thread)

        dst = os.path.join(path, board, thread)
        dst_thumbs = os.path.join(path, board, thread, 'thumbs')
        for post in r.json['posts']:
            if post.get('filename', False):
                if post.get('filedeleted', False):
                    continue
                file_name = '%s%s' % (post['tim'], post['ext'])
                file_path = os.path.join(dst, file_name)
                file_url  = 'https://images.4chan.org/%s/src/%s' % (board, file_name)
               
                if not os.path.exists(file_path):
                    print('%s downloading...' % file_name)
                    i = requests.get(file_url)
                    if i.status_code == 404:
                        print(' | Failed, try later (%s)' % file_url)
                    else:
                        open(file_path, 'w').write(i.content)
                else:
                    print('%s already downloaded' % file_name)

                if thumbs:
                    thumb_name = '%ss.jpg' % post['tim']
                    thumb_path = os.path.join(dst_thumbs, thumb_name)
                    thumb_url  = 'https://thumbs.4chan.org/%s/thumb/%s' % (board, thumb_name)
                    if not os.path.exists(thumb_path):
                        print('%s (thumb) downloading...' % thumb_name)
                        i = requests.get(thumb_url)
                        if i.status_code == 404:
                            print(' | Failed, try later (%s)' % thumb_url)
                        else:
                            open(thumb_path, 'w').write(i.content)
                    else:
                        print('%s (thumb) already downloaded' % thumb_name)

        json.dump(r.json, open(os.path.join(dst, '%s.json' % thread), 'w'))

        #Wait to execute code again
        print("Waiting %s seconds before retrying" % delay)
        time.sleep(int(delay))

if __name__ == '__main__':
    args = docopt(doc, version=0.3)
    main(args)
