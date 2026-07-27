# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # we traverse to find length
        # we detach the node at x position and re attach anythign after it

        curr = head
        leng = 0
        while curr:
            leng+=1
            curr =  curr.next
        
        print('length is',leng, 'overall node pointer needed is', leng-n+1)

        dummyNode = ListNode(0)
        tracker = dummyNode
        curr = head
        t_l = 0

        while curr:
            if t_l == leng - n:
                curr = curr.next

            tracker.next = curr
            tracker = tracker.next
            curr = curr.next if curr else None
            

            t_l+=1
        return dummyNode.next
        # curr = head
        
        # temp_len = 0
        # while curr:
        #     if temp_len == leng-n: # now we need to replace next node directly because we are seeing next one to be removed
        #         temp = curr.next
        #         curr.next = temp.next if temp else None
            
        #     temp_len+=1

        #     curr = curr.next            
        # # print(head, temp.val)
        #         # curr == curr.next # we skip the node without adding to our new ll? but we want in place
        # return head



            







