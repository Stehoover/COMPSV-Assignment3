# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    
    def __init__(self):
        self._head = None  # Pointer to the front of the queue
        self._tail = None  # Pointer to the back of the queue

    def is_empty(self):
        return self._head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        
        removed_node = self._head
        self._head = self._head.next
        
        # If the last item was dequeued, the tail must also be set to None
        if self._head is None:
            self._tail = None
            
        return removed_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self._head.data
        
    def display(self):
        if self.is_empty():
            print("No customers waiting.")
            return

        current_node = self._head
        while current_node:
            print(f"- {current_node.data}")
            current_node = current_node.next


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")
        print() # Print a blank line for spacing

        if choice == "1":
            name = input("Enter customer name: ")
            if name:
                # Add the customer to the queue
                queue.enqueue(name)
                print(f"{name} added to the queue.")
            else:
                print("Customer name cannot be empty.")
            
        elif choice == "2":
            # Help the next customer in the queue and return a message
            helped_customer = queue.dequeue()
            if helped_customer:
                print(f"Helped: {helped_customer}")
            else:
                print("No customers waiting.")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            next_customer = queue.peek()
            if next_customer:
                print(f"Next customer: {next_customer}")
            else:
                print("No customers waiting.")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.display()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
