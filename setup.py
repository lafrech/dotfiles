#!/usr/bin/env python

import os
import os.path

# src, dst tuples
# Note symlink is src <- dst
SRC_DST = (
    ('bash_aliases', '.bash_aliases'),
    ('git/gitconfig', '.gitconfig'),
    ('git/gitignore/Global/Vim.gitignore', '.vim_gitignore'),
)

DIRPATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))


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

for src_r, dst_r in SRC_DST:
    make_link(src_r, dst_r)
