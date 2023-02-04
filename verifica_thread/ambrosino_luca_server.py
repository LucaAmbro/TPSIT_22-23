from socket import socket, AF_INET, SOCK_STREAM
from ambrosino_luca_packet import leggi_file, Packet
import threading

MAX_SIZE = 8096

class MyClassThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self) # richiama il metodo della classa genitore
        self.conn = conn
    def run(self):
        try:
            running = True
            lista = []
            while running:
                msg = self.conn.recv(MAX_SIZE)
                packet = Packet.from_bytes(msg)
                if packet.stato == "":
                    msg = self.conn.recv(MAX_SIZE)
                    p = Packet.from_bytes(msg)
                    lista.append([p.username, p.messaggio])
                    print(lista)
                elif packet.stato == "leggi":
                    vecchio = lista.pop(0)
                    self.conn.send(Packet(username = vecchio[0], messaggio = vecchio[1]).to_bytes())
                    print(vecchio)
        except:
            print("no!")

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        sock = leggi_file("ambrosino_luca_confserver.csv")
        s.bind((sock[0], int(sock[1])))
        s.listen()
        while True:
            client, address = s.accept() # già nel while
            print(f"Connesso con {address}")
            t = MyClassThread(conn=client)
            t.run()
            
if __name__ == "__main__":
    main()