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

    def test_submission(self):
        try:
            login = rp.LoginPage(user=user, password=password)
            login.run()
        except HTTPError:
            sys.exit()
    
        sub = rp.SubmissionPage(login.get_session(),"1010","./1010.cpp")
        assert sub.run() == True
    
if __name__ == '__main__':
    unittest.main()
