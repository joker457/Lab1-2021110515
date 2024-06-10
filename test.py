import unittest
import io
from main import find_shortest_path

class TestFindShortestPath(unittest.TestCase):

    # 测试图中存在最短路径的情况
    def test_shortest_path_exists(self):
        graph = {'A': {'B': 1, 'C': 2}, 'B': {'D': 3}, 'C': {'D': 1}, 'D': {}}
        start_word = 'A'
        end_word = 'D'
        expected_output = "Shortest path from A to D is: A→C→D with length 3\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            find_shortest_path(graph, start_word, end_word)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # 测试图中不存在最短路径的情况
    def test_shortest_path_not_exists(self):
        graph = {'A': {'B': 1}, 'B': {'C': 2}, 'C': {}, 'D': {}}
        start_word = 'A'
        end_word = 'D'
        expected_output = "No word1 or word2 in the graph!\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            find_shortest_path(graph, start_word, end_word)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # 测试 end_word 为 None，图中存在最短路径的情况
    def test_end_word_none_shortest_path_exists(self):
        graph = {'A': {'B': 1, 'C': 2}, 'B': {'D': 3}, 'C': {'D': 1}, 'D': {}}
        start_word = 'A'
        expected_output = "Shortest path from A to B is: A→B with length 1\n" \
                          "Shortest path from A to C is: A→C with length 2\n" \
                          "Shortest path from A to D is: A→C→D with length 3\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            find_shortest_path(graph, start_word)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # 测试 start_word 不在图中的情况
    def test_start_word_not_in_graph(self):
        graph = {'A': {'B': 1}, 'B': {'C': 2}, 'C': {}, 'D': {}}
        start_word = 'E'
        expected_output = "No word1 in the graph!\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            find_shortest_path(graph, start_word)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    # 测试 start_word 和 end_word 都不在图中的情况
    def test_start_end_word_not_in_graph(self):
        graph = {'A': {'B': 1}, 'B': {'C': 2}, 'C': {}, 'D': {}}
        start_word = 'E'
        end_word = 'F'
        expected_output = "No word1 or word2 in the graph!\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            find_shortest_path(graph, start_word, end_word)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
