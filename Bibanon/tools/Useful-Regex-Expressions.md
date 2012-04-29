Mass Filename editing
---------------------

# Rename all .mdwn to .md
for file in *.mdwn ; do mv $file `echo $file | sed 's/\(.*\.\)mdwn/\1md/'` ; done

# Replace all underscores with dashes
for file in *; do [ -f "$file" ] && ( mv "$file" "$(echo $file | sed -e 's/_/-/g')" ); done

# Add file extension to every file
find . -type f -exec mv '{}' '{}'.mediawiki \;

# Recursively replace spaces with dashes
find . -type f -exec mv '{}' "$(echo '{}' | sed -e 's/ /-/g')" \;

# rename every *.htm file *.html
for f in *htm ; do mv $f `basename $f htm`html; done

# Space to underscores, append .mp3
for e in *; do mv "$e" "`echo $e | sed -e 's/\ /_/g'`.mp3"; done

Useful Regexes
---------------

# Italics (mediawiki to markdown)
# ex. 
f: ''(.+)''
r: _\1_

# Replace all broken mediawiki links with fixed wikilinks (Currently does not detect this:) [4chan Threads](/4chan_Threads) -> [[4chan]]) 
# ex. [4chan](/4chan)
f: \[(\w+)\]\(/\w+\)
r: [[\1]]

# Replace all broken mediawiki board links with fixed wikilinks
# ex. [/b/](//b/) -> [[/b/]]
f: \[/(\w+)/\]\(//\w+/\)
r: [[/\1/]]

# Replace Mediawiki titles with Markdown ones (flawed: MUST have spaces between equal signs)
# ex. == Title == -> ## Title ## OR === Subtitle === -> ### Subtitle ###
f: =+ (.+) =+
r: ## \1 ##

# Replace Mediawiki quotes with Markdown quotes
# ex. : (quote here) --> > (quote here)
f: \n:
r: \n>