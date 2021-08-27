#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python ts=4 sw=4 sts=4 et fenc=utf-8
# Original author: "Eivind Magnus Hvidevold" <hvidevold@gmail.com>
# License: GNU GPLv3 at http://www.gnu.org/licenses/gpl.html

'''
'''

import os
import sys
import re

def main():
    'entry point'
    fnames = sys.stdin.readlines()
    for fname in fnames:
        fname = fname.strip()
        bname = os.path.basename(fname)
        bname = bname.replace('.png', '').replace('_', ' ').title()
        print('<img src="' + fname + '" alt="' + bname + '"></img>')

if __name__ == '__main__':
    main()

