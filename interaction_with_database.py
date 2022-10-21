import mysql.connector as msc
import keyring


def connection():
    x = keyring.get_credential('wheelie', username=None)
    user = x.username
    password = x.password
    host = '80.211.255.121'
    port = 3396
    database = 'wheelie'
    mydb = msc.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = mydb.cursor()
    return mydb, cursor


def select_data(query):
    db, cursor = connection()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
