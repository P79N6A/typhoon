def removeNthFromEnd(self, head, n):
	"""
	:type head: ListNode
	:type n: int
	:rtype: ListNode
	"""
	he = ListNode(0)
	he.next = head
	h=he
	h1=he
	num=0
	while h:
		if num<n+1:num+=1
		else:h1=h1.next
		h=h.next
	if h1.next:h1.next= h1.next.next
	
	return he.next