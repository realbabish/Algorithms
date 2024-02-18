class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, key):
        current_node = self.head

        if current_node and current_node.data is key:
            self.head = None
            return

        prev_node = None

        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

            if current_node is None:
                print("Item not in the List")
                return

        prev_node.next = current_node.next
        current_node = None
        return

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next

Linked_list = LinkedList()
Linked_list.add(1)
Linked_list.add(2)
Linked_list.add(3)
Linked_list.add(4)
Linked_list.add(5)
Linked_list.add(6)

Linked_list.print()

print("Linked List after deleting 2 and 5 is")

Linked_list.delete(2)
Linked_list.delete(5)

Linked_list.print()
