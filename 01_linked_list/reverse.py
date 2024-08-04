from LinkedList import LinkedList, llist

def reverse_forward(linked: LinkedList):
    previous = linked.head
    current = previous.next
    while current.next:
        further = current.next
        current.next = previous
        previous = current
        current = further
    current.next = previous
    linked.head.next = None
    linked.head = current

if __name__ == "__main__":
    print("\nЗв'язний список:")
    llist.print_list()
    reverse_forward(llist)
    print("\nРеверс зв'язного списоку:")
    llist.print_list()
