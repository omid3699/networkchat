import socket
from utils import validate_username, sprint, encode, decode

username = input("enter your username: ")

while not validate_username(username=username):
    print(f"your username: {username} is not valid")
    username = input("enter your username: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# for TCP 

def listen(host="0.0.0.0", port=9999):
    s.bind((host, port))
    s.listen()
    print(f"waitnig for connection on port: {port}")
    cl, addr = s.accept()
    s.close()
    cl.send(encode({"username":username, "msg":"Hello Weloceme to chat."}))
    while True:
        data = cl.recv(1024)
        data = decode(data)
        sprint(username=data['username'], msg=data["msg"])
        msg = input("enter a message: ")
        cl.send(encode({"username":username, "msg":msg}))
        sprint(username="You", msg=msg)

def join(host="0.0.0.0", port=9999):
    s.connect((host, port))
    data = s.recv(1024)
    data = decode(data=data)
    sprint(username=data['username'], msg=data["msg"])
    while True:
        msg = input("enter a message: ")
        s.send(encode({"username":username, "msg":msg}))
        sprint(username="You", msg=msg)
        data = s.recv(1024)
        data = decode(data)
        sprint(username=data['username'], msg=data["msg"])
        
cmd = int(input(("chose a command 0 for listen, 1 for join: ")))
host = input("enter the host: ")
port = input("enter the port number: ")

if not host:
    host = "127.0.0.1"
if not port:
    port = 9999 
else:
    port = int(port)

if cmd == 0:
    listen(host=host, port=port)
else:
    join(host=host, port=port)
