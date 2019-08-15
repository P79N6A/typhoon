class Solution(object):
    def combinationSum(self, candidates, target):
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
        for i in range(id, len(candidates),1):
            if sum(lis) + candidates[i] > target:
                break
            elif sum(lis) + candidates[i] == target:
                lists.append(lis + [candidates[i]])
                break
            else:
                self.help(i, lis + [candidates[i]], lists, candidates, target)
    
a = Solution()
print(a.combinationSum([2,3,6,7], 7))