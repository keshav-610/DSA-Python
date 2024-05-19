class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self):
        last_element=input("Enter the Element you want to Enqueue: ")
        return self.queue.append(last_element)

    def dequeue(self):
        if len(self.queue)==0:
            print("Empty Queue")
        else:
            print("First element popped")
            return self.queue.pop(0)

    def update(self):
        while True:
            pos = int(input("Enter the position you want to update: "))
            if 0 <= pos <= len(self.queue):
                updated_element=input("Enter the element: ")
                self.queue[pos]=updated_element
                print("Element Updated")
                break
            elif len(self.queue)==0:
                print("Empty queue please fill the queue")
                break
            else:
                print("Queue Size is "+ len(self.queue)+" Please enter the position within the Queue size")



    def display(self):
        print(self.queue)



def main():
    qu=Queue()
    while True:
            print("----------------------------------------------------------------")
            choice = int(input("Enter the choice \n1.Enqueue\n2.Dequeue\n3.Update\n4.Display\n5.Exit: "))
            if choice ==1:
                qu.enqueue()
            elif choice ==2:
                qu.dequeue()
            elif choice ==3:
                qu.update()
            elif choice ==4:
                qu.display()
            elif choice ==5:
                break
            else:
                print("Please enter the valid choice")


if __name__=="__main__":
    main()