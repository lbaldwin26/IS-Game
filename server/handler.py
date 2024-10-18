from abc import ABC, abstractmethod


class PacketHeader:
    PACKET_HEADER_SIZE = 1

    def __init__(self, id: int = None):
        self.id = id

    def to_bytes(self) -> bytes:
        return id.to_bytes(self.PACKET_HEADER_SIZE, "big")

    def from_bytes(self, header):
        id = header
        self.id = id


class Packet(ABC):
    @abstractmethod
    def handle(self, connection):
        """Called when the server gets a packet from the client"""
        pass

    @abstractmethod
    def to_bytes(self) -> bytes:
        pass

    @abstractmethod
    def from_bytes(self, payload):
        pass


class PacketHandler:
    def __init__(self):
        self._current_id = 1
        self.id_to_class = {}
        self.class_to_id = {}

    def registerPacket(self, packetClass):
        packetID = self._current_id
        packetClass.header = PacketHeader(packetID)
        self.id_to_class[packetID] = packetClass
        self.class_to_id[packetClass] = packetID
        self._current_id += 1


packetHandler = PacketHandler()
