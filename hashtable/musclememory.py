

class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    # this is the node for the hash table
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table with 'capacity' buckets that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = [None] * capacity
    
    def fnv1(self, key):
        """
        FNV-1 64-bit hash function
        todo - 64 bit? 
        Implement this and/or DJB2.
        """

        # def fnv64(str):
        #     # todo - Come back to this

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1
        """

        string_key = str(key).encode()
        hash = 5381
        for x in string_key:
            hash = ((hash << 5) + hash) + x
        return hash &0xFFFFFFFF
    
    def djb2_alt(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5)) + hash + ord(x)
        return hash & 0xffffffff

    # todo TEST THIS ALTERNATE VERSION

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value): 
        # hash the key using your hash_index function so that you can put it in its hashed index location
        hIndx = hash_index(key)

        # creating a new node (called hashNode) inside of your hash table by passing the key-value input to the HashTableEntry function
        # hashNode is the case holding your information that you're going to put into your hashed index
        hashNode = HashTableEntry(key, value)

        # increase the length of the table by 1
        self.length += 1
       
        # name the space found for your key-value input, 'bucket'
        # bucket is the index in the table the hashNode will go into
        bucket = self.capacity[hIndx]

        # while there's something in the bucket you found, 
        while bucket is not None:

            # if that something has a key which matches the key of your input,...
            if bucket.key == key:

                # ...put or add the new value in your input's tuple to that key
                # todo is that actually a tuple?, no right because it's immutable
                bucket.value == value

                # if this happens, exit the put loop
                return

            # if the key finds not match, iterate by setting the current bucket to its next bucket, in the context of the 'bucket is not None loop' until you hit the next condition, in which there's an empty bucket reached
            bucket = bucket.next

        # if you find the bucket at that index is empty... 
        if bucket == None:
            
            # this part is fucking confusing
            # make your new hashNode the head of the table by making the empty index its next node
            hashNode.next = self.capacity[hIndx]

            # then set that hashed index the head of the list or table
            self.capacity[hIndx] = hashNode

        """
        Store the value with the given key.
        # todo - store a key and its value in a list as a node
        Hash collisions should be handled with Linked List Chaining.
        # todo - search for the hash value, if it's found, make that node it's found in the head node of a linked list and add the colliding value to that new list's tail
        Implement this.
        """



#     def delete(self, key):
#         """
#         Remove the value stored with the given key:

#         Prints a warning if the key is not found.

#         Implement this.
#         """
    
#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.

#         Returns None if the key is not found.

#         Implement this.
#         """
    
#     def resize(self):
#         """
#         Doubles the capacity of the hash table and rehash all key/value pairs.

#         Implement this.
#         """

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

    

if __name__ == "__main__":
    ht = HashTable(2)
    # todo Why is a 2 passed into this? 

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    

    print(ht.djb2("hello"))
    print(ht.djb2_alt("hello"))




# LECTURE EXAMPLE
# """
# [ "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
#    0        1        2        3      4       5              6             7
# ​
# "beej"
# "elit"
# ​
# f("elit") -> 7
# f("ipsum") -> 1
# f("ipsum") -> 1
# f("foobar") -> 1
# ​
# 1. Get bytes for the key
# 2. Make up a function that returns an index for those bytes
#    * Adding the bytes
#    * Modding with the hash table size
# """
# # How many slots the hash table has

# hash_table_size = 8
# ​
# # Space to hold values
# hash_table = [None] * hash_table_size
# ​
# def myhash(s):
# 	"""
# 	Naive hashing function to turn a string into a number.
# ​
# 	Don't use this in real life, ever. It's a horrible hashing function.
# ​
# 	* It doesn't give a nice uniform distribution over the space
# 	* Collisions are far more common than they need to be
# ​
# 	Output is 32 bits.
# 	"""
# ​
# 	# Convert the argument to a string, and then to the bytes of that
# 	# string:
# 	str_bytes = str(s).encode()
# ​
# 	total = 0
# ​
# 	# Loop through all the bytes
# 	for b in str_bytes:
# 		total += b
# ​
# 		total &= 0xffffffff  # clamp to 32 bits
# ​
# 		# To make your DJB2 hash correct, add this as the last line of the loop:
# 		#total &= 0xffffffff  # 32-bit (8 f's)
# ​
# 		# To make your FNV-1 hash correct, add this as the last line of the loop:
# 		#total &= 0xffffffffffffffff  # 64-bit (16 f's)
# ​
# 	return total
# ​
# def hash_index(s):
# 	"""
# 	Take a hash value and make sure it's in the range of the size
# 	of the hash table (so it won't fall out of bounds).
# 	"""
# 	h = myhash(s)
# ​
# 	return h % hash_table_size
# ​
# def put(key, value):
# 	"""
# 	Store a value in the table by a key.
# 	"""
# 	# Get the index into the hash table list
# 	index = hash_index(key)
# 	hash_table[index] = value
# ​
# def get(key):
# 	"""
# 	Get a value from the table by a key.
# 	"""
# 	index = hash_index(key)
# 	return hash_table[index]
# ​
# def delete(key):
# 	"""
# 	Delete a value in the table by a key.
# 	"""
# 	index = hash_index(key)
# 	hash_table[index] = None
# ​
# if __name__ == "__main__":
# 	# If running from the command line
# 	print(hash_index("Hello"))  # 4
# 	print(hash_index("foobar"))  # 1
# 	print(hash_index("cats"))
# 	print(hash_index("beej"))
# 	print(hash_index("foobaz"))  # 1, collision
# 	print(hash_index("qux"))
# ​
# 	put("Hello", 37)   # similar to dict: d["Hello"] = 37
# 	put("foobar", 128)
# 	put("cats", "dogs")
# ​
# 	print(hash_table)
# ​
# 	print(get("Hello"))  # 37
# ​
# 	print(get("Hello"))
# 	print(get("beej"))
# 	print(get("foobar"))
# ​
# 	delete("Hello")
# 	print(get("Hello"))  # None
# 
# 

# **********************************************