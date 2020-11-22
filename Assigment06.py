# ---------------------------------------------------------------------------- #
# Title: Assignment06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# e4ster, 11.21.2020, Modified code to complete assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing Tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Reads data from a file into a list of dictionary rows.

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        try:
            text_file = open(file_name, "x")
            text_file.close()
        except FileExistsError:
            pass

        list_of_rows.clear()  # clear current data
        text_file = open(file_name, "r")
        for line in text_file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        text_file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """
        Adds user input to our data table.

        :param task: String of a task name.
        :param priority: String of priority level.
        :param list_of_rows: The initial list of dictionaries.
        :returns: A list of dictionaries.
        """
        global dicRow
        dicRow = {"Task": task.strip(), "Priority": priority.strip()}
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """
        Removes a line item from the table.

        :param task: String name of a task.
        :param list_of_rows: The initial list of dictionaries.
        :return: The new list of dictionaries.
        """
        count = 0
        for row in list_of_rows:
            if task == row["Task"]:
                list_of_rows.remove(row)
                count = 1
        if count == 0:
            print("I'm sorry, that task doesn't exist.")
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """
        Writes the data table to the text file.

        :param file_name: String name of the text file.
        :param list_of_rows: Our list of dictionaries.
        :return: Nothing
        """
        text_file = open(file_name, "w")
        for row in list_of_rows:
            text_file.write(row["Task"].lower() + "," + row["Priority"].lower() + "\n")
        text_file.close()


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """
        Display a menu of choices to the user.

        :return: Nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """
        Gets the menu choice from a user.

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """
        Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: The data table you want to display.
        :return: Nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """
        Gets a yes or no choice from the user.

        :param message: String you want to display.
        :return: String
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """
        Pause program and show a message before continuing.

        :param optional_message:  An optional message you want to display
        :return: Nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """
        Gets and returns user input for task and priority.

        :returns: Two strings.
        """
        new_task = input("New Task: ").lower().strip()
        new_priority = input("Priority Level (High, Medium, Low): ").lower().strip()
        return new_task, new_priority

    @staticmethod
    def input_task_to_remove():
        """
        Gets and returns what the user wants to remove.

        :returns: One string.
        """
        task_remove = input("Task to remove: ").lower().strip()
        return task_remove


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Start the loop, display current data, get user's choice.
while True:
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 3 - Add a new task to the list.
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # Step 4 - Remove a task from the list.
    elif strChoice == '2':  # Remove an existing Task
        remove_task = IO.input_task_to_remove()
        Processor.remove_data_from_list(remove_task, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # Step 5 - Save data to the text file.
    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower().strip() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    # Step 6 - Reload data from file to our list in memory.
    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    # Step 7 - Exit program.
    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit
