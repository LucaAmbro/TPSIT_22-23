import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/percorsi')
def percorsi():
    pass

@app.route('/api/v1/percorsi/<id>')
def percorso(id):
    percorso = {"Id":id}
    return jsonify(percorso)

def main():
    app.run()

if __name__ == "__main__":
    main()