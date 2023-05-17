class ConsCell:
  def __init__(self, h, t):
    """Creates a new cell with head == h, and tail == t."""
    self.head = h
    self.tail = t

class List:
  """Describes a simple list data type."""

  def __init__(self, n):
    """creates a new list with n as the first element."""
    self.start = n

  def cons(self, e):
    """Adds a new element into the list; hence, procuding a new list."""
    return List(ConsCell(e, self.start))

  def length(self):
    """Returns the number of elements in the list."""
    len = 0
    cell = self.start
    while cell != 0:
       len += 1
       cell = cell.tail
    return len
    
  def append1(self, l): 
      new_list = List(0)
      cell = self.start
      while cell != 0:
          new_list = new_list.cons(cell.head)
          cell = cell.tail 
      cell = l.start
      while cell != 0:
          new_list = new_list.cons(cell.head)
          cell = cell.tail
      return new_list.reverse()
  
  
  def append(self,l): 

  
  def reverse(self): 
    reversed_list = List(0)
    cell = self.start
    while cell != 0: 
        reversed_list = List.cons(reversed_list, cell.head)
        cell = cell.tail
    return reversed_list
    
  def reverseMe(self): 
      self = self.reverse()
  
  def sort(self): 
      sorted_list = List(0)
      cell_i = self.start
      selected = [False for i in range(self.length())]
      idx = 0
      while(cell_i != 0): 
          cell_j = self.start
          maior = cell_i.head
          maior_idx = idx
          if selected[idx] == True: 
              cell_k = self.start
              idx_k = 0
              while cell_k != 0: 
                  if not selected[idx_k]:
                      maior = cell_k.head
                      maior_idx = idx_k
                      break
                  idx_k += 1
          idx_j = 0
          while cell_j != 0: 
              if cell_j.head > maior and selected[idx_j] == False: 
                  maior = cell_j.head
                  maior_idx = idx_j
              cell_j = cell_j.tail
              idx_j += 1 
          idx += 1
          print(maior)
          selected[maior_idx] = True
          sorted_list = sorted_list.cons(maior)
          
          cell_i = cell_i.tail
      print(selected)
      return sorted_list
                  
  
  
  def __str__(self):
    """Returns a textual representation of this list."""
    ans = "["
    cell = self.start
    while cell != 0:
      ans = ans + repr(cell.head)
      cell = cell.tail
      if cell != 0:
        ans = ans + ", "
    ans = ans + "]"
    return ans

def test():
  a = List(0)
  a = a.cons(9)
  a = a.cons(6)
  a = a.cons(4)
  b = List(0)
  b = b.cons(1)
  b = b.cons(3)
  b = b.cons(5)
  b = b.cons(2)
  c = b.cons("Hi!")
  d = b.cons(True)
  e = d.cons(False)
  print("List a = ", a.__str__(), " Length(a) = ", a.length())
  print( "List b = ", b.__str__(), " Length(b) = ", b.length())
  print(a.append(b))

test()
