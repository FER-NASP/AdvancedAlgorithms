import unittest
from Trie import Trie
from PatriciaTree import PatriciaTree

class SimpleStringCases(unittest.TestCase):
    def test_Trie(self):
        t=Trie()
        t.insert("dado")
        t.insert("da")
        t.insert("dalibor")
        t.insert("ana")
        t.remove("dado")
        self.assertTrue(t.search('dado'))

    def test_PatriciaTree1(self):
        pt=PatriciaTree()
        pt.insert("analisys")
        pt.insert("acronym")
        b1=pt.search('ana')
        pt.insert("analogy")
        pt.insert("acrobat")
        pt.insert("ana")
        self.assertTrue(not b1 and pt.search('ana'))

    def test_PatriciaTree2(self):
        pt=PatriciaTree()
        pt.insert("analisys")
        pt.insert("acronym")
        pt.insert("analogy")
        pt.insert("acrobat")
        pt.insert("ana")
        pt.remove('analisys')
        pt.remove('analogy')
        pt.remove('ana')
        pt.remove('acronym')
        pt.remove('acrobat')
        self.assertTrue(not pt.search('analisys'))

if __name__ == '__main__':
    unittest.main()
