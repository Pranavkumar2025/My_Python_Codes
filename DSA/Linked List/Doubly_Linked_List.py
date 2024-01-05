class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


def add_to_empty(head, data):
    ptr = Node(data)
    head = ptr
    return head


def add_to_end(head, data):
    ptr = Node(data)
    p = head

    while p.next is not None:
        p = p.next

    ptr.prev = p
    p.next = ptr
    ptr.next = None

    return head


def create_list(head):
    n = int(input("Enter the number of nodes: "))
    head = None

    for _ in range(n):
        data = int(input("Enter the Elements: "))
        head = add_to_empty(head, data)

    return head


def display(head):
    p = head

    while p is not None:
        print(p.data, end=" ")
        p = p.next

    print()


def count(head):
    count = 0
    p = head

    while p is not None:
        count += 1
        p = p.next

    print("Total number of Nodes:", count)


def search(head, data):
    p = head
    pos = 1

    while p is not None:
        if p.data == data:
            print(data, "data is at", pos, "position")
        pos += 1
        p = p.next


def add_at_index(head, data, index):
    ptr = Node(data)
    p = head

    for _ in range(index - 1):
        p = p.next

    ptr.data = data
    ptr.next = p.next
    p.next = ptr
    ptr.prev = p

    return head


def add_to_first(head, data):
    ptr = Node(data)

    if head is None:
        print("List is Empty")
        return head

    ptr.data = data
    ptr.next = head
    head.prev = ptr
    ptr.prev = None
    head = ptr

    return head


def delete_at_index(head, index):
    p = head

    for _ in range(index - 1):
        p = p.next

    p.prev.next = p.next
    p.next.prev = p.prev

    return head


def insert_after_node(head, elements, data):
    ptr = Node(data)

    if head.data == elements:
        ptr.data = data
        ptr.next = head
        head.prev = ptr
        ptr.prev = None
        head = ptr
        return head

    p = head

    while p is not None:
        if p.data == elements:
            ptr.data = data
            ptr.next = p.next
            p.next = ptr
            ptr.prev = p
            return head
        p = p.next

    return head


def my_choice(head, data):
    p = head

    while p is not None:
        if p.data == data:
            print("Data of previous elements is:", p.prev.data)
        p = p.next


if __name__ == "__main__":
    head = None

    while True:
        print("\n1. Create the doubly linked list")
        print("2. Add at End of the list")
        print("3. Add when list is Empty")
        print("4. Display the doubly linked list")
        print("5. Count")
        print("6. Search the elements of the list")
        print("7. Insert the data at a specific position")
        print("8. Add at the first of the list")
        print("9. Delete at any position")
        print("10. Enter after the nodes")
        print("11. Taking previous data")
        print("0. Exit the list")

        choose = int(input("\nEnter the choice: "))

        if choose == 1:
            head = create_list(head)
        elif choose == 2:
            data = int(input("Enter the data of the nodes: "))
            head = add_to_end(head, data)
        elif choose == 3:
            data = int(input("Enter the data of the nodes: "))
            head = add_to_empty(head, data)
        elif choose == 4:
            display(head)
        elif choose == 5:
            count(head)
        elif choose == 6:
            data = int(input("Enter the data which is to be searched: "))
            search(head, data)
        elif choose == 7:
            data = int(input("Enter the data of the nodes: "))
            index = int(input("Enter the position in which data is inserted: "))
            head = add_at_index(head, data, index)
        elif choose == 8:
            data = int(input("Enter the data: "))
            head = add_to_first(head, data)
        elif choose == 9:
            index = int(input("Enter the position: "))
            head = delete_at_index(head, index)
        elif choose == 10:
            elements = int(input("Enter the data after which you want to insert: "))
            data = int(input("Enter the data: "))
            head = insert_after_node(head, elements, data)
        elif choose == 11:
            data = int(input("Enter the data: "))
            my_choice(head, data)
        elif choose == 0:
            break
        else:
            print("Invalid Selection")
