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
    row1 = "1. Show all employees"
    row2 = "2. Show employee by email"
    row3 = "3. Show employee by name"
    row4 = "4. Show employee with max salary"
    row5 = "5. Show employee with min salary"
    row6 = "6. Show employee with max salary in Ukraine"
    row7 = "7. Show employee with max age by country"
    row8 = "8. Show average age by country"
    choice = int(input(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{
                 row6}\n{row7}\n{row8}\nChoose option:\t"))
    return choice


# 1. Показати всіх працівників
def fetch_all():
    cursor = connection.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()


# 2. Пошук по email
def fetch_by_email(email):
    cursor = connection.cursor()
    query = f"SELECT * FROM employee WHERE email = '{email}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 3. Пошук по імені
def fetch_by_name(name):
    cursor = connection.cursor()
    query = f"SELECT * FROM employee WHERE name = '{name}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 4. Показати працівника з найбільшою ЗП
def fetch_max_salary():
    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE salary = (SELECT MAX(salary) FROM employee)"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 5. Показати працівника з найменшою ЗП
def fetch_min_salary():
    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE salary = (SELECT MIN(salary) FROM employee)"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 6. Показати працівника який отримує найбільшу ЗП в Україні
def fetch_max_salary_ukraine():
    cursor = connection.cursor()
    query = "SELECT * FROM employee WHERE salary = (SELECT MAX(salary) FROM employee WHERE country = 'Ukraine')"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 7. Знайти найстаршого працівника по країні
def fetch_max_age_by_country(country):
    cursor = connection.cursor()
    query = f"SELECT * FROM employee WHERE YEAR(dateOfBirth) = (SELECT MIN(YEAR(dateOfBirth)) FROM employee WHERE country = '{
        country}') and country = '{country}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()


# 8. Знайти AVG вік по країні
def fetch_avg_age_by_country(country):
    cursor = connection.cursor()
    query = f"SELECT AVG(DATEDIFF(year, dateOfBirth, GETDATE())) FROM employee WHERE country = '{
        country}'"
    cursor.execute(query)

    rows = cursor.fetchall()
    print(rows)
    cursor.close()
