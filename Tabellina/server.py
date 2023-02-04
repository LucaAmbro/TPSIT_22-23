from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def server(conn, address):
    try:
        while True:
            print(f"Connesso con {address}")
            msg = conn.recv(4096).decode()
            if msg == "exit":
                conn.sendall(("exit".encode()))
                conn.close()
            else:
                try:
                    num = int(msg)
                    if (num > 0) and (num < 11):
                        for i in range(1, 11):
                            operazione = f"{num} * {i}"
                            risultato = eval(operazione)
                            messaggio = f"{operazione} = {risultato}"
                            print(messaggio)
                            conn.sendall((messaggio.encode()))
                            time.sleep(0.001)
                        conn.sendall(("-------".encode()))
                    else:
                        print("Numero inserito non valido")
                        conn.sendall(("errore_numerico".encode()))
                except:
                    print("Errore, operazione non inserita")
                    conn.sendall(("errore".encode()))
                    pass
    except:
        print("no!")
        

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    running = True
    while running:
        conn, address = s.accept()
        t = threading.Thread(target=server, args = (conn, address,))
        t.start()
        server(conn, address)

if __name__ == "__main__":
    main()