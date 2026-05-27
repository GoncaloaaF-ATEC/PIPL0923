import requests
from faker import Faker
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

fake = Faker()


@app.route('/')
def index():  # put application's code here

    ctx = {
        "titulo": "Ler dados de uma API",
        "conteudo": "Página principal",
    }

    return render_template("main.html", **ctx)


@app.route('/posts')
def ler_dados():
    url = "https://jsonplaceholder.typicode.com/posts/"

    resposta = requests.get(url)

    print(resposta.status_code)
    posts = resposta.json()
    print(posts)

    ctx = {
        "titulo": "Ler dados de uma API",
        "posts": posts,
    }

    return render_template("posts.html", **ctx)


def get_comt(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"
    cmts = requests.get(url)
    cmts = cmts.json()
    return cmts if len(cmts) > 0 else []


def get_user(usr_id: int):
    url_usr = f"https://jsonplaceholder.typicode.com/users/{usr_id}"
    cmts = requests.get(url_usr)
    cmts = cmts.json()
    return cmts if len(cmts) > 0 else []


@app.route('/post/<int:id>')
def post(id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"

    resposta = requests.get(url)
    my_post = resposta.json()
    usr_id = my_post["userId"]

    usr_data = get_user(usr_id)

    cmts = get_comt(id)
    ctx = {
        "titulo": "Ler dados de uma API",
        "post": my_post,
        "user": usr_data["username"],
        "user_id": usr_data["id"],
        "comments": cmts,
    }

    return render_template("post.html", **ctx)


@app.route('/user_info/<int:id>')
def user_info(usr_id: int):
    usr_data = get_user(usr_id)

    ctx = {
        "titulo": "Ler dados de uma API",
        "user": usr_data,
    }

    return render_template("userInfo.html",
                           **ctx)


@app.route("/add_post/", methods=["POST", "GET"])
def add_post():
    post = request.args.get("post")
    ctx = {
        "titulo": "Ler dados de uma API",
        "post": post
    }

    if request.method == "POST":
        title = request.form.get("titulo", "")
        content = request.form.get("body", "")
        ## fazer o post para o servidor
        data = {
            "title": title,
            "body": content,
            "userId": 1,
        }

        req = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

        post = None
        if req.status_code == 201:
            post = req.json()  # get

        return redirect(url_for("add_post",
                                post=post))

    return render_template("addPost.html",
                           **ctx)


if __name__ == '__main__':
    app.run()
