from FindIndex import find_index

if __name__ == "__main__":
    
    import unittest
    
    class TestFindIndex(unittest.TestCase):
    
        def test_with_target(self):
            self.assertEqual(find_index([2, 7, 11, 15], 9), [0, 1])
            self.assertEqual(find_index([3, 2, 4], 6), [1, 2])
            self.assertEqual(find_index([3, 3], 6), [0, 1])
        
        def test_without_target(self):
            self.assertEqual(find_index([2, 7, 11, 15], 11), -1)
            self.assertEqual(find_index([3, 2, 4], 8), -1)
        
    unittest.main()
