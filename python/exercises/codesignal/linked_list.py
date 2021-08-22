# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def printList(l):
    ptr=l
    print("DEBUG: ", end = '')
    while ptr:
        print(ptr.value, end = ',')
        ptr=ptr.next
    print('')
        
        
# Should I be recursive?
def removeKFromList(l, k):
    
    fakehead=ListNode(None)   # head ptr to initilize. sure not to be k
    fakehead.next = l
    current=fakehead
    
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
    
    # printList(fakehead.next)
    # printList(l)
    return(fakehead.next)
