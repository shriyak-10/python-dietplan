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
    cursor.execute('''CREATE TABLE IF NOT EXISTS food (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        calories INTEGER);''')
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

def insert_food(conn, food):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO food (name, calories) VALUES (?, ?)", food)
    conn.commit()

def update_food(conn, food):
    cursor = conn.cursor()
    cursor.execute("UPDATE food SET name=?, calories=? WHERE id=?", food)
    conn.commit()

def delete_food(conn, id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM food WHERE id=?", (id,))
    conn.commit()

def select_all_foods(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def join_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diet_plan INNER JOIN food ON diet_plan.id=food.id")
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
        print("5. Add Food")
        print("6. Update Food")
        print("7. Delete Food")
        print("8. View Foods")
        print("9. Join Tables")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            meal = input("Enter meal: ")
            calories = int(input("Enter calories: "))
            date = datetime.date.today().strftime('%Y-%m-%d')
            insert_diet_plan(conn, (meal, calories, date))
        elif choice == 2:
            meal = input("Enter new meal: ")
            calories = int(input("Enter new calories: "))
            date = int(input("Enter date (YYYY-MM-DD): "))
            update_diet_plan(conn, (meal, calories, date))
        elif choice == 3:
            date = input("Enter date (YYYY-MM-DD): ")
            delete_diet_plan(conn, date)
        elif choice == 4:
            select_all_diet_plans(conn)
        elif choice == 5:
            name = input("Enter food name: ")
            calories = int(input("Enter food calories: "))
            insert_food(conn, (name, calories))
        elif choice == 6:
            name = input("Enter new food name: ")
            calories = int(input("Enter new food calories: "))
            id = input("Enter food id: ")
            update_food(conn, (name, calories, id))
        elif choice == 7:
            id = input("Enter food id: ")
            delete_food(conn, id)
        elif choice == 8:
            select_all_foods(conn)
        elif choice == 9:
            join_tables(conn)
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()