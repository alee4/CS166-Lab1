# Austin Lee, CS166, Lab 1, Sep 15
#This program allows preregistered users to login.  Each login has different access levels
#that allows them to access different portions of the menu.
global INDEX

def main():
    # set up arrays
    array = getFile("newUserPass.txt")
    userArray = []
    passArray = []
    accessArray = []

    # creats arrays for the usernames, passwords, and accesslevels
    for x in range(0, len(array), 3):
        userArray.append(array[x])
    for y in range(1, len(array), 3):
        passArray.append(array[y])
    for z in range(2, len(array), 3):
        accessArray.append(array[z])

    # asks for username and password
    username = input("Username: ")
    password = input("Password: ")

    check = False
    while check == False:
        # # checks if username or password is in txt file, should show up on console so that you cant tell which is not in it
        while checkFile(username) is False or checkFile(password) is False:
                print("Username or Password does not exist in our database. Please reenter")
                username = input("Username: ")
                password = input("Password: ")
                checkFile(username)
                checkFile(password)
    # if both username and pass are in database, then checks if they match
        while checkFile(username) and checkFile(password):
            userIndex = userArray.index(username)
            passIndex = passArray.index(password)
            if userIndex == passIndex:
                # credentials accepted
                INDEX = userIndex
                print("Credentials accepted.")
                break
            else:
                print("Username or Password does not exist in our database. Please reenter")
                username = input("Username: ")
                password = input("Password: ")
                checkFile(username)
                checkFile(password)
        check = True

    # finds out what access level the account has based on the user given
    a = accessArray[INDEX]
    menu(a)

def menu(accessLevel):
    #creats the menu based on what access level the user has
    #takes accessLevel parameter, a string
    #returns nothing
    option = input("Press 1 for the Time Reporting Area (all access), "
                   "2 for Accounting Area (mid access), "
                   "3 for Financial Matters (admin access), or 4 to quit: ")
    # checks to see if menu option is valid
    while option not in ("1","2","3", "4"):
         option = input("Please select a valid option: ")

    # if your access level is 1, itll only allow for the first menu
    while accessLevel == "1":
        if option == "1":
            print("You have now accessed the Time Reporting Area.\n")
            option = input("Please input a new option: ")
        elif option == "2" or option == "3":
            print("You do not have high enough access for this option.\n")
            option = input("Please input a new option: ")
        elif option == "4":
            print("Thank you.")
            exit()
        else:
            option = input("Please select a valid option: ")

    # if access level is 2, itll allow first and second menu
    while accessLevel == "2":
        if option == "1":
            print("You have now accessed the Time Reporting Area.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option== "2":
            print("You have now accessed the Accounting Area.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option == "3":
            print("You do not have high enough access for this option.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option == "4":
            print("Thank you.")
            exit()
        else:
            option = input("Please select a valid option: ")

    # menu for admin, has access to every option
    while accessLevel == "3":
        if option == "1":
            print("You have now accessed the Time Reporting Area.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option == "2":
            print("You have now accessed the Accounting Area.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option == "3":
            print("You have now accessed the Financial Matters.\n")
            option = input("Please input a new option: ")
            while option not in ("1", "2", "3", "4"):
                option = input("Please select a valid option: ")
        elif option == "4":
            print("Thank you.")
            exit()
        else:
            option = input("Please select a valid option: ")

def checkFile(string):
    # checks if any line contains the user or password
    #takes in string parameter
    #returns True if the string is in the file
    # based on https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
    with open("newUserPass.txt", 'r') as read_obj:
        # Read lines, check if it contains the string
        for line in read_obj:
            if string in line:
                return True
    return False

def getFile(s):
    #takes in file name string
    #returns an array of the file
    #reads the file, splits it by ,
    file = open("newUserPass.txt", "r")
    credentials = file.read().split(',')
    file.close()
    return credentials

main()