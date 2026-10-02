import unittest
from main import to_upper


class Mytestcase(unittest.TestCase):
    def test_to_upper(self):
        name="Gaurav"
        upper_name=to_upper(name)
        self.assertEqual(upper_name,"GAURAV")


if __name__=="__main__":
    unittest.main()
