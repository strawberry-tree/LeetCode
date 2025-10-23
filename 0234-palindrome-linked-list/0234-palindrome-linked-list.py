# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 꼬리노드 찾기
        curr = head
        length = 0
        prev = None
        while curr:
            length += 1
            curr.prev = prev
            prev = curr

            if curr.next:
                curr = curr.next
            else:
                break

        # 맨앞, 맨뒤 노드 값 비교
        front = head
        back = curr
        for i in range(length // 2):
            if front.val != back.val:
                return False
            front = front.next
            back = back.prev

        return True