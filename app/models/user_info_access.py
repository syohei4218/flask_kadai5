import sqlite3

DB_DIR = "db/sqlite3.db"


def create_table():
    """
    テーブル作成。
    初期に1度だけ行うこと。
    """
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
    """
    初期値として固定のレコードを追加する用。
    """
    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    cur.execute('insert into user_info(name, pass)values("zako", "weak_pass")')
    cur.execute('insert into user_info(name, pass) values("ikarochan", "kawaii")')
    cur.execute('insert into user_info(name, pass) values("miku", "hatsune")')
    conn.commit()

    cur.close()
    conn.close()


def add(name, password):
    """
    user_infoテーブルに任意のレコードを追加

    """
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
    """
    user_infoテーブルのレコードを全検索。
    """
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('select * from user_info')

    return cur.fetchall()


