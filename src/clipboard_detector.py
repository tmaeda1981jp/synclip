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
        super(ClipboardDetector, self).__init__()
        self.__queue = queue
        self.__stop  = False


    def run(self):
        while not self.__stop:
            text = pyperclip.paste()
            self.memorize(text)
            time.sleep(1)
        print 'stopped correctly'


    def memorize(self, text):
        if text not in self.__queue.queue:
            self.__queue.put(text)
            print text


    def stop(self):
        self.__stop = True
