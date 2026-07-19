# Insertion-and-deletion-of-nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
def display(head):
     temp=head
     while temp is not None:
         print(temp.data,end="->")
         temp=temp.next
     print("None")
print("Original Linked List")
display(head)
print("Insertion at Beginning")
new_node=Node(5)
new_node.next=head
head=new_node
display(head)
print("Insertion in the middle")
new_node=Node(25)
temp=head
while temp.data!=20:
    temp=temp.next
new_node.next=temp.next
temp.next=new_node
display(head)
print("Insertion at End")
new_node=Node(40)
temp=head
while temp.next is not None:
    temp=temp.next
temp.next=new_node
display(head)
print("Deletion at Beginning")
head=head.next
display(head)
print("Deletion at Middle")
temp=head
while temp.next.data!=25:
    temp=temp.next
temp.next=temp.next.next
display(head)
print("Deletion at end")
temp=head
while temp.next.next is not None:
    temp=temp.next
temp.next=None
display(head)

