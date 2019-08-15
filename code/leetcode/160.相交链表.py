# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        headA_len = 0
        headB_len = 0
        h_A = None
        h_B = None
        num = 0
        temp = headA
        while temp is not None:
            headA_len+=1
            temp = temp.next
        temp = headB
        while temp is not None:
            headB_len+=1
            temp = temp.next
        if headA_len > headB_len:
            num = headA_len - headB_len
            temp = headA
            while num>0:
                temp = temp.next
                num-=1
            h_A = temp
            h_B = headB
        elif headA_len < headB_len:
            num = headB_len - headA_len
            temp = headB
            while num>0:
                temp = temp.next
                num-=1
            h_B = temp
            h_A = headA
        else:
            h_B = headB
            h_A = headA
            
        temp = None
        while h_B is not None and h_A is not None:
            if h_B != h_A:
                temp = None
            elif temp is None:
                temp = h_B
            h_B = h_B.next
            h_A = h_A.next
        return temp
                