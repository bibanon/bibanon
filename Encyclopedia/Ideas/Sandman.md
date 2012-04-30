I strongly prefer Pacman to any other package system. It's not easy to find a repository willing to put up custom packages, and making RPMs is already a challenge. Sometimes, when I just want to automate a build process, a PKGBUILD is the best.

So, *why don't we modify Pacman/Akabei to work as a cross-distro ports system?* This will bring the greatest feature of Arch Linux, it's PKGBUILDs and AUR, to all distros. 

I will refer to this conceptual package manager as "Sandman", and it's user repository as the SUR.

## Rationale

This will be extremely useful when you're on an Ubuntu system, for example, and need to compile a driver. Since it's usually not packaged as a DEB, all you can do is hope for the best and compile manually. Need to remove it, or recompile for the new kernel? Well, go through the mess again. This is the #1 problem that pushes prospective Linux users back to Windows.

With a cross-distro Pacman/Akabei, we could have a custom user repository so people could submit PKGBUILDs made to work on all distros. So if, say, a wireless driver is not provided by your distro, and someone made a PKGBUILD (probably by adapting the AUR equivalent) just fire up Sandman and install it painlessly like any other package.

There was once a program that could do something similar, known as Checkinstall. It would be run in the source folder's directory and then, out would come a nice little DEB package. There wasn't even a need to create a set of package routines. But this became a problem as time went on, and the author found the problem to be so damning that he abandoned the code as it became more inelegant. However, it is an important precendent to the creation of of this package management system.

There's been [a post about](http://timetobleed.com/yo-dawg-using-a-package-management-system-to-install-a-package-management-system/) installing and using Pacman on Debian[/url], so using two package managers does actually work in practice. So to make it usable, we'll need to make some modifications.

## Mods to the Package Manager

* We will need to create a special user repository for this program. Most of the packages will be ported from the AUR, just like we do with the CCR.

* All programs should be placed in /opt/sandman, rather than the rest of the system. Hopefully we could just link to this directory rather than dumping the files everywhere. This also makes it easy to delete if problems occur with Sandman.

* Unlike Arch's pacman, Sandman's primary purpose would be to use a source-based user repository, perhaps with a few binaries. Therefore, the functions of an AUR-grabber should be united with pacman, so it probably should work like "pacaur", along with an ability to find updates.

* The best way would be to use the PKGBUILDs to make DEB/RPM packages out of it, rather than adding another package system. If checkinstall could make DEBs without manual intervention, we can definitely make this work with preorganized PKGBUILDs.

## Ideas for the PKGBUILD

* The simplest way to get PKGBUILDs working for all distros would be to have a seperate dependency list, "DEPENDS". Since each distro has a different naming convention for their packages, such a list makes sure that all the packages for each distro can be grabbed from the host package manager.

There are two types of dependencies: User Repository (UR) dependencies, and Host Package dependencies. UR depends are used when the dependency is not otherwise available, or the host package is inferior. (If anything )

The package will still work if the packager only specifies dependencies for one distro. As a courtesy for other packagers, a proper name list of the needed packages should be put as a comment.

  # Package: 
  depends_ur=()		# User Repo 
  
  # Dependencies: 
  depends_debian=()
  depends_ubuntu=()
  depends_fedora=()
  depends_opensuse=()

## Ideas for the User Repository

* Because there will be a need to have multiple developers working on multiple distros, the User Repository should probably work more like github, so that people can directly make forks, rather than just suggesting a fix to a deadbeat developer in the comments. 

In the case of multiple competing forks, the package manager could ask the user which one to install.

* People should be able to create their own source code based User Repositories on their own servers easily. Perhaps we could implement this by borrowing the features of "srcman", a bash wrapper and "repo-add" mod which automatically installs and compiles ".src.tar.xz" files just as easily as normal pacman packages.

## Miscellaneous

To aid a PKGBUILD creator in porting something from the AUR, it might help to create a "namcap" module to check the PKGBUILD for common packaging errors, along with new ones that Arch packagers may be unfamiliar with.

## Not as good ideas

* To lessen the burden on the package creator, there could be a PKGBUILD function that uses alias for dependencies, which are converted to the builder's distro package names by scanning a name conversion list. (perhaps maintained on a github?)

Basically: 

[code]PKGBUILD dep. |   Name conversion list      |  Package to install
--------------------------------------------------------------
libusb-dev --> (Fedora's conversion list) -->  libusb-devel 
linux-3.3  --> (Debian's conversion list) -->  linux-base (3.3)
[/code]

(This idea would be excessively complex, and not a very sure fit.) 