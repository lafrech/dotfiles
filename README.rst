This repository stores configuration files (dotfiles) for a few applications.

First, install common applications::

    aptitude install git
    aptitude install vim vim-pathogen


Installation / update
---------------------

::

    # Clone repo + submodules
    git clone --recursive https://github.com/lafrech/dotfiles .dotfiles

    # Clone submodules on already cloned repo
    git submodule update --init --recursive

(Source: http://stackoverflow.com/a/4438292/4653485)

::

    # Pull and update submodules
    git pullall

Run setup script (creates symlinks in home dir, backuping existing files)::

    ./setup.py


Other stuff not (yet ?) in this repo
------------------------------------

Mongo-hacker::

    git clone https://github.com/TylerBrock/mongo-hacker ~/.mongo-hacker
    cd ~/.mongo-hacker
    make install
