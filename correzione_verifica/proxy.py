import sys
from socket import socket, AF_INET, SOCK_STREAM

BUF_SIZE = 4096

class Optioni():
    def __init__(self, porta_server, host, porta):
        self.porta_server = int(porta_server)
        self.host = host
        self.porta = int(porta)

    def get_socket(self):
        return self.host, self.porta 

def richiedi_dati(sock, percorso):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(sock)
        s.sendall(f"GET {percorso}.json HTTP/1.0\n\n".encode())
        data = s.recv(BUF_SIZE)
        data = data + s.recv(BUF_SIZE)
        return data
        """dati = []
        data = True
        while data != None:
            data = s.recv(BUF_SIZE)
            if data != None:
                dati.append(data)
        dati = b''.join(dati)
        print(dati)"""

def main(args):
    opt = Optioni(args[1], args[2], args[3])
    
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", opt.porta_server))
        s.listen()

        while True:
            client, client_address = s.accept()
            data = client.recv(BUF_SIZE)
            data = data.decode("utf-8")
            campi = data.split(" ")

            data = richiedi_dati(opt.get_socket(), campi[1])

            client.sendall(data)

if __name__ == "__main__":
    main(sys.argv)