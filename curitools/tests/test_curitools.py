import unittest
from curitools.curitools import uri
import click
from click.testing import CliRunner

class TestUri(unittest.TestCase):

    def test_print_tabela_submissions(self):
        runner = CliRunner()
        result = runner.invoke(uri, ['-r'])
        print(result.output)
        assert result.exit_code == 0
    
if __name__ == '__main__':
    unittest.main()
