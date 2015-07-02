#!/usr/bin/env python

""" All functions in this module must represent a valid vim command, that takes
a vimBuffer object as input and returns a buffer with modified position as
output """

import copy
import miv_util

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
        if(len(buf.text[line]) <= col):
            col = len(buf.text[line]) - 1
        buf.position = (line, col)
        return buf

def dollar(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    col = len(buf.text[line]) - 1
    buf.position = (line, col)
    return buf

def hat(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    col = 0
    while(buf.text[line][col] == ' ' or buf.text[line][col] == '\t'):
        col = col + 1
    buf.position = (line, col)
    return buf

def W(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    while(not miv_util.is_whitespace(buf.text[line][col])):
        col = col + 1
    buf.position = (line, col)
    return buf

def G(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    line = len(buf.text) - 1
    col = 0
    buf.position = (line,col)
    return hat(buf)

def zero(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    col = 0
    buf.position = (line,col)
    return buf

def right_bracket(vimBuffer):
    buf = copy.deepcopy(vimBuffer)
    line, col = buf.position
    while(line < len(buf.text) and buf.text[line] != ['\n']):
        line = line + 1
    col = 0
    buf.position = (line, col)
    return buf

