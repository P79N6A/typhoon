class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domains = {}
        for cpdomain in cpdomains:
            num, name = cpdomain.split(' ')
            num = int(num)
            while True:
                if name not in domains.keys():
                    domains[name] = num
                else:
                    domains[name] += num
                index = name.find('.')
                if index != -1:
                    name = name[index+1:]
                else:
                    break
        return [ str(value) + " " + key for key,value in domains.items()]

a = Solution()
cpdomains = ["9001 discuss.leetcode.com"]
print(a.subdomainVisits(cpdomains))