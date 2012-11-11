#!/usr/local/bin/python

# 4chan image grabber.
# Usage 4chanig.py [board] [thread number]"
# Written by clizana 
# cristian@lizana.in

# Some functions, I love functions.

def in_array(array, needle):
	for item in array:
		if(item==needle.lower()):
			return True
	return False

def number_files(array):
	number = 0
	for element in array['posts']:
		if element.has_key('filename'):
			number += 1
	return number
	
def download_file(url, file_name, curr_file, num_files):
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading file %s of %s (File Size: %s Bytes)" % (curr_file, num_files, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
		buffer = u.read(block_sz)
		if not buffer:
			break

		file_size_dl += len(buffer)
		f.write(buffer)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,

	f.close()

# What we need.	
import urllib, urllib2, simplejson, sys, os

# Valid Boards
BOARD_LIST = ['a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'gif' , 'h' , 'hr' , 'k' , 'm' , 'o' , 'p' , 'r' , 's' , 't' , 'u' , 'v' , 'vg' , 'w' , 'wg', 'i' , 'ic', 'r9k', 'cm' , 'hm' , 'y', '3' , 'adv' , 'an' , 'cgl' , 'ck' , 'co' , 'diy' , 'fa' , 'fit' , 'hc' , 'int' , 'jp' , 'lit' , 'mlp' , 'mu' , 'n' , 'po' , 'pol' , 'sci' , 'soc' , 'sp' , 'tg' , 'toy' , 'trv' , 'tv' , 'vp' , 'wsg' , 'x', 'q']

if len(sys.argv)==3 and (sys.argv[1]!="" and sys.argv[2]!="" and sys.argv[2].isdigit()):
	board = sys.argv[1]
	thread = sys.argv[2]
	IMG_PATH = "http://images.4chan.org/%s/src/" % (board)
	JSON_URL = "http://api.4chan.org/%s/res/%s.json" % (board, thread)
	
	#We check some stuff (maybe not too efficient)
	try:
		if not os.path.exists(thread):
			os.mkdir(thread)
	except:
		print "Error: creating the output dir"
		exit()
	
	if in_array(BOARD_LIST, board)==False:
		print "Error: The board doesn't exist"
		exit()
	try:
		results = simplejson.load(urllib.urlopen(JSON_URL))
		current_file = 1
		total_files = number_files(results)
		for result in results['posts']:
			if result.has_key('filename'): 
				if os.path.isfile("%s/%s%s" % (thread, result['filename'], result['ext']))==False:
					download_file("%s%s%s" % (IMG_PATH, result['tim'], result['ext']), "%s/%s%s" % (thread, result['filename'], result['ext']), "%s" % (current_file), "%s" % (total_files))
					#Using the urllib method without progress.
					#urllib.urlretrieve ("%s%s%s" % (IMG_PATH, result['tim'], result['ext']), "%s/%s%s" % (thread, result['filename'], result['ext']))
				current_file = current_file + 1
	except:
		print "The thread number is wrong or the thread doesn't exist anymore"
else:
	print "Usage 4chanthread.py [board] [thread number]"


