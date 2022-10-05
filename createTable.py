import json
from sys import argv


import mysql.connector
from mysql.connector import Error


def getType(type):
    if type == 'bool':
        return 'BOOLEAN'
    elif type == 'int':
        return 'INT'
    elif type == 'string' or type == 'str':
        return "VARCHAR(200)"
    else:
        print(f'Error type {type}: default value set: VARCHAR(200)')
        return "VARCHAR(200)"

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='Test',
                                        user='tom',
                                        password='zombis00')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

mycursor = connection.cursor()


new = ""


f = open(argv[1])
table = json.load(f)

# print(table)
for i in table:
    new += f"{i} {getType(table[i])}, "
new = new[:-2]

QUERY = f"CREATE TABLE {argv[2]} ({new});"
# print(new)
mycursor.execute(QUERY)





if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")