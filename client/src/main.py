import socket

import time

from connection import Connection

from handler import packetHandler

from packets.QueueMatch import QueueMatch
from packets.PlayCard import PlayCard
from packets.RaisePot import RaisePot

def main():
    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    ADDRESS = ('127.0.0.1', 1234)

    conn = Connection(client, ADDRESS)
    conn.start()

    # Registering packets {{{
    # These are ORDER DEPENDENT
    packetHandler.registerPacket(QueueMatch)
    packetHandler.registerPacket(PlayCard)
    packetHandler.registerPacket(RaisePot)
    # }}}

    # Start user interaction
    while True:
        time.sleep(5)

if __name__ == '__main__':
    main()
