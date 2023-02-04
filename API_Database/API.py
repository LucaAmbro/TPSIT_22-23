import json
import sqlite3
from flask import Flask, jsonify, request

def get_percorsi(cursor):
    cursor.execute("SELECT id, nome FROM Percorso")
    percorsi = cursor.fetchall()
    return [{"id":percorso[0], "nome":percorso[1]} for percorso in percorsi]


def get_mosse(cursor, cod_percorso):
    cursor.execute(f"SELECT codPercorso, posizione, codMovimento, tempo FROM Percorso, Mossa WHERE Percorso.id = {cod_percorso} AND Percorso.id = Mossa.codPercorso")
    mosse = cursor.fetchall()
    return [{"codPercorso":mossa[0], "posizione":mossa[1], "codMovimento":mossa[2], "tempo":mossa[3]} for mossa in mosse]


def get_percorso(id, cursor):
    cursor.execute("SELECT id, nome FROM Percorso WHERE id = ?", (id,))
    percorso = cursor.fetchone()
    mossa = cursor.execute("""SELECT posizione, codMovimento, tempo, nome FROM Mossa, Movimento WHERE codPercorso = ? AND 
                            codMovimento = Movimento.id ORDER BY posizione""", (id,))
    mossa = cursor.fetchall()
    print(mossa)
    mosse = [{"id":m[1], "nome":m[3], "tempo":m[2], "posizione":m[0]} for m in mossa]
    return {"id":percorso[0], "nome":percorso[1], "mossa":mosse}


app = Flask(__name__)

@app.route("/api/v1/percorsi", methods = ['GET'])
def lista_percorsi(): 
    try:
        with sqlite3.connect('percorsi.db') as conn:
            cursor = conn.cursor()
            percorsi = get_percorsi(cursor)
            temp = jsonify({"success":True, "result":percorsi})
            return temp
    except Exception as e:
        return jsonify({"success":False, "error":str(e)})


@app.route("/api/v1/percorsi", methods = ['POST'])
def crea_percorso():
    dati = request.get_json()
    print(dati)
    try:
        with sqlite3.connect('percorsi.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO Percorso VALUES({dati})")
            percorsi = get_percorsi(cursor)
            temp = jsonify({"success":True, "result":percorsi})
            return temp
    except Exception as e:
        return jsonify({"success":False, "error":str(e)})


@app.route("/api/v1/percorsi/<id>/mosse", methods = ['POST'])
def crea_mossa():
    dati = request.get_json()
    try:
        with sqlite3.connect('percorsi.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO Mossa VALUES({dati})")
            mosse = get_mosse(cursor)
            temp = jsonify({"success":True, "result":mosse})
            return temp
    except Exception as e:
        return jsonify({"success":False, "error":str(e)})


@app.route("/api/v1/percorsi/<id>")
def dettagli_percorso(id):
    conn = sqlite3.connect('percorsi.db')
    cursor = conn.cursor()
    percorso = get_percorso(id, cursor) 
    temp= jsonify(percorso) 
    conn.close()
    return temp


def main():
    app.run()

if __name__ == "__main__":
    main()