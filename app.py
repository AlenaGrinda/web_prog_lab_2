from flask import Flask, redirect, url_for, render_template
app=Flask(__name__)

@app.route("/")
@app.route("/index")

def start():
    return redirect("/menu", code=302)
@app.route("/menu")
def menu():
    return '''
<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
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
            <li><a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа 1</a></li>
        </main>
    
        <footer>
            &copy; Гринда Алена, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
    return '''
    <!DOCTYPE html>
<html>
    <head>
      <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
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
        <a href="/menu">Меню</a>
        <h2>Реализованные роуты</h2>
        
            <li><a href="http://127.0.0.1:5000/lab1/dog" target="_blank">Корги</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент НГТУ</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python" target="_blank">Питон</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/egor" target="_blank">Петровичев Егор Васильевич</a></li>
        </main>
        <footer>
            &copy; Гринда Алена, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''
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

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
    </head>
    <body>

    <h1>Гринда Алена Игоревна</h1>
    <img src="'''+ url_for('static', filename='logo.jpeg') + '''"> 
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
    </head>
    <h1>Язык приграммирования Python</h1>
    <body>
    <main>
    <div>
    Python полезен при написании серверного кода, поскольку он предлагает множество библиотек, состоящих из предварительно написанного кода для сложных серверных функций. Также разработчики используют широкий спектр платформ Python, которые предоставляют все необходимые инструменты для более быстрого и простого создания интернет-приложений. Например, разработчики могут создать «скелет» интернет-приложения за считанные секунды, потому что им не нужно писать код с нуля. Затем его можно протестировать с помощью инструментов тестирования платформы независимо от внешних инструментов тестирования.
    </div>
    <div>Веб-разработка на стороне сервера включает в себя сложные серверные функции, с помощью которых веб-сайты отображают информацию для пользователя. Например, веб-сайты должны взаимодействовать с базами данных и другими веб-сайтами, а также защищать данные при их отправке по сети. </div>
    </main>
    
    <img src="'''+ url_for('static', filename='python.png') + '''"> 
    </body>
</html>
'''
@app.route('/lab1/egor')
def egor():
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css') + '''"">
    </head>
    <body>

    <h1>Петровичев Егор Васильевич</h1>
    <main>
    <div>Егор, как правило, упрям, честолюбив и любит порядок. У мужчин с таким именем бывают непростые взаимоотношения с людьми, но их талант умело приспосабливаться к любой ситуации и нравиться людям помогает им найти близких друзей и хороших деловых партнеров. Из Егоров вырастают прекрасные отцы и верные мужья
</div>
    <div>Егор по природе своей трудолюбив и усидчив. Но несмотря на то, что он способен долго и упорно заниматься одним и тем же делом, даже не пытайтесь заставить его приложить хоть каплю усилий к тому, что ему не нравится.</div>
    </main>
    <img src="'''+ url_for('static', filename='egog.jpeg') + '''"> 
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name, group, course, lab_num  = 'Гринда Алена', 'ФБИ-13', '3 курс', 2
    fruits = [
        {'name':'яблоки', 'price': 100}, 
        {'name':'груши', 'price': 120}, 
        {'name':'апельсины', 'price': 80}, 
        {'name':'мандарины', 'price': 95}, 
        {'name':'манго', 'price': 321} 
        ]
    books = [
        {'author': 'Лев Толстой', 'name': 'Война и Мир', 'genre': 'Историческая проза', 'pages': 1300},
        {'author': 'Джордж Оруэлл', 'name': '1984', 'genre': 'Социальная фантастика', 'pages': 320},
        {'author': 'Джеймс Джойс', 'name': 'Улисс', 'genre': 'Роман', 'pages': 800},
        {'author': 'Владимир Набоков ', 'name': 'Лолита', 'genre': 'Роман', 'pages': 448},
        {'author': 'Уильям Фолкнер', 'name': 'Звук и ярость', 'genre': 'Роман', 'pages': 416},
        {'author': 'Ральф Эллисон', 'name': 'Человек-невидимка', 'genre': 'Роман', 'pages': 170},
        {'author': 'Вирджиния Вулф', 'name': 'На маяк', 'genre': 'Роман', 'pages': 288},
        {'author': 'Джейн Остен', 'name': 'Гордость и предубеждение', 'genre': 'Роман', 'pages': 416},
        {'author': 'Данте Алигьери', 'name': 'Божественная комедия', 'genre': 'Поэма', 'pages': 464},
        {'author': 'Джеффри Чосер', 'name': 'Кентерберийские рассказы', 'genre': 'Проза', 'pages': 800},
    ]

    return render_template('example.html', name = name, group =  group, course = course, lab_num = lab_num, fruits=fruits, books = books)  

@app.route('/lab2/')
def lab2():
 return render_template('lab2.html')

@app.route('/lab2/shoes')
def shoes():
 return render_template('shoes.html')