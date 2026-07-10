# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
# slow and fast pointers 
# both start at head
# we check as long as fast and fast.next arent nulls, because if thery were nulls means they have hit end = no cycle
# we dont need to check slow = fast first because both are equal first
# slow = slow.next, fast = fast.next.next one takes one step other takes two, meets at some point after running in circles
# but still the time is linear because lets say in worst case it does maybe 20 loops over the ll untill they meet it will still be 20* o(n)
# so yeah memory is o(1)            