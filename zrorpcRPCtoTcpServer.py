#-------------------------------------------------------------------------------
# Name:        zrorpcRPCtoTcpServer.py
# Purpose:
#
# Author:      Dragon
#
# Created:     20/09/2019
# Copyright:   (c) Dragon 2019
# Licence:     public domain
#-------------------------------------------------------------------------------

import zerorpc
import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:7978/")
class printrunRPC(object):
    def hello(self, arg=None):
        return "Hello, %s" % arg
    def status(self, arg=None):
        return server.status()
    def settemp(self, arg=None):
        return server.settemp(arg)
    def setbedtemp(self, arg=None):
        return server.setbedtemp(arg)
    def load_file(self, arg=None):
        return server.load_file()
    def startprint(self, arg=None):
        return server.startprint()
    def pauseprint(self, arg=None):
        return server.pauseprint()
    def startprint(self, arg=None):
        return server.startprint()
    def resumeprint(self, arg=None):
        return server.resumeprint()
    def sendhome(self, arg=None):
        return server.sendhome()
    def conn(self, arg=None):
        return server.connect()
    def disconn(self, arg=None):
        return server.disconnect()
    def send(self, arg=None):
        return server.send(arg)



if __name__ == '__main__':
    s = zerorpc.Server(printrunRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()



