class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = {}
        word_t = {}
        for letter in s:
            if letter not in word_s:
                word_s[letter] = 0
            word_s[letter] += 1
        for letter in t:
            if letter not in word_t:
                word_t[letter] = 0
            word_t[letter] += 1
        print(str(word_t) + "\n" + str(word_s))
        return word_s == word_t