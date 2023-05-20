# acima de Queue o codigo é do professor
# aparentemente tem diversos bugs na implementação
# por exemplo, Node.n é tanto um numero (0), quanto o proximo nó
# entao pode dar errado a aplicação de hasMore()

class Worklist:
  """Describes a simple list data type."""

  def add(self, element):
    """Adds a new element into this list."""

  def remove(self):
    """Removes the next element from this list."""

  def hasMore(self):
    """Returns True if this list is not empty."""

class Node:
  """The node that must be inserted into the different lists."""
  def __init__(self):
    self.n = 0
    self.e = ''
    
  def __str__(self):
      return str(self.e) + ' ' + str(self.n)

class Stack:
  """Describes a stack data type."""

  def __init__(self):
    self.top = Node()

  def add(self, element):
    """Adds a new element into this list."""
    self.top.e = element
    aux = Node()
    aux.n = self.top
    self.top = aux

  def remove(self):
    """Removes the next element from this list."""
    self.top = self.top.n
    return self.top.e

  def hasMore(self):
    """Returns True if this list is not empty."""
    return (self.top.n != 0)


def removeAll(s):
  """Removes all the elements from the data structure."""
  while (s.hasMore()):
    print(s.remove())
    
class Queue: 
    
    def __init__(self): 
        self.top = Node()
        self.tail = Node()
    
    def add(self,element): 
        if self.top.e == '':
            self.top.e = element
            self.top.n = 0
            self.tail = self.top
        else: 
            new = Node()
            new.e = element
            new.n = 0
            self.tail.n = new
            self.tail = new
    
    def remove(self): 
        removed = self.top.e
        self.top = self.top.n
        return removed
    
    def hasMore(self): 
        return self.top != 0
       
    def __str__(self):
        cell = self.top
        string = ''
        while cell != 0: 
            string += str(cell.e) + ' '
            cell = cell.n
        return string

class PriorityQueue:
    def __init__(self):
        self.top = Node()
        self.tail = Node()
    
    def add(self,element): 
        if self.top.e == '':
            self.top.e = element
            self.top.n = 0
            self.tail = self.top
        else: 
            new = Node()
            new.e = element
            new.n = 0
            self.tail.n = new
            self.tail = new
    
    def remove(self): 
        node = self.top
        menor = self.top.e
        while node != 0: 
            node = node.n 
            if node == 0: break
            if node.e < menor: 
                menor = node.e
        node = self.top
        if menor == self.top.e: 
            self.top = self.top.n
            return menor
            
        while node != 0: 
           if node.n.e == menor: 
               node.n = node.n.n 
               break
        return menor
       
def test():
    q = PriorityQueue()
    q.add(6)
    q.add(5)
    q.add(7)
    print(q)
    print(q.remove())
    print(q.remove())
    
test()
