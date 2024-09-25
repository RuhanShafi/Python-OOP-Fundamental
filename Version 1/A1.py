#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#

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

class ProjectDatabase:
    # Stores all Projects within a Dictionary
    def __init__(self):
        self.allProjects = []
    
    # For loop used to list all project within the self.allProjects list
    def list_all_projects(self):
        for project in self.allProjects:
            print(project)
    
    # Appends a new project object onto the self.allProjects List
    def create_new_project(self,project):
        self.allProjects.append(project)
    

    # The 4 search functions below returns a list of every project which contains a case insenestive substring of the user specified input.
    # E.g, if I searched for every 'test' in fArea, it would return objects which fArea Attrubite contains test, test1, tEsT3 etc

    def search_for_project_by_name(self,name):
        results = [project for project in self.allProjects if name.lower() in project.name.lower()]
        return results

    def search_for_project_by_country(self,country):
        results = [project for project in self.allProjects if country.lower() in project.country.lower()]
        return results
    
    # old one which only returned the first instance
    '''def search_for_project_by_country(self,country):
        for project in self.allProjects:
            if project.country == country:
                return project
        return None
    '''

    def search_for_project_by_org(self,org):
        results = [project for project in self.allProjects if org.lower() in project.org.lower()]
        return results

    def search_for_project_by_fArea(self,fArea):
        results = [project for project in self.allProjects if fArea.lower() in project.fArea.lower()]
        return results
    
    # The 5 Modify below takes a user input and overrides the selected Attrubite with it.
    # E.g, if the exisitng value for fArea was 'Education' and mod_fArea = 'Health'. the fArea for that object would be overidden to 'Health'
    # In UML Diagram, returns a bool value to indicate if modification was successful or not

    def modify_project_name(self,project,mod_name_change):
        if project in self.allProjects:
            project.name = mod_name_change
            return True
        return False

    def modify_project_org(self,project,mod_org):
        if project in self.allProjects:
            project.org = mod_org
            return True
        return False

    def modify_project_country(self, project,mod_country):
        if project in self.allProjects:
            project.country = mod_country
            return True
        return False

    def modify_project_fArea(self, project,mod_fArea):
        if project in self.allProjects:
            project.fArea = mod_fArea
            return True
        return False

    def modify_project_tFunding(self, project, mod_tFunding):
        if project in self.allProjects:
            project.tFunding = mod_tFunding
            return True
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class UserInterface:
    # This init function is used in order to use the different function within the class ProjectDatabase using the self.manager function
    def __init__(self):
        self.manager = ProjectDatabase()

        # This one is used in the modify section of the code.
        # Basically, since I made that search can return multiple values as explained in Line 33 within the right circumstance, the program needs to know which project it should be modifiying.
        # Thus, comes the following empty varaible where it can be stored into when it is required.
        self.current_project_selected = None 
    

    # The following 3 functions are Menu functions where the User can interact with the Terminal Based UI (TUI).
    # Looking at the output, the user is asked to input a number with each number coreaponding to a function located below that is ran.
    def TUI_menu(self):
        while True:
            print("\nPROJECT DATABASE\n\n1. Add New Project\n2. List all Projects\n3. Search for Project\n4. Modify a Project\n5. Exit the Program\n")

            choice = input("Enter your choice: ")
            
            # Runs the different functions
            if choice == "1":
                self.add_new_project()
            elif choice == "2":
                self.list_all_projects()
            elif choice == "3":
                self.tui_Search_Menu()
            elif choice == "4":
                self.tui_Modify_Menu()
            elif choice == "5":
                break
            else:
                print("Invaild Input")

    def tui_Search_Menu(self):
        print("\nSearch Database\n1. Search by Name\n2. Search by Organization\n3. Search by Focus Area\n4. Search by Country\n5. Return to Main Menu\n")

        search_choice = input("Enter your choice: ")
        # Runs the different function

        if search_choice == "1":
            self.search_for_project_by_name()
        elif search_choice == "2":
            self.search_for_project_by_org()
        elif search_choice == "3":
            self.search_for_project_by_fArea()
        elif search_choice == "4":
            self.search_for_project_by_country()
        elif search_choice == "5":
            pass
        else:
            print("Invalid input")

    def tui_Modify_Menu(self):
        print("\nDatabase Modification Menu\n")
        mod_name = input("What project do you wish to Modify?: ")
        projects = self.manager.search_for_project_by_name(mod_name)
        
        # Since new Search Update allows for multiple values return, it makes the old modification engine hard. Reworked version is below
        
        if projects: # If search is successful
            if len(projects) > 1:  # If more then one return value from search
                print("Multiple Projects found. Please select which project to modify using the Project Number\n")
                for i, project in enumerate(projects):
                    print("Project {0}.\n {1}".format(i+1,project)) # Prints out Projects details + Project ID in Human Language for user conveinces. I.E Project looks like how they should output and the ID value is increased by 1 so it starts at 1 as opposed to 0.
                mul_mod_choice = input("Enter Project Number to make Selection: ")
                try: # Exception Handeling to full proof against values out of range or non-int values
                    index = int(mul_mod_choice) - 1 # Formating User Number (Starts at 1) into Python interpration of numbers (Starts at 0)
                    if 0 <= index < len(projects): # User Input out of range
                        self.current_project_selected = projects[index] # Moves the selected project into the placeholder variable defined in the __init__ function above.
                    else:
                        print("Project Number out of Range") # User Inputted Incorrectly
                        return # Returns back to the main menu.
                except ValueError:
                    print("Invalid Input. Not a Number") # Exception Handeling for String Values/Decimal Values
                    return # Same as before.
            else:
                self.current_project_selected = projects[0] # If there is only one project, then just use the first value
        

            while True:
                # Now that the Project to modify has been selected. The actual modification can occur.
                #The current Attrubites of the project is displayed for User conveinces
                print("\nWhat do you wish to modify?\n1. Modify Project's Name\n2. Modify Project's Total Funding\n3. Modify Project's Organization\n4. Modify Project's Focus Area\n5. Modify Project's Country\n6. Save Changes and Exit back to Main Menu\n")
                print("\nCurrent Project Attrubite:\n{0}".format(self.current_project_selected))
                mod_choice = input("Enter your choice: ")
                
                # The different choices that the user can make are all just functions which is responsible for taking the inputs and running the actual modification function in ProjectDatabase using self.manager()
                if mod_choice == "1":
                    self.modify_project_name()
                elif mod_choice == "2":
                    self.modify_project_tFunding()
                elif mod_choice == "3":
                    self.modify_project_org()
                elif mod_choice == "4":
                    self.modify_project_fArea()
                elif mod_choice == "5":
                    self.modify_project_country()
                elif mod_choice == "6":
                    break
                else:
                    print("Invalid Input")

        else:
            print("Project not found")

        '''
        Old version of Modify Script to broke because new search can return multiple values instead of the first instance.
        if self.current_project_selected:
            print("\nCurrent Project Detials:\n{0}".format(self.current_project_selected))

            while True:
                print("\nWhat Do you wish to modify?\n1. Modify Project's Name\n2. Modify Project's Total Funding\n3. Modify Project's Organization\n4. Modify Project's Focus Area\n5. Modify Project's Country\n6. Save Current Changes and Exit back to Main Menu\n")
                print("{0}\nCurrent Project Attrubite Values\n{0}\n{1}".format("~"*34,self.current_project_selected()))
                mod_choice = input("Enter your choice: ")
                
                if mod_choice == "1":
                    self.modify_project_name()
                elif mod_choice == "2":
                    self.modify_project_tFunding()
                elif mod_choice == "3":
                    self.modify_project_org()
                elif mod_choice == "4":
                    self.modify_project_fArea()
                elif mod_choice == "5":
                    self.modify_project_country()
                elif mod_choice == "6":
                    break
                else:
                    print("Invalid Input")
        else:
            print("Project not found.")
        '''
    
    # This function is responsible for creating a new project, to do this, it takes the different inputs required, creates a new project where the add_new_project() function in ProjectDatabase is ran where it is appended onto the master list.
    def add_new_project(self):
        name = input("\nEnter Project Name: ")
        tFunding = input("Enter Total Funding: ")
        country = input("Enter Country: ")
        org = input("Enter Organization: ")
        fArea = input("Enter Focus Area: ")

        project = Projects(name,tFunding,country,fArea,org)
        self.manager.create_new_project(project)
        print("Project added successfully!")
    
    # The following 4 functions are the different search functions used to search for project by their different Attrubites.
    # To do this, an input is taken from the user, wher the respective serach function is ran and if there is an return value/s, they will be printed out. Otherwise the program will report that there was no returned value

    def search_for_project_by_name(self):
        name = input("Enter Project Name to Search: ")
        projects = self.manager.search_for_project_by_name(name)

        if projects:
            for project in projects:
                print("\nProject Detials:\n{0}".format(project))
        else:
            print("Project not found.")

    def search_for_project_by_country(self):
        country = input("Enter Country to Search: ")
        projects = self.manager.search_for_project_by_country(country)

        if projects:
            for project in projects:
                print("\nProject Detials:\n{0}".format(project))
        else:
            print("Project not found.")

    def search_for_project_by_org(self):
        org = input("Enter Organization to Search: ")
        projects = self.manager.search_for_project_by_org(org)

        if projects:
            for project in projects:
                print("\nProject Detials:\n{0}".format(project))
        else:
            print("Project not found.")

    def search_for_project_by_fArea(self):
        fArea = input("Enter Focus Area to Search: ")
        projects = self.manager.search_for_project_by_fArea(fArea)

        if projects:
            for project in projects:
                print("\nProject Detials:\n{0}".format(project))
        else:
            print("Project not found")
    
    # The following 5 functions allows the user to modify the different Attrubites of a selected project
    # To do this, a user input is taken, where the respective function in project database is ran where the orignal value for the respective Attrubites is overidden with the new one.

    def modify_project_name(self):
        mod_name_change = input("Enter new Project Name: ")
        if self.current_project_selected:
            self.manager.modify_project_name(self.current_project_selected, mod_name_change)
            print("Project name updated successfully!")
        else:
            print("Project Name could not be successfully updated.")

    def modify_project_country(self):
        mod_country = input("Enter Project's New Country: ")
        if self.current_project_selected:
            self.manager.modify_project_country(self.current_project_selected, mod_country)
            print("Project's Country Attrubite has been successfully updated!")
        else:
            print("Project's Country Attrubite could not be updated successfully.")

    def modify_project_org(self):
        mod_org = input("Enter Project's new Organization: ")
        if self.current_project_selected:
            self.manager.modify_project_org(self.current_project_selected, mod_org)
            print("Project's Organization Attrubite has been successfully updated!")
        else:
            print("Project's Organization Attrubite could not be updated successfully.")

    def modify_project_tFunding(self):
        mod_tFunding = input("Enter Project's New Total Funding Amount: ")
        if self.current_project_selected:
            self.manager.modify_project_tFunding(self.current_project_selected, mod_tFunding)
            print("Project's Total Funding Attrubite has been successfully updated!")
        else:
            print("Project's Total Funding Attrubite could not be updated successfully.")

    def modify_project_fArea(self):
        mod_fArea = input("Enter Project's new Focus Area: ")
        if self.current_project_selected:
            self.manager.modify_project_fArea(self.current_project_selected, mod_fArea)
            print("Project's Focus Area Attrubite has been successfully updated!")
        else:
            print("Project's Focus Area Attrubite could not be updated successfully.")

    # Just runs the list_all_projects function in ProjectDatabase
    def list_all_projects(self):
        self.manager.list_all_projects()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Run the Front end of the Program i.e The User Interface TUI where given the users choice, the different functions are ran.
if __name__ == '__main__':
    ui = UserInterface()
    ui.TUI_menu()
