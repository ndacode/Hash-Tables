

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



class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    

    def __init__(self, capacity):
        self.capacity = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        string_key = str(key).encode()
        hash = 5381
        for x in string_key:
            hash = ((hash << 5) + hash) + x
        return hash & 0xFFFFFFFF

        # hash = 5381
        #     for x in string_key:
        #         hash = (( hash << 5) + hash) + ord(x)
        #     return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")


    print(ht.djb2("hello"))