import unittest
from main import find_bridge_words

class TestValidInputWithBridgeWords(unittest.TestCase):

    def test_valid_input_with_bridge_words(self):
        # Define a sample graph
        graph = {'word1': {'bridge_word': 1}, 'bridge_word': {'word2': 1}, 'word2': {}}
        word1 = 'word1'
        word2 = 'word2'
        
        # Execute the function under test
        actual = find_bridge_words(graph, word1, word2)
        
        # Define the expected output
        expected = ['bridge_word']
        
        # Compare actual output with expected output
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
