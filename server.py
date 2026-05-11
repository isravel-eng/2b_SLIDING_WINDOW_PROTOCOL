import socket

server = socket.socket()
server.bind(('localhost', 8000))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024).decode()

    if not data:
        break

    print("Frames received:", data)

    ack = "ACK for " + data
    conn.send(ack.encode())

conn.close()
server.close()
