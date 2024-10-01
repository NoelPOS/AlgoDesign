import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    huffman_tree = heapq.heappop(heap)
    huffman_codes = {}

    def generate_codes(node, current_code=""):
        if node:
            if node.char:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(huffman_tree)
    return huffman_codes

frequencies = defaultdict(int, {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45})
codes = huffman_encoding(frequencies)
print(f"Huffman Codes: {codes}")
