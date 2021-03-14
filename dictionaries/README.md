## Dictionaries Defined
 
# Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.
# When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary, the key is specified first, followed by the corresponding value, separated by a colon. For example, animals = { "bears":10, "lions":1, "tigers":2 } creates a dictionary with three key value pairs, stored in the variable animals. The key "bears" points to the integer value 10, while the key "lions" points to the integer value 1, and "tigers" points to the integer 2. You can access the values by referencing the key, like this: animals["bears"]. This would return the integer 10, since that’s the corresponding value for this key.
# You can also check if a key is contained in a dictionary using the in keyword. Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False.
# Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists. You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals["zebras"] = 2. This creates the new key in the animal dictionary called zebras, and stores the value 2. You can modify the value of an existing key by doing the same thing. So animals["bears"] = 11 would change the value stored in the bears key from 10 to 11. Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals["lions"] you would remove the key value pair from the animals dictionary.

## Iterating Over Dictionaries
 
# You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values associated with the keys, you could use the keys as indexes. Or you can use the items method on the dictionary, like dictionary.items(). This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.
# If you only wanted to access the keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). If you only wanted the values, you could use the values() method: dictionary.values().

# When I plan on searching for a specific element, I will use dictionaries.


## Dictionary Methods Cheat Sheet
 
## Dictionary Methods Cheat Sheet
## Definition
x = {key1:value1, key2:value2} 
Operations
•	len(dictionary) - Returns the number of items in the dictionary
•	for key in dictionary - Iterates over each key in the dictionary
•	for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
•	if key in dictionary - Checks whether the key is in the dictionary
•	dictionary[key] - Accesses the item with key key of the dictionary
•	dictionary[key] = value - Sets the value associated with key
•	del dictionary[key] - Removes the item with key key from the dictionary
Methods
•	dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
•	dict.keys() - Returns a sequence containing the keys in the dictionary
•	dict.values() - Returns a sequence containing the values in the dictionary
•	dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
•	dict.clear() - Removes all the items of the dictionary
Check out the official documentation for dictionary operations and methods. 


Algo
1, In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, values in wardrobe.items():
    for value in values:
        print("{} {}".format(value, key))
 

# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

# def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for users, groups in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))

5. The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to complete this function.

