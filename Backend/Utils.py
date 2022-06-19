import sqlite3
from sqlite3 import Error
from flask import Flask, jsonify, request

DB_PATH = 'C:\\Users\\noamc\\PycharmProjects\\DataBasesUI\\identifier.sqlite'


def execute_action(sqlite_connection, query):
    conn = sqlite_connection.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    return True


def cursor_result_to_json(cursor):
    return [
        dict(
            (cursor.description[i][0], value)
            for i, value in enumerate(row)
        )
        for row in cursor.fetchall()
    ]


def get_table(sqlite_connection, table_name):
    with sqlite_connection.connection.cursor() as cursor:
        cursor.execute("select * from (%s)", table_name)
        result = cursor_result_to_json(cursor)
    return result


def execute_select(sqlite_connection, path, params={}):
    with open(path) as query:
        with sqlite_connection.connection.cursor() as cursor:
            cursor.execute(query.read())
            result = cursor_result_to_json(cursor)
    return result


def delete_from_table(sqlite_connection, table_name, row_id, id_col_name='id'):
    query = f"DELETE FROM {table_name} WHERE {id_col_name}={row_id}"
    execute_action(sqlite_connection, query)
