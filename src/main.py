#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from clipboard_detector import ClipboardDetector
from tcp_client import TCPClient
from Queue import Queue
import os, sys, time
import threading

if __name__ == '__main__':

    queue = Queue()
    detector = ClipboardDetector(queue)
    detector.start()

    tcp_client = TCPClient(queue)
    tcp_client.start()

    try:
        while True:
            time.sleep(5)

    except (KeyboardInterrupt, SystemExit):
        print 'interrupt!'
        detector.stop()
        tcp_client.stop()

        detector.join()
        tcp_client.join()
