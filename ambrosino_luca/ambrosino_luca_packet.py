def leggi_file(nome_file):
    with open(nome_file, "r") as f:
        riga = f.readline()
        sock = riga.split(",")
        return sock
    
class Packet():
    def __init__(self, stato = "", username = "", messaggio = ""):
        self.messaggio = messaggio
        self.stato = stato
        self.username = username
    
    def to_bytes_stato(self):
        buffer = len(self.stato).to_bytes(1, 'big')
        buffer = buffer = self.stato.encode('utf-8')

        return buffer

    @staticmethod
    def from_bytes_stato(buffer):
        stato_size = int.from_bytes(buffer[0:1], 'big')
        stato = buffer[1:stato_size + 1]
        return Packet(stato)

    def to_bytes(self):
        username_bytes = self.username.encode('utf8')
        buffer = len(username_bytes).to_bytes(1, 'big')
        buffer = buffer + username_bytes
        messaggio_bytes = self.messaggio.encode('utf8')
        buffer = buffer + len(messaggio_bytes).to_bytes(2, 'big')
        buffer = buffer + messaggio_bytes

        return buffer

    @staticmethod
    def from_bytes(buffer):
        username_size = int.from_bytes(buffer[0:1], 'big')
        username = buffer[1:username_size + 1]
        message_size = int.from_bytes(buffer[username_size + 1:username_size + 3], 'big')
        message = buffer[username_size + 3:username_size + 3 + message_size]
        username = username.decode('utf8')
        message = message.decode('utf8')
        return Packet(username = username, messaggio = message)