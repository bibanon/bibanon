#!/bin/bash

# This script do the following:
# 1. uses the mediawiki2html script to convert the mediawiki to HTML.
# 2. uses pandoc to convert HTML to markdown (leaving any unknown HTML as raw)
# 3. htmltable2pandoc to convert HTML tables into markdown syntax.

find -type f -name \*.mediawiki | while read i; do
NAME=`echo $i | sed -e's/.mediawiki$//'`
  echo "Converting $NAME.mediawiki -> $NAME.md"
  python mediawiki2markdown.py $NAME.mediawiki > $NAME.md
  echo "Done"
  echo
done