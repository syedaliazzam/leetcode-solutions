# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return None

        curr = ListNode(-101)
        currVal = curr.val

        dummy = curr

        while head:
            # if current head is equal to currVal (which should be dupe list node alr skipped), increment head
            if head.val == currVal:
                head = head.next
            # if head.val is new and is equal to val of next node, skip and set currVal, if head.next is null (the end), 
            elif head.next and head.val == head.next.val:
                currVal = head.val
                head = head.next
            # else head.val should be unique, and no dupes
            else:
                curr.next = head
                head = head.next
                curr = curr.next
                curr.next = None

        
        return dummy.next
        