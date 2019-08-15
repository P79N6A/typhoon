# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        temp1 = head
        temp2 = head.next
        temp = None
        while temp2 and temp2.next:
            if temp1 != temp2:
                temp1 = temp1.next
                temp2 = temp2.next.next
            else:
                temp = temp1
                break
        if temp is None:
            return temp
        one = head 
        while one:   
            te = temp.next
            while True:
                if one == te:
                    return one
                if te == temp:
                    break
                te = te.next
            one = one.next