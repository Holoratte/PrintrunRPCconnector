#-------------------------------------------------------------------------------
# Name:        zrorpcRPCtoTcpClient.py
# Purpose:     communicate with Pronterface
#
# Author:      holoratte
#
# Created:     20/09/2019
# Copyright:   (c) Holoratte 2019
# Licence:     public domain
#-------------------------------------------------------------------------------
##  from printrun/rpc.py:
##        self.server.register_function(self.get_status, 'status')
##        self.server.register_function(self.set_extruder_temperature,'settemp')
##        self.server.register_function(self.set_bed_temperature,'setbedtemp')
##        self.server.register_function(self.load_file,'load_file')
##        self.server.register_function(self.startprint,'startprint')
##        self.server.register_function(self.pauseprint,'pauseprint')
##        self.server.register_function(self.resumeprint,'resumeprint')
##        self.server.register_function(self.sendhome,'sendhome')
##        self.server.register_function(self.connect,'connect')
##        self.server.register_function(self.disconnect, 'disconnect')
##        self.server.register_function(self.send, 'send')


import zerorpc


def main():
    pass

if __name__ == '__main__':
    c = zerorpc.Client()
    c.connect("tcp://machine:4242")
    c.conn("COM4")
    c.send("M999")
    c.send("M80")
    c.send("MG28")
    c.settemp("50.0")
    c.setbedtemp("30.0")

    for i in range(10):
        status = c.status("status")
        print status
        print (status["temps"]["B"])
        print (status["temps"]["T"])
        print (status["progress"])
        print (status["eta"])
        print (status["z"])
        print (status["filename"])
    c.settemp("0.0")
    c.setbedtemp("0.0")
    c.send("M81")
    c.disconn("COM4")
    c.disconnect("tcp://machine:4242")
