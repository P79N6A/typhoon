class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lists = []
        lis=[]
        id=0
        candidates.sort()
        self.help(id, lis, lists, candidates, target)
        return lists

    def help(self, id, lis, lists, candidates, target):
        if sum(lis) + candidates[id] > target or id<len(candidates):
            return
        elif sum(lis) + candidates[id] == target:
            if (lis + [candidates[id]]) not in lists:
                lists.append(lis + [candidates[id]])
            return
        else:
            self.help(id+1, lis + [candidates[id]], lists, candidates, target)
            self.help(id+1, lis, lists, candidates, target)
    
a = Solution()
print(a.combinationSum2([2,5,2,1,2], 5))