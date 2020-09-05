# Import libraries
from os import system, name

# Function to clear terminal screen
def clear():

    # For Windows
    if name == "nt":

        _ = system("cls")

    # For Linux, Mac
    if name == "posix":

        _ = system("clear")

# note #
# Python terminal/shell uses "_" to store the last returned output, that's why 
# we used "_" to pass the system method to clear the terminal/shell screen