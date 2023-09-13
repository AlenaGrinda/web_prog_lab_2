from flask import Flask
app=Flask(__name__)

@app.route("/")
def start():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>
            Гринда Алена Игоревна, Лабораторная 1
        </title>
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>
            web-сервер на flask
        </h1>

        <footer>
            &copy; Гринда Алена, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""