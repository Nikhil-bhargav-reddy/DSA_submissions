# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the length of the linked list first using a pointer, keep counting
        # now if length is even divide that length by 2 and add 1 to get upper bound
        # if odd divide by 2
        # now we have the number for mid
        # traverse using a new pointer
        # keep counting till we reach mid
        # return that mid

        pointer = head # points to same memory address
        length = 0
        while pointer:
            length+=1
            pointer = pointer.next # pointer moves while head stays as is
        
        def mid_node(target_mid):
            curr = head
            temp_len = 1 # starting at 1 because even current where we are standing is 1, we keep adding and moving next as long as while curr is true
            while curr:
                print(temp_len, target_mid, curr.val)
                if temp_len == target_mid:
                    return curr
                elif temp_len != target_mid: # if our 
                    temp_len+=1
                    curr = curr.next
                
        
        target = (length//2)+1
        return mid_node(target)
        # fast = head
        # slow = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next 
        # return slow
        # after the loop, if we have fast.next means we dont have fast.next.next means its even
        # so we need to move fast pointer regardless even with 1, so we increment slow by 1 to return
        # when there is no fast.next and fast.next.next means all are covered and pointers finished means slow is exactly were it should be 
        

        