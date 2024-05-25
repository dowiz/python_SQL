from lib.functions import menu, fetch_by_email, fetch_all, fetch_by_name, fetch_max_salary, fetch_min_salary, fetch_max_salary_ukraine, fetch_max_age_by_country, fetch_avg_age_by_country

choice = menu()

if choice == 1:     # Показати всіх працівників
    fetch_all()
elif choice == 2:   # Пошук по email
    email = input("Enter employee email:\t")
    fetch_by_email(email)
elif choice == 3:   # Пошук по імені
    name = input("Enter employee name:\t")
    fetch_by_name(name)
elif choice == 4:   # Показати працівника з найбільшою ЗП
    fetch_max_salary()
elif choice == 5:   # Показати працівника з найменшою ЗП
    fetch_min_salary()
elif choice == 6:   # Показати працівника який отримує найбільшу ЗП в Україні
    fetch_max_salary_ukraine()
elif choice == 7:   # Знайти найстаршого працівника по країні
    country = input("Enter country:\t")
    fetch_max_age_by_country(country)
elif choice == 8:   # Знайти AVG вік по країні
    country = input("Enter country:\t")
    fetch_avg_age_by_country(country)
else:
    print("Error...")
