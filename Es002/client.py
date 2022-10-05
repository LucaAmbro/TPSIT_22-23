from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024

IP = "192.168.136.255"
PORT = 5000
# possibilità
# localhost 127.0.0.1



def chatClient(ip, port, nome):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("Pdf_prova.pdf", "r") as f:
            print(f)
            f = bytes(f)
            print(f)
      

if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    nome = input("Inserisci nome utente: ")
    chatClient(ip, port, nome)
