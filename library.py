import mysql.connector

def add_book():
    try:
        con = mysql.connector.connect(
            host     = "localhost",
            password = "",
            user     = "",
            database = "library_db"
        )

        cursor = con.cursor()

        ubook_name     = input("Enter Book Name:")
        ubook_quantity = eval(input("Enter Book Quantity:"))
        
        query =f""" insert into book(book_name ,book_quantity)values("{ubook_name}",{ubook_quantity});"""

        cursor.execute(query)
        con.commit()
        print(f"Book {ubook_name} is added to database successfully.")

    except:
        con.rollback()
        print("There Is Some Problem")
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()
add_book()


def list_of_books():
    try:
        con = mysql.connector.connect(
            host     = "localhost",
            password = "",
            user     = "",
            database = "library_db"
        )

        cursor =con.cursor()

        query =f"""select * from book;"""
        cursor.execute(query)
        data = cursor.fetchall()

        for x in data:
            print(f"""
            Book id is {x[0]}
            Book Name is {x[1]}
            Book Quantity {x[2]}
            Book Type is {x[3]}""")
            print()

    except:
        con.rollback()
        print("There is some problem")
    finally:
        if cursor:
            cursor.close()
        if con :
            con.close()

def add_student():
    try:
        con = mysql.connector.connect(
            host     = "localhost",
            password = "",
            user     = "",
            database = "library_db"
        )

        cursor =con.cursor()

        ustudent_name =input("Enter Student Name:")
        ustudent_mob_num=eval(input("Enter Student Mobile Number:"))
        ustudent_email_id =input("Enter Student Email id:")

        query =f""" insert into student(student_name,mobile_number,email_id)values("{ustudent_name}",{ustudent_mob_num},"{ustudent_email_id}");"""
        cursor.execute(query)
        con.commit()
        print(f"Student {ustudent_name} is added to database successfully.")
    
    except:
        con.rollback()
        print("There is some problem")
    finally:
        if cursor:
            cursor.close()
        if con :
            con.close()

def list_of_students():
    try:
        con = mysql.connector.connect(
            host     = "localhost",
            password = "",
            user     = "",
            database = "library_db"
        )

        cursor =con.cursor()

        query =f"""select * from student;"""
        cursor.execute(query)
        data = cursor.fetchall()
        

        for x in data:
            print(f"""
            Student id is {x[0]}
            Student Name is {x[1]}
            student Mobile Number is {x[2]}
            Student Email id is {x[3]}""")
            print()

    except:
        con.rollback()
        print("There is some problem")
    finally:
        if cursor:
            cursor.close()
        if con :
            con.close()




def issue_book():
    try:
        con = mysql.connector.connect(
            user     ="",
            host     ="localhost",
            password ="",
            database ="library_db"
        )

        cursor =con.cursor()

        id =eval(input("Enter Book Id you want to issue:"))
        student_id = eval(input("Enter student id to register:"))

        query1 =f""" select * from book where id ={id};"""
        cursor.execute(query1)
        data =cursor.fetchone()
        
        issue_book_quantity =eval(input(f"enter book quantity you want to issue[Total Books Are {data[2]}]:"))

        
        book_quantity = data[2] - issue_book_quantity
        query3 =f"""UPDATE book SET book_quantity ={book_quantity} where id ={id};"""
        cursor.execute(query3)
        con.commit()


        print(f"Book {data[1]} is issued successfully.")

        query2 =f"""insert into student_book_info(sid ,bid,book_quantity)values({student_id}, {id},{issue_book_quantity});"""
        cursor.execute(query2)
        con.commit()
        
        print(f"Student {student_id} issued book successfully.")
    except:
        con.rollback()
        print("There is some problem")
    finally:
        if cursor:
            cursor.close()
        if con :
            con.close()


def return_book():
    try:
        con = mysql.connector.connect(
            user     = "",
            host     ="localhost",
            password ="",
            database ="library_db"
        )

        cursor =con.cursor()

        id =eval(input("Enter Book Id you want to return:"))
        sid = eval(input("Enter student id to return book:"))

        query1 =f""" select * from student_book_info where sid ={sid};"""
        cursor.execute(query1)
        data =cursor.fetchone()        

        return_book_quantity =eval(input(f"enter book quantity you want to return[ issued Books Are {data[3]}]:"))
        
        ubook_quantity =  data[3] + return_book_quantity

        query3 =f"""UPDATE book SET book_quantity = {ubook_quantity} where id ={id};"""
        cursor.execute(query3)
        con.commit()

        book_quantity =  data[3] - return_book_quantity
        
        query2 =f"""UPDATE student_book_info SET book_quantity = {book_quantity} where sid ={sid} and bid ={id};"""
        cursor.execute(query2)
        con.commit()
        
        print(f"Student {sid} returned book successfully.")
    except Exception as e:
        con.rollback()
        print("There is some problem",e)
    finally:
        if cursor:
            cursor.close()
        if con :
            con.close()


def delete_student():    
    try:
        con =mysql.connector.connect(
            user     ="",
            host     ="localhost",
            password ="",
            database ="library_db"
        )

        cursor =con.cursor()
        sid =eval(input("Enter student id you want to delete:"))
        
        query =f"""select * from student_book_info where sid ={sid};"""
        cursor.execute(query)
        data =cursor.fetchone()

        
            
        if data[3] != 0 :
            choice =input(f"Do You Want To Return Your Issued Books( Book Are {data[3]})(y/n) :")
            if choice =="y":
                return_book()
                delete_student()
                
        else:
            print(f"Student Returned All Books")
            query2 = f'''
            delete from student_book_info
            where sid = {sid} and bid = {data[2]};'''
            cursor.execute(query2)
            con.commit()

            print(f"Student id {sid} is Deleted Successfully")            
            
    except:
        con.rollback()
        print("There Is Some Problem")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

while True:
    print("""
        1: Add Book
        2: List Of Books
        3: Add Student
        4: List of Student
        5: Issue Book 
        6: Return Book
        7: Delete Student
        8: Exit
        """)

    ch = input("Enter Your Choice:")

    if ch =="1":
        add_book()
    
    elif ch =="2":
        list_of_books()
    
    elif ch =="3":
        add_student()

    elif ch =="4":
        list_of_students()

    elif ch =="5":
        issue_book()

    elif ch =="6":
        return_book()

    elif ch =="7":
        delete_student()

    elif ch =="8":
        break

    


