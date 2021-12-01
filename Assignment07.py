# ---------------------------------------------------------------------------- #
# Title: Assignment 07 - Contact Tracker
# Description: Write a script that demonstrates pickling
#              and error handling in Python.
# ELeggett,11.29.2021,Created script
# ELeggett,11.30.2021,Scrapped and wewrote script,
#                     cleaned up code
# ---------------------------------------------------------------------------- #

# PICKLING DEMO -------------------------------------------------------------- #

# Step 1: Import the pickle module
import pickle

# Step 2: Introduce pickling demo to user
print()
input("Welcome to my pickling demonstration! Press Enter to begin.")
print("First, we'll need some data to work with. We're going to add an entry to an imaginary contact list." + "\n")

# Step 3: Collect and organize data to pickle to .dat file
contact_name = str(input("Enter the name of the contact you'd like to add: "))
contact_number = int(input("Enter a phone number for your contact (numbers only, please!): "))
contact_list = [contact_name, contact_number]
print("\n" + "Here's our contact data expressed as a list:")
print(contact_list)
print("\n" + "And here's that list further organized into a dictionary:")
contact_dict = [{"Name":contact_name, "Number":contact_number}]
print(contact_dict)

# Step 4: Save data to .dat file using pickle.dump
print("\n" + "Pickling (saving) data to file...")
myfile = open("Assignment07.dat", "wb")
pickle.dump(contact_dict, myfile)
myfile.close()
print("Assignment07.dat successfully saved and file closed.")

# Step 5: Read and display saved data from .dat file using pickle.load
print("\n" + "Unpickling (reading) data from file...")
myfile = open("Assignment07.dat", "rb")
mydata = pickle.load(myfile)
print(mydata)
myfile.close()

print("\n" + "Pickling tutorial complete!" + "\n")

# ERROR HANDLING DEMO -------------------------------------------------------- #
# Step 1: Introduce error handling demo to user
input("Press Enter to continue to error handling demonstration.")
print("\n" + "We'll use the inputs from our pickling demonstration to produce a Python error."+ "\n" + "Here's what happens when we try to concatenate our data instead of placing it into a list: " + "\n")

# Step 2: Demo basic try-except block
try:
    new_list = contact_name + contact_number
    print(new_list)
except Exception as e:
    print(e, type(e), sep = "\n")

# Step 3: Demo custom error handling
print()
input("Now, let's leverage exception classes and built-in Python functions to add a bit more detail. Press Enter to try again.")
try:
    new_list = contact_name + contact_number
    print(new_list)
except TypeError as e:
    print("\n" + "Error: Can't concatenate numeric and string data. Details: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep = "\n")
except FileNotFoundError as e:
    print("\n" + "Error: Assignment07.dat file must exist prior to running this script. Details: "+ "\n")
    print(e, e.__doc__, e.__str__, type(e), sep = "\n")
except Exception as e:
    print("\n" + "Error: An unspecified error occurred. Details: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")

print("\n" + "Error handling tutorial complete!" + "\n")

# ADVANCED DEMO -------------------------------------------------------------- #
# Step 1: Introduce combined functionality demo to user
input("Press Enter to re-run pickling script with custom error handling built in.")
print()

# Step 2: Define custom exception classes
class AlphaError(Exception):
    def __str__(self):
        return "Entry not accepted: Please use alphabetical characters in contact_name field."

class EntryError(Exception):
    def __str__(self):
        return "Entry not accepted: Please enter at least one character into contact_name field."

class NumError(Exception):
    def __str__(self):
        return "Entry not accepted: Please use only numbers in contact_number field."

class PhError(Exception):
    def __str__(self):
        return "Entry not accepted: Please input a 10-digit phone number into contact_number field."

# Step 3: First try-catch block - gather name
try:
    contact_name = input("Enter the name of the contact you'd like to add: ")
    if contact_name.isnumeric():
        raise AlphaError()
    elif len(contact_name)==0:
        raise EntryError()
    # Step 3: Second try-catch block - gather number and proceed with pickling/unpickling if no exceptions
    try:
        contact_number = input("Enter a phone number for your contact (numbers only, please!): ")
        if contact_number.isalpha():
            raise NumError()
        elif len(contact_number) != 10:
            raise PhError()
        else:
            contact_list = [contact_name, contact_number]
            print("\n" + "Valid entry! Preparing data to save to Assignment07.dat...")
            contact_dict = [{"Name": contact_name, "Number": contact_number}]
            print("\n" + "Opening Assignment07.dat and pickling...")
            myfile = open("Assignment07.dat", "wb")
            pickle.dump(contact_dict, myfile)
            myfile.close()
            print("\n" + "Assignment07.dat successfully saved. Closing file...")
            myfile = open("Assignment07.dat", "rb")
            mydata = pickle.load(myfile)
            print("\n" + "Assignment07.dat re-opened and unpickled. Here's your data:")
            print(mydata)
            myfile.close()
            print("\n" + "Assignment07.dat closed. Thank you for using my tutorial. Goodbye!")
    except Exception as e:
        print("\n" + "Error: " + "\n")
        print(e)
except Exception as e:
    print("\n" + "Error: " + "\n")
    print(e)