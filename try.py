# Import module 
import sqlite3   
# Connecting to sqlite 
conn = sqlite3.connect('gfg1.db') 
# Creating a cursor object using  
# the cursor() method 
cursor = conn.cursor() 
# Creating table 
table = """CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255),  
LAST_NAME VARCHAR(255),AGE int, SEX VARCHAR(255), INCOME int);"""
cursor.execute(table) 
# Queries to INSERT records. 
cursor.execute( 
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)  
    VALUES ('Anand', 'Choubey', 25, 'M', 10000)''') 
cursor.execute( 
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)  
    VALUES ('Mukesh', 'Sharma', 20, 'M', 9000)''') 
cursor.execute( 
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Ankit', 'Pandey', 24, 'M', 6300)''') 
cursor.execute( 
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Subhdra ', 'Singh', 26, 'F', 8000)''') 
cursor.execute( 
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Tanu', 'Mishra', 24, 'F', 6500)''')  
# Display data inserted 
print("EMPLOYEE Table: ") 
data = cursor.execute('''SELECT * FROM EMPLOYEE''') 
for row in data: 
    print(row)  
# Updating 
cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''') 
print('\nAfter Updating...\n')   
# Display data 
print("EMPLOYEE Table: ") 
data = cursor.execute('''SELECT * FROM EMPLOYEE''') 
for row in data: 
    print(row) 
# Commit your changes in the database 
conn.commit()  
# Closing the connection 
conn.close()