from Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM
import time

def run_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        with open("Pdf_prova.pdf", "rb") as f:
            s.send(Packet(Packet.NEW_FILE, b'').to_bytes())
            data = True
            print("Inizio invio dati")
            while data:
                data = f.read(4096)
                if data:
                    s.send(Packet(Packet.GO_ON, data).to_bytes())
                    print('pacchetto inviato')
                    #time.sleep(0.001)

            s.send(Packet(Packet.END_FILE, b'').to_bytes())

if __name__ == "__main__":
    run_client()