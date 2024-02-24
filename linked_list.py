"""A normal list in python is an array that uses indexed storage.
 This means it can call upon individual elements of that array without
 cycling through all of them."""

"""A linked list cannot call upon individual components of its storage.
Rather it cycles through the list in a direction based off address nodes which
are placed with the actual information.  It cycles through until it gets what 
it needs.  It is like a FOR loop with the array list.  It checks each obj in the
list until it finds what it needs."""

#Singly Linked List
"""Unidirectional from "head" node to "tail" node"""

class Node:
    def __init__(self, data):                  #4  new_node = Node(1)
        self.data = data                       #5  data = 1
        self.next = None                       #6  since this is the last node, address to next is None

class LinkedList:
    def __init__(self):
        self.head = None                        #7  since this is the first node and no nodes exist yet, it is None                        
                                                #1  list=LinkedList()
    def append(self, data):                     #2  list.append(1)
        new_node = Node(data)                   #3  new_node = Node(1)
        if self.head is None:                   #8  Recognizes empty list
            self.head = new_node                #9  Creates new node from data in step 3
            return
        current_node = self.head                #10 Head node becomes current node (for traversal sequence)
        while current_node.next:                #since current_node became a value and is not empty,False,0, or None... The loop continues                
            current_node = current_node.next    #Current_node is now empty because we are at the end of the list again.
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(str(current_node.data), end=" -> ")
            current_node = current_node.next
        print("None")
foxtrot=LinkedList()

node1 = Node("Objectt 1")
node2 = 6
node3 = 7

foxtrot.append(Node(1))
foxtrot.append(Node(2))
foxtrot.append(Node(3))
foxtrot.print_list
