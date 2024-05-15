import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import random
#B1
def process_text_file(file_path):
    # 读取文本文件
    with open(file_path, 'r') as file:
        text = file.read()

    # 用空格替换换行符和回车符
    text = text.replace('\n', ' ').replace('\r', ' ')
    
    # 使用正则表达式将非字母字符替换为空格
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # 将多个空格替换为单个空格
    text = re.sub(r'\s+', ' ', text)

    # 将文本转换为小写
    text = text.lower()

    return text

def construct_graph(text):
    graph = defaultdict(dict)
    words = text.split()
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        if word2 not in graph[word1]:
            graph[word1][word2] = 1
        else:
            graph[word1][word2] += 1
    return graph

def draw_graph(graph, path=None):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)  # 设置节点位置
    if path:
        path_edges = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        edge_colors = ['red' if edge in path_edges else 'black' for edge in G.edges()]
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True, edge_color=edge_colors)
    else:
        nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def find_bridge_words(graph, word1, word2):
    if word1 not in graph or word2 not in graph:
        return []

    bridge_words = []
    for word in graph[word1]:
        if word in graph and word2 in graph[word]:
            bridge_words.append(word)

    return bridge_words

def insert_bridge_words(new_text, graph):
    words = new_text.split()
    result_text = []
    for i in range(len(words)-1):
        result_text.append(words[i])
        word1 = words[i]
        word2 = words[i+1]
        bridge_words = find_bridge_words(graph, word1, word2)
        if bridge_words:
            result_text.append(bridge_words[0])  # 插入第一个找到的桥接词
    result_text.append(words[-1])
    return ' '.join(result_text)

def find_shortest_path(graph, start_word, end_word=None):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    if end_word:
        if start_word not in G or end_word not in G:
            print("No word1 or word2 in the graph!")
            return
        try:
            path = nx.dijkstra_path(G, source=start_word, target=end_word, weight='weight')
            length = nx.dijkstra_path_length(G, source=start_word, target=end_word, weight='weight')
            print("Shortest path from {} to {} is: {} with length {}".format(start_word, end_word, '→'.join(path), length))
            draw_graph(graph, path)
        except nx.NetworkXNoPath:
            print("No path found from {} to {}!".format(start_word, end_word))
    else:
        if start_word not in G:
            print("No word1 in the graph!")
            return
        paths = nx.single_source_dijkstra_path(G, source=start_word, weight='weight')
        lengths = nx.single_source_dijkstra_path_length(G, source=start_word, weight='weight')
        for target in paths:
            if target != start_word:
                print("Shortest path from {} to {} is: {} with length {}".format(start_word, target, '→'.join(paths[target]), lengths[target]))

def random_traversal(graph):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    start_node = random.choice(list(G.nodes))
    current_node = start_node
    visited_edges = set()
    traversal_path = [current_node]

    print("Starting random traversal from:", start_node)
    while True:
        neighbors = list(G.neighbors(current_node))
        if not neighbors:
            print("No more outgoing edges from", current_node)
            break
        next_node = random.choice(neighbors)
        edge = (current_node, next_node)
        if edge in visited_edges:
            print("Encountered a repeated edge:", edge)
            break
        visited_edges.add(edge)
        traversal_path.append(next_node)
        current_node = next_node

        stop = input("Press 's' to stop traversal or any other key to continue: ").lower()
        if stop == 's':
            print("Traversal stopped by user.")
            break

    traversal_text = ' '.join(traversal_path)
    print("Traversal path:", traversal_text)

    # 将遍历路径写入文件
    with open('traversal_path.txt', 'w') as file:
        file.write(traversal_text)

def main():
    file_path = 'input.txt'  # 替换为你的文件路径
    processed_text = process_text_file(file_path)
    graph = construct_graph(processed_text)

    while True:
        print("\nSelect an option:")
        print("1. Draw directed graph")
        print("2. Find bridge words")
        print("3. Insert bridge words into new text")
        print("4. Find shortest path")
        print("5. Random traversal")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            draw_graph(graph)
        elif choice == '2':
            word1 = input("Enter word1: ").lower()
            word2 = input("Enter word2: ").lower()
            bridge_words = find_bridge_words(graph, word1, word2)
            if bridge_words:
                print("The bridge words from {} to {} are: {}.".format(word1, word2, ", ".join(bridge_words)))
            else:
                print("No bridge words from {} to {}!".format(word1, word2))
        elif choice == '3':
            new_text = input("Enter new text: ").lower()
            new_text_with_bridge_words = insert_bridge_words(new_text, graph)
            print("New text with bridge words inserted:")
            print(new_text_with_bridge_words)
        elif choice == '4':
            word1 = input("Enter word1: ").lower()
            word2 = input("Enter word2 (or leave blank for single source shortest path): ").lower()
            if word2:
                find_shortest_path(graph, word1, word2)
            else:
                find_shortest_path(graph, word1)
        elif choice == '5':
            random_traversal(graph)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
