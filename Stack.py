class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self):
        last_element=input("Enter the element you want to push: ")
        return self.stack.append(last_element)
    
    def pop(self):
        if len(self.stack)==0:
            print("Empty stack")
        else:
            print("Last Element popped")
            return self.stack.pop()
            
    
    def update(self):
        while True:
            pos=int(input("Enter the position you want to update the element: "))
            if 0<=pos<=len(self.stack):
                updated_element=input("Enter the element you want to update: ")
                self.stack[pos]=updated_element
                print("Element updated")
                break
            elif len(self.stack)==0:
                print("Empty stack please fill the stack")
                break
            else:
                print("Stack size is "+len(self.stack)+" Please enter the position within the stack size")
                
    def display(self):
        print(self.stack)
    
    
    
def main():
    st=Stack()
    try:
        while True:
            print("----------------------------------------------------------------")
            choice=int(input("Enter the choice \n1.Push\n2.Pop\n3.Update\n4.Display\n5.Exit: "))
            if choice ==1:
                st.push()
            elif choice ==2:
                st.pop()
            elif choice ==3:
                st.update()       
            elif choice ==4:
                st.display()
            elif choice ==5:
                break
            else:
                print("Please enter the valid choice \n1.Push\n2.Pop\n3.Update\n4.Display\n5.Exit\n ")  
                
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")
    
if __name__=="__main__":
    main()