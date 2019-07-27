from list_node import ListNode

class HashMap:
    def __init__(self, initial_capacity=8):
        self.__initial_capacity = initial_capacity
        self.curr_capacity = initial_capacity
        self.curr_size = 0
        self.map = [None for i in range(initial_capacity)]

    def __hash(self, key):
        """
        Hashes key into an index within the map arr

        Parameters
        ----------
        key :   str
            Key to be hashed

        Returns:
        int
            Index of bucket within map arr
        """
        char_arr = [char for char in key]

        sum = 0
        for char in char_arr:
            sum += ord(char)

        return sum % self.curr_capacity

    def __should_grow(self):
        """Checks whether it is appropriate for the map to double it's capacity."""

        return self.curr_size / self.curr_capacity > .75
        
    def __should_shrink(self):
        """Checks whether it is appropriate for the map to halve it's capacity."""

        return self.curr_capacity > self.__initial_capacity and self.curr_size / self.curr_capacity < .25

    def __add_to_bucket(self, map, bucket_indx, node):
        """"
        Given a bucket (linked list of nodes), update node value or add to end of bucket

        Parameters
        ----------
        bucket  :   ListNode
            List of nodes that collided within the same bucket
        key     :   str
            Key of newly added or soon to be updated node
        value   :   any
            Value of newly added or new value of previously existing node
        """

        bucket = map[bucket_indx]

        if not bucket:
            map[bucket_indx] = node
        else:
            curr_node = bucket
            while curr_node:
                if curr_node.key == node.key:
                    curr_node.val = node.val
                    return # no need to go further, just updating value
                
                if not curr_node.next: break
                curr_node = curr_node.next

            curr_node.next = node
            node.prev = curr_node

        self.curr_size += 1

    def __resize(self, new_size):
        """
        Handles resizing of hashmap

        Parameters
        ----------
        new_size    :   int
            New hashmap capacity
        """

        new_map = [None for i in range(new_size)]

        self.curr_capacity = new_size
        self.curr_size = 0

        # Iterate through old array of buckets
        for old_bucket in self.map:
            if not old_bucket: continue
            
            curr_node = old_bucket
            # Traverse through all elements in the old bucket, then reassign them to their new home
            while curr_node:
                bucket_indx = self.__hash(curr_node.key)
                
                self.__add_to_bucket(new_map, bucket_indx, ListNode(curr_node.key, curr_node.val))
                curr_node = curr_node.next

        self.map = new_map

    def get(self, key):
        """
        Given a key, checks to see if it exist withing the hashmap and returns its value

        Parameters
        ----------
        key : str
            key mapped to value within hashmap
        
        Returns
        ----------
        any
            value paired with key
        """

        hash = self.__hash(key)
        bucket = self.map[hash]

        if not bucket: return None
        
        curr_node = bucket
        while curr_node:
            if curr_node.key == key:
                return curr_node.val
            
            curr_node = curr_node.next

        return None

    def put(self, key, value):
        """
        Add/Updates an key/value pair to hashmap

        Parameters
        ----------
        key     :   str
            key to access value from hashmap
        value   :   any
            value binded to key
        """

        bucket_indx = self.__hash(key)

        new_node = ListNode(key, value)
        self.__add_to_bucket(self.map, bucket_indx, new_node)

        if self.__should_grow():
            self.__resize(self.curr_capacity * 2)


    def remove(self, key):
        """
        Removes key-value from hashmap

        Parameters
        ----------
        key : str
            key of item in hashmap
        """

        hash = self.__hash(key)
        bucket = self.map[hash]

        if not bucket: return
        
        curr_node = bucket

        while curr_node:
            if curr_node.key == key:
                if not curr_node.prev:
                    self.map[hash] = curr_node.next
                else:
                    curr_node.prev.next = curr_node.next
                
                if curr_node.next:
                    curr_node.next.prev = curr_node.prev

                self.curr_size -= 1
                break
            
            curr_node = curr_node.next


        if self.__should_shrink():
            self.__resize(self.curr_capacity // 2)

    def size(self):
        """Returns current size of hashmap."""
        return self.curr_size

    def capacity(self):
        """Returns current capacity of hashmap."""
        return self.curr_capacity

    def is_empty(self):
        """Returns whether or not hashmap is empty."""
        return self.curr_size == 0