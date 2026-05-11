import socket

client = socket.socket()
client.connect(('localhost', 8000))

n = int(input("Enter number of frames: "))
w = int(input("Enter window size: "))

frames = list(range(1, n + 1))

i = 0

while i < n:
    send_frames = frames[i:i + w]
    msg = " ".join(map(str, send_frames))

    print("Sending frames:", msg)
    client.send(msg.encode())

    ack = client.recv(1024).decode()
    print("Received:", ack)

    i += w

client.close()
