class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
def print_list(self):
    while self.head:
        print(self.head.data, self.head.next)
        self.head=self.head.next
linked=LinkedList()
linked.head=Node(int(input()))
n1=Node(int(input()))
n2=Node(int(input()))
linked.head.next=n1
n1.next=n2
print_list(linked)