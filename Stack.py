class Node:
    def __init__ (self,data):
       self.data=data
       self.next=None
class stack:
    def __init__ (self):
        self.top=None
    def is__empty(self):
        return self.top is None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.is__empty():
            return None
        popped_data=self.top.data
        self.top=self.top.next
        return popped_data
    def peek(self):
        if self.is__empty():
            return None
        return self.top.data
Stack=stack()
num=int(input("Enter the num to push"))
Stack.push(num)
num1=int(input("Enter the num1 to push"))
Stack.push(num1)
num2=int(input("Enter the num2 to push"))
Stack.push(num2)
print("Peek:",Stack.peek())
print("Pop:",Stack.pop())
print("Pop:",Stack.pop())
print("Peek:",Stack.peek())
print("Pop:",Stack.pop())
print("Pop:",Stack.pop())
print("Is Empty:",Stack.is__empty())
