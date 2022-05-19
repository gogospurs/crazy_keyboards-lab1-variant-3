from typing import List, Union
import unittest
from hypothesis import given
import hypothesis.strategies as st
from binary_tree_mutable import *


class Test(unittest.TestCase):
    @given(st.lists(st.integers()))
    def test_toAndfrom_list(self, list1: List[T]) -> None:
        '''test from_list and to_list int version'''
        tree1 = BinaryTree()
        tree1.from_list(list1)
        self.assertEqual(sorted(tree1.to_list()), sorted(list(set(list1))))

    def test_findElem(self) -> None:
        '''test fineElem'''
        tree1 = BinaryTree()
        list1: List[Union[int, float]] = [2, 1.0, 3.1]
        tree1.from_list(list1)
        for value in list1:
            self.assertEqual(tree1.findElem(value)[0], True)
        for value in [2.0, 3]:
            if value not in list1:
                self.assertEqual(tree1.findElem(value)[0], False)
        tree2 = BinaryTree()
        list2: List[T] = []
        tree2.from_list(list2)
        self.assertEqual(tree2.findElem(0)[0], False)

    def test_add(self) -> None:
        '''test add'''
        tree1 = BinaryTree()
        self.assertEqual(tree1.add(2), True)
        self.assertEqual(tree1.add(2), False)
        self.assertEqual(tree1.add(1), True)
        self.assertEqual(tree1.add(3.0), True)

    def test_delete(self) -> None:
        '''test delete'''
        tree = BinaryTree()
        self.assertEqual(tree.delete(0), False)
        tree.from_list([5, 3, 8, 1, 4, 6, 10])
        self.assertEqual(tree.delete(1), True)
        self.assertEqual(tree.delete(3), True)
        self.assertEqual(tree.delete(8), True)

    @given(st.lists(st.integers()))
    def test_getSize(self, list1: List[T]) -> None:
        '''test getsize'''
        tree = BinaryTree()
        self.assertEqual(tree.getSize(), 0)
        tree.from_list(list1)
        self.assertEqual(tree.getSize(), len(set(list1)))

    def test_filter(self) -> None:
        '''test filter'''
        def isEven(data: T) -> bool:
            if data % 2 == 0:
                return True
            else:
                return False
        tree1 = BinaryTree()
        list1: List[T] = [1, 2, 3, 4]
        tree1.from_list(list1)
        tree1.filter(isEven)
        self.assertEqual(tree1.to_list(), [2, 4])
        tree2 = BinaryTree()
        list2: List[T] = [11, 7, 5, 9, 4, 6, 8, 13]
        tree2.from_list(list2)
        tree2.filter(isEven)
        self.assertEqual(sorted(tree2.to_list()), sorted([8, 6, 4]))

    def test_map(self) -> None:
        '''test map'''
        tree1 = BinaryTree()
        tree1.map(str)
        self.assertEqual(tree1.to_list(), [])

        tree2 = BinaryTree()
        tree2.from_list([2, 1, 3])
        tree2.map(str)
        self.assertEqual(tree2.to_list(), ['2', '1', '3'])
        tree3 = BinaryTree()
        tree3.add(2)
        tree3.add(1)
        tree3.add(3)
        tree3.map(str)
        self.assertEqual(tree3.to_list(), ['2', '1', '3'])
        tree4 = BinaryTree()
        list2: List[T] = [-1, 1, 2]
        tree4.from_list(list2)

        def abs_(value: T) -> T:
            if value < 0:
                value = -value
            return value
        tree4.map(abs_)
        self.assertEqual(sorted(tree4.to_list()), sorted([1, 2]))

    def test_reduce(self) -> None:
        '''test reduce'''
        def sum1(data: T) -> T:
            return data
        tree1 = BinaryTree()
        list1: List[T] = [1, 2, 3]
        tree1.from_list(list1)
        self.assertEqual(tree1.reduce(sum1), 6)

    def test_mempty(self) -> None:
        '''test mempty'''
        tree = BinaryTree()
        mempty = tree.mempty()
        self.assertEqual(mempty.to_list(), BinaryTree().to_list())

    @given(st.lists(st.integers()))
    def test_monoid(self, list1: List[T]) -> None:
        '''test monoid'''
        tree1 = BinaryTree()
        tree1.from_list([])
        tree2 = BinaryTree()
        tree2.from_list(list1)
        tree3 = BinaryTree()
        tree3.from_list([])
        tree3.mconcat(tree2)
        tree2.mconcat(tree1)
        self.assertEqual(sorted(tree2.to_list()), sorted(tree3.to_list()))
        tree4 = BinaryTree()
        tree4.from_list([4, 2, 3, 1])
        tree5 = BinaryTree()
        tree5.from_list([4, 2, 1, 3])
        tree4.mconcat(tree2)
        tree2.mconcat(tree5)
        self.assertEqual(sorted(tree2.to_list()), sorted(tree4.to_list()))

    def test_iter_next(self) -> None:
        '''test iter and next'''
        tree1 = BinaryTree()
        list1: List[T] = [1, 2, 3, 4]
        tree1.from_list(list1)
        it = tree1.__iter__()
        for i in list1:
            self.assertEqual(tree1.stack[it].ele, i)
            it = tree1.__next__()


if __name__ == '__main__':
    unittest.main()
