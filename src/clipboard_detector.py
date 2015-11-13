#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time
import sys
import os
import pyperclip


class ClipboardDetector:


    def __init__(self, memos=[]):
        self.__memos = memos


    def watch(self):
        while True:
            text = pyperclip.paste()
            self.append(text)
            time.sleep(.1)


    def append(self, text):
        if text not in self.__memos:
            self.__memos.append(text);
            if 10 <= len(self.__memos):
                self.__memos.pop(0)
#            print ''.join(' | '. join(self.__memos))
