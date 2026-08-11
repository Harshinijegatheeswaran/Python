class BookStack:
    def __init__(self, capacity=None):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.capacity is None:
            return False
        return len(self.stack) >= self.capacity

    def push(self, book_title):
        if self.is_full():
            print("\nError: Stack Overflow! Cannot add '" + str(book_title) + "'. Stack is full.")
            return False
        
        self.stack.append(book_title)
        print("\nSuccess: Added '" + str(book_title) + "' to the stack.")
        return True

    def pop(self):
        if self.is_empty():
            print("\nError: Stack Underflow! No books to remove.")
            return None
        
        removed_book = self.stack.pop()
        print("\nSuccess: Removed '" + str(removed_book) + "' from the stack.")
        return removed_book

    def peek(self):
        if self.is_empty():
            print("\nThe stack is currently empty.")
            return None
        print("\nTop Book: '" + str(self.stack[-1]) + "'")
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("\nThe stack is currently empty.")
            return

        print("\n--- Current Library Stack (Top to Bottom) ---")
        for index, book in enumerate(reversed(self.stack), start=1):
            print(" " + str(index) + ". " + str(book))
        print("---------------------------------------------\n")


def main():
   
    try:
        get_input = raw_input
    except NameError:
        get_input = input

   
    capacity_input = get_input("Enter max capacity for the stack (press Enter for unlimited): ").strip()
    capacity = int(capacity_input) if capacity_input.isdigit() else None

    library_stack = BookStack(capacity=capacity)

    while True:
        print("\n=================================")
        print("  LIBRARY BOOK STACK MANAGEMENT  ")
        print("=================================")
        print("1. Push (Add Book Title)")
        print("2. Pop (Remove Top Book)")
        print("3. Peek (View Top Book)")
        print("4. Display All Books")
        print("5. Exit")
        
        choice = get_input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = get_input("Enter the book title to add: ").strip()
            if title:
                library_stack.push(title)
            else:
                print("\nError: Book title cannot be empty.")

        elif choice == '2':
            library_stack.pop()

        elif choice == '3':
            library_stack.peek()

        elif choice == '4':
            library_stack.display()

        elif choice == '5':
            print("\nExiting Library Management System. Goodbye!")
            break

        else:
            print("\nError: Invalid choice! Please select a valid option (1-5).")


if __name__ == "__main__":
    main()
