# 풀이 날짜 : 2024.01.01
# 문제 유형 : Linked List, Math, Recursion
# 문제 제목 : Add Two Numbers
# 문제 링크 : https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 결과 링크드 리스트(ListNode로 초기화)
        answer = ListNode()
        # 현재 노드
        current = answer
        # 올림할 값
        carry = 0

        while l1 or l2 or carry:
            # 자릿수의 합계
            s = 0

            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            s += carry
            carry = s // 10

            current.next = ListNode(s % 10)
            current = current.next

        return answer.next
