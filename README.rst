# Clone repo + submodules
git clone --recursive -j8 https://github.com/lafrech/dotfiles .dotfiles

# Clone submodules on already cloned repo
git submodule update --init --recursive

(Source: http://stackoverflow.com/a/4438292/4653485)

# Pull and update submodules
git pullall
