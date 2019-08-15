# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tile = ListNode(0)
        tile.next = head
        temp2 = head
        while temp2 and temp2.next:
            temp1 = tile
            temp = temp2.next
            is_change = False
            while temp1.next and temp1 != temp2:
                if temp1.next.val > temp.val:
                    temp2.next = temp.next
                    temp.next = temp1.next
                    temp1.next = temp
                    is_change = True
                    break
                else:
                    temp1 = temp1.next
            if is_change is False:
                temp2 = temp2.next
        return tile.next