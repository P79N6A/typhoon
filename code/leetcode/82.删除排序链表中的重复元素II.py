# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tile = ListNode(0)
        temp = head
        tile.next = temp
        last_temp = tile
        
        is_eque = False
        while temp and temp.next:
            if temp.val != temp.next.val:
                if is_eque:
                    last_temp.next = temp.next
                else:
                    last_temp = temp
                is_eque = False
            else:
                is_eque = True
            temp = temp.next
        if is_eque:
            last_temp.next = None
        return tile.next