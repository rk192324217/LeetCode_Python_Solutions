# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        res=[]
        while head is not None:
            res.append(head.val)
            head=head.next
        print(res)
        return res==res[::-1]
