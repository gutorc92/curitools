import unittest
from curitools.curitools import uri
import click
from click.testing import CliRunner

class TestUri(unittest.TestCase):

    def print_tabela_submissions(self):
        runner = CliRunner()
        result = runner.invoke(uri, ['-r'])
        assert result.exit_code == 0
    
    
if __name__ == '__main__':
    unittest.main()
