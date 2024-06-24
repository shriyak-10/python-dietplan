import sqlite3
import datetime

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('diet_plan.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS diet_plan (
                        id INTEGER PRIMARY KEY,
                        meal TEXT,
                        calories INTEGER,
                        date TEXT);''')
    conn.commit()

def insert_diet_plan(conn, diet_plan):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO diet_plan (meal, calories, date) VALUES (?, ?, ?)", diet_plan)
    conn.commit()

def update_diet_plan(conn, diet_plan):
    cursor = conn.cursor()
    cursor.execute("UPDATE diet_plan SET meal=?, calories=? WHERE date=?", diet_plan)
    conn.commit()

def delete_diet_plan(conn, date):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM diet_plan WHERE date=?", (date,))
    conn.commit()

def select_all_diet_plans(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diet_plan")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn = create_connection()
    create_table(conn)
    while True:
        print("Diet Plan Management System")
        print("1. Add Diet Plan")
        print("2. Update Diet Plan")
        print("3. Delete Diet Plan")
        print("4. View Diet Plans")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            meal = input("Enter meal: ")
            calories = int(input("Enter calories: "))
            date = datetime.date.today().strftime('%Y-%m-%d')
            insert_diet_plan(conn, (meal, calories, date))
        elif choice == 2:
            meal = input("Enter new meal: ")
            calories = int(input("Enter new calories: "))
            date = input("Enter date (YYYY-MM-DD): ")
            update_diet_plan(conn, (meal, calories, date))
        elif choice == 3:
            date = input("Enter date (YYYY-MM-DD): ")
            delete_diet_plan(conn, date)
        elif choice == 4:
            select_all_diet_plans(conn)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()