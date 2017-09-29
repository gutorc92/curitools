import unittest
from curitools.views.academic import AcademicView
import os

class TestSubmissionsPage(unittest.TestCase):


    def test_extract_table(self):
        repositorio_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(repositorio_dir, "academicView.html")
        fn = open(file_name, 'r')
        text = fn.read()
        fn.close()
        s = AcademicView(text)
        s.extract_table()
        s.get_max_length()
        self.assertEqual(len(s.max_column), 2)
        s.print_table()
        self.assertEqual(len(s.data), 2)

    
if __name__ == '__main__':
    unittest.main()
