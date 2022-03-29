Unix cheatsheet
===============

The `$` sign is the prompt for shell. A shell is a Unix program that runs above
the Unix kernel. The Unix kernel is the root program that bind a linux machine
together including the hardware (drivers). Every other program like a shell or
even this text editor is running depending on the kernel. There are many types
of shell for example, cshell, BASHell (Bourne Again SHell, we only need to know
about BASHell and in short hand known as bash). It is a usual case that there is
a shell running around a kernel which knows how to utilize the resources of the
kernel.

The command pwd stands for present working directory, which will show you which
directory you are in at the moment::

  $ pwd

cd stands for change directory. And a directory in Unix (is a Unix path) is like
a folder in windows.

  $ cd

to move to a parent directory we use as such::

  $ cd ..

another example would be, if we have a directory named
`learning-computer-programming` in our current directory then we can navigate to
the `learning-computer-programming` by calling::

  $ cd learning-computer-programming

the following command shows a list view of all the contents inside the
directory. Example usages::

  $ find

to make a new directory named `python` in our current directory, we can use the
following::

  $ mkdir python

here `mkdir` stands for make(mk) directory(dir). To remove an EMPTY directory
named `python` we can use the following::

  $ rmdir python

here `rmdir` stands for remove(rm) directory(dir). To remove a NON-EMPTY
directory named `python` we can use the following::

  $ rm -r python

In the init.sh file the first line has this notation `#!/bin/bash`. Here `#!` is
call shebang, which basically points to the program that should run the file.
And in our case, it is pointing to the `/bin/bash` application that will run
this file if we call `$ source init.sh`.

The command `ls` lists the content of the directory.

  $ ls

The command `rm` stands for remove. Used to remove something from a Unix
directory.

  $ rm

if you have a file named `intro.py` in you directory and you want to remove this
file. You can use the example command below::

  $ rm intro.py

a plain `rm` commands works with a file without complaining. To use `rm` to
remove a directory see the example command above.

To create an empty file we can use the following command::

  $ touch filename.py

this will create an empty file name `filename.py` inside our current directory.
