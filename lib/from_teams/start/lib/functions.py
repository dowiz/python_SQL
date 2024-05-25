import pyodbc

server = '10.7.201.111'
database = 'CMR321'
username = 'sa'
password = 'Qwerty-1'

connection = pyodbc.connect('DRIVER={SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD=' + password)


def menu():
    choice = int(input(f"1. Show all employees\n2. Show employee by email\n"))
    return choice


def fetch_all():
    cursor = connection.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


def fetch_by_email(email):
    cursor = connection.cursor()
    query = f"SELECT * FROM employee WHERE email = '{email}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()
