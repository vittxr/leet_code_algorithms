# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def storeNode(self, node, string="") -> str:
        s = str(node.val) + string
        if not node.next:
            return s

        return self.storeNode(node.next, s)

    def lst_to_linked_lst(self, lst) -> ListNode:
        currentNode = initialNode = ListNode(0)
        for e in lst:
            currentNode.next = ListNode(e)
            currentNode = currentNode.next
        return initialNode.next

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1 = self.storeNode(l1)
        n2 = self.storeNode(l2)

        sum_lst = reversed(list(str(int(n1) + int(n2))))
        return self.lst_to_linked_lst(sum_lst)
