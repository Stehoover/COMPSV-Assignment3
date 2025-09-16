# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

    def pop(self):
        if self.is_empty():
            return None
        
        removed_node = self._head
        self._head = self._head.next
        
        return removed_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self._head.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current_node = self._head
        while current_node:
            print(f"- {current_node.data}")
            current_node = current_node.next


def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")
        print() # Print a blank line for spacing

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            if action:
                # Push the action onto the undo stack and clear the redo stack
                undo_stack.push(action)
                # Clear the redo stack as a new action invalidates the redo history
                redo_stack = Stack()
                print(f"Action performed: {action}")
            else:
                print("Action cannot be empty.")

        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            undone_action = undo_stack.pop()
            if undone_action:
                redo_stack.push(undone_action)
                print(f"Undid action: {undone_action}")
            else:
                print("Nothing to undo.")

        elif choice == "3":
            # Pop an action from the redo stack and push it onto the undo stack
            redone_action = redo_stack.pop()
            if redone_action:
                undo_stack.push(redone_action)
                print(f"Redid action: {redone_action}")
            else:
                print("Nothing to redo.")

        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.display()

        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.display()
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()
