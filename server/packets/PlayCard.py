from handler import Packet
from model import players


class PlayCard(Packet):
    def __init__(self, card_id=None):
        self.card_id = card_id

    def handle(self, connection):
        if players[connection.UUID].isTurn is True:
            pass

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    def from_bytes(self, payload):
        raise NotImplementedError
