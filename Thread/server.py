from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

def server(conn, address):
    try:
        while True:
            print(f"Connesso con {address}")
            msg = conn.recv(4096).decode()
            if msg == "exit":
                running = False
                conn.sendall(("exit".encode()))
                conn.close()
            else:
                try:
                    risultato = eval(msg)
                    print(risultato)
                    #time.sleep(5)
                    conn.sendall((str(risultato).encode()))
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