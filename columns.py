from typing import NamedTuple


class ColumnInfo(NamedTuple):
    cid: int
    name: str
    type: str
    notnull: int
    dflt_value: str
    pk: int


def columns_data(cur, table_name: str) -> tuple:
    sql = f"PRAGMA table_info({table_name});"
    res = cur.execute(sql)
    cols = res.fetchall()
    return tuple(ColumnInfo(*col) for col in cols)


def columns_names(cur, table_name: str) -> tuple:
    col_data = columns_data(cur, table_name)
    return tuple(col.name for col in col_data)


def columns_types(cur, table_name: str) -> tuple:
    col_data = columns_data(cur, table_name)
    return tuple(col.type for col in col_data)


def primary_keys(cur, table_name: str) -> tuple:
    col_data = columns_data(cur, table_name)
    return tuple(col.name for col in col_data if col.pk)


if __name__ == '__main__':
    import sqlite3

    with sqlite3.connect('data/test.db',
                        detect_types=sqlite3.PARSE_DECLTYPES |
                        sqlite3.PARSE_COLNAMES) as con:
        cur = con.cursor()
        print(columns_data(cur, 'train'))
        print(columns_names(cur, 'train'))
        print(columns_types(cur, 'train'))
        print(primary_keys(cur, 'train'))