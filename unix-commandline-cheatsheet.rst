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

cd stands for change directory. And a directory in Unix is like a folder in
windows.

  $ cd

In the init.sh file the first line has this notation `#!/bin/bash`. Here `#!` is
call shebang, which basically points to the program that should run the file.
And in our case, it is pointing to the `/bin/bash` application that will run
this file if we call `$ source init.sh`.

The command `ls` lists the content of the directory.

  $ ls

The command `rm` stands for remove. Used to remove something from a Unix
directory.

  $ rm
