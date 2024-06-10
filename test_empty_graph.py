import unittest
from main import find_bridge_words

class TestEmptyGraph(unittest.TestCase):

    def test_empty_graph(self):
        # Define an empty graph
        graph = {}
        word1 = 'word1'
        word2 = 'word2'
        
        # Execute the function under test
        actual = find_bridge_words(graph, word1, word2)
        
        # Define the expected output
        expected = []
        
        # Compare actual output with expected output
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
