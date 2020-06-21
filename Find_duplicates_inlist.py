# Check for duplicates in list

my_list = ['a','b','c','b','d','m','n','n']

duplicates = []

for items in my_list:
    if my_list.count(items) > 1:
         
         if items not in duplicates:
             duplicates.append(items)
print(duplicates)
