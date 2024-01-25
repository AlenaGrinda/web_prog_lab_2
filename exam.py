from flask import Blueprint, request, render_template
exam = Blueprint('exam', __name__)

days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

def check_number(number):
    try:
        number = int(number)
        if number >= 1 and number <= 7:
            return f'{number}: {days_of_week[number - 1]}'
        else:
            return 'Введите число от 1 до 7'
    except ValueError:
        return 'Введите корректное число'

@exam.route('/exam/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = request.form['number']
        if number and number.isdigit():
            result = check_number(int(number))
        else:
            result = 'Введите корректное число'

    return render_template('exam.html', result=result)

