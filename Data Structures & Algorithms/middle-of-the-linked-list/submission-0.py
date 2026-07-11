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
            temp_len = 1
            while curr:
                print(temp_len, target_mid, curr.val)
                if temp_len == target_mid:
                    return curr
                elif temp_len != target_mid: # if our 
                    temp_len+=1
                    curr = curr.next
                
        
        if length%2 == 0:
            target = (length//2)+1
            return mid_node(target)
        else:
            target = math.ceil(length/2)
            return mid_node(target)
                




        