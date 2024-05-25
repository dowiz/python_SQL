import pyodbc
from datetime import datetime

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
    row9 = "9. Add employee"
    row10 = "10. Delete employee"
    choice = int(input(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{
                 row6}\n{row7}\n{row8}\n{row9}\n{row10}\nChoose option: "))
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


# 9. Додати працівника в базу даних ()
def add_employee():

    cursor = connection.cursor()
    column_names = get_column_names()
    column_data_types = get_column_data_types()
    column_values = []
    i = 0
    for column_name in column_names:
        if column_name == "dateOfBirth ":
            date_string = input(f"Enter dateOfBirth (dd.mm.yyyy): ")
            date_object = datetime.strptime(date_string, "%d.%m.%Y")
            column_value = date_object.strftime("%b %d, %Y")
            column_values.append(f"'{column_value}'")
        else:
            if column_data_types[i] == "int":
                column_value = input(f"Enter {column_name}: ")
                column_values.append(column_value)
            elif column_data_types[i] == "varchar":
                column_value = input(f"Enter {column_name}: ")
                column_values.append(f"'{column_value}'")
            else:
                print("Unknown data type")
                column_value = input(f"Enter {column_name}: ")
                column_values.append(f"'{column_value}'")
        i += 1
    column_names_string = ", ".join(column_names)
    column_values_string = ", ".join(column_values)
    print(column_names_string)
    print(column_values_string)

    query = f"INSERT INTO employee ({column_names_string}) VALUES ({
        column_values_string})"
    cursor.execute(query)
    connection.commit()
    cursor.close()


def get_column_names():
    cursor = connection.cursor()
    query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' and COLUMN_NAME != 'employeeID'"
    cursor.execute(query)

    rows = cursor.fetchall()
    column_names = [row[0] for row in rows]
    cursor.close()
    return column_names


def get_column_data_types():
    cursor = connection.cursor()
    query = "SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'employee' and COLUMN_NAME != 'employeeID'"
    cursor.execute(query)

    rows = cursor.fetchall()
    column_data_types = [row[0] for row in rows]
    cursor.close()
    return column_data_types


def delete_employee():
    cursor = connection.cursor()
    employee_id = input("Enter employeeID: ")
    query = f"DELETE FROM employee WHERE employeeID = {employee_id}"
    cursor.execute(query)
    connection.commit()
    cursor.close()


if __name__ == "__main__":
    print(get_column_data_types())
