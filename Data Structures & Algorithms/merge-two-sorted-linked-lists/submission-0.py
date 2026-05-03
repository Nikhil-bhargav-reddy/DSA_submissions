class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1      # 1. Attach the box
                list1 = list1.next     # 2. Move the line forward
            else:
                tail.next = list2      # 1. Attach the box
                list2 = list2.next     # 2. Move the line forward
            
            # Step the tail forward onto the box we just attached
            tail = tail.next
            
        # Attach the leftovers
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next