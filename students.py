# Libraries
import sqlite3
from alpha import test_alpha
from num import test_num
import csv
from clear import clear
from sys import exit

def students():

    # Define connection to sqlite3 database
    connection = sqlite3.connect("STUDENTS DATABASE/students.db")

    # Cursor to connect to sqlite3 database
    db_cursor = connection.cursor()

    # Create table for students database
    db_cursor.execute("CREATE TABLE IF NOT EXISTS students (ID INTEGER, First TEXT, Middle TEXT, Last TEXT, Age INTEGER, Class INTEGER, Father TEXT, Number INTEGER)")

    # Forever Loop
    while (True):

        # UI Menu
        print("1. New Entry     2. Open Entries     3. Search For Student      4. Delete Entry     5.Update Entry")
        print("---------------------------------------------------------------------------------------------------\n")

        answer = input("Type option: ")

        ## NEW ENTRY ##
        if answer == "1":

            clear()

            # Keep entering the data until user exits
            while (True):

                # Welcome screen
                print(" \n---| NEW STUDENT DATABASE |---\n")

                # Student ID initializer
                ID = 1

                # Ask for student's first name  
                while (True):

                    # Prompt for valid first name
                    first = input("First Name: ")
                
                    # Call function to check validity
                    check = test_alpha(first)

                    # Check if correct
                    if check == True:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid Name")
            
                # Ask for student's middle name
                while (True):

                    # Prompt for valid middle name
                    middle = input("Middle Name: ")

                    # Call function to check validity
                    check = test_alpha(middle)

                    # Check if correct
                    if check == True:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid Name")

                # Ask student's last name
                while (True):

                    # Prompt for valid last name
                    last = input("Last Name: ")

                    # Call function to check validity
                    check = test_alpha(last)

                    # Check if correct
                    if check == True:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid Name")

                # Ask for student's age
                while (True):

                    # Prompt again for valid age
                    age = input("Age: ")

                    # Call function to check validity
                    check = test_num(age)

                    # Check if correct
                    if check == True and int(age) >= 5 and int(age) <= 30:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid age between 5 - 30")

                # Ask for Class
                while (True):
                    
                    # Prompt for valid class
                    class_no = input("Class: ")
                
                    # Call function to check validity
                    check = test_num(class_no)

                    # Check if correct
                    if check == True and int(class_no) <= 10 and int(class_no) >= 1:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid Class between 1 - 10")

                # Ask for student's father name
                while (True):

                    # Prompt again for valid father name
                    father = input("Father Name: ")

                    # Call function to check validity
                    check = test_alpha(father)

                    # Check if correct
                    if check == True:
                        break
                
                    # Print Error if input is not correct
                    print("Enter Valid Name")
            
                # Ask student's number
                while (True):
                    
                    # Prompt for valid number
                    number = input("Phone Number: ")

                    # Call function to check validity
                    check = test_num(number)

                    # Check if correct
                    if check == True:
                        break

                    print("Enter Valid Phone Number")
            
                print()

                # GENERATES NEW STUDENT ID
                # Return last ID
                key = db_cursor.execute("SELECT ID from students ORDER BY ID DESC LIMIT 1")

                # Fetch data into list
                value = key.fetchone()

                # Value to store student ID
                student_id = 0

                # If first student ID
                if value == None:
                    student_id = 0

                # Else
                if value != None:
                    student_id = int(value[0])

                # Update ID
                ID = student_id + 1

                # Ask for confirmation
                clear()
                
                print()
                print("------------------")
                print("Confirm New Entry")
                print("------------------")
                print(f"First Name: {first}")
                print(f"Middle Name: {middle}")
                print(f"Last Name: {last}")
                print(f"Age: {age}")
                print(f"Class: {class_no}")

                print()

                print(f"Father's Name: {father}")
                print(f"Phone Number: {number}")
                print("---------------------")

                # Prompt for option
                option = input("Type YES or NO: ")

                # If yes, insert new data into table
                if option.lower() == "yes" or option.lower() == "y":

                    # Insert data into database
                    db_cursor.execute("INSERT INTO students (ID, First, Middle, Last, Age, Class, Father, Number) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (ID, first, middle, last, int(age), int(class_no), father, int(number)))

                    # Commit connection
                    connection.commit()

                    # Print success
                    print("Entry Successful")

                # Ask for re-entering data
                if option.lower() == "no" or option.lower() == "n":

                    # Prompt again to re-enter data
                    print("Do you want to re-enter data ?")
                    ask = input("Type YES or NO: ")

                    # If no, exit the loop
                    if ask.lower() == "no" or ask.lower() == "n":
                        print("\nOK")
                        break
            
                # Ask for new data entry
                option = input("New data entry?\n Type YES or NO: ")

                # If no, exit the loop
                if option.lower() == "no" or option.lower() == "n":
                    print("\nOK")
                    break
            
            # Compliment
            print("Thankyou!")
            db_cursor.close()
            connection.close()

        ## OPEN ENTRIES ##
        if answer == "2":

            clear()

            # Keep prompting until valid option no
            while (True):

                # UI Menu
                print("\n                   ---| Open Entries |---")
                print("---------------------------------------------------------------\n")
                print("1. By Age     2. By Class    3.By Alphabet   4.Open All Entries\n")

                # Ask for option no
                query = input("(1 - 5): ")
            
                ## SEARCH BY AGE ##
                if query == "1":

                    clear()

                    print("---| SEARCH BY AGE |---")

                    # Keep prompting until valid age
                    while (True):

                        query_age = input("Enter Age: ")

                        check = test_num(query_age)

                        if check == True:
                            break

                        else:
                            print("Enter Correct Age\n")

                    # Look into database and select all columns
                    age_entries = db_cursor.execute("SELECT * from students WHERE Age = ? ORDER BY First", (query_age,))

                    # Fetch data into nested lists
                    entries = age_entries.fetchall()
                    
                    # List to store full name of student
                    full_name = []

                    # Get first, last and middle name of student
                    for i in range(len(entries)):

                        # Store in list
                        full_name.append([entries[i][1], entries[i][2], entries[i][3]])

                    # Be ready to print results
                    print("\nStudent ID | Full Name      | Age | Class | Father | Number\n")

                    # Iterate through each nested list in entries
                    for i in range(len(entries)):
                        
                        # Get Student ID
                        ID_no = entries[i][0]

                        # Print ID and Full Name of Student
                        print(ID_no, " | ", full_name[i][0], full_name[i][1], full_name[i][2], "|", end="")

                        # Print Every column after 'Last' name column
                        for j in range(4, 8):
                            values = entries[i][j]
                            print(values, "|", end="")

                        # Print New-line
                        print("\n")

                    # Print New-line, Exit loop
                    print()
                    break
                
                ## SEARCH BY CLASS ##
                if query == "2":
                    
                    clear()

                    print("---| SEARCH BY CLASS |---")

                    # Keep prompting until valid age
                    while (True):

                        query_class = input("Enter Class: ")

                        check = test_num(query_class)

                        if check == True:
                            break

                        else:
                            print("Enter Correct Class No\n")

                    # Look into database and select all columns
                    class_entries = db_cursor.execute("SELECT * from students WHERE Class = ? ORDER BY First", (query_class,))

                    # Fetch data into nested lists
                    entries = class_entries.fetchall()
                    
                    # List to store full name of student
                    full_name = []

                    # Get first, last and middle name of student
                    for i in range(len(entries)):

                        # Store in list
                        full_name.append([entries[i][1], entries[i][2], entries[i][3]])

                    # Be ready to print results
                    print("\nStudent ID | Full Name     | Age | Class | Father | Number\n")

                    # Iterate through each nested list in entries
                    for i in range(len(entries)):
                        
                        # Get Student ID
                        ID_no = entries[i][0]

                        # Print ID and Full Name of Student
                        print(ID_no, " | ", full_name[i][0], full_name[i][1], full_name[i][2], "|", end="")

                        # Print Every column after 'Last' name column
                        for j in range(4, 8):
                            values = entries[i][j]
                            print(values, "|", end="")

                        # Print New-line
                        print("\n")

                    # Print New-line, Exit loop
                    print()
                    break
                
                ## SEARCH BY FIRST ALPHABET ##
                if query == "3":

                    clear()

                    print("---| SEARCH BY ALPHABET |---")

                    # Select all data from students database
                    alpha_entries = db_cursor.execute("SELECT * from students ORDER BY first")

                    # Fetch all entries
                    entries = alpha_entries.fetchall()

                    # Keep prompting till valid input
                    while (True):

                        query_alpha = input("Enter Alphabet (A - Z): ")

                        check = test_alpha(query_alpha)

                        if len(query_alpha) == 1 and check == True:
                            break

                        print("Incorrect Alphabet")

                    # Ready to print queries
                    print("\nStudent ID | Full Name       | Age | Class | Father' Name | Phone Number\n")

                    # List to store full name of students
                    full_name = []
                    student_id = None

                    # Get first, last and middle name of student
                    for i in range(len(entries)):

                        # Store in list
                        full_name.append([entries[i][1], entries[i][2], entries[i][3]])

                        # Get first, middle and last name
                        first_name = full_name[i][0]
                        middle_name = full_name[i][1]
                        last_name = full_name[i][2]
                        
                        # Check if 1st char of first name matches with query
                        if first_name[0] == query_alpha.upper():

                            # Get Student ID
                            student_id = entries[i][0]

                            # Get student age
                            age = entries[i][4]

                            # Get student class no
                            class_no = entries[i][5]

                            # Get student's father name
                            father_name = entries[i][6]

                            # Get student's phone number
                            number = entries[i][7]

                            # Print ID, full name, age, class, father's name and phone number
                            print(student_id, "|", first_name, middle_name, last_name, "|", age, "|", class_no, "|", father_name, "|", number)

                    # Print New-line, exit the loop
                    print("\n")
                    break
                
                ## OPEN ALL ENTRIES ##
                if query == "4":
                    
                    clear()

                    # UI Title
                    print("\n\n---| ALL ENTRIES |---\n\n")

                    # COUNT all rows in database
                    entries = db_cursor.execute("SELECT COUNT(*) from students")

                    # Fetch data
                    entries_no = entries.fetchone()

                    # Store total number of entries
                    total = entries_no[0]

                    # Print total Number of entries
                    print("Found Total: ", total, "\n")

                    # Ready to print all entries
                    print("\n\nID   |   Full Name       | Age | Class | Father's Name | Phone Number\n\n")

                    # Select all entries from database
                    entries = db_cursor.execute("SELECT * from students")

                    # Fetch data
                    all_entries = entries.fetchall()

                    # For each entry
                    for i in range(len(all_entries)):

                        # Get student ID
                        student_id = all_entries[i][0]

                        # Get first, middle and last name of student
                        first_name = all_entries[i][1]
                        middle_name = all_entries[i][2]
                        last_name = all_entries[i][3]

                        # Print ID, First, Middle and Last name of student
                        print(student_id, "|", first_name, "|", middle_name, "|", last_name, "|", end="")

                        # Print Age, Class, Father's Name and Phone number of student
                        for j in range(4, 8):

                            print(all_entries[i][j], "|", end="")

                        # Print New-line
                        print("\n")

                else:
                    print("Type Correct Option\n")

        ## SEARCH FOR STUDENT ##
        if answer == "3":

            clear()

            # UI Menu
            print("\n---| SEARCH FOR STUDENT |---\n")

            # Keep prompting till valid input for first name    
            while (True):
                search_first = input("Enter Student's First Name: ")

                check = test_alpha(search_first)

                if check == True:
                    break

                print("Enter Correct Name!")

            # Keep prompting till valid input for middle name
            while (True):
                search_middle = input("Enter Student's Middle Name: ")

                check = test_alpha(search_middle)

                if check == True:
                    break

                print("Enter Correct Name!")

            # Keep prompting till valid input for last name
            while (True):
                search_last = input("Enter Student's Last Name: ")

                check = test_alpha(search_last)

                if check == True:
                    break
                
                print("Enter Correct Name!")

            # Go inside database and select required info
            entry = db_cursor.execute("SELECT ID, First, Middle, Last, Age, Class, Father, Number from students WHERE First = ? AND Middle = ? AND Last = ?", (search_first, search_middle, search_last))

            # Fetch all entries
            student_entries = entry.fetchall()

            # If no record or entry found
            if len(student_entries) == 0:
                print("\nNo record Found!\n")

            # Print number of record(s) found
            print("\nFound: ", len(student_entries), "\n")

            # Be ready to print matching queries
            print("ID |  Full Name    |   Age  |   Class |  Father's Name |  Phone Number")

            # Print all matching queries
            for i in range(len(student_entries)):

                for j in range(len(student_entries[i])):
                    print(student_entries[i][j], "|", end="")

                print()

            # Print New-line
            print()

        ## DELETE ENTRY ##
        if answer == "4":

            clear()

            # UI Menu
            print("\n---| DELETE ENTRY |---\n")

            # Keep prompting till valid student ID
            while (True):

                ask_id = input("Enter Student ID: ")

                check = test_num(ask_id)

                if check == True and len(ask_id) < 100 and ask_id > "0":
                    break

                print("\nEnter Correct Student ID!\n")

            print()

            # Select entry from database matching input ID
            id_entry = db_cursor.execute("SELECT ID, First, Middle, Last, Age, Class, Father, Number from students WHERE ID = ?", (ask_id, ))

            # Fetch student entry
            id_match = id_entry.fetchone()

            # If no record Found
            if id_match == None:
                print("No record Found!\n")
                print()

            # Start printing full name of student
            print("Name: ", end="")

            # Print first, middle and last name of student
            for i in range(1, 4):
                print(id_match[i], "", end="")

            # Print New-line
            print()

            # Get age, class, father's name, phone number
            id_age = id_match[4]
            id_class = id_match[5]
            id_father = id_match[6]
            id_number = id_match[7]

            # Print all info
            print("Age: ", id_age)
            print("Class: ", id_class)
            print("Father Name: ", id_father)
            print("Phone Number: ", id_number)

            # Print New-line
            print()

            # Ask for confirmation
            print("\nCONFIRM DELETE ENTRY?    (once done it cannot be reversed)\n")

            # Keep promting till valid option
            while (True):
                
                confirm = input("Type YES or NO: ")

                # If confirmation is cancelled
                if confirm.lower() == "n" or confirm.lower() == "no":
                    print("\nOK DELETE QUERY CANCELLED\n")
                    break
                
                # Else
                if confirm.lower() == "y" or confirm.lower() == "yes":
                    
                    # Select entry from database matching input ID, DELETE entry
                    db_cursor.execute("DELETE from students WHERE ID = ?", (ask_id, ))
                    connection.commit()

                    # Print Success
                    print("\nENTRY DELETED SUCCESSFULLY! \n")
                    break

                print("Please Type Correct Option!\n\n")

            # Print New-line
            print()

        ## UPDATE EXISTING ENTRY ##
        if answer == "5":

            clear()

            # UI Menu
            print("\n---| UPDATE EXISTING ENTRY |---\n")

            # Keep prompting till valid student ID
            while (True):

                ask_id = input("Enter Student ID: ")

                check = test_num(ask_id)

                if check == True:
                    break

                print("\nEnter Correct Student ID\n")

            # Print New-line
            print("\n")

            # Go inside database and select entry matching ID
            id_entry = db_cursor.execute("SELECT ID from students WHERE ID = ?", (ask_id, ))

            # Fetch data
            id_match = id_entry.fetchone()

            # If no record found
            if id_match == None:
                print("\nNo record Found!\n")
                print()

            # Be ready to collect required info
            print("\nENTER INFO\n\n")

            # Keep prompting till valid first name
            while (True):

                ask_first = input("First Name: ")

                check = test_alpha(ask_first)

                if check == True:
                    break

                print("\nEnter Valid Name!\n\n")

            # Keep prompting till valid middle name
            while (True):

                ask_middle = input("Middle Name: ")

                check = test_alpha(ask_middle)

                if check == True:
                    break

                print("\nEnter Valid Name!\n\n")

            # Keep prompting till valid last name
            while (True):

                ask_last = input("Last Name: ")

                check = test_alpha(ask_last)

                if check == True:
                    break

                print("\nEnter Valid Name!\n\n")

            # Keep prompting till valid age
            while (True):

                ask_age = input("Age: ")

                check = test_num(ask_age)

                if check == True:
                    break

                print("\nEnter Valid Age between 5 - 30!\n\n")

            # Keep prompting till valid class no
            while (True):

                ask_class = input("Class: ")

                check = test_num(ask_class)

                if check == True:
                    break

                print("\nEnter Valid Class No Between 1 - 10\n\n")

            # Keep prompting till valid father's name
            while (True):

                ask_father = input("Father's Name: ")

                check = test_alpha(ask_father)

                if check == True:
                    break

                print("\nEnter Valid Name!\n\n")

            # Keep prompting till valid phone number
            while (True):

                ask_number = input("Phone Number: ")

                check = test_num(ask_number)

                if check == True:
                    break

                print("\nEnter Valid Phone Number!\n\n")

            # Ask for confirmation
            print("\n")
            print("CONFIRM UPDATE ENTRY\n")
            print("First Name: ", ask_first)
            print("Middle Name: ", ask_middle)
            print("Last Name: ", ask_last)
            print("Age: ", ask_age)
            print("Class: ", ask_class)
            print("Father's Name: ", ask_father)
            print("Phone Number: ", ask_number)

            # Keep prompting till valid option
            while (True):

                # Ask for option
                option = input("\nType YES or NO: ")

                # If no, cancel operation
                if option.lower() == "n" or option.lower() == "no":
                    print("\nOPERATION CANCELLED\n\n")

                # Else
                if option.lower() == "y" or option.lower() == "yes":
                    
                    # Update entry inside database, matching input ID of student
                    db_cursor.execute("UPDATE students SET First = ?, Middle = ?, Last = ?, Age = ?, Class = ?, Father = ?, Number = ? WHERE ID = ?", (ask_first, ask_middle, ask_last, ask_age, ask_class, ask_father, ask_number, ask_id))
                    connection.commit()

                    # Print Success
                    print("\nENTRY UPDATED SUCCESSFULLY!\n\n")
                    print()
