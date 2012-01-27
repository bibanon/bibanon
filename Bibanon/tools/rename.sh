for file in *.mdwn ; do mv $file `echo $file | sed 's/\(.*\.\)mdwn/\1md/'` ; done
 
for file in *; do [ -f "$file" ] && ( mv "$file" "$(echo $file | sed -e 's/_/-/g')" ); done