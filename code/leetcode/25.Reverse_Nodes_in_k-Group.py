class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def reverseKGroup(head, k):
	"""
	:type head: ListNode
	:type k: int
	:rtype: ListNode
	"""
	h1=head
	h2=head
	num=0
	li=[]
	while h1:
		if num==k:
			for i in range(num-1, -1, -1):
				h2.val=li[i]
				h2=h2.next
			num=0
			li.clear()
		li.append(h1.val)
		print(num)
		num+=1
		h1=h1.next
	return head
	
head = ListNode(1)
h=head
h.next=ListNode(2)
h=h.next
h.next=ListNode(3)
h=h.next
h.next=ListNode(4)
h=h.next
h.next=ListNode(5)

reverseKGroup(head, 2)
