from typing import Dict


# class TrieNode:
#     """ A node in the trie structure """
#     def __init__(self):
#         self.children = [None] * 26  # Array to hold 26 lowercase alphabet characters
#         self.is_end_of_word = False   # Flag to check the end of a word
#
#
# class WordDictionary:
#     """ Class to implement a word dictionary using a trie """
#
#     def __init__(self):
#         """ Initializes the word dictionary with a root trie node """
#         self.root = TrieNode()
#
#     def addWord(self, word: str) -> None:
#         """ Adds a word into the dictionary """
#         node = self.root
#         for char in word:
#             index = ord(char) - ord('a')  # Calculate the index for the relevant character
#             # If the current character path does not exist, create a new node
#             if node.children[index] is None:
#                 node.children[index] = TrieNode()
#             node = node.children[index]
#         node.is_end_of_word = True  # Mark the end of a word
#
#     def search(self, word: str) -> bool:
#         """ Searches the dictionary for a word, can contain "." as a wildcard character """
#         def dfs(index, node):
#             """
#             Depth-First Search helper function to recursively search
#             for the word in the trie
#             """
#             for i in range(index, len(word)):
#                 char = word[i]
#                 char_index = ord(char) - ord('a')
#                 # If the current character is a wildcard
#                 if char == '.':
#                     # Check all possible child paths
#                     return any(child is not None and dfs(i + 1, child) for child in node.children.value)
#                 elif node.children[char_index] is None:
#                     # Character path doesn't exist
#                     return False
#                 # Move on to the next trie node
#                 node = node.children[char_index]
#             return node.is_end_of_word  # Check if it's the end of a word
#
#         return dfs(0, self.root)  # Start the depth-first search from the root


class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = {}
    self.isWord = False


class WordDictionary:
  def __init__(self):
    self.root = TrieNode()

  def addWord(self, word: str) -> None:
    node: TrieNode = self.root
    for c in word:
      node = node.children.setdefault(c, TrieNode())
    node.isWord = True

  def search(self, word: str) -> bool:
    return self._dfs(word, 0, self.root)

  def _dfs(self, word: str, s: int, node: TrieNode) -> bool:
    if s == len(word):
      return node.isWord
    if word[s] != '.':
      child = node.children.get(word[s], None)
      return self._dfs(word, s + 1, child) if child else False
    return any(self._dfs(word, s + 1, child) for child in node.children.values())

# Your WordDictionary object will be instantiated and called as such:
word = "bad"
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search("bad2")
print(param_2)