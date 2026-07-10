# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lookup = set()

        curr = head
        while curr:
            if curr in lookup:
                return True
            
            lookup.add(curr)
            curr = curr.next

        return False

        # --> we need to see if the linked list has a cycle within, which means if we ever hit a seen memory address
        # so we store memory addresses of visited nodes
        # when we say curr its memory address of node, not node value itself.
        # curr.val is value
        # curr.next is next ones memory address not value again
        # since ll can have duplicates, what we can do is to keep a set o(1) lookup for seen memory addresses using node
        # and making curr = curr.next at the end, re pointing curr's value to its next element
        # 1->2->3->4
        # we process 1's address to the set and then make our curr to point to curr.next's address