from socket import socket, AF_INET, SOCK_STREAM
import threading
import time

class MyClassThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self) # richiama il metodo della classa genitore
        self.conn = conn
    def run(self):
        try:
            while True:
                
                msg = self.conn.recv(4096).decode()
                if msg == "exit":
                    running = False
                    self.conn.sendall(("exit".encode()))
                    self.conn.close()
                else:
                    try:
                        risultato = eval(msg)
                        print(risultato)
                        #time.sleep(5)
                        self.conn.sendall((str(risultato).encode()))
                    except:
                        print("Errore, operazione non inserita")
                        self.conn.sendall(("errore".encode()))
                        pass
        except:
            print("no!")

def server(conn, address):
    try:
        while True:
            
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
        print(f"Connesso con {address}")
        t = MyClassThread(conn=conn)
        t.run()

if __name__ == "__main__":
    main()