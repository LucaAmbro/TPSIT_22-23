import requests

HOST = "http://localhost:5000"

def get_percorsi():
    percorsi = requests.get(f"{HOST}/api/v1/percorsi") # api perchè è solo una parte del programma, v1 perchè ci possono essere più versioni
    # quelle più vecchie deprecate
    return percorsi

def crea_percorso():
    try:
        percorso = input("Inserisci nome percorso: ")
        data = {"nome":percorso, }
        requests.post(f"{HOST}/api/v1/percorsi", json=data)
        return True
    except:
        return False

def crea_mossa():
    try:
        mossa = input("Inserici mossa da aggiungere: ")
        percorso = input("Inserisci percorso: ")
        data = {"mossa":mossa, }
        requests.post(f"{HOST}/api/v1/{percorso}/mossa", json=data)
        return True
    except:
        return False

def get_movimenti():
    movimenti = requests.get(f"{HOST}/api/v1/movimenti")
    return movimenti

def main():
    running = True
    while running:
        comando = int(input("""Inserisci comando (1 -> inserisci percorso, 2 -> inserisci mossa, 3 -> visualizza percorsi, 4 -> 
                            visualizza movimenti): """))
        
        if comando == 1:
            crea_percorso()
        elif comando == 2:
            crea_mossa()
        elif comando == 3:
            percorsi = get_percorsi()
            print(percorsi.content)
        elif comando == 4:
            movimenti = get_movimenti()
            print(movimenti)

if __name__ == "__main__":
    main()