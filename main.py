import json
from flask import Flask, render_template, request
from utils.database import Database
from utils.schemas import Users
# from sample import sample_fn

app = Flask(__name__)
db = Database("db_sqlite3")
db.init()


@app.route('/')
def index():
    cursor = db.get_cursor()
    # cursor.execute("""INSERT INTO users (id, username, password, role, age)
    #               VALUES ("BOB", "4444", "admin", 25 )
    #               """)
    data = cursor.execute("SELECT * FROM users").fetchall()
    print(data)
    response_data = [Users(*obj) for obj in data]
    data = {'users': response_data}
    return render_template('index.html', users = response_data)


@app.route('/', methods=['POST'])
def create_user():
    if request.method =='POST':
        print(request.form)
        cursor = db.get_cursor()
        cursor.execute(f"""INSERT INTO users (id, username, password, role, age)
                      VALUES ({request.form.get('username')}, "4444", "admin", 25 )
                      """)
    return 'asd'













# def main_fn():
#     print(__name__)
#     sample_fn()
#
#
# if __name__ == '__main__':
#     main_fn()