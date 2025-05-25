import socket
import ssl
import threading
from concurrent.futures import ThreadPoolExecutor
from server.search_engine import load_lines, search_lines
from server.config import Config
import logging
import os  # for os._exit
import sys

config = Config()
log = logging.getLogger("TCPServer")

class TCPServer:
    def __init__(self):
        self.host = config.get("HOST")
        self.port = config.get("PORT")
        self.reread = config.get("REREAD_ON_QUERY")
        self.text_file = config.get("TEXT_FILE_PATH")
        self.max_workers = config.get("MAX_WORKERS")
        self.ssl_enabled = config.get("SSL_ENABLED")
        self.certfile = config.get("CERTFILE")
        self.keyfile = config.get("KEYFILE")
        self.lines = [] if self.reread else load_lines(self.text_file)
        self.running = True  # Flag to control server state

    def handle_client(self, conn, addr):
        try:
            with conn:
                log.info(f"Connected: {addr}")
                while True:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break

                    log.info(f"Query from {addr}: {data}")

                    if data.lower() == "exit":
                        log.info(f"Received 'exit' from {addr}. Shutting down server.")
                        conn.sendall(b"Server shutting down...\n")
                        conn.close()
                        os._exit(0)  # Force exit the server process
                        return

                    if self.reread:
                        self.lines = load_lines(self.text_file)
                    matches = search_lines(data, self.lines)
                    response = "\n".join(matches) if matches else "No matches found."
                    conn.sendall(response.encode())
        except Exception as e:
            log.exception(f"Error handling client {addr}: {e}")

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen()
            log.info(f"Server listening on {self.host}:{self.port}")
            print(f"[INFO] Server is up and accepting connections at {self.host}:{self.port}...")

            if self.ssl_enabled:
                context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
                wrap_socket = lambda s: context.wrap_socket(s, server_side=True)
            else:
                wrap_socket = lambda s: s

            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                while self.running:
                    print("[WAITING] Waiting for a new client connection...")
                    client, addr = sock.accept()
                    print(f"[CONNECTED] Client connected from {addr}")
                    conn = wrap_socket(client)
                    executor.submit(self.handle_client, conn, addr)
