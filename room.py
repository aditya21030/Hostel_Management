from db import connect_db

def create_room():
    db = connect_db()
    cursor = db.cursor()
    room_no = int(input("Enter Room Number: "))
    capacity = int(input("Enter Room Capacity: "))
    cursor.execute("INSERT INTO rooms (room_no, capacity, occupied) VALUES (%s, %s, %s)", (room_no, capacity, 0))
    db.commit()
    print("Room created successfully.")


def view_rooms():
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT * FROM rooms"
    cursor.execute(query)
    for room in cursor.fetchall():
        print(room)
    db.close()