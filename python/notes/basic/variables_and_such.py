# Basics
my_list = [ 1 , 2, 3 ]
my_dict = {}

# swap without a temp var
a, b = 1, 2
a, b = b, a

word="bar"
word_list = ['alpha','beta','gama','foo','bar']
if word in word_list:
    print("found word")

list = []
list.append("foo")

d1 = {'first': 1, 'second':2}
d2 = dict(first=1, second=2)
d3 = dict({'first': 1, 'second':2})
print(d1['first']) # 1

# Lists
list_a = [] 
list_b = []
list_a.extend(list_b)  # append list_b to list_a

list_a.sort(key=str.lower, reverse=False) # Apply str.lower to each key when doing compare
list_a.sort(key=None, reverse=False)
item='bar'
list._a.count(item) # return number of occurrences of item

# Sets
set1 = { 1,2,3,4,5} # Each element is unique (no dups). like a hash w/o a value and unordered
set1.add(9)
set1.update({2,3,10,7], {11,12}) # Add more than one element to a set -> output: { 1,2,3,4,5,9,10,7,11,12 }
set1.discard(5) # remove 5 from set. does nothing if it doesn't exist
set1.remove(5) # raise error if it does not exist 

# Dicts
key='bar'
d='foo'
d1 = {'first': 1, 'second':2}
my_dict = d1.copy()
d1.items()
d1.keys()
d1.values()
d1.pop(key,[d]) # Pop key and return value. optional default value
d1.pop(key,'not_found')


other_dict = {}.fromkeys([1,2,3], 0) # Return a new dict with keys from seq and value equal to value (0 in this case)

# Loops
for x in [ 0, 1, 3, 4 ]:
    print(x)

for k,v in my_dict.items():
    print(k,v)

for i, v in enumerate(my_list):
    print(i,v ) # Returns index of list/array and value

# Very cool: Loop over both in parallel
for f,s in zip(first_list, second_list):
    print(f,s)

for f in sorted(my_list):   # for f in reversed(sorted(set(my_list))):
    print(f)

def Functions(a,b,d=0):
    print("nothing new")
