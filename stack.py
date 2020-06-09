
# The following program shows implementation of Stack Abstract data type using list. 
# In a stack, elements are pushed and popped from one end of the stack which is called the top of the stack.
# This implementation has no maximum limit on the size of the stack. 
# You have to introduce a maximum limit by adding a class variable named MAX_SIZE. 
# In the push method, before inserting a new element, check the size of the stack and raise a RuntimeError
#  if the stack is full. 

class Stack:   

    #class variables
    MAX_SIZE = 5

    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def size(self):
        return len(self.items)
 
    def push(self, item):
        if self.size() >= Stack.MAX_SIZE:
            raise RuntimeError("Stack is full")
        self.items.append(item)
 
    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items.pop()
 
    def peek(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        return self.items[self.size() - 1]
    
    def display(self):
        print(self.items)
 
if __name__ == "__main__":
    st = Stack()
 
    while True:
        print("1.Push") 
        print("2.Pop") 
        print("3.Peek") 
        print("4.Size")
        print("5.Display") 
        print("6.Quit")
         
        choice = int(input("Enter your choice : "))
 
        if choice == 1:
            x=int(input("Enter the element to be pushed : "))
            st.push(x) 
        elif choice == 2:
            x=st.pop() 
            print("Popped element is : " , x) 
        elif choice == 3:
            print("Element at the top is : " , st.peek()) 
        elif choice == 4:
            print("Size of stack " , st.size()) 
        elif choice == 5:
            st.display()         
        elif choice == 6:
          break
        else:
          print("Wrong choice") 
        print() 