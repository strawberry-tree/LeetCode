# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import copy

class Solution(object):
    def insertionSortList(self, head):
        insert = ListNode(float("-inf"))
        insert.next = copy(head)
        insert.next.next = None

        head = head.next

        while head:
            curr = insert
            in_node = copy(head)

            while curr and curr.next and in_node.val > curr.next.val:
                curr = curr.next
            in_node.next, curr.next = curr.next, in_node

            head = head.next

        return insert.next