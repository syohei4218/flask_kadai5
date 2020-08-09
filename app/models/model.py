import sqlite3

DB_DIR = "db/sqlite3.db"


def create_table():

    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    cur.execute('CREATE TABLE user_info'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name STRING not null,'
                'pass STRING not null)')

    conn.commit()

    cur.close()
    conn.close()


def init_add_user_info():

    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    cur.execute('insert into user_info(name, pass)values("zako", "weak_pass")')
    cur.execute('insert into user_info(name, pass) values("ikarochan", "kawaii")')
    cur.execute('insert into user_info(name, pass) values("miku", "hatsune")')
    conn.commit()

    cur.close()
    conn.close()


def get_all():
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('select * from user_info')

    return cur.fetchall()


