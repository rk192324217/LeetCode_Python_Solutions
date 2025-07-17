# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        new=head
        length=0
        while new:
            length+=1
            new=new.next
        for _ in range(1,length//2 +1):
            head=head.next
        return head

