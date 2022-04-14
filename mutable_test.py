import unittest
from hypothesis import given
import hypothesis.strategies as st

from binary_tree_mutable import *

class TestMutableTree(unittest.TestCase):
    '''test from_list and to_list'''
    def test_toAndfrom_list(self):
        list1 = []
        tree1 = BinaryTree()
        tree1.from_list(list1)
        self.assertEqual(tree1.to_list(), list1)
        list2 = [2, 1, 3]
        tree2 = BinaryTree()
        tree2.from_list(list2)
        self.assertEqual(tree2.to_list(), list2)

    '''test fineElem'''
    def test_findElem(self):
        list1 = [3, 1, 2, 4]
        tree1 = BinaryTree()
        tree1.from_list(list1)
        self.assertEqual(tree1.findElem(1)[0], True)
        self.assertEqual(tree1.findElem(3)[0], True)
        self.assertEqual(tree1.findElem(2)[0], True)
        self.assertEqual(tree1.findElem(5)[0], False)
        list2 = []
        tree2 = BinaryTree()
        tree2.from_list(list2)
        self.assertEqual(tree2.findElem(1)[0], False)

    '''test add'''
    def test_add(self):
        tree1 = BinaryTree()
        self.assertEqual(tree1.add(2), True)
        self.assertEqual(tree1.add(2), False)
        self.assertEqual(tree1.add(1), True)
        self.assertEqual(tree1.add(3), True)

    '''test delete'''
    def test_delete(self):
        tree = BinaryTree()
        self.assertEqual(tree.delete(0), False)
        tree.from_list([5, 3, 8, 1, 4, 6, 10])
        self.assertEqual(tree.delete(1), True)
        self.assertEqual(tree.delete(3), True)
        self.assertEqual(tree.delete(8), True)

    '''test getsize'''
    def test_getSize(self):
        tree = BinaryTree()
        self.assertEqual(tree.getSize(), 0)
        list1 = [1, 2, 3, 4]
        tree.from_list(list1)
        self.assertEqual(tree.getSize(), len(list1))

    '''test filter'''
    def test_filter(self):
        def isEven(data):
            if data % 2 == 0:    return True
            else: return False
        tree1 = BinaryTree()
        list1 = [1, 2, 3, 4]
        tree1.from_list(list1)
        tree1.filter(isEven)
        self.assertEqual(tree1.to_list(), [2, 4])
        tree2 = BinaryTree()
        list2 = [11, 7, 5, 9, 4, 6, 8, 13]
        tree2.from_list(list2)
        tree2.filter(isEven)
        self.assertEqual(tree2.to_list().sort(), [8, 6, 4].sort())

    '''test map'''
    def test_map(self):
        def plus1(data):
            return data +1
        tree1 = BinaryTree()
        tree1.map(plus1)
        self.assertEqual(tree1.to_list(), [])
        list1 = [1, 2, 3, 4, 5]
        tree1.from_list(list1)
        tree1.map(plus1)
        self.assertEqual(tree1.to_list(),[2, 3, 4, 5, 6])

    '''test reduce'''
    def test_reduce(self):
        def sum1(data):
            return data
        tree1 = BinaryTree()
        list1 = [1, 2, 3]
        tree1.from_list(list1)
        self.assertEqual(tree1.reduce(sum1), 6)

    '''test mempty'''
    def test_mempty(self):
        tree = BinaryTree()
        mempty = tree.mempty()
        self.assertEqual(mempty.to_list(), BinaryTree().to_list())

    '''test monoid'''
    def test_monoid(self):
        tree1 = BinaryTree()
        tree1.from_list([])
        tree2 = BinaryTree()
        tree2.from_list([])
        mconcat1 = tree1.mconcat(tree2)
        mconcat2 = tree2.mconcat(tree1)
        self.assertEqual(mconcat1.to_list(), mconcat2.to_list())
        
        tree3 = BinaryTree()
        list3 = [1, 2, 3, 4]
        tree3.from_list(list3)
        mconcat3 = tree3.mconcat(tree2)
        mconcat4 = tree2.mconcat(tree3)
        self.assertEqual(mconcat3.to_list(), mconcat4.to_list())
        
        tree4 = BinaryTree()
        list4 = [3, 1, 5]
        tree4.from_list(list4)
        mconcat5 = tree3.mconcat(tree4)
        mconcat6 = tree4.mconcat(tree3)
        self.assertEqual(mconcat5.to_list().sort(), mconcat6.to_list().sort())

    '''test iter and next'''
    def test_iter_next(self):
        tree1 = BinaryTree()
        list1 = [1, 2, 3, 4]
        tree1.from_list(list1)
        it = tree1.__iter__()
        for i in list1:
            self.assertEqual(tree1.stack[it].ele, i)
            it = tree1.__next__()

if __name__ == '__main__':
    unittest.main()