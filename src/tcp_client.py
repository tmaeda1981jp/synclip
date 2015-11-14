#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import socket
import time
import threading
from Queue import Queue, Empty

class TCPClient(threading.Thread):


    def __init__(self, queue):
        super(TCPClient, self).__init__()
        self.__queue = queue
        self.__stop = False
        self.__last = None


    def run(self):

        while not self.__stop:
            try:
                text = self.__queue.get_nowait()
                self.__queue.task_done()
            except Empty:
                time.sleep(1)
                continue

            if self.__last == text:
                time.sleep(1)
                continue

            print text
            self.__last = text

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 9999))
            sock.send(text.encode('utf-8') + '\n')
            sock.close()

            time.sleep(1)
        print 'stopped correctly tcp_client'


    def stop(self):
        self.__stop = True
