import mysql.connector


def get_connection():
    connection = mysql.connector.connect(host='localhost',
                                         database='hospital_db',
                                         user='root',
                                         password='3128735409cd')
    return connection


def close_connection(connection):
    if connection:
        connection.close()
