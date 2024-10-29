import socket
import threading

from handler import PacketHeader, packetHandler

class Connection(threading.Thread):
    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self._socket = socket
        self.address = address
        self.isOk = True

    def run(self):
        """Entry point for thread initiation"""
        try:
            self._socket.connect(self.address)
        except socket.error:
            print("[!] Could not connect to server")
            self._close_connection()
            return

        while self.isOk:
            self.read()

        self._close_connection()
    
    def _close_connection(self):
        print("[!] Server disconnected")
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
        data.extend(packetHeader.to_bytes())
        data.extend(packet.to_bytes())

        self._socket.sendall(data)  # Get OS error if sent to a dead socket

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

        header = data[PacketHeader.PACKET_HEADER_SIZE - 1]
        packetHeader = PacketHeader()
        packetHeader.from_bytes(header)
        if packetHeader.id not in packetHandler.id_to_class.keys():
            return

        payload = data[PacketHeader.PACKET_HEADER_SIZE :]
        packet = packetHandler.id_to_class[packetHeader.id]()
        packet.from_bytes(payload)
        packet.handle(self)
