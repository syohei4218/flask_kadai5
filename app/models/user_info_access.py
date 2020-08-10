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


def init_add():

    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    cur.execute('insert into user_info(name, pass)values("zako", "weak_pass")')
    cur.execute('insert into user_info(name, pass) values("ikarochan", "kawaii")')
    cur.execute('insert into user_info(name, pass) values("miku", "hatsune")')
    conn.commit()

    cur.close()
    conn.close()


def add(name, password):

    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    try:
        cur.execute('insert into user_info(name, pass)values("{}", "{}")'.format(name, password))
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    else:
        conn.commit()
        return True
    finally:
        cur.close()
        conn.close()


def get_all():
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('select * from user_info')

    return cur.fetchall()


