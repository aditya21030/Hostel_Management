def login():
    username = input("Enter Username : ")
    password = input("Enter Password : ")
    return username == "admin" and password == "admin123"