import socket
import sys

from connection import Connection
from MatchFinder import match_finder_thread
from debug import logger

from handler import packetHandler
from packets.QueueMatch import QueueMatch
from model import players, States


def listen_for_connection(socket):
    sock, addr = socket.accept()
    conn = Connection(sock, addr)
    logger.info("New connection established: %s:%s" % addr)

    players[conn.UUID] = {
        "state": States.IDLE,
        "connection": conn,
        "opponent": None,
        "game_data": {
            "money": 200,
            "isTurn": False,
        },
    }

    conn.start()


def main():
    host = "127.0.0.1"
    port = 1234 if len(sys.argv) == 1 else int(sys.argv[1])

    server = socket.socket(
        socket.AF_INET,  # IPv4 protocols
        socket.SOCK_STREAM,  # TCP streams
    )

    server.bind((host, port))
    server.listen()

    # Registering packets {{{
    packetHandler.registerPacket(QueueMatch)
    # }}}

    match_finder_thread.start()

    logger.info("Socket listening for new connections at %s on port %s" % (host, port))
    while True:
        listen_for_connection(server)


if __name__ == "__main__":
    main()
