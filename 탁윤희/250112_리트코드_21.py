# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            # 값 value 비교 후 더 작은 쪽을 tail에 넣기
            # 그 다음 넣어진 쪽은 다음 값으로 바꿈
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
            # 마지막으로 남은 걸 tail에 넣어 마무리
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next