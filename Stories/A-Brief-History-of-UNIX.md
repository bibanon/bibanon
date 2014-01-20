    ... floating around again ...
    ... originated in rec.humor.funny - January 1993 ...
    ... Ian Horswill (ian@ai.mit.edu) ...

Unix was a program gone bad. Born into poverty, its parents, the phone company, couldn't afford more than a roll of teletype paper a year, so Unix never had decent documentation and its source files had to go without any [[comments]] whatsoever.  Year after year, Papa Bell would humiliate itself asking for rate increases so that it could feed its [[child]].  Still, Unix had to go to [[school]] with only two and three letter command names because the phone company just couldn't afford any better.  At school, the other operating systems with real command names, and even command completion, would taunt poor little Unix for not having any job or terminal management facilities or for having to use its file system for interprocess communication and locking. 

Then, bitter and emasculated by its poverty, the phone company began to drink. During lost weekends of drunken excess, it would brutally beat poor little Unix about the face and neck. Eventually, Unix ran away from home.  Soon it was living on the streets of Berkeley.  There, Unix got involved with a bad crowd.  Its life became a degrading journey of drugs and debauchery.  To keep itself alive, it sold cheap source licenses for itself to universities which used it for medical experiments.  Being wantonly hacked by an endless stream of nameless, faceless undergraduates, both [[men]] and [[women]], often by more than one at the same time, Unix fell into a hell-hole of depravity. 

And so it was that poor little Unix began to go [[insane]].  It retreated steadily into a dreamworld, the only place where it felt safe.  It took heroin and dreamed of being a real operating system. 

It took LSD and dreamed of being a raspberry flavored three-toed yak. 

It liked that better.  As Unix became increasingly attracted to LSD, it would spend weekends reading Hunter Thompson and taking cocktails of [[acid]] and speed while writing crazed poetry in which it found deep meaning but which no one else could understand:

    <pre>
    $sed <$mf >$mf.new -e '1,/^# AUTOMATICALLY/!d'

    make shlist || ($echo "Searching for .SH files..."; \
	    $echo *.SH | $tr ' ' '\012' | $egrep -v '\*' >.shlist)
    if $test -s .deptmp; then
	for file in `cat .shlist`; do
	    $echo `$expr X$file : 'X\(.*\).SH'`: $file config.sh \; \
		/bin/sh $file >> .deptmp
	done
	$echo "Updating $mf..."
	$echo "# If this runs make out of memory, delete /usr/include lines." \
	    >> $mf.new
	$sed 's|^\(.*\.o:\) *\(.*/.*\.c\) *$|\1 \2; '"$defrule \2|" .deptmp \
	   >>$mf.new
    else
	make hlist || ($echo "Searching for .h files..."; \
	    $echo *.h | $tr ' ' '\012' | $egrep -v '\*' >.hlist)
	$echo "You don't seem to have a proper C preprocessor.  Using grep instead."
	$egrep '^#include ' `cat .clist` `cat .hlist`  >.deptmp
	$echo "Updating $mf..."
	<.clist $sed -n							\
	    -e '/\//{'							\
	    -e   's|^\(.*\)/\(.*\)\.c|\2.o: \1/\2.c; '"$defrule \1/\2.c|p"
	\
	    -e   d							
	\
	    -e '}'							
	\
	    -e 's|^\(.*\)\.c|\1.o: \1.c|p' >> $mf.new
	<.hlist $sed -n 's|\(.*/\)\(.*\)|s= \2= \1\2=|p' >.hsed
	<.deptmp $sed -n 's|c:#include "\(.*\)".*$|o: \1|p' | \
	   $sed 's|^[^;]*/||' | \
	   $sed -f .hsed >> $mf.new
	<.deptmp $sed -n 's|c:#include <\(.*\)>.*$|o: /usr/include/\1|p' \
	   >> $mf.new
	<.deptmp $sed -n 's|h:#include "\(.*\)".*$|h: \1|p' | \
	   $sed -f .hsed >> $mf.new
	<.deptmp $sed -n 's|h:#include <\(.*\)>.*$|h: /usr/include/\1|p' \
	   >> $mf.new
	for file in `$cat .shlist`; do
	    $echo `$expr X$file : 'X\(.*\).SH'`: $file config.sh \; \
		/bin/sh $file >> $mf.new
	done
    fi
    </pre>

Eventually, Unix began walking down Telegraph Avenue talking to itself, saying "Panic: freeing free inode," over and over again.

Sometimes it would accost perfect strangers and yell "Bus error (core dumped)!" or "UNEXPECTED INCONSISTENCY: RUN FSCK MANUALLY!" at them in a high pitched squeal like a chihuahua with amphetamine psychosis.  Upstanding citizens pretended it was invisible.  Mothers with children crossed to the other side of the street. 

Then one evening Unix watched television, an event which would change its life.  There it discovered professional wrestling and knew that it had found its true calling.  It began to take huge doses of corticosteroids to build itself up even bigger than the biggest of the programs which had beaten it up as a child.  It ate three dozen pancakes and four dozen new features for breakfast each day.  As the complications of the steroids grew worse, its internal organs grew to the point where Unix could no longer contain them.  First the kernel grew, then the [[C]] library, then the number of daemons.  Soon one of its window systems was requiring two megabytes of swap space for each open window.  Unix began to bulge in strange, unflattering places.  But Unix continued to take the drugs and its internal organs continued to grow.  They grew out its ears and nostrils.  They placed incredible stresses on Unix's brain until it finally liquefied under pressure. 

Soon Unix had the mass of Andre the Giant, the body of the Elephant Man, and the mind of a forgotten Jack Nicholson character. 

The worst strain was on Unix's mind.  Unable to assimilate all the conflicting patchworks of features it had ingested, its personality began to fragment into millions of distinct, incompatible operating systems.  People would cautiously say "good morning Unix.  And who are we today?" and it would reply "Beastie" ([[BSD]]), or "Domain", or "I'm System III, but I'll be System V tomorrow."  [[e-Psychiatrist|Psychiatrist]]s labored for years to weld together the two major poles of Unix's personality, "Beasty Boy", an inner-city youth from Berkeley, and "Belle", a southern transvestite who wanted a to be a woman.
With each attempt, the two poles would mutate, like psychotic retroviruses, leaving their union a worthless blob of protoplasm requiring constant life support to remain compatible with its parent personalities. 

Finally, unbalanced by its own cancerous growth, Unix fell into a vat of toxic radioactive wombat urine, from which it emerged, skin white and hair green.   It smelled like somebody's dead grandmother. 

With a horrible grin on its face, it set out to conquer the world.