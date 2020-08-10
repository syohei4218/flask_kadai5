import sqlite3

DB_DIR = "db/sqlite3.db"


def create_table():
    """
    テーブル作成。
    初期に1度だけ行うこと。
    """
    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()
    cur.execute('CREATE TABLE books'
                '(id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name STRING not null,'
                'price int not null)')

    conn.commit()
    cur.close()
    conn.close()


def init_add():
    """
    初期値として固定のレコードを追加する用。
    """
    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    cur.execute('insert into books(name, price)values("鬼滅の刃 1", 200)')
    cur.execute('insert into books(name, price) values("鬼滅の刃 2", 300)')
    cur.execute('insert into books(name, price) values("鬼滅の刃 3", 400)')

    conn.commit()
    cur.close()
    conn.close()


def add(name, price):
    """
    booksテーブルに任意のレコードを追加
    """
    conn = sqlite3.connect(DB_DIR)
    cur = conn.cursor()

    try:
        cur.execute('insert into books(name, price)values("{}", {})'.format(name, price))
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


def get(id=None, name=None, price=None):
    """
    booksテーブルのレコードを任意で検索。
    引数がない場合、全検索と同じ動きをするようにしている。
    """
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    where = []
    sql = 'select * from books'

    # それぞれの引数が存在すれば、条件文に追加
    if id:
        where.append('id = {}'.format(id))
    if name:
        where.append('name = "{}"'.format(name))
    if price:
        where.append('price = {}'.format(price))

    if where:
        # 条件文が存在する場合、"where"を追加し、条件分を"and"で結合
        sql = sql + " where " + " and ".join(where)

    cur.execute(sql)

    return cur.fetchall()


def update(id, name, price):
    """
    booksテーブルの1レコードを更新
    """
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sql = 'update books set name = "{}", price = {} ' \
          'where id = {}'.format(name, price, id)

    try:
        cur.execute(sql)
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

    return cur.fetchall()


def delte(id):
    """
    booksテーブルの1レコードを更新
    """
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    sql = 'delete from books where id = "{}"'.format(id)

    try:
        cur.execute(sql)
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

    return cur.fetchall()


def get_all():
    """
    booksテーブルのレコードを全検索。
    """
    conn = sqlite3.connect(DB_DIR)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    #全検索
    cur.execute('select * from books')

    return cur.fetchall()


