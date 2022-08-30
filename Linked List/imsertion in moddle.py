class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

def print_list(self):
    ptr=self.head
    while ptr:
        print(ptr.data)
        ptr=ptr.next

def insertion_in_mid(self,prev_data,curr_data):
    ptr = self.head
    new_node=Node(curr_data)
    while ptr:
        if ptr.data==prev_data:
            ptr.next=new_node
            new_node.next=ptr.next.next
        break
linked_list=LinkedList()
linked_list.head=Node(int(input()))
n1=Node(int(input()))
n2=Node(int(input()))
linked_list.head.next=n1
n1.next=n2
print(print_list(linked_list))
print("Enter Previous data after which node is to be Entered:")
a=int(input())
print("Enter Node to be Entered:")
b=int(input())
insertion_in_mid(linked_list,a,b)
print(print_list(linked_list))