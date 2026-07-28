class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(5)
n2=Node(10)
n3=Node(20)
n4=Node(30)
n1.next=n2
n2.next=n3
n3.next=n4
head=n1
def display(head):
    temp=head
    while temp is not None:
        print(temp.data)
        temp=temp.next
    print("None")
print("Original Linked list")
display(head)
print("\n Insertion at Middle")
new_node=Node(25)
temp=head
while temp.data!=20:
    temp=temp.next
new_node.next=temp.next
temp.next=new_node
display(head)
