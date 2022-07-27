import unittest
from Trie import Trie

class SimpleStringCases(unittest.TestCase):
    def test_Trie(self):
        t=Trie()
        t.insert("dado")
        t.insert("da")
        t.insert("dalibor")
        t.insert("ana")
        t.remove("dado")
        self.assertTrue(t.search("da"))

if __name__ == '__main__':
    unittest.main()
