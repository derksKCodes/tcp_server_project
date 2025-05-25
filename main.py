from server.tcp_server import TCPServer
from server.log_config import setup_logging

if __name__ == "__main__":
    setup_logging()
    server = TCPServer()
    server.start()
