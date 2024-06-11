
pub struct Stack<T> {
    elements: Vec<T>,
}

impl <T> Stack<T> {

    pub fn new() -> Self {
        Stack { elements: Vec::new() }
    }


    pub fn push(&mut self, item:T) {
        self.elements.push(item);
    }


    pub fn pop(&mut self) -> Option<T> {
        self.elements.pop()
    }

    pub fn peek(&self) -> Option<&T>{
        self.elements.last()
    }

    pub fn size(&self) -> usize {
        self.elements.len()
    }

    pub fn is_empty(&self) -> bool {
        self.elements.is_empty()
    }

}


fn main() {
    // Create a new stack
    let mut stack: Stack<i32> = Stack::new();

    // Push elements onto the stack
    stack.push(1);
    stack.push(2);
    stack.push(3);

    // Peek at the top element
    println!("Top element is: {:?}", stack.peek());

    // Pop elements from the stack
    println!("Popped element is: {:?}", stack.pop());
    println!("Popped element is: {:?}", stack.pop());

    // Check if the stack is empty
    println!("Is the stack empty? {}", stack.is_empty());

    // Check the size of the stack
    println!("Stack size is: {}", stack.size());
}