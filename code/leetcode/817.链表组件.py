# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        num = 0
        temp = head
        is_component = False
        while temp:
            if temp.val in G:
                if is_component is False:
                    num+=1
                    is_component = True
            else:
                is_component = False
            temp = temp.next
        return num