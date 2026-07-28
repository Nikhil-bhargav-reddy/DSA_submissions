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

        dummyNode = ListNode(0,head)

        curr = dummyNode
        temp_leng = 0
        while curr:
            if temp_leng == leng-n:
                curr.next =  curr.next.next
            
            temp_leng+=1
            curr =  curr.next
        
        return dummyNode.next


        # #     t_l+=1
        # # return dummyNode.next
        # curr = head
        
        # temp_len = 0
        # while curr:
        #     if temp_len == leng-n: # now we need to replace next node directly because we are seeing next one to be removed
        #         curr = curr.next
        #     temp_len+=1

        #     curr = curr.next            
        # # print(head, temp.val)
        #         # curr == curr.next # we skip the node without adding to our new ll? but we want in place
        # return head



            







