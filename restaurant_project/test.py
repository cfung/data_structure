from linked_list import Node, LinkedList
#from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    #self.array = [None for number in range(size)]
    self.array = [LinkedList() for i in range(self.array_size)]
    
  def hash(self, key):
    # use encode to get the byte representation of string
    hash = sum(key.encode())
    return hash
  
  # array has a fixed length, use modulo to get position
  def compress(self, hash_code):
    #print ("compress: ", hash_code % self.array_size)
    return hash_code % self.array_size

  
  def assign(self, key, value):
  	
    array_index = self.compress(self.hash(key))
    #self.array[array_index] = [key, value]
    print ("array_index is...: ", array_index)
    
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        #return
    list_at_array.insert(payload) 
    #print ("what is list_at_array: ", list_at_array)
      
        
  
  def retrieve(self, key):
    #print ("trying to retrieve...: ", key)
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      #print ("what is item[0] and key: {0},{1}: ".format(item[0], key))
      if item[0] == key:
        return item[1]
      #else:
    print ("returning None...")
    return None


blossom = HashMap(len(flower_definitions)) 
for element in flower_definitions:
  print ("element is...", element)
  blossom.assign(element[0], element[1])

print ('daisy: ', blossom.retrieve('daisy')) 
print ('begonia: ', blossom.retrieve('begonia'))
print ('chrysanthemum: ',blossom.retrieve('chrysanthemum'))
print ('carnation: ',blossom.retrieve('carnation'))
print ('daisy: ',blossom.retrieve('daisy'))
print ('hyacinth: ',blossom.retrieve('hyacinth')) # None
print ('lavender: ',blossom.retrieve('lavender'))
print ('magnolia: ',blossom.retrieve('magnolia'))
print ('morning glory: ',blossom.retrieve('morning glory')) # None
print ('periwinkle: ',blossom.retrieve('periwinkle'))
print ('poppy: ',blossom.retrieve('poppy'))
print ('rose: ',blossom.retrieve('rose'))  # None
print ('snapdragon: ',blossom.retrieve('snapdragon'))
print ('sunflower: ',blossom.retrieve('sunflower'))
print ('wisteria: ',blossom.retrieve('wisteria'))  # None

#blossom.assign('rose', 'red')
print (blossom.retrieve('rose'))
