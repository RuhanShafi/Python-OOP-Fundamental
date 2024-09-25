import os
import platform

class Projects:
    # init() function that creates the class
    def __init__(self,name,tFunding,country,fArea,org):
        self.name = name
        self.tFunding = tFunding
        self.country = country
        self.fArea = fArea
        self.org = org

    # String Formating
    def __str__(self):
        return "\nProject name: {0}\nTotal Funding: {1}\nOrganization: {2}\nFocus Area: {3}\nCountry: {4}\n".format(self.name,self.tFunding,self.org,self.fArea,self.country)


class ProjectDatabase(Projects):
    def __init__(self):
        # Stores all the project within a List
        self.projects = []
        # Variable which is used to hold the object to be modified
        self.current_project_selected = None
    
    # String Formating The Physical Object as reduency
    def __str__(self):
        project_details = ""
        for project in self.projects:
            project_details += str(project) + "\n"
        return project_details if project_details else "No projects added yet."
    
    # Appends a new project object onto the self.Project List if it is valid
    def add_project(self,project):
        if isinstance(project, Projects):  # Check if it's a valid Projects object
            self.projects.append(project)
        else:
            print("Invalid project")
    
    # For loop used to list all projects within the self.Project list, a enumerate function is used to increase readability
    def list_all_projects(self):
        if self.projects:
            for pindex, project in enumerate(self.projects, start=1):   # Enumerate is used in order to Create a Numerical Index for Easier Readability.
                print("Project {0}:\n{1}".format(pindex,project))
        # User Feedback should User List All Project without any project stored in the system         
        else:
            print("Nothing to List Just Yet. Please either Import Objects or Create a New Project")
    
    # Search Modules Imported from previous Version of the Program, returns a list of every project containing search term regardless of formating
    # Search for project by name
    def search_for_project_by_name(self, name):
        return [project for project in self.projects if name.lower() in project.name.lower()]

    # Search for project by organization
    def search_for_project_by_org(self, org):
        return [project for project in self.projects if org.lower() in project.org.lower()]

    # Search for project by focus area
    def search_for_project_by_fArea(self, fArea):
        return [project for project in self.projects if fArea.lower() in project.fArea.lower()]

    # Search for project by country
    def search_for_project_by_country(self, country):
        return [project for project in self.projects if country.lower() in project.country.lower()]
    
    # The 5 Modify below takes a user input and overrides the selected Attrubite with it. Again taking from previous version
    # E.g, if the exisitng value for fArea was 'Education' and mod_fArea = 'Health'. the fArea for that object would be overidden to 'Health'
    # In UML Diagram, returns a bool value to indicate if modification was successful or not

    # Modify project attributes
    def modify_project_name(self, project, new_name):
        if project in self.projects:
            project.name = new_name
            return True
        return False

    def modify_project_org(self, project, new_org):
        if project in self.projects:
            project.org = new_org
            return True
        return False

    def modify_project_fArea(self, project, new_fArea):
        if project in self.projects:
            project.fArea = new_fArea
            return True
        return False

    def modify_project_country(self, project, new_country):
        if project in self.projects:
            project.country = new_country
            return True
        return False

    def modify_project_tFunding(self, project, new_tFunding):
        if project in self.projects:
            project.tFunding = new_tFunding
            return True
        return False

# New class for all the different File operations within the Project. Using Inheritance, this is directly interfaced with the class above, removing all user's abstraction seen in the class below.'
class FILES(ProjectDatabase):
    def export_all_projects(self, filename):
        #Export all projects to a text file
        # Exception handeling is used to indicate errors
        try:
            with open(filename, 'w') as file:   #If project list is empty
                if not self.projects:
                    file.write("No projects available.\n")
                    print("No projects available to export.")
                else:
                    for project in self.projects:   # For loop used to write every line
                        file.write(str(project) + '\n') #new line for proper formatting
                    print("All projects successfully exported to {0}".format(filename)) #User feedback
        except Exception as e: #Debugger
            print("An error occurred while exporting projects: {0}".format(e))

    # Same code as previous, just with a search query built in
    def export_projects_by_country(self,country,filename):
        try:
            with open(filename, 'w') as file:
                country_project = [project for project in self.projects if project.country.lower() == country.lower()] #Can't use Inheritance so I did it the manual way search_for_project_by_country(country)
                if not country_project:
                    file.write("No Projects found for {0}".format(country))
                else:
                    for project in country_project:
                        file.write(str(project)+'\n')
                    print("All Projects from {0} sucessfuly exported to {1}".format(country,filename))
        except Exception as e:
            print("An error has occured while exporting projects: {0}".format(e))
    
    # This was hell.

    def import_projects(self, filename):
        #Import projects from a text file
        try:
            with open(filename, 'r') as file:
                project_data = []  # This will collect data for one project at a time and store it within a list for later use

                for line in file:
                    line = line.strip()  # Remove leading/trailing whitespace to maintain formatting

                    # If there is an empty line, it signifies the end of a project
                    if not line:
                        if project_data: # RESTART FROM 0, Insert that one hindi song.
                            # Anways, what this code does is that it addes the previous information to the next function and resests this function to add the next project
                            self._create_project_from_data(project_data)
                            project_data = []  # Reset for the next project
                    else:
                        project_data.append(line)

                # After finishing the loop, create the last project if project_data is not empty
                if project_data:
                    self._create_project_from_data(project_data)
            #User feedback + Debugger in the form of exception handeling
            print("Projects successfully imported from {0}".format(filename))
        except FileNotFoundError:
            print("File {0} not found.".format(filename))
        except Exception as e:
            print("An error occurred while importing projects: {0}.".format(e))

    def _create_project_from_data(self, data):
        # Helper method to create a project from a list of strings (data)
        try:
            # Ensure the project data has exactly 5 fields
            if len(data) == 5:
                name = data[0].split(": ", 1)[1]
                tFunding = data[1].split(": ", 1)[1]
                org = data[2].split(": ", 1)[1]
                fArea = data[3].split(": ", 1)[1]
                country = data[4].split(": ", 1)[1]  # Base Country

                # Create a project and add it to the project list
                project = Projects(name, tFunding, country, fArea, org)
                self.add_project(project)
                print("Imported project: {0}".format(name))
            else:
                print("Skipping invalid project data: {0}".format(data))    # Helps to skip unwanted stuff
        except IndexError as e: # Same as before, User Feedback + Debugger
            print("Error parsing project data: {0} - {1}".format(data,e))
        except Exception as e:
            print("An unexpected error occurred: {0}".format(e))

# Frontend of Program, Inheritance is used to get the functions from the previous class.
class TUI(ProjectDatabase):

    # Litle Snipet of Code that clears the screen.
    def clear_screen(self):
        if platform.system() == 'Windows':
            os.system("cls")
        else:
            os.system("clear")

    #Neat Little & Clean Quit Menu
    def quit_program(self):
        quitprompt = input("Are you sure you want to quit the program?\nPlease enter (\'q\',\'y\' or \'yes\' (case insenestive)) to quit, otherwise press any other button to return to the main menu: ")
        if quitprompt.lower() != 'q' and quitprompt.lower() != 'yes' and quitprompt.lower != 'y':
            self.clear_screen()
            self.main_menu()
        else:
            self.clear_screen()
            exit()
            
    # Function that waits for user input to return to the main menu, usefully for when outputing stuff and the reader needs time to read
    def return_to_menu(self):
        input("\nPress any key to return to the main menu...")
        self.clear_screen()  # Clear screen once they press a key
    
    # If invalid inputs occur
    def user_stuck(self):
                print("I do not recognise the action")
                failrep = input("Do you wish go back to the Main Menu? (Y/n): ")
                if failrep.lower() == 'y':
                    self.clear_screen()
                    self.main_menu
                else:
                    self.clear_screen
                    exit()

    #Actual Main Menu that either performs and action to leads to an action
    def main_menu(self):
        self.clear_screen()
        print("Welcome to The Main Menu\n")
        while True:
            print("1. Create New Object\n2. List All Projects\n3. Search for Project\n4. Modify a Project\n5. Inport Project from File\n6. Export all Projects\n7. Generate Summary Report\n8. Perform Unittest\n9. View Change Logs and Features\nQ. Quit the Program\n")
            key = input("Which Operation do you wish to Perform? ")

            if key == '1':
                self.add_new_project()
                continue
            elif key == '2':
                self.clear_screen()
                print("List of All Projects\n")
                self.list_all_projects()
                self.return_to_menu()
                continue
            elif key == '3':    #Goes to Search Menu
                self.clear_screen()
                self.tui_search_menu()
                self.return_to_menu()
            elif key == '4':    #Goes to Mod Menu
                self.clear_screen()
                self.tui_mod_menu()
            elif key == '5':    #Imports Projects
                self.clear_screen()
                files = FILES()
                filename = input("Enter the name of the file to import projects from (e.g, projects.txt): ")
                files.projects = self.projects
                files.import_projects(filename)
                self.return_to_menu()
            elif key == '6':    #Exports all Projects
                self.clear_screen()
                files = FILES()
                exfilename = input("Enter the name of the file to export all projects into (e.g allproject.txt): ")
                files.projects = self.projects
                files.export_all_projects(exfilename)
                self.return_to_menu()
            elif key == '7':    #Exports all Projects within a Country
                self.clear_screen()
                files = FILES()
                files.projects = self.projects
                country = input("Enter the country for which to generate the summary report on: ")
                filename = input("Enter the filename to export to (e.g, country_report.txt): ")
                files.export_projects_by_country(country, filename)
                self.return_to_menu()
            elif key == '8':    #Performs Unittest from within the main program. Impressive/s (in one of those advertser voices from the 90`s)
                if platform.system() == 'Windows':
                    self.clear_screen()
                    os.system('python3 test_A2.py')
                    self.return_to_menu()
                else:
                    self.clear_screen()
                    os.system('python test_A2.py')
                    self.return_to_menu()
            elif key == '9':    #Debug Meny
                self.clear_screen()
                self.change_log_menu()
            elif key.lower() == "q":    #Quits Program
                self.clear_screen()
                self.quit_program()
            else:   #If invalid input
                self.user_stuck()

        
    #Left over script to add new project, if it aint broke, don't fix it. 
    def add_new_project(self):
        self.clear_screen()
        print("Define the following parameters for the new project")
        name = input("\nEnter Project Name: ")
        tFunding = input("Enter Total Funding: ")
        country = input("Enter Country: ")
        org = input("Enter Organization: ")
        fArea = input("Enter Focus Area: ")
        
        # Creating a new project instance
        new_project = Projects(name, tFunding, country, fArea, org)

        # Adding the new project to the inherited database
        self.add_project(new_project)


        print("Project added successfully!\n")
        self.return_to_menu()
        self.clear_screen()
    
    # Easter Egg, plus script to add dummy object for testing
    def change_log_menu(self):
        while True:
            print("Change Log\n\n1. Added Screen Clearing\n2. Added File I/O Support\n3. A LOT of Idiot Proofing\n4. Using Inheritance and Poloymphorism")

            testkey=input("\nCreate Dummy Objects? (y/n): ")
            if testkey.lower() == 'y':
                dummy_object = Projects("test","test","test","test","test")
                self.add_project(dummy_object)
                self.clear_screen()
                break
            else:
                self.clear_screen()
                break
    #The classic search menu, now with Inheritance, so the code is much cleaner.
    def tui_search_menu(self):
        print("Search Database\n\n1. Search by Name\n2. Search by Organization\n3. Search by Focus Area\n4. Search by Country\n5. Return to Menu\nQ. Quit Program\n")

        search_choice = input("Enter your choice: ")
        if search_choice == '1':
            name = input("Enter project name: ")
            results = self.search_for_project_by_name(name)
        elif search_choice == '2':
            org = input("Enter organization: ")
            results = self.search_for_project_by_org(org)
        elif search_choice == '3':
            fArea = input("Enter focus area: ")
            results = self.search_for_project_by_fArea(fArea)
        elif search_choice == '4':
            country = input("Enter country: ")
            results = self.search_for_project_by_country(country)
        else:
            print("Invalid Input")
            return
        #If no results are returned
        if results:
            for result in results:
                print(result)
        else:
            print("No matching projects found.")

    # Modify menu, same as before, so copy + pasted comments
    def tui_mod_menu(self):
        print("Database Modification Menu\n")
        name = input("Enter the name of the project to modify: ")
        modproject = self.search_for_project_by_name(name)

        if not modproject:  # If no projects are found
            print("No matching project found with the name '{0}'. Returning to the main menu.".format(name))
            self.return_to_menu()  # Return to the main menu
            return

        # If multiple projects are found, let the user select which one to modify
        if len(modproject) > 1:
            self.clear_screen()
            print("Multiple Projects found. Please select which project to modify using the Project Number\n") # # Prints out Projects details + Project ID in Human Language for user conveinces. I.E Project looks like how they should output and the ID value is increased by 1 so it starts at 1 as opposed to 0.
            for i, project in enumerate(modproject):
                print("Project {0}.\n{1}".format(i + 1, project))  # Show the list of matching projects with index

            try:    # Exception Handeling to full proof against values out of range or non-int values
                mul_mod_choice = int(input("Enter Project Number to make Selection: ")) - 1 # Formating User Number (Starts at 1) into Python interpration of numbers (Starts at 0)
                if 0 <= mul_mod_choice < len(modproject):
                    self.current_project_selected = modproject[mul_mod_choice]
                else:
                    print("Project number out of range. Returning to the main menu.")  # User Inputted Incorrectly
                    self.return_to_menu()
                    return
            except ValueError:  #Exception Handelling for String Values/Decimal Numbers
                print("Invalid input. Please enter a valid number. Returning to the main menu.")
                self.return_to_menu()
                return
        else:
            # If only one project is found, select it automatically
            self.current_project_selected = modproject[0]


        while True:
                # Now that the Project to modify has been selected. The actual modification can occur.
                #The current Attrubites of the project is displayed for User conveinces
            self.clear_screen()
            print("What do you wish to modify?\n1. Modify Project's Name\n2. Modify Project's Total Funding\n3. Modify Project's Organization\n4. Modify Project's Focus Area\n5. Modify Project's Country\n6. Save Changes and Exit back to Main Menu\n")
            print("\nCurrent Project Details:\n{0}".format(self.current_project_selected))
            mod_choice = input("Enter your choice: ")

            # Different Mod options available, points to the function in the ProjectDatabase class using Inheritance
            if mod_choice == '1':
                new_name = input("Enter new name: ")
                self.modify_project_name(self.current_project_selected, new_name)
            elif mod_choice == '2':
                new_funding = input("Enter new total funding: ")
                self.modify_project_tFunding(self.current_project_selected, new_funding)
            elif mod_choice == '3':
                new_org = input("Enter new organization: ")
                self.modify_project_org(self.current_project_selected, new_org)
            elif mod_choice == '4':
                new_fArea = input("Enter new focus area: ")
                self.modify_project_fArea(self.current_project_selected, new_fArea)
            elif mod_choice == '5':
                new_country = input("Enter new country: ")
                self.modify_project_country(self.current_project_selected, new_country)
            elif mod_choice == '6':
                print("Changes saved successfully!")
                self.clear_screen()
                return
            else:
                print("Invalid Input")
        else:
            print("No matching projects found.")

# Runs the program
if __name__ == '__main__':
    ui = TUI()
    ui.main_menu()
