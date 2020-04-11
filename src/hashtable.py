# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        # if two values hash to the same int, set self.next of the first value to the current LinkedPair
        # prev.self.next = current
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        curr_node = self
        curr_val = f"{curr_node.value}"
        while curr_node.next is not None:
            curr_val += f" ->> {curr_node.next.value}"
            curr_node = curr_node.next
        return curr_val

    def find(self, key):
        while self.key != key:
            if self.key != key and self.next is not None:
                self = self.next
        return self


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity, items=0):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.items = items

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hashed = hash(key)
        return hashed

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)
        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.
        Fill this in.
        '''
        # if self.items > self.capacity * 1.5:
        #     self.resize()
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        last_pair = None

        while current_pair is not None and current_pair.key != key:
            print('Warn: Collision detected for key ' + key)
            last_pair = current_pair
            current_pair = last_pair.next
        if current_pair is not None:
            current_pair.value = value
        else:
            new_pair = LinkedPair(key, value)
            self.items += 1
            new_pair.next = self.storage[index]
            self.storage[index] = new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        self.storage[index] = None

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        return self.storage[index].find(key).value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        # create new array of size * 2
        self.storage = [None] * self.capacity
        # move all values to new array
        for pair in old_storage:
            if pair is not None:
                next_pair = pair
                while next_pair is not None:
                    self.insert(next_pair.key, next_pair.value)
                    next_pair = next_pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")