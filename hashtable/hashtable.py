



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
        self.length = 0
        self.initial_size = capacity
        # self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        'The core of the FNV-1 hash algorithm is as follows:'
     

    def fnv32a( str ):
        hash = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in str:
            hash = hash ^ ord(s)
            hash = (hash * fnv_32_prime) % uint32_max
        return hval


        
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
        return self.djb2(key) % self.initial_size

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # for the resize, you want to check if the number of entries is more than 70% of the size of the table
        # this has to happen with the put in mind

        # hash table count
        # hast table entries 


        hIndx = self.hash_index(key)
        hashNode = HashTableEntry(key, value)
        self.length += 1
        bucket = self.capacity[hIndx]
        while bucket is not None:
            if bucket.key == key:
                bucket.value = value
                return
            bucket = bucket.next
        if bucket == None:
            hashNode.next = self.capacity[hIndx]
            self.capacity[hIndx] = hashNode

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # if the key in the input matches the key in the bucket, make it None
        hIndx = self.hash_index(key)
        bucket = self.capacity[hIndx]
        if bucket.key == key:
                bucket.key = None
                bucket.value = None
                self.length -= 1
                return

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        
        hIndx = self.hash_index(key)
        bucket = self.capacity[hIndx]
        while bucket is not None:
            if bucket.key == key:
                return bucket.value
            bucket = bucket.next
        if bucket is None:
            return None



    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        # if there's more entries in the table than there are table spaces,
        print(f'capacity: {self.capacity}, length: {self.length}')
        if self.capacity < self.length:
            
            # double the capacity size
            self.capacity * 2
            # for every entry in the table
            for i in HashTable:
                # rehash the entry
                hash_index(i)
                # put it back into the table
                put(i)
                return


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




    # refresher
#     (1)->(2)->(3)->None
#      ^
#      head


# #   Case in which the head is empty
#     None
#      ^
#      head


#     class Node:
#         def__init__(self, value):
#             self.value = value
#             self.next = None
        
#     # class HashTableEntry:
#     #     def__init__(self, key, value):
#     #         self.key = key
#     #         self.value = value
#     #         # add next to make it a linked list
#     #         self.next = None

    
    
    
#     # we need to keep track of the head, the first element of the list
#     # 

#     # Empty linked list
#     head = None 

#     # Insert (at head)

#     (99)(1)->(2)->(3)->None
#     # ^
#     #  insert at head
#     def insert_at_head(value):
#         # create the new Node
#         n = Node(value)
#         # point new node's next to current head
#         n.next = head
#         # make the new node the head
#         head = n

#         return n


#     # Append (at tail)
    
#      #  insert at tail
#               cur   n
#                v    v
#     (1)->(2)->(3)->(99)->None
#      ^
#      head

#     def append_at_tail(value):
#         n = Node(value)
#         # handle the special case for if head is None
#         if head is None:
#             head = n
#             return
#         cur = head
#         # this will fail with None as the head because cur doesn't have a next attribute
#         while cur.next is not None:
#             cur = cur.next

#         cur.next = n


#     # Find
#     cur
#      v
#     (1)->(2)->(3)->None
#      ^
#      head

#     def find(value):
#         cur = head

#         while cur is not None:
#             if cur.value == value:
#                 return cur    (you can also return the value)

#             cur = cur.next

#         return None
        

#     # Delete
#       #  delete ( skip over the node we want to cut out)   
#       #   we also need a reference to a previous node so that we can change what it's pointing to
#     prev cur
#      v    v    
#     (1)->(2)->(3)->None
#      ^
#      head
#     def delete(value):
#         global head
#         # find the node
#         cur = head
#         # Delete the head special case
#         if cur.value = value:
#             head = head.next
#             cur.next = None
#             return cur

#         prev = None

#         while cur is not None:
#             if cur.value == value:
#                 # Found it, delete it
#                 prev.next = cur.next
#                 cur.next = None
#                 return cur

#             prev = cur
#             # prev = prev.next
#             cur = cur.next

#         return None
        

