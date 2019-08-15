"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def digui(self, head):
        temp = head
        while temp:
            if temp.child:
                last = self.digui(temp.child)

                last.next = temp.next

                temp.next = temp.child
                temp.child.prev = temp

                temp.child = None
                if last.next is None:
                    return last
                else:
                    temp = last.next
                    temp.prev = last
            else:
                if temp.next is None:
                    return temp
                else:
                    temp = temp.next
           
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.digui(head)
        return head
