from socket import socket, AF_INET, SOCK_STREAM

def main():
    cl = socket(AF_INET, SOCK_STREAM)
    cl.connect(("127.0.0.1", 8000))
    running = True
    while running:
        try:
            num = input("Inserisci numero compreso tra 1 e 10 (exit per uscire): ")
            cl.sendall(num.encode())
            current_operation = True
            while current_operation:
                risp = cl.recv(4096).decode()
                print(risp)
                if risp == "errore" or risp == "errore_numerico":
                    print("Errore, dato inviato non corretto")
                    current_operation = False
                elif risp == "-------":
                    current_operation = False
        except:
            running = False

if __name__ == "__main__":
    main()