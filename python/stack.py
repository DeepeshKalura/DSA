class Stack :
    def __init__(self) -> None:
        self.elements = []

    def push(self, element) -> None:
        self.elements.append(element)

    def pop(self):
        if(self.is_empty()):
            raise Exception("Your Stack is empty cannot pop the elements")
        return self.elements.pop()
    
    def peek(self):
        if(self.is_empty()):
            raise Exception("Your Stack is empty so there is no element to peek at")
        return self.elements[-1]

    def is_empty(self):
        if((len(self.elements)) == 0):
            return True
        return False
    
    def size(self):
        return len(self.elements)


def main():
    st = Stack()

    print(st.is_empty())
    print("Oh! yes it is empty")
    print(st.push(2))
    print("Lol None print hoga")
    st.push(1)
    st.push(3)

    print(st.peek())
    print(st.pop())
    print(st.peek())

    print(st.size())

if  __name__  == "__main__":
    main()

