class Node:
    def __init__(self, value=None):
      self.value = value
      self.next = None

class LinkedList:
    def __init__(self):
      self.head = None
      
    def print_list(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    
    def back(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last_elem = self.head
        while(last_elem.next):
            last_elem = last_elem.next
        last_elem.next = new_node
        

list_1 = LinkedList()

for x in range(10):
    list_1.back(x)
    
list_1.print_list()