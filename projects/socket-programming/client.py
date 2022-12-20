import socket
HEADER = 64
PORT = 5050
FORMATE = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMATE)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMATE)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMATE))
   

connected = True
while connected:
    txt = input()
    if txt == "!DISCONNECTED":
        send(txt)
        connected = False
    else:
        send(txt)