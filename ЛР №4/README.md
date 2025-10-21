# Лабораторная работа №4
**Задача**: Разработайте программу на языке Python, которая будет строить **бинарное дерево** (_дерево, в каждом узле которого может быть только два потомка_). Отображение результата в виде словаря (как базовый вариант решения задания). Решить нерекурсивным методом

**Параметры дерева**: *Root* = 8; *height* = 4, *left_leaf* = root + root/2, *right_leaf* = root^2
___

**Код**:
```python
def gen_bin_tree(height, root, left_branch=lambda root: 1.5 * root, right_branch=lambda root: root**2):

    """
    Создаем список из пустых списков в количестве,
    равном высоте дерева + 1. Заполяем его первое значение
    """

    data = [[] for x in range(height + 1)]
    data[0] = [root]

    """
    Заполняем списки по порядку рассмотрения дерева
    """

    for i in range(height):
        for j in range(2**i):
            data[i + 1].append(left_branch(data[i][j]))
            data[i + 1].append(right_branch(data[i][j]))

    return data


"""
Результат работы функции при аргументах height = 4, root = 8:

[
[8],
[12.0, 64],
[18.0, 144.0, 96.0, 4096],
[27.0, 324.0, 216.0, 20736.0, 144.0, 9216.0, 6144.0, 16777216],
[40.5, 729.0, 486.0, 104976.0, 324.0, 46656.0, 31104.0, 429981696.0, 216.0, 20736.0, 13824.0, 84934656.0, 9216.0, 37748736.0, 25165824.0, 281474976710656]
]
"""
```
___
**Тесты**:
```python
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
```
**Результат тестов**:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK
```
