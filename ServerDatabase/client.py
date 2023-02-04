from socket import socket, AF_INET, SOCK_STREAM

MAX_SIZE = 4098

def run_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(receiver)
        running = True
        print("Inizio invio dati")
        while running:
            stato = input("Inserisci stato ('signup' - 'login' - 'exit' per uscire): ")
            if stato == "signup" or stato == "login": 
                errore = True
                while errore:
                    username = input("Inserisci nome utente: ")
                    password = input("Inserisci password: ")
                    messaggio = stato + ";" + username + ";" + password
                    s.send(messaggio.encode())
                    mex = s.recv(MAX_SIZE)
                    mex = mex.decode()
                    print(mex)
                    if "Errore" in mex:
                        print("Inserire nuovamente i dati")
                    else:
                        uscita = True
                        if stato == "login":
                            while uscita:
                                elemento = input("Inserisci elemento da ricercare (exit per uscire): ")
                                if elemento == "exit":
                                    uscita = False
                                s.send(elemento.encode())
                                msg = s.recv(MAX_SIZE)
                                msg = msg.decode()
                                print(msg)
                        errore = False
            elif stato == "exit":
                running = False                

if __name__ == "__main__":
    run_client()