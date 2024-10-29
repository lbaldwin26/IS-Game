
from handler import Packet

class QueueMatch(Packet):
    def __init__(self, opponent_uuid=None, gets_starting_turn=None):
        self.opponent_uuid = opponent_uuid
        self.gets_starting_turn = gets_starting_turn

    def handle(self, connection):
        pass

    def to_bytes(self) -> bytes:
        return bytes()

    def from_bytes(self, data):
        pass
        # self.opponent_uuid = UUID.
