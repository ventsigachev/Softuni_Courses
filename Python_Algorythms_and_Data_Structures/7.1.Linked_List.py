class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def represent_link_list(self):
        ll_list = []
        curr_node = self.head
        if curr_node:
            while curr_node:
                ll_list.append(curr_node.data)
                curr_node = curr_node.next
            print(ll_list)
        else:
            print("The Linked List is empty!")

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_new_header(self, value):
        curr_header = self.head
        new_header = Node(value)
        self.head = new_header
        new_header.next = curr_header

    def add_specific_node(self, value, specification):
        new_node = Node(value)
        specific_node = None
        curr_node = self.head
        while curr_node:
            if curr_node.data == specification:
                specific_node = curr_node
                break
            curr_node = curr_node.next
        next_node = specific_node.next
        specific_node.next = new_node
        new_node.next = next_node

    def delete_node(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next


ll = LinkedList()
ll.add_node("A")
ll.add_node("B")
ll.add_node("C")
ll.add_node("D")
ll.add_node("E")
ll.represent_link_list()
ll.add_new_header("0")
ll.represent_link_list()
ll.add_specific_node("S", "B")
ll.represent_link_list()
ll.delete_node("D")
ll.represent_link_list()
