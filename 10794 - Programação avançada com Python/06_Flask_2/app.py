from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here

    ctx = {
        "titulo": "Página 1 - backend v3",
        "conteudo": "conteúdo - backend v3"
    }

    return render_template('index.html', **ctx)


@app.route('/nomes')
def nomes():  # put application's code here

    lista_nomes = ["Rita", "Rui", "Joana", "Pedro"]
    ctx = {
        "titulo": "Lista de nomes",
        "nomes": lista_nomes
    }

    return render_template('nomes.html', **ctx)


@app.route('/registar')
def register():
    ctx = {
        "titulo": "Registar Alunos",
    }

    return render_template('registar.html', **ctx)


@app.route('/process_registo', methods=['POST'])
def proc_register():
    print("Processo de registo")

    nome = request.form.get("nome")
    email = request.form.get("email")
    media = request.form.get("media")

    print(nome, email, media)

    return redirect(url_for('register'))


if __name__ == '__main__':
    app.run()
