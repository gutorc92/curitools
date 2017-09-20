import unittest
from curitools.status import ProblemOutput
import os

class TestSubmissionsPage(unittest.TestCase):


    def test_extract_table(self):
        repositorio_dir = os.path.dirname(os.path.realpath(__file__))
        file_name = os.path.join(repositorio_dir, "problemview.html")
        fn = open(file_name, 'r')
        text = fn.read()
        fn.close()
        s = ProblemOutput(text)
        s.extract_table()
        s.print_table()
        self.assertEqual(len(s.max_column), 6)

        self.assertEqual(len(s.table), 22)

    
if __name__ == '__main__':
    unittest.main()
