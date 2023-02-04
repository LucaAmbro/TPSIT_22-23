from socket import socket, AF_INET, SOCK_STREAM

def main():
    cl = socket(AF_INET, SOCK_STREAM)
    cl.connect(("127.0.0.1", 8000))
    running = True
    while running:
        try:
            operazione = input("Inserisci operazione (exit per uscire): ")
            cl.sendall(operazione.encode())
            risp = cl.recv(4096).decode()
            print(risp)
        except:
            running = False

if __name__ == "__main__":
    main()