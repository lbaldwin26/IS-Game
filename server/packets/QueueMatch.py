from server.handler import Packet
from server.model import queue


class QueueMatch(Packet):
    def __init__(self, opponent_uuid):
        self.opponent_uuid = opponent_uuid

    def handle(self, connection):
        """
        In lieu of a direct callback, a reference to the players' connection will be placed inside the match making queue and when matched will receive back a QueueMatch packet initiated by the matchfinder thread.
        """
        if connection not in queue:
            queue.append(connection)

    def to_bytes(self) -> bytes:
        return self.opponent_uuid.bytes

    def from_bytes(self, data):
        """Queue match is only a signal, it does not hold data when being sent to the server side"""
        pass
