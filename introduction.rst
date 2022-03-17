A talk about operating systems
==============================

There are a verieties of operating systems in the world but the most popular
ones are either `Windows` or `Unix`.

MacOS, iOS, Android and a lot other variations of Linux that are derivations of
Unix.

Our machine has Ubuntu install which is a derivation of Debian; Debian is a
derivation of Linux; Linux is a derivation of Unix.


Installing the atom editor
==========================

We downloaded the atom package named `atom-amd64.deb` from
`https://atom.io/download/deb?channel=nightly` using browser and it was stored
in our `~/Downloads` (here `~` points to our unix `$HOME`) directory and the
path to the file was `~/Downloads/atom-amd64.deb`. We had to navigate to our
`~/Downloads` directory using the following command::

    $ cd
    $ cd Downloads

While we were in our `~/Downloads` directory we used the following command to
install the `atom-amd64.deb` package::

    $ sudo dpkg -i atom-amd64.deb

here dpkg stands for debian(d) package(pkg) and the `atom-amd64.deb` is a debian
package which we can tell from the extension `.deb`.

Types of programming language
=============================

There are many types of programming languages but for the moment we are
concerned about the following two:

- Compiled language
- Interpreted language

Compiled language
-----------------

Has compiler(s), there maybe many compilers provided by different vandors.

The example languages are kotlin, Java. Android studio has full functionalities related
to building/compiling kotlin programs. As said above, there maybe other
compilers from different vardors.

A compiler usually turns the compiled program into binary packages.
