from datetime import datetime
import sqlite3


if __name__ == '__main__':
    data = [
        (1, 'Odos', datetime(1986, 1, 4)),
        (2, 'Kayla', datetime(1993, 9, 21)),
        (3, 'Dexter', datetime(2022, 5, 1)),
    ]

    with sqlite3.connect('test3.db',
                        detect_types=sqlite3.PARSE_DECLTYPES |
                        sqlite3.PARSE_COLNAMES) as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO people VALUES(?, ?, ?)", data)