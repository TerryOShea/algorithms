class Trie:
    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):
        current_node = self.root_node
        is_new_word = False

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        if "*" not in current_node:
            is_new_word = True
            current_node["*"] = {}

        return is_new_word
