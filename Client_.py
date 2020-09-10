import socket
import sys
import time

x=socket.socket()
h_name = str('127.0.0.1')
port = 9899
x.connect((h_name,port))
print('Connected to chat server')

while 1: 
   incoming_message=x.recv(9899)
   incoming_message=incoming_message.decode()
   print(' Server :', incoming_message)
   message = input(str('>>'))
   Message = message.encode()
   x.send(bytes(message, 'utf-8'))
   print(' message has been sent...')