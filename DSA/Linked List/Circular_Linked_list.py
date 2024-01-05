class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_to_empty(last, data):
    ptr = Node(data)
    last = ptr
    last.next = last
    return last


def add_to_end(last, data):
    ptr = Node(data)

    if last is None:
        print("List is Empty")
        return last

    ptr.data = data
    ptr.next = last.next
    last.next = ptr
    last = ptr

    return last


def create_list(last):
    n = int(input("Enter the number of nodes in the list: "))

    if n == 0:
        return last

    data = int(input("Enter the data: "))
    last = add_to_empty(last, data)

    for _ in range(2, n + 1):
        data = int(input("Enter the data: "))
        last = add_to_end(last, data)

    return last


def display_the_list(last):
    if last is None:
        print("List is Empty")
        return

    p = last.next

    while True:
        print(p.data, end=" ")
        p = p.next
        if p == last.next:
            break

    print()


def add_to_beginning(last, data):
    if last is None:
        print("List is Empty")
        return last

    ptr = Node(data)
    ptr.data = data
    ptr.next = last.next
    last.next = ptr

    return last


def add_to_node(last, data, index):
    ptr = Node(data)

    if last is None:
        print("List is Empty")

    if last.next.data == index:
        last = add_to_beginning(last, data)
        return last

    if last.data == index:
        last = add_to_end(last, data)
        return last

    p = last.next
    p = p.next

    while p != last.next:
        if p.data == index:
            ptr.data = data
            ptr.next = p.next
            p.next = ptr
            return last
        p = p.next

    return last


def search(last, data):
    p = last.next
    i = 1

    if last.next.data == data:
        print(data, "is found at 1 position.")
        return

    p = p.next

    while p != last.next:
        if p.data == data:
            print(data, "is found at", i, "position.")
            return
        i += 1
        p = p.next

    print(data, "is not found in the list")


def deletion_of_node(last, index):
    p = last.next

    if last.next.data == index:
        ptr = last.next
        last.next = ptr.next
        ptr = None
        return last

    while p.next != last:
        if p.next.data == index:
            ptr = p.next
            p.next = ptr.next
            ptr = None
            return last
        p = p.next

    if last.data == index:
        ptr = last
        p.next = last.next
        last = p
        ptr = None
        return last

    return last


if __name__ == "__main__":
    last = None

    while True:
        print("\n1. Create the list")
        print("2. Insert at empty list")
        print("3. Insert at end of the list")
        print("4. Display the list")
        print("5. Insert at beginning of the list")
        print("6. Insert at any node of the list")
        print("7. Search the element of the list")
        print("8. Deletion of the data of the list")

        choose = int(input("Choose the above option: "))

        if choose == 1:
            last = create_list(last)
        elif choose == 2:
            data = int(input("Enter the data: "))
            last = add_to_empty(last, data)
        elif choose == 3:
            data = int(input("Enter the data: "))
            last = add_to_end(last, data)
        elif choose == 4:
            display_the_list(last)
        elif choose == 5:
            data = int(input("Enter the data: "))
            last = add_to_beginning(last, data)
        elif choose == 6:
            index = int(input("Enter the index of the data: "))
            data = int(input("Enter the data: "))
            last = add_to_node(last, data, index)
        elif choose == 7:
            data = int(input("Enter the data to be searched: "))
            search(last, data)
        elif choose == 8:
            index = int(input("Enter the data index: "))
            last = deletion_of_node(last, index)
        else:
            print("INVALID SELECTION")
