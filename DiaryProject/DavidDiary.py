import os.path
import os
from pathlib import Path

# Path for where files are stored
LOCAL_FILE = "C:/Users/hungt/OneDrive/Desktop/Python Projects/VSC/DiaryProject/DiaryFiles"


# function for creating a correctly formatted path name
def newFilePath(entryDate):
    x = os.path.join(LOCAL_FILE, entryDate + ".txt")
    Path(x)
    return x


# function to add a new entry or replace an existing one
def addEntry():
    entryDate = input("Enter today's date (format example: jan05).\n")
    print()
    newFile = newFilePath(entryDate)
    fileCheck = os.path.isfile(newFile)
    if fileCheck == True:
        i = 0
        while i == 0:
            doubleCheck = input("This entry already exists. Would you like to replace it? Y/N (This deletes your old file, use command \"edit\" to add to an exsisting file)\n")
            print()
            if doubleCheck == "N":
                print("Cancelling file replacement")
                return
            elif doubleCheck == "Y":
                print("Replacing " + entryDate + " with a new file.")
                i += 1
            else:
                print("Please enter Y or N.")
    else:
        pass
    print()
    diaryEntry = input("Enter today's diary entry.\n")
    print()
    f = open(newFile, "w")
    f.write("\n" + diaryEntry)
    i = 0
    while i == 0:
        addCheck = input("Would you like to add more? Y/N\n")
        if addCheck == "N":
            i += 1
        elif addCheck == "Y":
            print()
            additionalInput = input("Continue editing:\n")
            f.write("\n" + additionalInput)
        else:
            print("Please enter Y or N.")
    f.close()
    return


# function to show all files currently stored in the Path chosen from LOCAL_FILE variable
def showAll():
    print("List of all file dates:")
    print(os.listdir(LOCAL_FILE))
    return


# function to view an existing diary entry file
def viewEntry():
    entryDate = input("Enter the diary entry's date (format example: jan23).\n")
    print()
    filePath = newFilePath(entryDate)
    x = os.path.isfile(filePath)
    if x == True:
        f = open(filePath, "r")
        print("\"" + f.read() + "\"")
        f.close()
    else:
        print("There is no file for the date you entered.")
    return


# appends new entries to a file
def expandEntry():
    entryDate = input("Enter the date of the diary entry you would like to add on to(format example: jan05).\n")
    print()
    filePath = newFilePath(entryDate)
    fileCheck = os.path.isfile(filePath)
    if fileCheck == True:
        userAppend = input("Add to diary entry " + entryDate + "(type \"cancel\" to cancel revision).\n")
        if userAppend == "cancel":
            print("File edit cancelled.")
        else:
            f = open(filePath, "a")
            f.write("\n" + userAppend)
            i = 0
            while i == 0:
                print()
                addCheck = input("Would you like to add more? Y/N\n")
                if addCheck == "N":
                    i += 1
                elif addCheck == "Y":
                    additionalInput = input("Continue editing.\n")
                    f.write("\n" + additionalInput)
                else:
                    print("Please enter Y or N.")
            f.close()
    else:
        print("There is no file for the date you entered.")
    return

# deletes a file of the users choice from the Path given by LOCAL_FILE variable
def deleteEntry():
    entryDate = input("Enter the date of the diary entry you want removed (format example: jan23).\n")
    filePath = newFilePath(entryDate)
    fileCheck = os.path.isfile(filePath)
    if fileCheck == True:
        doubleCheck = input("Are you sure you want to remove the file for " + entryDate + "? Y/N\n")
        print()
        i = 0
        while i == 0:
            if doubleCheck == "Y":
                os.remove(filePath)
                print("Entry for " + entryDate + " has been deleted.")
                break
            elif doubleCheck == "N":
                print("Cancelling Deletion.")
                break
            else:
                print("Please enter Y or N.")
    else:
        print("There is no file for the date you entered.")
    return      


# main body of the code, takes user commands to activate corresponding functions from above
i = 0
print()
while i == 0:
    initialComm = input("Welcome to David's Python Diary. What would you like to do? (type \"commmands\" for options)\n")
    print()

    if initialComm == "commands":
        print("\"new\" = Enter a new diary entry")
        print("\"showall\" = Show all existing diary entry dates")
        print("\"view\" = View a previous diary entry")
        print("\"edit\" = Add onto existing diary entries.")
        print("\"delete\" = Delete an existing diary extry.")
        print("\"end\" = End script")
    elif initialComm == "new":
        addEntry()
    elif initialComm == "showall":
        showAll()
    elif initialComm == "view":
        viewEntry()
    elif initialComm == "edit":
        expandEntry()
    elif initialComm == "delete":
        deleteEntry()
    elif initialComm == "end":
        break
    else:
        print("Invalid command, type \"commands\" for a list of valid commands.")
    print()

print("Thanks for using the diary, come back tomorrow.")
