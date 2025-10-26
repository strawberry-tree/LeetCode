# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print()
        # 노드가 0개 / 1개인 경우
        if head is None or head.next is None:
            return head
        
        # 가운데 노드 확인
        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # 두 연결리스트 분리
        if prev:
            prev.next = None

        # 처음부터 slow / slow 다음부터로 자르기 
        left = self.sortList(head)
        right = self.sortList(slow)

        # 이미 정렬된 배열의 재정렬
        sentinel = ListNode()
        curr = sentinel
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return sentinel.next