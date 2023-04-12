from datetime import datetime
import sqlite3

def date_to_str(d: datetime):
    return d.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    d1 = datetime(1980, 1, 1)
    d2 = datetime(1995, 1, 1)
    sql = f'SELECT * FROM people WHERE date BETWEEN "{date_to_str(d1)}" AND "{date_to_str(d2)}";'

    with sqlite3.connect('test1.db',
                        detect_types=sqlite3.PARSE_DECLTYPES |
                        sqlite3.PARSE_COLNAMES) as con:
        cur = con.cursor()
        res = cur.execute(sql)
        print(res.fetchall())