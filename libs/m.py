#!/usr/bin/env python3
from os import popen

def cmd(c):
    return popen(c).read()
