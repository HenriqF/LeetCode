#problemas de leetcode que foram solucionados aqui:
#https://leetcode.com/problems/reverse-linked-list/description/ INVERTER LISTAS    206.
#https://leetcode.com/problems/merge-two-sorted-lists/          JUNTAR DUAS LISTAS 21.
#https://leetcode.com/problems/add-two-numbers/description/     Add Two Numbers 2.
#

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def create(self, n):
        if n > 0:
            self.next = ListNode(self.val+1)
            self.next.create(n-1)

    def transform(self, nums):
        if nums != []:
            self.next = ListNode(nums[0])
            nums.pop(0)
            self.next.transform(nums)

    def add(self, n):
        current = self #Isso aqui nao cria uma nova linked list, simplesmente põe um ponteiro para onde está a linked list
        while current.next:
            current = current.next
        current.next = ListNode(n)
        return(self)

    def list(self):
        print(self.val, end="")
        if self.next != None:
            print(" -> ", end="")
            self.next.list()
        else:
            print("")

def reverseList(head): #206. INVERTER LISTAS
    lista = None
    while head:
        rest = head.next
        head.next = lista
        lista = head
        head = rest
    return(lista)

def merge(list1 , list2): #21. JUNTAR DUAS LISTAS
    lista = ListNode()
    tail = lista

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2

    return(lista.next)

def addTwoNumbers(l1, l2): #2. Add Two Numbers
    list = ListNode(0)
    current = list
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry

        result = sum % 10
        carry = sum // 10

        current.next = ListNode(result)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return(list.next)

