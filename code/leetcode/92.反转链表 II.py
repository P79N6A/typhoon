class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i=1
        temp = head
        last_temp = None
        last = None
        r = None
        while temp:
            temp_next = temp.next
            if m==i:
                last = last_temp
                r = temp
            if m <= i and i <= n:
                temp.next = last_temp
            if i == n:
                if last:
                    last.next = temp
                else:
                    head = temp
                r.next = temp_next
                return head
            last_temp = temp
            temp = temp_next 
            i+=1
            print(i)