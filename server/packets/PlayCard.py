from handler import Packet


class PlayCard(Packet):
    def __init__(self):
        pass

    def handle(self, connection):
        pass

    def to_bytes(self) -> bytes:
        pass

    def from_bytes(self, payload):
        pass
