# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
      if head == None or head.next == None:
            return

        pre = head
        lat = head.next
        while lat != None and lat.next != None:
            pre = pre.next
            lat = lat.next.next

        p = pre.next
        pre.next = None
        # reverse

        cur = None        
        while p != None:
            q = p.next
            p.next = cur
            cur = p 
            p = q

        pre = head
        while pre != None and cur != None:
            tmp = cur.next  
            cur.next = pre.next
            pre.next = cur
            pre = pre.next.next
            cur = tmp 
            
a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
# e = ListNode(5)
# d.next = e



g = Solution()
g = g.reorderList(a)

print(g.val)
print(g.next.val)
print(g.next.next.val)
print(g.next.next.next.val)
# print(g.next.next.next.next.val)


        
            
        
        
        