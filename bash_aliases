# Aliases
alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'

# Editor
if [ -z $DISPLAY ] ; then
    export EDITOR=vi
else
    export EDITOR="gvim --nofork"
fi

# Find in source code
sfind()
{
    find "$1" -type f \! -path "./.*" | xargs grep -In --color "$2"
}

# Find and replace in source code
sreplace()
{
    for f in `find "$1" -type f \! -path "./.*" `;
    do
      sed -i "s/$2/$3/" $f;
    done
}

# Python
# Clean compiled files
alias clpy='find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf'
# Virtualenvwrapper
export VIRTUALENV_PYTHON=/usr/bin/python3
VENVWRP_SH=/usr/share/virtualenvwrapper/virtualenvwrapper.sh
if [ -f $VENVWRP_SH ]
then
    export WORKON_HOME=$HOME/.virtualenvs
    source $VENVWRP_SH
fi

# Clean vim swap files
# https://superuser.com/a/805168/
alias clswp='find . -type f -name ".*.sw[klmnop]" -delete'

# Local configuration
if [ -f ~/.bashrc_local ]; then
    . ~/.bashrc_local
fi
