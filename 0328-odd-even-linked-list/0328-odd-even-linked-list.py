# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        # 짝수노드 배치용 샌티넬
        evenHead = ListNode()

        # curr은 무조건 홀수번째 노드
        while curr:
            if not curr.next:
                prev = curr
                break
            
            evenOut = curr.next
            curr.next = curr.next.next

            if curr.next is None:
                prev = curr
            curr = curr.next
            
        
            evenCurr = evenHead
            while evenCurr and evenCurr.next:
                evenCurr = evenCurr.next
            evenCurr.next = evenOut
            evenOut.next = None #!!

        if prev:
            prev.next = evenHead.next
        
        return head

        



            
            
            