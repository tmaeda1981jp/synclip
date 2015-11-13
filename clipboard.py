#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time
import sys
import os
import pyperclip

memos = []
while True:
    text = pyperclip.paste()
    if text not in memos:
        memos.append(text);
        if 10 <= len(memos):
            memos.pop(0)
        print ''.join(' | '. join(memos))
    time.sleep(.1)
