# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# 0이상의 정수로 이루어진 linked list 두 개가 주어진다. 각 노드의 값은 한 자리 숫자이다. linked list는 거꾸로된 방향으로 각 자리가 저장되어있다. 이 두개의 숫자를 더한 linked list를 리턴하라.

# 예를 들어, l1 = [2,4,3], l2 = [5,6,4] 라면 342 + 465 = 807 이므로 [7, 0, 8]을 리턴

# 예
# input : l1 = [2,4,3], l2 = [5,6,4]

# output : [7,0,8]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        curr = result
        carry = 0 #올림 자리 보관
        
        while l1 or l2 or carry:
            curr.next = ListNode()
            curr = curr.next
            num1 = num2 = 0
            if l1 :
                num1 = l1.val
                l1 = l1.next
            if l2 :
                num2 = l2.val
                l2 = l2.next
            curr.val = (num1 + num2 + carry) % 10
            carry = (num1 + num2 + carry) // 10
        
        return result.next
            