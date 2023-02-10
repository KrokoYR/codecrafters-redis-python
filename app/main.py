# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("0.0.0.0", 6379), reuse_port=True)
    server_socket.listen(1)

    connection, address = server_socket.accept()
    while True:
        connection.recv(1024).decode('utf-8')
        connection.send(b"+PONG\r\n")


if __name__ == "__main__":
    main()
