# Peter Savinelli

# Imports all the neccesary imports needed for the program to run
import glob
import json
import os
import sys

# The Terminal window of all previous text when the program stops
os.system("clear")

# Prints out a welcome message for user
print ("Welcome to Knower! Let's talk about your day...\n")

# Creates a list of all ".json" files in the same directory as the program
journals = glob.glob("*.json")

# Prints all items in the list of ".json" files. Seperates them by commas and removes the ".json" extension too
for i in range (len(journals)):
    printed = str(journals[i])
    print (printed[0: printed.find(".json")], end="")
    if i < len(journals) - 1:
        print (", ", end="")

# Prints out a blank line, then gets the user's input for which file they want to open. Appends ".json" to the end of it
print ()
journalChoice = input(
    "\nType the name of the file you'd like to open, or type a new name to make a new journal: ") + ".json"

# Clears screen again
os.system ("clear")

# Tries to open the file named what the user inputted
try:
    file = open(journalChoice, 'r+')

    # Then tries to save the dictionary saved in the opened file to the "openJournal" variable
    try:
        openJournal = json.load(file)

    # If there is no dictionary in the saved file, then "openJournal" is assigned to an empty dictionary
    except json.decoder.JSONDecodeError:
        openJournal = {}

    # Closes the open file
    file.close ()

# If there is no file with the user's inputted name in the program directory, a new file is created
except FileNotFoundError:
    file = open(journalChoice, 'w')

    # An empty dictionary is assigned to "openJournal"
    openJournal = {}

    # The file is closed
    file.close ()

# Function that opens the ".json" file, writes the contents of "openJournal" to it, then closes the file
def save ():
    file = open(journalChoice, 'w')
    json.dump (openJournal, file)
    file.close ()

# Function that creates a new entry in "openJournal" adds a new entry with "title" as the key and "content" as the value
def newentry ():
    os.system ("clear")
    title = input("Title your entry please: ")
    content = input("\nWhat do you want to write?: ")
    openJournal.update ({title: content})

    # Calls the save function
    save()

    # Clears screen for the user
    os.system("clear")

# Function for viewing a previously written journal entry
def viewentry ():

    # Clears the screen for the journal
    os.system ("clear")

    # Variable "num" gets assigned to the length of "openJournal"
    num = len(openJournal)

    # Blank dictionary that later serves to assign a numerical ID to each title of "openJournal" entry
    keyIDs = {}

    # Loop populates "keyIDs" with the key of "num" assigned to a written journal entry title, num then subtracts by 1
    for i, x in openJournal.items():
        print (num, ". ", i, sep="")
        keyIDs.update({num: i})
        num -= 1

    # Also prints the option for the user to exit the view menu
    print ("\n0. Exit")

    # Asks user which entry they want to view
    viewedEntry = int(input("\nWhich entry would you like to view?: "))

    # If they choose to exit, then the screen clears and then the program continues
    if viewedEntry == 0:
        os.system("clear")
        return

    # If they choose to view an entry, they are shown that entry and then press the enter key to continue the program
    else:
        os.system("clear")
        print ("Journal entry \"", keyIDs[viewedEntry], "\":\n\n", openJournal[keyIDs[viewedEntry]], sep="")
        input ("\nPress enter to continue...")
        os.system ("clear")

# Function that lists off all the journal entries, then prompts user to delete one
def delentry ():

    # Clears screen for user
    os.system("clear")

    # Variable "num" gets assigned to the length of "openJournal"
    num = len(openJournal)

    # Blank dictionary that later serves to assign a numerical ID to each title of "openJournal" entry
    keyIDs = {}

    # Loop populates "keyIDs" with the key of "num" assigned to a written journal entry title, num then subtracts by 1
    for i, x in openJournal.items():
        print(num, ". ", i, sep="")
        keyIDs.update({num: i})
        num -= 1

    # Also prints the option for the user to exit the view menu
    print ("\n0. Exit")

    # Asks user which entry they want to delete
    deletedEntry = int(input("\nWhich entry would you like to get rid of?: "))

    # Screen clears and program continues if the user decides against deleting an entry
    if deletedEntry == 0:
        os.system("clear")
        return

    # Removes the entry that the user selected from the dictionary, user presses enter and then the dictionary saves
    else:
        os.system("clear")
        print ("Deleted \"", openJournal[keyIDs[deletedEntry]], "\", press enter to continue...", sep="")
        input ()
        del openJournal[keyIDs[deletedEntry]]
        save ()
        os.system("clear")

# Loop that continues until the user decides to quit the program
while True:

    # Clears screen
    os.system ("clear")

    # Lists out all options for what the user can choose
    print (
        "Would you like to: \n1. Make a new journal entry\n2. View a previously written journal entry\n"
        "3. Delete an entry\n4. Delete the journal\n\n0. Quit")

    # Prompts them to cheese
    try:
        newOrView = int(input("Enter your choice: "))
        os.system("clear")

    # If they don't give a integer value for the input, restarts the loop
    except ValueError:
        print ("You must enter a valid choice")
        os.system ("clear")
        continue

    # Calls all the associated functions depending on the user's input
    if newOrView == 1:
        newentry ()
    elif newOrView == 2:
        viewentry ()
    elif newOrView == 3:
        delentry ()

    # User chooses to delete the whole journal
    elif newOrView == 4:

        # Asks user if they are sure that they want to delete the whole journal
        really = input("Do you want to delete the entire journal? (y/n): ")

        # If they are sure, then the journal file is deleted and the program quits after the user presses enter
        if really == "y":
            os.remove(journalChoice)
            input ("\nOk, your journal is deleted. \n\nPress enter to exit program...")
            quit()

        # If they don't say "y" as the previous input, then the program just continues
        else:
            continue

    # Prints out a "goodbye" message and then quits the program
    elif newOrView == 0:
        print ("Goodbye!")
        quit()

    # If the user doesn't give a valid integer, then the loop restarts
    else:
        print ("That isn't a valid option!")
        continue
