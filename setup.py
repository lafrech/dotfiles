#!/usr/bin/env python3
"""Setup dotfiles

Create symlink to files in .dotfiles repository
"""
from pathlib import Path


class DotfilesError(Exception):
    """Generic .dotfiles exception"""


class MkDirError(DotfilesError):
    """Path exists and is not a directory"""


# Path to .dotfiles directory
DIRPATH = Path(__file__).resolve().parent

# Python virtual environments directory
VIRTUALENVS_DIR = Path.home() / ".virtualenvs"

# .vim directory
VIM_DIR = Path.home() / ".vim"

# .vim/pack directory
VIM_PACK_DIR = VIM_DIR / "pack"


# src, dst tuples
# Note symlink is src <- dst
SRC_DST = (
    # Bash
    ("bash_aliases", ".bash_aliases"),
    # Git
    ("git/gitconfig", ".gitconfig"),
    ("git/gitignore/Global/Vim.gitignore", ".vim_gitignore"),
    # Vim
    ("vim/vimrc", ".vimrc"),
    ("vim/plugins/", VIM_PACK_DIR / "dotfiles-plugins"),
    # Python
    ("python/postmkvirtualenv", VIRTUALENVS_DIR / "postmkvirtualenv"),
    ("python/pypirc", ".pypirc"),
)


def make_link(src_rel, dst_rel):
    """Create a symbolic link pointing to src named dst

    Make a few checks/backups before symlinking

    src: path relative to this directory
    dst: path relative to HOME
    """

    src = DIRPATH / src_rel
    dst = Path.home() / dst_rel

    if dst.is_symlink():
        print(f"Remove symlink {dst}")
        dst.unlink()
    elif dst.is_file() or dst.is_dir():
        bak = f"{dst}.bak"
        print(f"Backup {dst} into {bak}")
        dst.rename(bak)
    print(f"Create symlink {dst} -> {src}")
    dst.symlink_to(src)


def make_dir(dir_path):
    try:
        dir_path.mkdir()
    except FileExistsError:
        if not dir_path.is_dir():
            raise MkDirError(f"{dir_path} exists and is not a directory")


# Create virtualenvs directory
make_dir(VIRTUALENVS_DIR)


# Create .vim/pack directory
make_dir(VIM_DIR)
make_dir(VIM_PACK_DIR)


# Create / update symbolic links
for src_r, dst_r in SRC_DST:
    make_link(src_r, dst_r)
