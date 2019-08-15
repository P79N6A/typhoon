class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_list = []
        char_str = {'a':2,
                    'b':3,
                    'c':3,
                    'd':2,
                    'e':1,
                    'f':2,
                    'g':2,
                    'h':2,
                    'i':1,
                    'j':2,
                    'k':2,
                    'l':2,
                    'm':3,
                    'n':3,
                    'o':1,
                    'p':1,
                    'q':1,
                    'r':1,
                    's':2,
                    't':1,
                    'u':1,
                    'v':3,
                    'w':1,
                    'x':3,
                    'y':1,
                    'z':3}
        for word in words:
            len_word = len(word) 
            word_lower = word.lower()
            for i in range(len_word):
                if i < len_word-1 and char_str[word_lower[i]] != char_str[word_lower[i+1]]:
                    break
                if i == len_word-1:
                    word_list.append(word)
        return word_list

a = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"] 
print(a.findWords(words))