# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0) # 리스트노드 자료형의 변수 dummy, cur 생성
        # 변수 두 개 만드는 이유?
        # dummy : return 값
        # cur : 새 값을 넣을 임시 변수
        carry = 0
        while l1 or l2 or carry:
            if l1:
                # val은 하면 바로 0번째 노드 value부터 나오드라
                carry += l1.val
                # 연결된 다음 노드로 전환
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            # 10으로 나눈 나머지만 남기고, 합산 10이상은 1 앞으로 넘겨줌
            cur.next = ListNode(carry%10)
            cur = cur.next # 이제 다음 cur 값 구할 것
            carry //= 10 # 10으로 나눈 몫 넣어줌 (10이상이면 1이 들어가 있을 것)

        return dummy.next