'''
All of your code (unless you choose the Trie implementation mentioned below) will be written in script.py.

The data is stored in data.py and imported into script.py so you can properly access the data. You also have access to various data structures. If these data structures don't fit your needs for the project, feel free to make up your own variations! We just ask that you do NOT utilize Python's built-in list class to handle your data.

This project consists of main two parts:

Implementing an autocomplete for food types that returns a list of possible food types based on the beginning of a word. You'll use the data stored in food_types, which is a list of all the different types of food the user can select from. It is up to you how to properly store and retrieve the data. Some possible options are listed under the Part 1 section.
Retrieving and displaying all of the restaurant data. This data is stored in restaurant_data, which is currently a list of lists. The first value in each list is the food type, the second value is the restaurant name, the third value is the price, the fourth value is the rating, and the fifth value is the address. It is up to you how to properly store and retrieve the data. Some possible options are listed under the Part 2 section.
'''

from linked_list import Node, LinkedList
from restaurant_lib import restaurant_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    #self.array = [None for number in range(size)]
    self.array = [LinkedList() for i in range(self.array_size)]
    
  def hash(self, key):
    hash = sum(key.encode())
    return hash
  
  def compress(self, hash_code):
  	return hash_code % self.array_size
  
  def assign(self, key, value):
  	
    array_index = self.compress(self.hash(key))
    #self.array[array_index] = [key, value]
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if key == item[0]:
        item[1] = value
    #print ("what is list_at_array: ", list_at_array)
    list_at_array.insert(payload)   
        
  
  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for item in list_at_index:
      if key == item[0]:
        return item[1]
      else:
        return None


blossom = HashMap(len(flower_definitions)) 
for elememt in flower_definitions:
	blossom.assign(elememt[0], elememt[1])
print ('daisy: ', blossom.retrieve('daisy')) 
print ('begonia: ', blossom.retrieve('begonia'))
print ('wisteria: ',blossom.retrieve('wisteria'))
print 
print (blossom.retrieve('rose'))
#blossom.assign('rose', 'red')
print (blossom.retrieve('rose'))




