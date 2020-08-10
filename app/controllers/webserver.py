from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

from app.models import user_info_access
from app.models import books_access

app = Flask(__name__, static_folder='../../static', template_folder='../views')


@app.route("/", methods=['GET'])
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    # 全てのユーザをDBから取得
    user_datas = user_info_access.get_all()

    user_name = request.form.get("name")
    user_pass = request.form.get("pass")

    # 入力された情報と合致するデータがDBに存在するか判定
    for user_data in user_datas:
        if user_name == user_data["name"]:
            if user_pass == user_data["pass"]:
                # ログイン成功ページへ
                return redirect(url_for("home"))
            else:
                # パスワードが異なる場合、ログインエラーページへ
                return render_template("login.html", message="ログインエラー。パスワードが違います。")
    # ユーザが未存在の場合、ログインエラーページへ
    return render_template("login.html", message="ログインエラー。ユーザが存在しません。")



@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        # 書籍の追加ページを表示
        return render_template("add_user.html")
    else:
        name = request.form.get("name")
        password = request.form.get("pass")

        # ユーザ情報をDBに登録
        result = user_info_access.add(name, password)
        if result:
            # 登録に成功した場合
            return render_template("login.html", message="ユーザの追加に成功しました。")
        else:
            # 登録に失敗した場合
            return render_template("add_user.html", error="ユーザの追加に失敗しました。")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/book_list")
def get_books():
    # 全ての書籍を取得
    books = books_access.get_all()

    return render_template("book_list.html", books=books)


@app.route("/book_list/<id>")
def get_book(id):
    # 全ての書籍を取得
    book = books_access.get(id)

    return render_template("book_list.html", books=book)


@app.route("/edit_book/<id>", methods=["GET", "POST"])
def edit_book(id):
    if request.method == "GET":
        book = books_access.get(id)
        if book:
            # 編集する書籍を取得できた場合
            return render_template("edit_book.html", book=book[0])
        else:
            # 編集する書籍を取得できなかった場合
            return redirect(url_for("error"))
    else:
        id = request.form.get("id")
        name = request.form.get("name")
        price = request.form.get("price")

        book = books_access.get(id)
        result = books_access.update(id, name, price)

        if result:
            # 更新に成功した場合
            return redirect(url_for("home"))
        else:
            # 更新に失敗した場合
            return render_template("edit_book.html", book=book[0], error="書籍の更新に失敗しました。")


@app.route("/search_book", methods=["GET", "POST"])
def search_book():
    if request.method == "GET":
        # 書籍の検索ページを表示
        return render_template("search_book.html")
    elif request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("name")
        price = request.form.get("price")

        # 全ての書籍を取得
        books = books_access.get(id, name, price)
        return render_template("book_list.html", books=books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        # 書籍の追加ページを表示
        return render_template("add_book.html")
    elif request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")

        # 書籍情報をDBに登録
        result = books_access.add(name, price)
        if result:
            # 登録に成功した場合
            return redirect(url_for("home"))
        else:
            # 登録に失敗した場合
            return render_template("add_book.html", error="書籍の追加に失敗しました。")


@app.route("/delete_book/<id>")
def delete_book(id):
    result = books_access.delte(id)
    if result:
        return redirect(url_for("home"))
    else:
        # 登録に失敗した場合
        return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("error.html")


def start():
    app.run(host='127.0.0.1', port=8080, threaded=True)