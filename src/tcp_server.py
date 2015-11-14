#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import pyperclip
import SocketServer

class TCPHandler(SocketServer.StreamRequestHandler):


    def handle(self):
        self.data = self.rfile.readline().strip()
        print "[%s] %s" % (self.client_address[0], self.data)
        pyperclip.copy(self.data)
#        self.wfile.write(self.data)

if __name__ == '__main__':
    HOST, PORT = 'localhost', 9999
    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()
