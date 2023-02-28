
class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newList = ListNode()
        current = newList
        carry = 0
        while l1 or l2 or carry:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            carry = value // 10
            value = value % 10
            current.next = ListNode(value)
            current = current.next
        return newList.next
