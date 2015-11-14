#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from clipboard_detector import ClipboardDetector
from Queue import Queue
import os, sys, time
import threading

if __name__ == '__main__':

    queue = Queue()
    detector = ClipboardDetector(queue)
    detector.start()

    try:
        while True:
            time.sleep(5)

    except (KeyboardInterrupt, SystemExit):
        print 'interrupt!'
        detector.stop()
        detector.join()
