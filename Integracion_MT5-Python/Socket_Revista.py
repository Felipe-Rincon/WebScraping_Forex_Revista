#Socket_Revista.py

import numpy as np
import socket 
from CodigoWebScraping_Revista import Z_1,Z_2,Z_3,Z_4


class socketserver:
    def __init__(self, address = '', port = 9090):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))
        self.cummdata = ''
        
    def recvmsg(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connected to', self.addr)
        self.cummdata = ''

        while True:
            data = self.conn.recv(10000)
            self.cummdata+=data.decode("utf-8")
            if not data:
                break    
            self.conn.send(bytes(info_enviar(self.cummdata), "utf-8"))
            # print (self.cummdata)
            return self.cummdata
            
    def __del__(self):
        self.sock.close()
        
def info_enviar(msg = ''):

    np.fromstring(msg, dtype=float, sep= ' ')
    zones_total = str(Z_1) + ' ' + str(Z_2) + ' ' + str(Z_3) + ' ' + str(Z_4)

    print(zones_total)
    return str(zones_total)
    
serv = socketserver('127.0.0.1', 9090)

while True:  
    msg = serv.recvmsg()
