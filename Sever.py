import socket

HOST = '192.168.0.4'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

try:
    s.bind((HOST, PORT))

except socket.error:
    print("BINDING FAILED!")

s.listen(10)
(conn, addr) = s.accept()
print("Connection established")

while True:
    data = conn.recv(1024)
    data = data.decode('utf-8')
    print("Message in response to ", data)
    f = open("RVCE.txt", "a+")
    
    if data == "Hi":
        reply = "Hi! updated"
        f.write(data)
        f.close()
        
    elif data == "Hello MCA":
        reply = "OK, i have done that work!"
        f.write(data)
        f.close()
        
    elif data == "quit":
        conn.send(str.encode("terminate"))
        break
    
    else:
        reply = "UNKNOWN COMMAND!"
        
    conn.send(str.encode(reply))
    
conn.close()