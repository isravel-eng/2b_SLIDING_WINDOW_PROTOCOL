# 2B IMPLEMENTATION OF SLIDING WINDOW PROTOCOL

## AIM

To implement the Sliding Window Protocol using Python socket programming.

---

## ALGORITHM

1. Start the server program.
2. Create a socket and bind it to localhost with port number 8000.
3. Wait for the client connection.
4. Start the client program.
5. Enter the number of frames and window size.
6. Client sends multiple frames based on the window size.
7. Server receives the frames and sends acknowledgement.
8. Client receives ACK and slides the window.
9. Repeat until all frames are transmitted.
10. Close the connection.

---

## FILES

### `server.py`

```python
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
```

### `client.py`

```python
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
```

---

## HOW IT WORKS

1. Client sends multiple frames together according to the window size.
2. Server receives the frames.
3. Server sends acknowledgement for received frames.
4. Client slides the window and sends the next set of frames.

---

## SAMPLE OUTPUT

### Server Output

```text
Waiting for connection...
Connected to ('127.0.0.1', 54321)
Frames received: 1 2 3
Frames received: 4 5 6
Frames received: 7 8
```
<img width="480" height="135" alt="image" src="https://github.com/user-attachments/assets/e11d96cf-1848-453c-a59e-e7359e3517c4" />

### Client Output

```text
Enter number of frames: 8
Enter window size: 3
Sending frames: 1 2 3
Received: ACK for 1 2 3
Sending frames: 4 5 6
Received: ACK for 4 5 6
Sending frames: 7 8
Received: ACK for 7 8
```
<img width="661" height="203" alt="image" src="https://github.com/user-attachments/assets/5a3511fa-4473-4417-b885-f0416fdfa8a2" />


---

## RESULT

Thus, the Python program to implement the Sliding Window Protocol was successfully executed.
