from flask import Blueprint,render_template, request, redirect, session, abort, jsonify
from datetime import datetime

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('/lab8/index.html')

courses = [
    {'name': 'c++', 'videos':3, 'price': 3000, 'creation_date': '2024.01.17'},
    {'name': 'basic', 'videos':30, 'price': 0},
    {'name': 'c#', 'videos':8}
]


@lab8.route('/lab8/api/courses/', methods=["GET", "POST"])
def get_courses():
    if request.method == "GET":
        return jsonify(courses)
    elif request.method == "POST":
        course = request.get_json()
        course["creation_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        courses.append(course)
        return jsonify(courses)


@lab8.route('/lab8/api/courses/<int:course_num>', methods=["GET"])
def get_course(course_num):
    if 0 <= course_num < len(courses):
        return courses[course_num]
    else:
        abort(404)


@lab8.route('/lab8/api/courses/<int:course_num>', methods=["DELETE"])
def del_course(course_num):
    if 0 <= course_num < len(courses):
        del courses[course_num]
        return '', 204
    else:
        abort(404)


@lab8.route('/lab8/api/courses/<int:course_num>', methods=["PUT"])
def put_course(course_num):
    if 0 <= course_num < len(courses):
        course = request.get_json()
        courses[course_num] = course
        return courses[course_num]
    else:
        abort(404)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=["POST"])
def add_course(course_num):
    course = request.get_json()
    course["creation_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    courses.append(course)
    return {"num": len(courses)-1}