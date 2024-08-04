class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node|None = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_beginning(self, data):
        new_node = Node(data)
        self.length += 1
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.length += 1
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_Node(self, node:Node|None):
        if not node:
            return
        node.next = None
        self.length += 1
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert_after(self, prev_node: Node|None, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        self.length += 1
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            self.length -= 1
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
        self.length -= 1

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def get_by_index(self, idx: int) -> Node | None:
        if (idx<0 or idx >= self.length):
            raise IndexError("Linked list index out of range")
        cur = self.head
        for _ in range(idx):
            cur = cur.next
        return cur

    def get_list_till(self, idx):
        if (idx<0 or idx >= self.length):
            raise IndexError("Linked list index out of range")
        new_list = LinkedList()
        cur = self.head
        for _ in range(idx):
            new_list.insert_at_end(cur.data)
            cur = cur.next
        return new_list

    def get_list_from(self, idx):
        if (idx<0 or idx >= self.length):
            raise IndexError("Linked list index out of range")
        new_list = LinkedList()
        cur = self.get_by_index(idx)
        for _ in range(idx, self.length):
            new_list.insert_at_end(cur.data)
            cur = cur.next
        return new_list

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

if __name__ == "__main__":
    llist.insert_at_beginning(45)
    after = llist.search_element(20)
    llist.insert_after(after, 35)
    llist.insert_at_end(55)
    print("Зв'язний список:", llist.length)
    llist.print_list()
    # Видаляємо вузол
    llist.delete_node(35)
    llist.delete_node(45)
    llist.delete_node(55)
    print("Зв'язний список:", llist.length)
    llist.print_list()
