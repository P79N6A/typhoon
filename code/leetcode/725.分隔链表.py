# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        len_num = 0
        temp = root
        while temp:
            len_num += 1
            temp = temp.next
        group = int(len_num / k)
        add_1 = len_num % k
        list_node = []
        temp = root
        for i in range(k):
            head = temp
            group_num = group
            if i < add_1:
                group_num += 1
            while group_num > 0:
                group_num-=1
                if temp:
                    next_temp = temp.next
                    if group_num == 0:
                        temp.next = None 
                    temp = next_temp 
            list_node.append(head)
        return list_node
