class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min = 99999
        min_name = ""
        dices={}
        results = [] 
        for i, li in enumerate(list1):
            dices[li] = i
        for i ,li in enumerate(list2):
            if li in dices.keys():
                if min > dices[li] + i:
                    results.clear()
                    min = dices[li] + i
                    min_name = li
                    results.append(li)
                elif min == dices[li] + i:
                    results.append(li)
        return results