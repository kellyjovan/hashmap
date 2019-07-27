import unittest
from hashmap import HashMap

class HashMapTest(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap()

    def populate(self, values):
        for value in values:
            self.hashmap.put(*value)

    def remove(self, values):
        for value in values:
            self.hashmap.remove(value)

    def test_put(self):
        # Can add to hashmap
        self.hashmap.put('Apples', 5)
        self.assertEqual(self.hashmap.get('Apples'), 5)
        
        # Size should increase with added elements 
        self.assertEqual(self.hashmap.size(), 1)

        # Hashmap should no longer be marked as empty
        self.assertEqual(self.hashmap.is_empty(), False)

        # Should still work with multiple items added
        fruits = [
            ('Oranges', 1), ('Pineapples', 10), ('Mangos', 7),
            ('Grapefruit', 9), ('Avocado', 53), ('Blueberry', 16),
            ('Strawberries', 42), ('Cherries', 21), ('Durian', 18),
            ('Guava', 99), ('Blackberries', 53), ('Cranberries', 42)]
        
        self.populate(fruits)

        # All inputted items should be retrievable
        for fruit in fruits:
            self.assertEqual(self.hashmap.get(fruit[0]), fruit[1])

        self.assertEqual(self.hashmap.size(), len(fruits) + 1)

        # Should be able to override pre-existing values
        self.hashmap.put('Apples', 20)
        self.assertEqual(self.hashmap.get('Apples'), 20)

        # Should not increase hashmap size
        self.assertEqual(self.hashmap.size(), len(fruits) + 1)

    def test_remove(self):
        # Should work if hashmap contains only one element in bucket
        self.hashmap.put('Apples', 15)
        self.hashmap.remove('Apples')
        self.assertEqual(self.hashmap.get('Apples'), None)


        fruits = [('Oranges', 1), ('Bananas', 2), ('Pineapples', 10), ('Mangos', 7)]
        self.populate(fruits)

        # Should remove pre-existing element
        self.hashmap.remove('Bananas')
        self.assertEqual(self.hashmap.get('Bananas'), None)

        # Size should decrease
        self.assertEqual(self.hashmap.size(), len(fruits) - 1)

        for fruit in fruits:
            self.hashmap.remove(fruit[0])

        # Hash Map should be empty
        self.assertEqual(self.hashmap.size(), 0)
        self.assertEqual(self.hashmap.is_empty(), True)

    def test_resize(self):
        # Initialize HashMap with Initial Capacity of 4
        self.hashmap = HashMap(4)
        self.assertEqual(self.hashmap.capacity(), 4)

        fruits = [('Oranges', 1), ('Bananas', 2), ('Pineapples', 10), ('Mangos', 7)]
        self.populate(fruits)
        
        # Hashmap should double in capacity
        self.assertEqual(self.hashmap.size(), 4)
        self.assertEqual(self.hashmap.capacity(), 8)

        # Items should still be accessible
        for fruit in fruits:
            self.assertEqual(self.hashmap.get(fruit[0]), fruit[1])

        for fruit in fruits:
            self.hashmap.remove(fruit[0])

        # Hashmap should halve in size
        self.assertEqual(self.hashmap.capacity(), 4)

    def test_mixed_calls(self):
        fruits = [
            ('Oranges', 1), ('Pineapples', 10), ('Mangos', 7),
            ('Grapefruit', 9), ('Avocado', 53), ('Blueberries', 16),
            ('Strawberries', 42), ('Cherries', 21), ('Durian', 18),
            ('Guava', 99), ('Blackberries', 53), ('Cranberries', 42)
        ]
        
        self.populate(fruits)

        # Hashmap capacity should increase
        self.assertEqual(self.hashmap.capacity() > 8, True)

        fruits_to_remove = {'Grapefruit', 'Cherries', 'Guava', 'Oranges'}

        # Remove fruits from hashmap
        for fruit in fruits_to_remove:
            self.hashmap.remove(fruit)

        # Checks to make sure they are all deleted
        self.remove(fruits_to_remove)

        remaining = len(fruits) - len(fruits_to_remove)
        self.assertEqual(self.hashmap.size(), remaining)

        # Make sure all other fruits are still fine
        for fruit, val in fruits:
            if fruit in fruits_to_remove: continue
            self.assertEqual(self.hashmap.get(fruit), val)

        # Add some more fruits
        additional_fruits = [('Longan', 32), ('Pomegranate', 82), ('Papaya', 92)]
        self.populate(additional_fruits)

        # Size should update accordingly
        new_size = remaining + len(additional_fruits)
        self.assertEqual(self.hashmap.size(), new_size)

        # Updating some existing fruit values
        updates = [('Papaya', 53), ('Cranberries', 32), ('Durian', 9)]
        self.populate(updates)

        # Size should not increase
        self.assertEqual(self.hashmap.size(), new_size)

        additional_fruits_to_remove = {
            'Longan', 'Pomegranate', 'Papaya', 'Strawberries', 'Blueberries',
            'Blackberries', 'Durian', 'Cranberries'
        }
        fruits_to_remove = fruits_to_remove.union(additional_fruits_to_remove)

        self.remove(fruits_to_remove)
        # Hashmap size should be a quarter of its capacity, capacity should halve
        self.assertEqual(self.hashmap.capacity(), 8)

if __name__ == '__main__':
    unittest.main()