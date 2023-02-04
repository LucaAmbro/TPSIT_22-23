from socket import socket, AF_INET, SOCK_STREAM
from ambrosino_luca_packet import leggi_file, Packet

MAX_SIZE = 8096

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        sock = leggi_file("ambrosino_luca_confclient.csv")
        sock = (sock[0], int(sock[1]))
        running = True
        s.connect(sock)
        while running:
            # i comandi visualizzati nel server sono quelli n° pari
            stato = input("Inserisci stato (salva - leggi): ")
            if stato == "salva":
                messaggio = input("Inserisci messaggio da inviare: ")
                username = input("Inserisci nome utente: ")
                s.send(Packet(username = username, messaggio = messaggio).to_bytes())
            elif stato == "leggi":
                s.send(Packet(stato = stato).to_bytes_stato())
                mex = s.recv(MAX_SIZE)
                p = Packet.from_bytes(mex)
                print(p)

if __name__ == "__main__":
    main()