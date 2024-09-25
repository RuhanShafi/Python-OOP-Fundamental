import unittest
import os
from io import StringIO #Library for file Unittest
from unittest.mock import patch #Patches for some of the stuff used here
from A2 import Projects, ProjectDatabase, FILES #Imports the important stuff

# Testing the different functions from both the ProjectDatabase and FILES class
class TestProjectSystem(unittest.TestCase):

    def setUp(self):
        # Setting Up Functions
        self.db = ProjectDatabase()
        self.files = FILES()
        # Setting up dummy objects
        self.project1 = Projects('Project A', '1000', 'USA', 'Education', 'Org1')
        self.project2 = Projects('Project B', '2000', 'UK', 'Health', 'Org2')
        self.project3 = Projects('Project C', '1500', 'India', 'Agriculture', 'Org3')

    def test_add_project(self):
        #est if the information inputted has been sucessfully converted to the different attrubites within the Project object
        self.db.add_project(self.project1)
        self.assertIn(self.project1, self.db.projects)
        self.assertEqual(len(self.db.projects), 1)

    def test_list_all_projects(self):
        # Testing out list all projects
        self.db.add_project(self.project1)
        self.db.add_project(self.project2)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout: # Testing if output is correct
            self.db.list_all_projects()
            output = mock_stdout.getvalue().strip()
            self.assertIn('Project A', output)
            self.assertIn('Project B', output)

    def test_search_by_name(self):
        #Test searching for a project by name
        self.db.add_project(self.project1)
        self.db.add_project(self.project2)
        result = self.db.search_for_project_by_name('Project A')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.project1)

    def test_search_by_organization(self):
        #Test searching for projects by organization. """
        self.db.add_project(self.project1)
        result = self.db.search_for_project_by_org('Org1')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.project1)

    def test_modify_project_name(self):
        #Test modifying the project name.
        self.db.add_project(self.project1)
        self.db.modify_project_name(self.project1, 'New Project Name')
        self.assertEqual(self.project1.name, 'New Project Name')

    def test_modify_project_country(self):
        #Test modifying the project country.
        self.db.add_project(self.project1)
        self.db.modify_project_country(self.project1, 'Canada')
        self.assertEqual(self.project1.country, 'Canada')

    def test_export_all_projects(self):
        # Testing out if export is working properly
        self.db.add_project(self.project1)
        self.db.add_project(self.project2)
        filename = 'test_projects.txt'
        self.files.projects = self.db.projects
        self.files.export_all_projects(filename)

        # Check file content
        with open(filename, 'r') as file:
            content = file.read()
            self.assertIn('Project A', content)
            self.assertIn('Project B', content)

        # Clean up the file
        os.remove(filename)

    def test_import_projects(self):
        #Testing Import
        filename = 'import_test_projects.txt'
        with open(filename, 'w') as file:
            file.write("Project name: Project D\n")
            file.write("Total Funding: 5000\n")
            file.write("Organization: Org4\n")
            file.write("Focus Area: Tech\n")
            file.write("Country: Germany\n")

        self.files.import_projects(filename)
        self.assertEqual(len(self.files.projects), 1)
        self.assertEqual(self.files.projects[0].name, 'Project D')

        # Clean up the file
        os.remove(filename)

    def test_export_projects_by_country(self):
       # Testing Summary Report
        self.db.add_project(self.project1)
        self.db.add_project(self.project2)
        self.db.add_project(self.project3)
        filename = 'country_export.txt'
        self.files.projects = self.db.projects
        self.files.export_projects_by_country('India', filename)

        # Check file content
        with open(filename, 'r') as file:
            content = file.read()
            self.assertIn('Project C', content)
            self.assertNotIn('Project A', content)

        # Clean up the file
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
