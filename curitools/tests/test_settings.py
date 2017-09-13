import unittest
import os
from curitools.settings import Settings

class TestSettings(unittest.TestCase):

    def test_create_user(self):
        uritools_dir = os.path.expanduser("~")
        file_settings = os.path.join(uritools_dir, ".uri.settings")
        file_created = open(file_settings, "w")
        file_created.write("Teste")
        file_created.close()
        s = Settings()
        assert file_settings == s.find_settings_file()
        os.remove(file_settings)

    def test_get_user_and_password(self):
        uritools_dir = os.path.expanduser("~")
        file_settings = os.path.join(uritools_dir, ".uri.settings")
        file_created = open(file_settings, "w")
        file_created.write("user: teste@hotmail.com\n")
        file_created.write("password: testando")
        file_created.close()
        s = Settings()
        s.read_settings()
        assert "teste@hotmail.com" == s.user
        assert "testando" == s.password
        os.remove(file_settings)
    
if __name__ == '__main__':
    unittest.main()
