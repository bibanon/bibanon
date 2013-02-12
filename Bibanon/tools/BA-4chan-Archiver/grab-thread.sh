#!/bin/bash

$tnumbertnumber=`echo $1 | cut -c32-`

mkdir $tnumber
cd $tnumber

while :
	do
		wget -e robots=off -E -nd -nc -np -r -k -H -D images.4chan.org,thumbs.4chan.org $1
		cp $tnumber.html index.html
		sleep 10
	done
#backup
#echo "thread number?"
#read tnumber#mkdir
