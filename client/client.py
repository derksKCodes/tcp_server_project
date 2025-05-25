import socket
import ssl
import os

def main():
    host = "127.0.0.1"
    port = 9001
    use_ssl = True

    if use_ssl:
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations('../cert/server.pem')
        context.check_hostname = False  # For development only
        conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)

    else:
        conn = socket.socket(socket.AF_INET)

    conn.connect((host, port))
    print("Connected. Type your query:")
    try:
        while True:
            query = input("> ").strip()
            if not query:
                break
            conn.sendall(query.encode())
            data = conn.recv(4096)
            print(data.decode())
    finally:
        conn.close()

if __name__ == "__main__":
    main()
