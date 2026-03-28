#!/usr/bin/python3
"""Defines Node and SinglyLinkedList classes."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
            data (int): The node data.
            next_node (Node, optional): The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a sorted singly linked list."""

    def __init__(self):
        """Initialize empty list."""
        self.__head = None

    def __str__(self):
        """Return string representation of the list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Insert a new Node in sorted order."""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
