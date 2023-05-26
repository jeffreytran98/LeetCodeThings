# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
             return list2
        if not list2:
             return list1

        elif list1.val < list2.val: 
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else: 
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        '''
        if list1 == None: # for empty lists
            return list2
        elif list2 == None:
            return list1
        
        if list2.val < list1.val: # initialize a merged list head
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        head.next = None
        ptr = head
        
        while list1 != None and list2 != None: # merge the two lists 
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
                ptr = ptr.next
            else:
                ptr.next = list2
                list2 = list2.next
                ptr = ptr.next
        
        while list1 != None: # handle case: len(list1) > len(list2)
            ptr.next = list1
            list1 = list1.next
            ptr = ptr.next
            
        while list2 != None: 
            ptr.next = list2
            list2 = list2.next
            ptr = ptr.next
            
        return head
        '''