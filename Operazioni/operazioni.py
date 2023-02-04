from flask import Flask, request

app = Flask(__name__)

@app.route("/somma", methods=['GET']) # decorator: prende in input la funzione somma, e restituisce una funzione. Trasforma la funzione python in una richiesta GET
def somma():
    try:
        a = int(request.args.get("txtA"))
        b = int(request.args.get("txtB"))
        c = a + b
        return str(c)
    except:
        return "<h1>Errore nell'input</h1>"

@app.route("/", methods=['GET'])
def home_page():
    return """
    <html>
        <body>
            <form action="/somma" method="POST">
                <label for="primoNumero">Primo numero</label>
                <input type="text" id="primoNumero" name="txtA"></input>
                <br>
                <label for="secondoNumero">Secondo numero</label>
                <input type="text" id="secondoNumero" name="txtB"></input>
                <br>
                <input type="submit" value="Somma">
            </form>
        </body>
    </html>
    """
@app.route("/somma", methods=['POST']) 
def somma_post():
    try:
        a = int(request.form.get("txtA"))
        b = int(request.form.get("txtB"))
        c = a + b
        return str(c)
    except:
        return "<h1>Errore nell'input</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")