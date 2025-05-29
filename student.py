from db import connect_db

def add_student():
    db = connect_db()
    cursor = db.cursor()
    name = input("Name : ")
    age = int(input("Age : "))
    gender = input("Gender: ")
    room = int(input("Room No: "))
    cursor.execute("SELECT capacity, occupied FROM rooms WHERE room_no=%s", (room,))
    result = cursor.fetchone()
    if result and result[1] < result[0]:
        cursor.execute("INSERT INTO students (name, age, gender, room_no) VALUES (%s, %s, %s, %s)",(name,age,gender,room))
        cursor.execute("UPDATE rooms SET occupied = occupied + 1 WHERE room_no = %s", (room,))
        db.commit()
        print("Student added successfully.")
    else:
        print("Room full or not found.")
        db.close()
        
