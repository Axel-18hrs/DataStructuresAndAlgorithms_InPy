from Interfaces.ImethodLists import ImethodLists
from Classes.Nodes.Node import Node


class SimpleList(ImethodLists):
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        # case 1: List is empty
        if self.is_empty():
            self.head = new_node
            return

        # case 2: The data already exists
        if self.exist(data):
            print(f"- [{data}] Ya existe en la lista")
            return

        # case 3: Head has a data greater than that of the new node
        if self.head.data > new_node.data:
            new_node.next = self.head
            self.head = new_node
            return

        # case 3: The list is not empty
        current_node = self.head
        while current_node.next is not None and current_node.next.data < new_node.data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        pass

    def remove(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacia")
            return

        # case 2: the head has the courage to remove
        if self.head.data == data:
            print(f"- Dato[{data}] Se elimino de la lista")
            self.head = self.head.next
            return

        # case 3: Any of the following nodes has the data to be removed
        current_node = self.head
        while current_node.next is not None and current_node.next.data < data:
            current_node = current_node.next

        # case 4: The node to be removed was found
        if current_node.next.data == data:
            print(f"- Dato[{data}] Se elimino de la lista")
            current_node.next = current_node.next.next
            return

        # case 5: Node not found
        print(f"- Dato[{data}] No Existe en la lista")
        pass

    def exist(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacía")
            return False

        # case 2: The 'head' node contains the data
        if self.head.data == data:
            return True

        # case 3: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not None and current_node.next.data <= data:
            current_node = current_node.next

        # case 4: The data already exists in the list
        if current_node.data == data:
            return True

        # case 5: We reached the end and found nothing
        return False
        pass

    def search(self, data):
        # case 1: List is empty
        if self.is_empty():
            print("// La lista esta vacía")
            return False

        # case 2: The 'head' node contains the data
        if self.head.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        # case 3: Any node in the list can have the data
        current_node = self.head
        while current_node.next is not None and current_node.next.data <= data:
            current_node = current_node.next

        # case 4: The data already exists in the list
        if current_node.data == data:
            print(f"- Dato[{data}] Existe en la lista")
            return

        # case 5: We reached the end and found nothing
        print(f"- Dato[{data}] No Existe en la lista")
        return
        pass

    def show(self):
        # case 1: List is empty.
        if self.is_empty():
            print("// La lista esta vacía")
            return

        # case 2: List is not empty or is not None
        print("=== Mi lista simple ===")
        i = 0
        current_node = self.head
        while True:
            print(f"- Nodo[{i}] y dato: {current_node.data}")
            current_node = current_node.next
            i += 1
            if current_node is None:
                break
        pass

    def show_reverse(self):
        # Case 1: If the list is empty
        if self.is_empty():
            print("Empty list.")
            return

        temArr = []
        current_node = self.head
        i = 0
        while current_node is not None:
            i += 1
            temArr.append(current_node.data)
            current_node = current_node.next

        stack_array = list(reversed(temArr))

        for node in stack_array:
            i -= 1
            print(f"- Node[{i}] and data: {node}")
        pass

    def is_empty(self):
        return self.head is None
        pass

    def clear(self):
        self.head = None
        pass
