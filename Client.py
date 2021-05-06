import socket

HOST = '192.168.0.4'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    c = input("ENTER COMMAND: ")
    c = str.encode(c)
    s.send(c)
    
    reply = s.recv(1024)
    reply = reply.decode('utf-8')
    
    if reply == "terminate":
        break
    
    print(reply)