from flask import Blueprint, render_template, request, redirect
import psycopg2

lab5 = Blueprint("lab5", __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        port = "5433",
        database = "knowledge_base",
        user = "alena_knowledge_base",
        password = "123"
    )
    return conn;

def dbClose(cursor,connection):
    cursor.close()
    connection.close()

@lab5.route("/lab5")
def main():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        port = "5433",
        database = "knowledge_base",
        user = "alena_knowledge_base",
        password = "123"
    )

    cur=conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()

    print(result)

    return "go to console" 


@lab5.route("/lab5/users")
def users():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        port = "5433",
        database = "knowledge_base",
        user = "alena_knowledge_base",
        password = "123"
    )

    cur=conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    cur.close()
    conn.close()


    return render_template('users.html', result=(result[0][1],result[1][1],result[2][1],result[3][1])) 

