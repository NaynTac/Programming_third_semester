# Лабораторная работа №3
**Задача**: Разработайте программу на языке Python, которая будет строить **бинарное дерево** (_дерево, в каждом узле которого может быть только два потомка_). Отображение результата в виде словаря (как базовый вариант решения задания).

**Параметры дерева**: *Root* = 8; *height* = 4, *left_leaf* = root + root/2, *right_leaf* = root^2
___

**Код**:
```python
def gen_bin_tree(height=4, root=8, right_leaf=lambda x: x * x, left_leaf=lambda x: x + x / 2):
    """
    Функция gen_bin_tree() принимает на вход 4 аргумента: 2 типа int и два типа function <lambda>
    height отвечает за высоту дерева, root – за корень дерева, right_leaf и left_leaf – за значение листьев дерева

    При высоте, равной нулю, выводим только корень бинарного дерева
    При отрицательной высоте дерева не существует => ничего не возвращаем

    Возвращаем словарь, ключом в котором является корень, а значением – кортеж листьев
    Листья в кортеже представляют из себя результаты работы функции при меньшей на 1 высоте

    """
    # При высоте, равной нулю, выводим только корень бинарного дерева
    if height == 0:
        return (root)

    if height < 0:
        return None

    while height > 1:
        left = left_leaf(root)
        right = right_leaf(root)

        return {root: (gen_bin_tree(height - 1, left), gen_bin_tree(height - 1, right))}

    return {root: (root + root/2, root**2)}


print(gen_bin_tree())

"""
Получившееся бинарное дерево при значениях gen_bin_tree(4, 8):
{8:(
    {12.0: (
        {18.0:(
            {27.0: (
                40.5, 729.0
            )}, 
            {324.0: (
                486.0, 104976.0
            )}
        )},
        {144.0: (
            {216.0: (
                324.0, 46656.0
            )}, 
            {20736.0: (
                31104.0, 429981696.0
            )}
        )}
    )},
    {64: (
        {96.0: (
            {144.0: (
                216.0, 20736.0
            )}, 
            {9216.0: (
                13824.0, 84934656.0
            )}
        )},
        {4096: (
            {6144.0: (
                9216.0, 37748736.0
            )}, 
            {16777216: (
                25165824.0, 281474976710656
            )}
        )}
    )}
)}

"""
```
___
**Тесты**:
```python
from binTree import gen_bin_tree

if __name__ == "__main__":
    
    import unittest
    
    class TestFindIndex(unittest.TestCase):
    
        def test_1(self):
            self.assertEqual(gen_bin_tree(1, 8), {8: (12, 64)})
            
        def test_2(self):
            self.assertEqual(gen_bin_tree(2, 8), {8: ({12: (18, 144)}, {64: (96, 4096)})})
            
        def test_3(self):
            self.assertEqual(gen_bin_tree(3, 8), {8: ({12: ({18: (27, 324)}, {144: (216, 20736)})},
            {64: ({96: (144, 9216)}, {4096: (6144, 16777216)})})})
            
        def test_4(self):
            self.assertEqual(gen_bin_tree(1, 6), {6: (9, 36)})
            
        def test_5(self):
            self.assertEqual(gen_bin_tree(2, 6), {6: ({9: (13.5, 81)}, {36: (54, 1296)})})
            
        def test_6(self):
            self.assertEqual(gen_bin_tree(3, 6), {6: ({9: ({13.5: (20.25, 182.25)}, {81: (121.5, 6561)})},
            {36: ({54: (81, 2916)}, {1296: (1944, 1679616)})})})

        def test_zero(self):
            self.assertEqual(gen_bin_tree(0), 8)

        def test_neg(self):
            self.assertEqual(gen_bin_tree(-1), None)
        
    unittest.main()
```
**Результат тестов**:
```
........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```
