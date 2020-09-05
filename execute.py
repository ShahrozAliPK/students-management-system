# STUDENTS MANAGEMENT SYSTEM # (Main Program)

# Import Programs -> as a function
from user import login
from students import students

# Store returning value for login access
check = login()

# If TRUE, allow access to the user
if check == True:
    students()

# If FALSE, don't allow user to access and exit the program
else:
    print("ACCESS DENIED")
    exit(1)