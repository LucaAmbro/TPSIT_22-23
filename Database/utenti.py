import sqlite3 as sq

def inserisci_utente():
    nome = input("Inserisci nome utente: ")
    password = input("Inserisci password: ")
    conn = sq.connect("utenti.db")
    curs = conn.cursor() # ottiene un cursore (permette lo scorrimento dei dati)
    curs.execute("INSERT into UTENTI (Nome, Password) values (?, ?)", (nome, password)) # inserisce le query
    conn.commit() # invia le query accodate
    conn.close() # termina il collegamento con il db
    
if __name__ == "__main__":
    inserisci_utente()