from handler import Packet


class PlayCard(Packet):
    def __init__(self, card_id=None):
        self.card_id = card_id

    def handle(self, connection):
        raise NotImplementedError

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    def from_bytes(self, payload):
        raise NotImplementedError
