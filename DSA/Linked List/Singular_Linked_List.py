class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_at_beg(start, data):
    tmp = Node(data)
    tmp.next = start
    start = tmp
    return start


def add_at_end(start, data):
    tmp = Node(data)
    p = start
    while p.next is not None:
        p = p.next
    p.next = tmp
    tmp.next = None
    return start


def create_list(start):
    n = int(input("Enter the number of nodes: "))
    start = None
    if n == 0:
        return start
    data = int(input("Enter the element to be inserted: "))
    start = add_at_beg(start, data)
    for i in range(2, n + 1):
        data = int(input("Enter the element to be inserted: "))
        start = add_at_end(start, data)
    return start


def display(start):
    p = start
    if start is None:
        print("List is Empty")
        return
    print("List is: ")
    while p is not None:
        print(p.data, end=" ")
        p = p.next
    print()


def count(start):
    p = start
    cnt = 0
    while p is not None:
        p = p.next
        cnt += 1
    print("Number of elements are", cnt)


def search(start, item):
    p = start
    pos = 1
    while p is not None:
        if p.data == item:
            print("Item", item, "found at position", pos)
            return
        p = p.next
        pos += 1


def add_after(start, data, item):
    tmp = Node(data)
    p = start
    while p is not None:
        if p.data == item:
            tmp.next = p.next
            p.next = tmp
            return start
        p = p.next
    print(item, "not present in the list")
    return start


def add_before(start, data, item):
    tmp = Node(data)
    if start is None:
        print("List is Empty")
        return start
    if item == start.data:
        tmp.next = start
        start = tmp
        return start
    p = start
    while p.next is not None:
        if p.next.data == item:
            tmp.next = p.next
            p.next = tmp
            return start
        p = p.next
    print(item, "not present in the list")
    return start


def add_at_pos(start, data, pos):
    tmp = Node(data)
    if pos == 1:
        tmp.next = start
        start = tmp
        return start
    p = start
    i = 1
    while i < pos - 1 and p is not None:
        p = p.next
        i += 1
    if p is None:
        print("There are less than", pos, "elements")
    else:
        tmp.next = p.next
        p.next = tmp
    return start


def delete_node(start, data):
    if start is None:
        print("List is Empty")
        return start
    if start.data == data:
        tmp = start
        start = start.next
        tmp = None
        return start
    p = start
    while p.next is not None:
        if p.next.data == data:
            tmp = p.next
            p.next = tmp.next
            tmp = None
            return start
        p = p.next
    print(data, "not found in the list")
    return start


def reverse_list(start):
    prev = None
    ptr = start
    while ptr is not None:
        after = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = after
    start = prev
    return start


def delete_all_list(start):
    ptr = start
    while ptr is not None:
        temp = ptr.next
        ptr = None
        ptr = temp
    return start


if __name__ == "__main__":
    start = None
    while True:
        print("\n1. Create List")
        print("2. Display")
        print("3. Count")
        print("4. Search")
        print("5. Add to empty list/ Add at beginning")
        print("6. Add at end")
        print("7. Add after node")
        print("8. Add before node")
        print("9. Add at position")
        print("10. Delete")
        print("00. For Delete whole list")
        print("11. Reverse")
        print("12. Quit\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            start = create_list(start)
        elif choice == 2:
            display(start)
        elif choice == 3:
            count(start)
        elif choice == 4:
            item = int(input("Enter the element to be searched: "))
            search(start, item)
        elif choice == 5:
            data = int(input("Enter the element to be inserted: "))
            start = add_at_beg(start, data)
        elif choice == 6:
            data = int(input("Enter the element to be inserted: "))
            start = add_at_end(start, data)
        elif choice == 7:
            data = int(input("Enter the element to be inserted: "))
            item = int(input("Enter the element after which to insert: "))
            start = add_after(start, data, item)
        elif choice == 8:
            data = int(input("Enter the element to be inserted: "))
            item = int(input("Enter the element before which to insert: "))
            start = add_before(start, data, item)
        elif choice == 9:
            data = int(input("Enter the element to be inserted: "))
            pos = int(input("Enter the position at which to insert: "))
            start = add_at_pos(start, data, pos)
        elif choice == 10:
            data = int(input("Enter the element to be deleted: "))
            start = delete_node(start, data)
        elif choice == 00:
            start = delete_all_list(start)
            if start is None:
                print("Linked list is deleted successfully")
        elif choice == 11:
            start = reverse_list(start)
        elif choice == 12:
            break
        else:
            print("Wrong choice")
