class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummylist = ListNode(0)
        tail = dummylist
        res = dummylist
        # overall concept is that we create a empty listnode with 0
        # then we use a tail pointer to keep track of our current location of where we need to add vals


        while list1 and list2: # if both of them are non empty
            if list1.val >list2.val:
                tail.next = list2
                list2 = list2.next
                
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next  
        
        if not list1:
            tail.next = list2
            
        elif not list2:
            tail.next = list1

        return res.next


                