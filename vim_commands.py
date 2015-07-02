#!/usr/bin/env python

""" All functions in this module must represent a valid vim command, that takes
a vimBuffer object as input and returns a buffer with modified position as
output """

import copy

def h(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    if(col == 0):
        return buf
    else:
        col = col - 1
        buf.position = (line, col)
        return buf

def l(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    if(col == len(buf.text[line]) - 1):
        return buf
    else:
        col = col + 1
        buf.position = (line, col)
        return buf

def k(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    if(line == 0):
        return buf
    else:
        line = line - 1
        if(len(buf.text[line]) < col):
            col = len(buf.text[line])
        buf.position = (line, col)
        return buf

def j(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    if(line == len(buf.text) - 1):
        return buf
    else:
        line = line + 1
        if(len(buf.text[line]) < col):
            col = len(buf.text[line])
        buf.position = (line, col)
        return buf
