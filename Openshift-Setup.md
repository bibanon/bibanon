# Get your own gollom wiki onto OpenShift Express

This project is all about getting your own [gollum](https://github.com/github/gollum) wiki hosted on
Red Hat's [Openshift](https://openshift.redhat.com/app/). It's quite straight forward. Just sign up
for an OpenShift account and follow these instructions:

    $ git clone git@github.com:hferentschik/gollum-openshifted.git
    $ git remote rm origin
    $ rhc-create-domain -n <your-domain> -l <email> -p <password>
    $ rhc-create-app -a <app> -t rack-1.1 -l <email> -p <password> --nogit
    
        Found a bug? Post to the forum and we'll get right on it.
        IRC: #openshift on freenode
        Forums: https://www.redhat.com/openshift/forums

        Attempting to create remote application space: <app>
        Contacting https://openshift.redhat.com
        API version:    1.1.1
        Broker version: 1.1.1

        RESULT:
        Successfully created application: <app>

        Checking ~/.ssh/config
        Contacting https://openshift.redhat.com
        Found rhcloud.com in ~/.ssh/config... No need to adjust
        Now your new domain name is being propagated worldwide (this might take a minute)...

        Pulling new repo down
        Confirming application fubar is available
        Attempt # 1

        Success!  Your application is now published here:

           http://<app>-<your-domain>.rhcloud.com/

        The remote repository is located here:

           <git-url> 

        To make changes to your application, commit to <app>.
        Then run 'git push' to update your OpenShift Express space

    $ git remote add openshift <git-url>  
    $ git push -f openshift master
    
* \<your-domain\> - The domain name you want to use for your apps
* \<email\>       - The email you signed up with for OpenShift  
* \<password\>    - Your OpenShift password
* \<git-url\>     - The OpenShift git URL which you receive when executing _rhc-create-app_	(see above sample output)

The commits will be made by John Doe. Make sure to edit the action hook '[build](https://github.com/hferentschik/gollum-openshifted/blob/master/.openshift/action_hooks/build)'
to change this. The default login is wiki/wiki. This can be changed in [config.ru](https://github.com/hferentschik/gollum-openshifted/blob/master/config.ru).

See also

* http://www.highlevelbits.com/2011/11/gollum-wiki-reloaded.html
* http://www.highlevelbits.com/2011/11/my-precious-wiki.html

Let me know if you have problems ...

Enjoy,

Hardy