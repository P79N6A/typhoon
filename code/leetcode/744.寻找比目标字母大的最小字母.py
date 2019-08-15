class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # max_char = max(letters)
        # higt = letters.find(max_char)
        high = len(letters)-1
        low = 0
        while low <= high:
            mid = low+(high-low)//2
            if letters[mid] > target:
                high = mid-1
            else:
                low = mid+1
        if low < len(letters):
            return letters[low]
        return letters[0]