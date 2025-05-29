from db import connect_db

def update_fees():
    db = connect_db()
    cursor = db.cursor()
    student_id = int(input("Student ID : "))
    cursor.excute("UPDATE students SET fees_paid = TRUE WHERE id = %s", (student_id,))
    db.commit()
    print("Fee Updated.")
    db.close()
    
    