from socket import socket, AF_INET, SOCK_STREAM
from ambrosino_luca_packet import leggi_file, Packet

MAX_SIZE = 8096

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        sock = leggi_file("ambrosino_luca_confserver.csv")
        s.bind((sock[0], int(sock[1])))
        lista = []
        s.listen()
        client, address = s.accept() # già nel while
        while True:
            msg = client.recv(MAX_SIZE)
            packet = Packet.from_bytes(msg)
            if packet.stato == "":
                msg = client.recv(MAX_SIZE)
                p = Packet.from_bytes(msg)
                lista.append([p.username, p.messaggio])
                print(lista)
            elif packet.stato == "leggi":
                vecchio = lista.pop(0)
                client.send(Packet(username = vecchio[0], messaggio = vecchio[1]).to_bytes())
                print(vecchio)

if __name__ == "__main__":
    main()