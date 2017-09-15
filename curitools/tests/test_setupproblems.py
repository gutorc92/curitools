import unittest
from curitools.setup_problems import SetupProblem 
import os
from shutil import rmtree

class TestSetupProblem(unittest.TestCase):


    def setUp(self):
        cwd = os.getcwd()
        template_dir = os.path.dirname(os.path.realpath(__file__))
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.template_dir = os.path.join(template_dir,"..", "templates")
        self.setup = SetupProblem("1006", cwd, self.template_dir, "c++")
         
    def test_hasmakefiles(self):
        self.assertTrue(self.setup.has_makefile())
        self.setup = SetupProblem("1010", os.getcwd(), self.template_dir, "python")
        self.assertFalse(self.setup.has_makefile())
        self.setup = SetupProblem("1010", os.getcwd(), self.template_dir, "c")
        self.assertFalse(self.setup.has_makefile())
        

    def test_get_base_template(self):
        base_file = os.path.join(self.template_dir, "base.cpp")
        self.assertEqual(base_file, self.setup.get_base_template())
    
    def test_get_makefile_template(self):
        makefile = os.path.join(self.template_dir, "Makefile.c++")
        self.assertEqual(makefile, self.setup.get_makefile_template())

    def test_create_makefile(self):
        self.setup.create_makefile(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir,"Makefile"))) 
        os.remove(os.path.join(self.test_dir,"Makefile"))

    def test_create_files(self):
        self.setup = SetupProblem("1006", self.test_dir, self.template_dir, "c++")
        self.setup.create_files()
        self.assertTrue(os.path.exists(os.path.join(self.test_dir,"1006"))) 
        self.assertTrue(os.path.exists(os.path.join(self.test_dir,"1006", "1006.cpp"))) 
        self.assertTrue(os.path.exists(os.path.join(self.test_dir,"1006", "Makefile"))) 
        rmtree(os.path.join(self.test_dir,"1006"))
        self.setup = SetupProblem("1010", os.path.join(self.test_dir, "test_settings.py"), self.template_dir, "c++")
        self.assertRaises(NotADirectoryError, self.setup.create_files)

    def test_create_base_files(self):
        self.setup.create_base_files(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir,"1006.cpp"))) 
        os.remove(os.path.join(self.test_dir,"1006.cpp"))   
        self.setup = SetupProblem("1010", os.getcwd(), os.path.join(self.template_dir, ".."), "c++")
        self.assertRaises(FileExistsError, self.setup.create_base_files, self.test_dir)

if __name__ == '__main__':
    unittest.main()
