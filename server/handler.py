from abc import ABC, abstractmethod

class Packet(ABC):
    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def encode(self):
        pass

    @abstractmethod
    def decode(self):
        pass

# Singleton
class PacketHandler:
    def __init__(self):
        self.id_to_class = {}
        self.class_to_id = {}

    def registerPacket(self, packetClass, packetID: int):
        self.id_to_class[packetID] = packetClass
        self.class_to_id[packetClass] = packetID
