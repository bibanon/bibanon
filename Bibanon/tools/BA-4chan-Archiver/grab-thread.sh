#!/bin/bash

boardid="$1"
tnumber="$2"

echo "$boardid $tnumber"

echo "Starting thread text archival..."
while :
	do
		curl http://api.4chan.org/$boardid/res/$tnumber.json | python2 -mjson.tool > b-$tnumber.json
		sleep 10
	done
#backup
#echo "thread number?"
#read tnumber#mkdir
