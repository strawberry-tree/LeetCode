# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 맨 끝인 경우 / 1개만 남은경우
        if not head or not head.next:
            return head
        
        # 2개씩 노드 분석 -> 더 뒤에 있는 노드
        laterNode = head.next

        # 뒷노드는 앞노드를 가리키고, 앞노드는 그 다음 두 노드의 결과값을 반환
        laterNode.next, head.next = head, self.swapPairs(laterNode.next)
        return laterNode
