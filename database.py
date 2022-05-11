import sqlite3
import os


def StartDatabase():

    # Remove if already exists
    if os.path.exists("bdExemplo.db"):
        os.remove("bdExemplo.db")

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


def FetchUsers():
    conn = sqlite3.connect("bdExemplo.db")
    cursor = conn.cursor()

    sqlQuerry = open("GetTableResults\getAllUsers.sql").read()

    cursor.execute(sqlQuerry)

    return cursor.fetchall()


def FetchPosts():
    conn = sqlite3.connect("bdExemplo.db")
    cursor = conn.cursor()

    sqlQuerry = open("GetTableResults\getAllPosts.sql").read()

    cursor.execute(sqlQuerry)

    return cursor.fetchall()

# StartDatabase()
# AdicionarUtilizador(["Sagiri721_", "變態猫「紗霧」", 24,
#                    "Tiago Simões, desenvolvedor de software",
#                     "Porto", "Portugal", "21/7/2005"])
#FazerUmPost([0, "Olá Mundo!", 0])


print("-----------------------------------------\nUsers")
print(FetchUsers())

print("-----------------------------------------\nPosts")
print(FetchPosts())
