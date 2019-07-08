import unittest
from SampleProjects.Examples import Example

class MyTestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("This will run once before all the methods")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This will run once after all the methods")

    def setUp(self) -> None:
        print("This will run before every method")

    def tearDown(self) -> None:
        print("this will run after every method")


    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result,30)
    def test_sum(self):
         result = Example.sub(self,40,10)
         self.assertEqual(result,30)

if __name__ == '__main__':
    unittest.main()
