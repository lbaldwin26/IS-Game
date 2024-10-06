import socket

import sys
import logging

from .connection import Connection

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

def main():
    host = '127.0.0.1'
    port = 1234 if len(sys.argv) == 1 else int(sys.argv[1])


    server = socket.socket(
        socket.AF_INET,     # IPv4 protocols
        socket.SOCK_STREAM  # TCP streams
    )

    server.bind((host, port))
    server.listen()

    logging.info("Socket listening for new connections at %s on port %s" % (host, port))

    while True:
        sock, addr = socket.accept()
        conn = Connection(sock, addr)
        conn.start()

if __name__ == '__main__':
    main()
