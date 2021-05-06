import unittest
from soraman import auth

class AuthTest(unittest.TestCase):

    def test_auth(self):
        soraman = auth.soraman()

        soraman.auth()

if __name__ == "__main__":
    unittest.main()
