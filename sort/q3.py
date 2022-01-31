# 리스트 정렬
# 1) 연결리스트 -> 파이썬리스트
# 2) 리스트 정렬
# 3) 파이썬리스트 -> 연결리스트

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        list: List = []

        while node:
            list.append(node.val)
            node = node.next

        list.sort()

        node = head
        for i in range(len(list)):
            node.val = list[i]
            node = node.next

        return head