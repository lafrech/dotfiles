#!/usr/bin/env python3
"""Setup dotfiles

Create symlink to files in .dotfiles repository
"""
import os
import os.path


class DotfilesError(Exception):
    """Generic .dotfiles exception"""


class MkDirError(DotfilesError):
    """Path exists and is not a directory"""


# Path to .dotfiles directory
DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Python virtual environments directory
VIRTUALENVS_DIR = os.path.join(os.environ['HOME'], '.virtualenvs')

# .vim directory
VIM_DIR = os.path.join(os.environ['HOME'], '.vim')

# .vim/pack directory
VIM_PACK_DIR = os.path.join(VIM_DIR, 'pack')


# src, dst tuples
# Note symlink is src <- dst
SRC_DST = (
    # Bash
    ('bash_aliases', '.bash_aliases'),
    # Git
    ('git/gitconfig', '.gitconfig'),
    ('git/gitignore/Global/Vim.gitignore', '.vim_gitignore'),
    # Vim
    ('vim/vimrc', '.vimrc'),
    ('vim/plugins/', '.vim/pack/dotfiles-plugins'),
    # Python
    ('python/postmkvirtualenv',
     os.path.join(VIRTUALENVS_DIR, 'postmkvirtualenv')),
    ('python/pypirc', '.pypirc'),
)


def make_link(src_rel, dst_rel):
    """Create a symbolic link pointing to src named dst

    Make a few checks/backups before calling os.symlink

    src: path relative to this directory
    dst: path relative to HOME
    """

    src = os.path.join(DIRPATH, src_rel)
    dst = os.path.join(os.environ['HOME'], dst_rel)

    if os.path.islink(dst):
        print('Remove symlink {}'.format(dst))
        os.remove(dst)
    elif os.path.isfile(dst) or os.path.isdir(dst):
        bak = '{}.bak'.format(dst)
        print('Backup {} into {}'.format(dst, bak))
        os.rename(dst, bak)
    print('Create symlink {} -> {}'.format(dst, src))
    os.symlink(src, dst)



def mkdir(dir_path):
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        if not os.path.isdir(dir_path):
            raise MkDirError(
                "{} exists and is not a directory".format(dir_path))


# Create virtualenvs directory
mkdir(VIRTUALENVS_DIR)


# Create .vim/pack directory
mkdir(VIM_DIR)
mkdir(VIM_PACK_DIR)


# Create / update symbolic links
for src_r, dst_r in SRC_DST:
    make_link(src_r, dst_r)
