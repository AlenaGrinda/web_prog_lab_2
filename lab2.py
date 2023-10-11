from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
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

@lab2.route('/lab2/')
def lab_2():
 return render_template('lab2.html')


@lab2.route('/lab2/shoes')
def shoes():
 return render_template('shoes.html')

