#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time
import sys
import os
import pyperclip
import threading
from Queue import Queue

class ClipboardDetector(threading.Thread):


    def __init__(self, queue):
        self.__queue = queue


    def run(self):
        while True:
            text = pyperclip.paste()
            self.memorize(text)
            time.sleep(.1)

    def memorize(self, text):
        if text not in self.__queue.queue:
            self.__queue.put(text);
