class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
def print_list(self):
    ptr = self.head
    while ptr:
        print(ptr.data,ptr.next)
        ptr =ptr.next
def insertion_in_end(self,n):
    ptr=self.head
    node=Node(n)
    if ptr is None:
        ptr = node
        return
    fin = ptr
    while (fin.next):
        fin = fin.next
    fin.next =node

n1=Node(int(input()))
n2=Node(int(input()))
listt.head.next=n1
n1.next=n2
print_list(listt)
a=int(input())
insertion_at_start(listt,a)
print_list(listt)
