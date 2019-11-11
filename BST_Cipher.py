#  File: BST_Cipher.py

#  Description: Using a BST with a specific key, encrypt and decrypt passages. 

#  Student Name: Marissa Green

#  Student UT EID: mdg3554

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/21/19

#  Date Last Modified: 4/22/19
class Node (object):
  def __init__(self, data = None):
    self.data = data
    self.lchild = None
    self.rchild = None
    
class Tree (object):
  # the init() function creates the BST with the encryption string
  # If the encryption string contains any character other than the
  # characters 'a' through 'z' or the space character drop that character.
  def __init__ (self, encrypt_str):
    # create root
    self.root = None

    # create rest of tree
    for ch in encrypt_str:
      # filter through st and only encrypt valid chars
      if (ord(ch) > 96 and ord(ch) < 123) or ord(ch) == 32:
        self.insert(ch)
        
  # the insert() function adds a node containing a character in the BST
  # if the character already exists, it doesn't add that character
  def insert (self, ch):
    node = Node(ch)

    # tree is empty
    if self.root == None:
      self.root = node

    
    else:
      current = self.root
      parent = self.root

      # find where to put node
      while current != None:
        parent = current
        if ch == current.data:
          break
        elif ch < current.data:
          current = current.lchild
        elif ch > current.data:
          current = current.rchild

      # found where to put node
      if ch < parent.data:
        parent.lchild = node
      elif ch > parent.data:
        parent.rchild = node
        
  # the search() function will search for a character in the BST
  # and return a string containing a series of lefts (<) and rights (>)
  # needed to reach that character
  # return a blank string if the character does not exist in the tree.
  # return * if the character is the root of the tree.
  def search (self, ch):
    current = self.root
    parent = self.root
    search_str = ""
    
    if self.root.data == ch:
      return "*"

    while current != None:
      parent = current
      if ch == current.data:
        return search_str
      elif ch < current.data:
        search_str += "<"
        current = current.lchild
      elif ch > current.data:
        search_str += ">"
        current = current.rchild

    if ch == parent.data:
      return search_str
    else:
      return ""

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    
    for ch in st:
      if current != None:
        if ch == "*":
            return self.root.data
        elif ch == "<":
          current = current.lchild
        elif ch == ">":
          current = current.rchild
      else:
        return ""

    if current != None:
      return current.data
    else:
      return ""

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    st = st.lower()
    encrypted_str = ""
    
    for ch in st:
      # filter through st and only encrypt valid chars
      if (ord(ch) > 96 and ord(ch) < 123) or ord(ch) == 32:
        encrypted_str += self.search(ch) + "!"

    return encrypted_str[:-1] # don't need last "!"

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    decrypted_str = ""
    st = st.split("!")
    
    for ch in st:
      decrypted_str += self.traverse(ch)

    return decrypted_str

def main ():
  key = input("Enter encryption key: ")
  print()
  tree = Tree(key)
    
  encrypt_str = input("Enter string to be encrypted: ")
  print("Encrypted string:", tree.encrypt(encrypt_str))
  print()

  decrypt_str = input("Enter string to be decrypted: ")
  print("Decrypted string:", tree.decrypt(decrypt_str))
  
main ()
