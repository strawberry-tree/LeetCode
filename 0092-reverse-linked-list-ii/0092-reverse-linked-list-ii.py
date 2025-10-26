# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        curr = head
        prev = sentinel
        curr_idx = 1
        
        while curr_idx < left:
            curr = curr.next
            prev = prev.next
            curr_idx += 1


        # reverse 시작 지점
        beforeReverse = prev
        endOfReverse = curr
        curr = curr.next
        prev = prev.next

        # 모두 뒤집기

        for _ in range(right - left):
            nextNode = curr.next
            curr.next = prev 
            prev, curr = curr, nextNode

        # 연결짓기
        beforeReverse.next = prev
        endOfReverse.next = curr

        return sentinel.next
        



    
        