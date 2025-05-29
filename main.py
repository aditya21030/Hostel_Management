from auth import login
from student import add_student
from room import view_rooms, create_room

def main():
    if not login():
        print("Access Denied.")
        return

    while True:
        print("\n1. Add Student")
        print("2. Create Rooms")
        print("3. View Room")   
        print("4. Exit")

        choice = input("Choice : ")

        if choice == '1':
            add_student()
        elif choice == '2':
            create_room()
        elif choice == '3':
            view_rooms()        
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
