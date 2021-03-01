from flask import Flask, render_template, redirect, url_for, request
import json

app = Flask(__name__)

dados = {} # dicionário dos dicionários dos dados
contador = 0 # posição onde estará o próximo dicionário

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Recebe os dados do formulário
        nome = request.form["nomecompleto"]
        grupo = request.form["grupo"]
        regional = request.form["regional"]
        dose = request.form["dose"]

        # Adiciona os dados ao dicionário
        global contador
        dados[contador] = {"nome":nome, "grupo":grupo, "regional":regional, "dose":dose}
        contador += 1

        # salva o dicionário no arquivo json
        with open('dados.json', "w") as file:
            json.dump(dados, file)

        return redirect(url_for("index"))
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)