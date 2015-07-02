#!/usr/bin/env python

import argparse
from miv import VimBuffer, reverse_engineer

parser = argparse.ArgumentParser( description='Reverse engineer a way to \
        create a selection in a Vim buffer.')

parser.add_argument(
        'inputFile',
        type=file, 
        help='A file containing the text to play with'
        )

parser.add_argument(
        'line',
        type=int,
        help='The line where the cursor is.'
        )

parser.add_argument(
        'column',
        type=int,
        help='The column where the cursor is.'
        )

parser.add_argument(
        'targetLine',
        type=int,
        help='The line we want the cursor to end up in'
        )

parser.add_argument(
        'targetColumn',
        type=int,
        help='The column we want the cursor to end up in'
        )

ns = parser.parse_args()

textArray = []
for line in ns.inputFile:
    textArray.append(line)

vimBuffer = VimBuffer(textArray, (ns.line, ns.column))
commandSequence = reverse_engineer(
        vimBuffer, 
        ((ns.line, ns.column), (ns.targetLine, ns.targetColumn))
        )

print("Soltn: ")
for command in commandSequence:
    print(command)
