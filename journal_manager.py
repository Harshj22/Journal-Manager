import os
from datetime import datetime

class JournalManager:

    def __init__(self):
        self.filename = "exam6.txt"


    def add_entry(self):
        try:
            entry = input("\nEnter your Journal entry:\n")
            with open(self.filename, "a") as f:
                f.write(str(datetime.now()) + "\n")
                f.write(entry + "\n\n")
            print("Entry Added Successfully.\n")
        except:
            print("Entry not Added.\n")


    def view_entries(self):
        try:
            with open(self.filename, "r") as f:
                print("\nYour Journal Entries:\n")
                print(f.read())
        except:
            print("\nFile not found. Please add a new entry first.\n")


    def search_entry(self):
        try:
            keyword = input("Enter keyword OR date: ")
            with open(self.filename, "r") as f:
                lines = f.readlines()

            found = False
            print("\nMatching Entries for this Keyword:\n")

            for i in range(len(lines)):
                if keyword in lines[i]:
                    print(lines[i].strip())  
                    if i + 1 < len(lines):
                        print(lines[i + 1].strip())  
                    print()
                    found = True

            if not found:
                print("No matching entry found.\n")

        except:
            print("\nFile not found. Please add a new entry first.\n")


    def delete_entries(self):
        try:
            os.remove(self.filename)
            print("\nAll journal entries have been deleted.\n")
        except:
            print("\nThe journal file does not exist. Please add a new entry first.\n")


def show():
    journal = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager.\n")
        print("1. Add a new Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nPlease Select an Option: ")

        if choice == "1":
            journal.add_entry()
        elif choice == "2":
            journal.view_entries()
        elif choice == "3":
            journal.search_entry()
        elif choice == "4":
            journal.delete_entries()
        elif choice == "5":
            print("Thank You for using personal journal manager. Goodbye!")
            break
        else:
            print("Invalid choice. please select between 1 - 5.\n")


show()
