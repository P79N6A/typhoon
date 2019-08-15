class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        results = []
        temps = []
        is_read = []
        for i in range(len(S)-1, -1, -1):
            if S[i] not in is_read:
                is_read.append(S[i])
                start = S.find(S[i])
                temps.append([start, i])
        temps = sorted(temps, key=lambda x: (x[0], -x[1]))
        start = 0
        end = -1
        for temp in temps:
            if temp[0] > end:
                results.append(end - start + 1)
                start = temp[0]
                end = temp[1]
            else:
                end = max(end, temp[1])
        results.append(end - start + 1)
        return results[1:]

b = "ababcbacadefegdehijhklij"
a = Solution()
print(a.partitionLabels(b))