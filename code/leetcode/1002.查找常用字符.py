class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        results = {}
        tagers = {}
        for char in list(A[0]):
            if char not in results.keys():
                results[char] = 0
            results[char] += 1
        for a in A:
            tagers.clear()
            for char in list(a):
                if char not in tagers.keys():
                    tagers[char] = 0
                tagers[char] += 1
            for key in results.keys():
                if key in tagers.keys() and results[key] != 0:
                    results[key] = min(results[key], tagers[key])
                else:
                    results[key] = 0
        result = []
        for key, value in results.items():
            result += [key for _ in range(value)]
        return result

a = Solution()
A = ["cool","lock","cook"]
print(a.commonChars(A))