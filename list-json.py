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
import json

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def main():
    'entry point'
    fnames = sys.stdin.readlines()
    unique = {}
    jlist = []
    for fname in fnames:
        fname = fname.strip()
        bname = os.path.basename(fname)
        dname = os.path.basename(os.path.dirname(fname))
        bname = bname.replace('.png', '').replace('_', ' ')
        bname = (bname + ' ' + dname).title()
        if 'hand_right' in fname:
            bname = 'Right Hand ' + bname
        if 'hand_left' in fname:
            bname = 'Left Hand ' + bname
        if bname in unique:
            print("Error: Not unique: " + bname)
        category = ' '.join(splitall(fname)[1:-1])
        category = category.title()
        unique[bname] = True
        url = 'https://emh.lart.no/kaupanger-goods/art/' + fname
        jobj = {
            'title': bname,
            'category': category,
            'url': url
        }
        jlist.append(jobj)
        #print('<img src="' + fname + '" alt="' + bname + '"></img>')
        #print(bname + ';' + 'https://emh.lart.no/kaupanger-goods/art/' + fname)
    print(json.dumps(jlist, indent=4))

if __name__ == '__main__':
    main()

