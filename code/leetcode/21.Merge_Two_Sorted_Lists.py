def mergeTwoLists(self, l1, l2):
	"""
	:type l1: ListNode
	:type l2: ListNode
	:rtype: ListNode
	"""
	l3 = ListNode(0)
	l4 = l3
	while True:
		if l1 and l2:
			if l1.val > l2.val:
				l5 = ListNode(l2.val)
				l2 = l2.next
			else:
				l5 = ListNode(l1.val)
				l1 = l1.next
		elif l1:
			l5 = ListNode(l1.val)
			l1 = l1.next
		elif l2:
			l5 = ListNode(l2.val)
			l2 = l2.next
		else:return l3.next
		l4.next = l5
		l4 = l5
	return l3.next
		
		