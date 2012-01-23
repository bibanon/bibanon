#!/bin/sh

# A shell script that tries its best to convert documents thrown at it
# to pandoc's extended markdown.
#
# Depends on: 
#    
# +   textutil:      an OS X only command line utility
# +   odt2pandoc.py: a tweaked version of odt2txt.py
# +   pdftohtml:     a utility for converting pdf to html
# +   pandoc:        a utility for converting lots of things
#                    to lots of things
#
# odt2pandoc.py: https://gist.github.com/1230498
# pdftohtml:     http://pdftohtml.sourceforge.net/
# pandoc:        http://johnmacfarlane.net/pandoc/
#


if [ ! $(which pandoc) ]; then
	echo "pandoc not found: unable to process files."
	exit
fi

for file in "$@"
do
    base="${file%%.*}"
    ext="${file#*.}"
	case $ext in
		doc | docx | webarchive | rtf | rtfd | odt )
			if [ ! $(which textutil) ]; then
				echo "textutil not found:"
				echo "  unable to process doc, docx, webarchive, rtf, rtfd, or odt files"
			    exit
			fi
    		textutil -format "$ext" -convert "html" -stdout "$file" \
				| pandoc -f html -t markdown -s --reference-links \
				    -o "${base}.markdown"
		;;
		pdf )
			if [ ! $(which pdftohtml) ]; then
				echo "pdftohtml not found: unable to process pdf files."
				exit
			fi
			pdftohtml -noframes -stdout "$file" \
				| pandoc -f html -t markdown --reference-links \
				     -o "${base}.markdown"   
        ;;
	    tex )
		    pandoc -f latex -t markdown -s --reference-links "$file" \
				-o "${base}.markdown"
		;;
		rst | html | latex | textile )
            pandoc -f "$ext" -t markdown -s --reference-links "$file" \
				-o "${base}.markdown"
		;;
        * )
			echo "Cannot convert $file: unknown type." ;;
	esac
done
