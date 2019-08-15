# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        data_list=[]
        for list in lists:
            while list:
                data_list.append(list.val)
                list=list.next
        data_list.sort()
        head_node = ListNode(0)
        node = head_node
        for data in data_list:
            new_node = ListNode(data)
            node.next = new_node
            node = new_node
        return head_node.next
            
