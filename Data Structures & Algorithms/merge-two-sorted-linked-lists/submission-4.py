class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummylist = ListNode(0)

        tracker = dummylist

        while list1 and list2:

            if list1.val < list2.val:
                tracker.next = list1
                list1 = list1.next
            else:
                tracker.next = list2
                list2 = list2.next
            
            tracker = tracker.next # keeps moving 
        
        if list1:
            tracker.next = list1
        else:
            tracker.next = list2
        return dummylist.next



                