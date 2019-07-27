# Hashmap
Hashmap (with amortized constant time look-ups) implemented in python

# Usage
```
from hashmap import Hashmap

# Initialize hashmap with an inital capacity size, defaults to 8
hashmap = Hashmap(initial_capacity)

# Retrieve value associated with key from hashmap
hashmap.get(key) 

# Add key-value pair or update existing pair in hashmap
hashmap.put(key, value)

# Remove key-value pair from hashmap
hashmap.remove(key)

# Check if hashmap is empty
hashmap.is_empty()

# Get the number of elements currently in hashmap
hashmap.size()

# Get current_capacity of hashmap
hashmap.capacity()
```

# Test
```
python hashmap.test.py
```
