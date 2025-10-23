# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 순회용 포인터
        curr1 = list1   # list1
        curr2 = list2   # list2
        curr3 = None    # 최종

        # 최종리스트의 머리
        answer = None
        if curr1 and curr2:
            if curr1.val <= curr2.val:
                answer = curr1
                curr1 = curr1.next
        
            else:
                answer = curr2
                curr2 = curr2.next

        # 1번리스트만 존재
        elif curr1:
            return curr1

        # 2번리스트만 존재
        elif curr2:
            return curr2

        curr3 = answer
        while curr1 and curr2:
            # 양쪽 중 더 작은 값
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
        
        if curr1:
            curr3.next = curr1
        if curr2:
            curr3.next = curr2

        return answer