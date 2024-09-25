# Importing Unittest Module
import unittest
# Importing Backend Parts from Orginal Project
from A1 import Projects, ProjectDatabase

# Testing the Projects Class
class TestProjects(unittest.TestCase):
    
    # Creating Dummy Variable
    def setUp(self):
        # This method will be called before each test - think of this as a __init__ function
        # No ned for a self.db function as there is no functions in Projects
        # This creates a new Projects Object i.e a new project is created by the user
        self.project = Projects(name="test1", tFunding="Classified", country="Bangladesh", fArea="Health", org="LWFB")
    
    def test_project_init(self):
        # Test if the information inputted has been sucessfully converted to the different attrubites within the Project object 
        self.assertEqual(self.project.name, "test1")
        self.assertEqual(self.project.tFunding, "Classified")
        self.assertEqual(self.project.country, "Bangladesh")
        self.assertEqual(self.project.fArea, "Health")
        self.assertEqual(self.project.org, "LWFB")
    
    def test_project_str(self):
        # Test the string representation of a Projects object as defined in the main code
        expected_str = "\nProject name: test1\nTotal Funding: Classified\nOrganization: LWFB\nFocus Area: Health\nCountry: Bangladesh\n"
        self.assertEqual(str(self.project), expected_str)

# Testing the ProjectDatabase Class
class TestProjectDatabase(unittest.TestCase):
    def setUp(self):
        # Sets up the two objects to be used for testing i.e a user creates 2 new project objects
        # This self.db function allows for the different functions in ProjectDatabase to be used
        self.db = ProjectDatabase()
        self.project1 = Projects(name="test1", tFunding="Classified", country="Bangladesh", fArea="Health", org="LWFB")
        self.project2 = Projects(name="test2", tFunding="2000000", country="Australia", fArea="Education", org="LFWA")
        self.db.create_new_project(self.project1)
        self.db.create_new_project(self.project2)

    def test_create_new_project(self):
        # Test if new projects are correctly added to the database as intended
        self.assertIn(self.project1, self.db.allProjects)
        self.assertIn(self.project2, self.db.allProjects)

    def test_search_for_project_by_name(self):
        # Test searching for a project by name
        results = self.db.search_for_project_by_name("test1")
        self.assertIn(self.project1, results)
        self.assertNotIn(self.project2, results)
    
    def test_search_for_project_by_country(self):
        # Test searching for a project by country works is working intended i.e Australia would only return the second object
        results = self.db.search_for_project_by_country("Australia")
        self.assertIn(self.project2, results)
        self.assertNotIn(self.project1, results)
    
    def test_search_for_project_by_org(self):
        # Test searching for a project by organization i.e LWFB returns only the first object
        results = self.db.search_for_project_by_org("LWFB")
        self.assertIn(self.project1, results)
        self.assertNotIn(self.project2, results)
    
    def test_search_for_project_by_fArea(self):
        # Test searching for a project by focus area i.e Health input only returns first object
        results = self.db.search_for_project_by_fArea("Health")
        self.assertIn(self.project1, results)
        self.assertNotIn(self.project2, results)
    
    def test_modify_project_name(self):
        # Test modifying a project's name and is saved properly
        self.db.modify_project_name(self.project1, "Test1")
        self.assertEqual(self.project1.name, "Test1")
    
    def test_modify_project_org(self):
        # Test modifying a project's organization and is saved properly
        self.db.modify_project_org(self.project1, "Let's work for Bangladesh")
        self.assertEqual(self.project1.org, "Let's work for Bangladesh")
    
    def test_modify_project_country(self):
        # Test modifying a project's country and is save properly
        self.db.modify_project_country(self.project1, "Bangladesh/India")
        self.assertEqual(self.project1.country, "Bangladesh/India")
    
    def test_modify_project_fArea(self):
        # Test modifying a project's focus area and is saved properly
        self.db.modify_project_fArea(self.project1, "Technology")
        self.assertEqual(self.project1.fArea, "Technology")
    
    def test_modify_project_tFunding(self):
        # Test modifying a project's total funding and is saved properly
        self.db.modify_project_tFunding(self.project1, "1500000")
        self.assertEqual(self.project1.tFunding, "1500000")

# Runs the Program
if __name__ == '__main__':
    unittest.main()

