import unittest
from curitools.setup_problems import SetupProblem 
import os

class TestSetupProblem(unittest.TestCase):


    def setUp(self):
        cwd = os.getcwd()
        template_dir = os.path.dirname(os.path.realpath(__file__))
        self.template_dir = os.path.join(template_dir, "templates")
        print(self.template_dir)
        self.setup = SetupProblem("1010", cwd, self.template_dir, "c++")
         
    def test_hasmakefiles(self):
        self.assertTrue(self.setup.has_makefile())

    def test_get_base_template(self):
        base_file = os.path.join(self.template_dir, "base.cpp")
        self.assertEqual(base_file, self.setup.get_base_template())
    
    def test_get_makefile_template(self):
        makefile = os.path.join(self.template_dir, "Makefile.c++")
        self.assertEqual(makefile, self.setup.get_makefile_template())

if __name__ == '__main__':
    unittest.main()
