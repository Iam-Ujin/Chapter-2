class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head : 정렬해야할 대상
        # cur : 정렬 끝난 대상
        cur = parent = ListNode(0)
        # cur 에 정렬을 끝낸 연결리스트를 추가
        while head:
            # head와 비교하여 더 작다면 다음으로 이동
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            # 찾은 cur위치 다음에 head
            # cur.next로 연결
            # head = head.next로 연결
            cur.next, head.next, head = head, cur.next, head.next

            # cur가 head보다 틀때만 cur을 맨처음으로
            if head and cur.val > head.val:
                cur = parent

        return parent.nexy






