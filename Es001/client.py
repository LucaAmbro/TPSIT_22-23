from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024

IP = "192.168.0.255"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatClient(ip, port, nome):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI':
                running = False
            else:
                mex = nome + ": " + mex
                mex = mex.encode()
                s.sendto(mex, (ip, port))

if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    nome = input("Inserisci nome utente: ")
    chatClient(ip, port, nome)