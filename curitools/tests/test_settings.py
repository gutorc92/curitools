import unittest
from curitools.settings import Settings

class TestSettings(unittest.TestCase):

    def test_create_user(self):
        s = Settings()
        s.find_settings_file()

    
if __name__ == '__main__':
    unittest.main()
