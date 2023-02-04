from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import sqlite3 as sq

def inserisci_utente(username, password):
    conn = sq.connect("utenti.db")
    curs = conn.cursor() # ottiene un cursore (permette lo scorrimento dei dati)
    curs.execute("INSERT into UTENTI (Username, Password) values (?, ?)", (username, password)) # inserisce le query
    conn.commit() # invia le query accodate
    conn.close() # termina il collegamento con il db
    return True

def login_utente(username, password):
    conn = sq.connect("utenti.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM UTENTI WHERE Username = ? AND Password = ?", (username, password))
    conn.commit()
    rows = curs.fetchall()
    conn.close()
    return rows

def ricerca_elemento(elemento):
    conn = sq.connect("utenti.db")
    curs = conn.cursor()
    #print('%'+elemento+'%')
    try:
        curs.execute("SELECT Username FROM UTENTI WHERE Username LIKE ?",  ('%' + elemento + '%',))
    except:
        return False
    conn.commit()
    rows = curs.fetchall()
    conn.close()
    return rows

MAX_SIZE = 7000

def run_server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("0.0.0.0", 5000))

        s.listen()
        print("In Ascolto")

        client, clientAddress = s.accept()
        print(f"Si è connesso: {clientAddress[0]} con successo alla porta {clientAddress[1]}")
        running = True
        while running:
            msg = client.recv(MAX_SIZE)
            msg = msg.decode()
            msg = msg.split(";")
            if msg[0] == "signup":
                try:
                    valore = inserisci_utente(msg[1], msg[2])
                    if valore:
                        client.sendall("Utente registrato correttamente".encode())
                except:
                    client.sendall("Errore, nome utente o password errati".encode())
            else:
                righe = login_utente(msg[1], msg[2])
                if len(righe) > 0:
                    client.sendall("Dati inseriti corretti".encode())
                    richiesta = True
                    while richiesta:
                        msg = client.recv(MAX_SIZE)
                        msg = msg.decode()
                        if msg == "exit":
                            richiesta = False
                        else:
                            ris = ricerca_elemento(msg)
                            if ris == False:
                                client.sendall("Elemento inserito non esistente".encode())
                            else:
                                print(ris)
                                m  = "Elemento trovato: " + ris[0][0]
                                client.sendall(m.encode())
                            
if __name__ == "__main__":
    run_server() 