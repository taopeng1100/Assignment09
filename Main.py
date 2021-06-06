# Title: Main script to complete "Assignment 09"
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# <Tao Peng>,<06.04.2021>,Modified code to complete assignment 9

# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio

else:
    raise Exception("This file was not created to be imported")
# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Declare variable and read the employee.txt data into the object
# Print out the imported data
lstTable = []
FileName = 'EmployeeData.txt'
lstFileData = Fp.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))

# Work through the menu choices
while (True):
    Eio.print_current_list_items(lstTable)  # Show current data in the list/table
    Eio.print_menu_items()  # Shows menu
    strChoice = Eio.input_menu_options()  # Get menu option
    # Process user's menu choice
    if strChoice.strip() == '1':  # Show the current employee list
        Eio.print_current_list_items(lstTable)
        Eio.input_press_to_continue()
        continue  # to show the menu

    elif strChoice.strip() == '2':  # Add a new Task
        New = Eio.input_employee_data()
        lstTable.append(New)
        Eio.input_press_to_continue()
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        YorN = Eio.input_yes_no_choice("Save this data to file? (y/n) - ")
        if YorN.lower() == "y":
            status = Fp.save_data_to_file (FileName, lstTable)
            print(status)
            Eio.input_press_to_continue()
        else:
            Eio.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
# Main Body of Script  ---------------------------------------------------- #