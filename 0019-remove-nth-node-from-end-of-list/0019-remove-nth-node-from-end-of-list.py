# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list1=[]
        curr=head
        while curr:
            list1.append(curr.val)
            curr=curr.next
        length=len(list1)
        index=length-n
        list1.pop(index)

        dummy=ListNode(0)
        curr=dummy
        for i in list1:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next