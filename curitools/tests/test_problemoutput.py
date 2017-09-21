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
        s.print_table()
        self.assertEqual(s.get_title(), "Número Ímpares")
        self.assertEqual(s.get_input(), "O arquivo de entrada contém 1 valor inteiro qualquer.")
        self.assertEqual(s.get_output(), "Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.")


    
if __name__ == '__main__':
    unittest.main()
