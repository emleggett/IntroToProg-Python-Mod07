# ---------------------------------------------------------------------------- #
# Title: Assignment 07 - Contact Tracker
# Description: Write a script that demonstrates pickling
#              and error handling in Python.
# ELeggett,11.29.2021,Created script
# ---------------------------------------------------------------------------- #

# PICKLING DEMO -------------------------------------------------------------- #

# Step 1: Import the pickle module
import pickle

# Step 2: Introduce pickling demo to user
print()
input("Press Enter to begin pickling demonstration.")
print("First, let's get some data to work with." + "\n")

# Step 3: Collect and organize data to pickle to .dat file
contact_name = str(input("Enter a name to add to contact list: "))
contact_number = int(input("Enter a phone number for your contact (numbers only, please!): "))
contact_list = [contact_name, contact_number]
print("\n" + "Here is our data as a row in a list:")
print(contact_list)
print("\n" + "And here's that list converted into a dictionary:")
contact_dict = [{"Name":contact_name, "Number":contact_number}]
print(contact_dict)

# Step 4: Save data to .dat file using pickle.dump
print("\n" + "Saving dictionary data binary file... (= PICKLING)")
myfile = open("Assignment07.dat", "wb")
pickle.dump(contact_dict, myfile)
myfile.close()
print("Assignment07.dat successfully saved!")

# Step 5: Read and display saved data from .dat file using pickle.load
print("\n" + "Reading dictionary data from binary file... (= UNPICKLING)")
myfile = open("Assignment07.dat", "rb")
mydata = pickle.load(myfile)
print(mydata)
myfile.close()

print("\n" + "Pickling tutorial complete!" + "\n")

# ERROR HANDLING DEMO -------------------------------------------------------- #
# Step 1: Introduce error handling demo to user
input("Press Enter to continue to error handling demonstration.")
print("\n" + "We'll use the inputs from our pickling demonstration to produce a Python error."+ "\n" + "Here's what happens when we try to concatenate our data instead of placing it into a list object: " + "\n")

# Step 2: Demo basic try-except block
try:
    new_list = contact_name + contact_number
    print(new_list)
except Exception as e:
    print(e, type(e), sep = "\n")

# Step 3: Demo custom error handling
input("\n" + "Now, let's leverage exception classes and built-in functions to add more detail. Press Enter to try again.")
try:
    new_list = contact_name + contact_number
    print(new_list)
except TypeError as e:
    print("\n" + "Can't concatenate numeric and string data! Error report: " + "\n")
    print(e, e.__doc__, e.__str__,type(e), sep = "\n")
except FileNotFoundError as e:
    print("\n" + "Assignment07.dat file must exist prior to running this script! Error report: "+ "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")
except Exception as e:
    print("\n" + "An unspecified error occurred! Error report: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")

print("\n" + "Error handling tutorial complete!" + "\n")

# ADVANCED DEMO -------------------------------------------------------------- #
# Step 1: Introduce combined functionality demo to user
input("Press Enter to re-run pickling script with custom error handling.")
print()

# Step 2: Define custom exception classes
class AlphaError(Exception):
    def __str__(self):
        return "Contact name must be alphabetical!"

class EntryError(Exception):
    def __str__(self):
        return "Please input one or more characters for entry!"

class NumError(Exception):
    def __str__(self):
        return "Phone number must be numeric!"

class PhError(Exception):
    def __str__(self):
        return "Phone number must be 10 digits in length!"

# Step 3: First try-catch block - gather name
try:
    contact_name = input("Enter a name to add to contact list: ")
    if contact_name.isnumeric():
        raise AlphaError()
    elif len(contact_name)==0:
        raise EntryError()
except Exception as e:
    print("\n" + "Error report: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")

# Step 3: Second try-catch block - gather number and proceed with pickling/unpickling if no exceptions
try:
    contact_number = input("Enter a phone number for your contact (numbers only, please!): ")
    if contact_number.isalpha():
        raise NumError()
    elif len(contact_number)!=10:
        raise PhError()
    else:
        contact_list = [contact_name, contact_number]
        print("\n" + "Valid entry! Name and number added to list data.")
        contact_dict = [{"Name": contact_name, "Number": contact_number}]
        myfile = open("Assignment07.dat", "wb")
        pickle.dump(contact_dict, myfile)
        myfile.close()
        print("\n" + "Assignment07.dat successfully overwritten!")
        myfile = open("Assignment07.dat", "rb")
        mydata = pickle.load(myfile)
        print("\n" + "Assignment07.dat successfully read:")
        print(mydata)
        myfile.close()
        print("\n" + "Assignment07.dat closed. Thank you for using my tutorial. Goodbye!")
except Exception as e:
    print("\n" + "Error report: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")