Basic rule: Security is a continuing process, not a state. Do audits on a regular and scheduled basis. And do encrypted backups. Backups are important, as there are two types of people, those who have backups and those who have lost their data.

## Protips

* use the operating system you are familiar with (Linux and Unix are better though, way easier to secure)
* uninstall everything you not need
* disable all remote tools
* shred or encrypt /temp, /var/temp and all world-readable files
* Encrypt your hard disk (Truecrypt : www.truecrypt.org)
* Debian and other linux distros offer to encrypt the harddrive during installation. Use it.
* Use a distro that boots from DVD/CD/USB
* Never ever keep logs
* Shutdown all unneeded services
* Use a firewall
* Use random password generators (KeePassX is a great tool for keeping such passwords somewhere safe)

* Public access points are perfect - just about. (correlating logins with CCTV could prove disastrous so security cameras should be avoided while using such 'free' services. Cyber cafés, Mc Donalds, and many companies offer Free internet access, remember though, not to surf those nets without a VPN and/or Tor.
* Keep private keys (pgp/gnupgp) in a removable device, and that removable device away from curious eyes. Encrypt the private key before doing this.
* Keep VPN certs away from curious eyes via removable device, or common hidden folders.
* Never use the same users/passwords on reinstall. Take the time to create a new one each time. Use password generators.
* BE paranoid. All rare activity in your computer must be checked and monitored. That will provide 2 things: knowledge once you identify it, and added safety. 

## Detecting potentially security flaws on Linux

But be careful, if you don't know how to read Lynis' output, you'll become paranoid deluxe.

* http://www.rootkit.nl/projects/lynis.html

Scanner for rootkits, backdoors and local exploits on *Nix

Again, if you don't know how to read Rootkit Hunters output, you'll get paranoid.

* http://www.rootkit.nl/projects/rootkit_hunter.html

## Destroying data securely

### Unix/Linux

To securely destroy data under *Nix you have some possibillities. The command shred -u overwrites

singe files and deletes them finally, with wipe -rcf you overwrite and delete directories. Be carefull

because the shredded/wiped data cannot be recovered.

Open a Terminal and type

    shred -u <filename>
    wipe -rcf <directory>

If you feel the need to wipe the whole harddrive, the command is as follows for IDE-HDs (/dev/hda is the first HD)

    wipe -kq /dev/hda

For SATA and SCSI HDs you type (/dev/sda ist the first HD)

    wipe -kq /dev/sda

If wipe is not available to you, you can use dd. (again the first HD)

    dd if=/dev/zero of=/dev/hda
    dd if=/dev/urandom of=/dev/hda

Use *both* commands, one after the other, if especially paranoid. Use them multiple times.

## Mac

Anonymous' Privacy Pack for Mac users. It includes a Top Secret Docs secure Shredder & AES-256

Encryption tool (and some Design as extra stuff)

* http://www.mediafire.com/?1xmu0m8jpy9b2a1

MD5 (Anonymous-MacPackage-Privacy.dmg) = 36e9ea524a86b94a451577ca46d3e15f

## Windows

* AxCrypt http://www.axantum.com/AxCrypt
