from binTreeAlt import gen_bin_tree

if __name__ == "__main__":
    
    import unittest
    
    class TestFindIndex(unittest.TestCase):
    
        def test_1(self):
            self.assertEqual(gen_bin_tree(1, 8), [[8], [12, 64]])
            
        def test_2(self):
            self.assertEqual(gen_bin_tree(2, 8), [[8], [12, 64], [18, 144, 96, 4096]])
            
        def test_3(self):
            self.assertEqual(gen_bin_tree(3, 8), [[8], [12, 64], [18, 144, 96, 4096],
                [27, 324, 216, 20736, 144, 9216, 6144, 16777216]])
            
        def test_4(self):
            self.assertEqual(gen_bin_tree(1, 6), [[6], [9, 36]])
            
        def test_5(self):
            self.assertEqual(gen_bin_tree(2, 6), [[6], [9, 36], [13.5, 81, 54, 1296]])
            
        def test_6(self):
            self.assertEqual(gen_bin_tree(3, 6), [[6], [9, 36], [13.5, 81, 54, 1296],
                [20.25, 182.25, 121.5, 6561, 81, 2916, 1944, 1679616]])
        
    unittest.main()
