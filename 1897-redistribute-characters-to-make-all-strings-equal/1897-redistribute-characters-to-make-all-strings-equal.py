class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = {}
        total_strings = len(words)

        # Count occurrences of each character
        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        # Check if each character count is divisible by the number of strings
        for count in char_count.values():
            if count % total_strings != 0:
                return False

        return True