# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentinel = ListNode()
        curr = sentinel
        queue = []
        counter = 0

        for headNode in lists:
            if headNode:
                heapq.heappush(queue, (headNode.val, counter, headNode))
                counter += 1

        while queue:
            _, _, smallestNode = heapq.heappop(queue)
            if smallestNode.next:
                heapq.heappush(queue, (smallestNode.next.val, counter, smallestNode.next))
                counter += 1
            curr.next = smallestNode
            curr = curr.next
        
        return sentinel.next