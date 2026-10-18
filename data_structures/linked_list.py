class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data):
        """Remove the first node holding data. Returns True if something was removed."""
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        return False

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def to_list(self):
        out = []
        current = self.head
        while current:
            out.append(current.data)
            current = current.next
        return out

    def __len__(self):
        return self.size

    def __str__(self):
        return " -> ".join(str(x) for x in self.to_list()) or "(empty)"


if __name__ == "__main__":
    ll = LinkedList()
    for x in [1, 2, 3, 4]:
        ll.append(x)
    ll.prepend(0)
    print(ll)
    ll.delete(3)
    ll.reverse()
    print(ll)
