class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dict = {}
        for group in prerequisites:
            dict[group[0]] = group[1]
        results = list(set([i for i in range(numCourses)]) - set(dict.keys()))
        i=0
        while i < numCourses:
            for key in dict.keys():
                if dict[key] in results and key not in results:
                    print dict[key], results
                    results.append(key)
            i += 1
        if len(results) == numCourses:
            return True
        else:
            return False


a = Solution()
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print a.canFinish(numCourses, prerequisites)
