class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = defaultdict(int)
        word_t = defaultdict(int)

        for letter in s:
            word_s[letter] += 1

        for letter in t:
            word_t[letter] += 1

        return word_s == word_t