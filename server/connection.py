import threading
import uuid
from .handler import packetHandler

class Connection(threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.isOk = True
        self.UUID = uuid.uuid4()

    def run(self):
        """ This function is executed on a new thread. """
        while self.isOk:
            self.read()
        self._close_connection()

    def _close_connection(self):
        self.socket.close()
        
    def send_packet(self, packet):
        """
        This method does three things:
            1. Serialize the packet
            2. Send to client
        """
        pass

    def read(self):
        """
        This method does three things:
            1. Recieve the packet from client
            2. Deserialize the packet data
            3. Handle the packet class
        """

        data = self.socket.recv(32)

        # Close the connection if data is not coming through
        if not data:
            self.isOk = False
            return

        packetID = data.slice()

        packet = packetHandler.id_to_class[packetID]()
        packet.from_bytes()
        packet.handle(self)
        # TODO: Where to parse when the packet is forbidden?
