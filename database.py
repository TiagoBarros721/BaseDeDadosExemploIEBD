from re import S
import sqlite3


def StartDatabase():

    conn = sqlite3.connect("bdExemplo.db")
    cursor = conn.cursor()

    tableText = open("createTables.sql").read()

    cursor.executescript(tableText)

    cursor.close()


def AdicionarUtilizador(recordList):

    conn = sqlite3.connect("bdExemplo.db")
    cursor = conn.cursor()

    sqlQuerry = open("insertUser.sql").read()

    cursor.execute(sqlQuerry, recordList)

    conn.commit()
    cursor.close()


def FazerUmPost(recordList):

    conn = sqlite3.connect("bdExemplo.db")
    cursor = conn.cursor()

    sqlQuerry = open("insertPost.sql").read()

    cursor.execute(sqlQuerry, recordList)

    conn.commit()
    cursor.close()
