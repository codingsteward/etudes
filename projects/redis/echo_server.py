import socket

HOST = "localhost"
PORT = 6379
MAX_CONN = 5

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(MAX_CONN)
    while True:
        print("waiting for a connection")
        client_socket, client_address = s.accept()
        with client_socket:
            print(f"Connected by {client_address}")
            while True:
                data = client_socket.recv(1024)
                print("test")
                print(f"Received {data} from {client_address}")
                if not data: break
                client_socket.sendall(data)
