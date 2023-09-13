from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route("/")
@app.route("/index")

def start():
    return redirect("/menu", code=302)
@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>
            «НГТУ, ФБ, Лабораторные работы»1
        </title>
    </head>

    <body>
        <header>
           «НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных»
        </header>
        <main>
        <h1>Лабораторные работы по WEB-программированию</h1>
        <ol>
            <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a></li>
        </ol>
        </main>
    
        <footer>
            &copy; Гринда Алена, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
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
        <main>
        <h1>
            web-сервер на flask
        </h1>
            <div> 
        Flask — фреймворк для создания веб-приложений на языке программирования Python,
        использующий набор инструментов Werkzeug, а также шаблонизатор Jinja2. 
        Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
        сознательно предоставляющих лишь самые ба- зовые возможности.
        </div>
        </main>
        <footer>
            &copy; Гринда Алена, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/dog')
def dog():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
    </head>
    <body>

    <h1>Корги</h1>
    <img src="'''+ url_for('static', filename='dog.jpeg') + '''"> 
    </body>
</html>
'''