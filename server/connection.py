import threading
import uuid
from handler import PacketHeader, packetHandler


class Connection(threading.Thread):
    def __init__(self, socket, address, *, logger):
        threading.Thread.__init__(self)
        self._socket = socket
        self.address = address
        self.isOk = True
        self.UUID = str(uuid.uuid4())
        self._logger = logger

    def run(self):
        """Entry point for thread initiation"""
        while self.isOk:
            self.read()
        self._close_connection()

    def _close_connection(self):
        self._logger.info("Connection closed: %s" % self.UUID)
        self._socket.close()

    def send_packet(self, packet):
        """
        This method does three things:
            1. Serialize the packet
            2. Send to client
        """
        packetID = packetHandler.class_to_id[packet.__class__]
        packetHeader = PacketHeader(packetID)

        data = bytearray()
        data.append(packetHeader.to_bytes())
        data.append(packet.to_bytes())

        self._socket.send(data)

    def read(self):
        """
        This method does three things:
            1. Receive the packet from client
            2. Deserialize the packet data
            3. Handle the packet class
        """

        data = self._socket.recv(4096)

        # Close the connection if data is not coming through
        # Data would not be received if they were still connected
        if not data:
            self.isOk = False
            return

        # Improve?
        header = data[PacketHeader.PACKET_HEADER_SIZE - 1]
        packetHeader = PacketHeader()
        packetHeader.from_bytes(header)
        if packetHeader.id not in packetHandler.id_to_class.keys():
            self._logger.warning("PacketHeader id not found within registered packets. Dropping read")
            return

        payload = data[PacketHeader.PACKET_HEADER_SIZE :]
        packet = packetHandler.id_to_class[packetHeader.id]()
        packet.from_bytes(payload)
        packet.handle(self)
