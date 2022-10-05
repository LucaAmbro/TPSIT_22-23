# | 1 byte (#username) | username | 2 byte (#message) | message

from tkinter import Pack

class Packet:
    def __init__(self, username, message):
        # validazione 
        self.username = username
        self.message = message

    # Converte un oggetto Packet in bytes
    def to_bytes(self):
        username_bytes = self.username.encode('utf8')
        buffer = len(username_bytes).to_bytes(1, 'big') #big endian byte più significativo -> ultimo, destra; il little il contrario
        buffer = buffer + username_bytes
        message_bytes = self.message.encode('utf8')
        buffer = buffer + len(message_bytes).to_bytes(2, 'big')
        buffer = buffer + message_bytes

        return buffer

    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1:username_size + 1]
        message_size = int.from_bytes(buffer[username_size + 1:username_size + 3], 'big')
        message = buffer[username_size + 3:username_size + 3 + message_size]
        username = username.decode('utf8')
        message = message.decode('utf8')
        return Packet(username, message)

def run_tests():
    # test unitar / unit test
    pkt0 = Packet("user", "message")
    pkt1 = Packet.from_bytes(pkt0.to_bytes())
    assert(pkt0.message == pkt1.message)
    assert(pkt0.username == pkt1.username)

if __name__ == "__main__":
    run_tests()