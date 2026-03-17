from flask import Flask, request, url_for, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    n = "Gonçalo"
    return render_template("index.html",
                           nome=n)


@app.route('/profile')
def profile():
    return render_template("perfil.html")


@app.route('/info')
def infos():
    id = request.args.get('id', "foo")
    return f"<h1>infos - {escape(id)}</h1>"


@app.route('/infos/<int:user_id>')
def info_id(user_id: int):
    return f"<h1>infos id - {escape(user_id)}</h1>"


@app.route('/infos2/<path:user_path>')
def info2_id(user_path):
    return f"<h1>infos 2 id - {escape(user_path)}</h1>"


@app.route('/infos3/<user_path>')
def info3_id(user_path):
    return f"<h1>infos 3 id - {escape(user_path)}</h1>"


@app.route('/infos4')  # /infos4/ -> Erro
def pag3():
    id = request.args.get('id', "foo")
    return f"<h1>pag3 v1 - {escape(id)}</h1>"


@app.route('/infos5/')  # /infos5  -> /infos5/
def pag32():
    id = request.args.get('id', "foo")
    return f"<h1>pag3 v2 - {escape(id)} </h1>"


"""

<p> </p> -> 
<h1> </h1> -> 
</br> -> 
<a> </a> -> 
<div> </div> -> 

<body> </body> -> 

<input > </input> -> 
<button > </button> -> 

"""


@app.route('/user/<name>')
def user(name: str):
    return f"<h1>user - {escape(name)}</h1>"


@app.route('/profile/info')
def profile_infos():
    id = request.args.get('id', "foo")
    return f"infos do perfil {id}"


@app.route('/teste_urls')
def testeURL():
    url_1 = url_for('profile_infos', id=1)
    return f"""
    <a href='{url_1}'> click me query </a> 
    <br \>
    <a href='{url_for('user', name="goncalo")}'> click me  path</a> 
    """


if __name__ == '__main__':
    app.run()
