from lib.functions import fetch_by_email, fetch_all, menu


choice = menu()
print(choice)

if choice == 1:
    fetch_all()
elif choice == 2:
    email = input("Enter employee email\t")
    fetch_by_email(email)
else:
    print("Error...")
