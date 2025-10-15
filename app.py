# app.py

from storage import create_user, read_users, read_user, update_user, delete_user

def menu():
    print("\n--- Simple CRUD App ---")
    print("1. Create User")
    print("2. View All Users")
    print("3. View Single User")
    print("4. Update User")
    print("5. Delete User")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            user = create_user(name, email)
            print("User created:", user)

        elif choice == '2':
            print("All Users:")
            for u in read_users():
                print(u)

        elif choice == '3':
            uid = int(input("Enter user ID: "))
            user = read_user(uid)
            print(user if user else "User not found.")

        elif choice == '4':
            uid = int(input("Enter user ID to update: "))
            name = input("Enter new name (or press Enter to skip): ")
            email = input("Enter new email (or press Enter to skip): ")
            user = update_user(uid, name or None, email or None)
            print("Updated:", user if user else " User not found.")

        elif choice == '5':
            uid = int(input("Enter user ID to delete: "))
            delete_user(uid)
            print("User deleted (if existed).")

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
