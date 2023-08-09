class Node:
    def __init__(self,value) -> None:
        """

        :param value:
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        """

        :param value:
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def make_empty(self) -> None :
        """

        :return:
        """
