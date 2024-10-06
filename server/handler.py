from abc import ABC, abstractmethod

# Use pickle instead?
# https://docs.python.org/3/library/pickle.html

class PacketHeader:
    def __init__(self, version, id: int):
        self.version = version
        self.id = id

    def to_bytes(self) -> str:
        pass

class Packet(ABC):

    @abstractmethod
    def handle(self, connection):
        pass

    @abstractmethod
    def to_bytes(self) -> str:
        pass

    @abstractmethod
    def from_bytes(self, data):
        pass

class PacketHandler:
    def __init__(self):
        self._current_id = 1
        self.id_to_class = {}
        self.class_to_id = {}

    def registerPacket(self, packetClass):
        packetID = self._current_id
        self.id_to_class[packetID] = packetClass
        self.class_to_id[packetClass] = packetID
        self._current_id += 1

packetHandler = PacketHandler()
