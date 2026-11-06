# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        #Step1: Find The Middle

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Step2: Reverse THe second half

        curr = slow.next
        slow.next= None
        prev = None

        while curr:
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp
        #Step3:Merge both the halves
        first =head
        second=prev

        while second:
            temp1=first.next
            temp2=second.next
            first.next=second 
            second.next=temp1
            first=temp1
            second=temp2

