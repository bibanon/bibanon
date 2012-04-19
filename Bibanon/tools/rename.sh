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