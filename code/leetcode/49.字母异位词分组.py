class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for st in strs:
            li = "".join(sorted(st))
            if li not in dic.keys():
                dic[li] = []
            dic[li].append(st)
        return [dic[x] for x in dic]

a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))