import unittest
from soraman import auth

class GlobalAuthTest(unittest.TestCase):

    def test_auth(self):
        soraman = auth.global_soraman()

        soraman.auth()

if __name__ == "__main__":
    unittest.main()
