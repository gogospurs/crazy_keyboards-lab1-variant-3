from typing import Optional, TypeVar, Tuple, Callable, Generic, Union
from typing import List, Any

T = Union[int, float]


class TreeNode(object):
    def __init__(self, elem: T, left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None) -> None:
        '''initial function'''
        self.ele: T = elem
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root: Optional['TreeNode'] = None) -> None:
        '''initial function'''
        self.root = root
        self.stack: List[TreeNode] = []
        self.it = -1

    def __iter__(self) -> int:
        '''iter function, if root not exists, return -1'''
        if self.root is not None:
            self.it = 0
            self.stack = []
            queue = [self.root]
            self.stack.append(self.root)
            while queue:
                currNode = queue.pop(0)
                if currNode.left:
                    queue.append(currNode.left)
                    self.stack.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                    self.stack.append(currNode.right)
        else:
            self.it = -1
        return self.it

    def __next__(self) -> int:
        '''get the next iterator, if unsatisfied, raise StopIteration'''
        if (self.it >= len(self.stack)) or (self.it == -1):
            raise StopIteration
        else:
            self.it += 1
            return self.it

    def findElem(self, item: T) -> Tuple[bool,Optional[TreeNode],
                                           Optional[TreeNode]]:
        '''find the node which its elem equal to the item,
        if not exists, return False'''
        parentNode = None
        currNode = None
        if self.root is None:
            print("the set is empty")
            res = False
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if abs(currNode.ele - item) < 1e-9:
                    res = True
                    # if item is equal to the root.ele, return node
                    break
                elif currNode.ele - item > 0:
                    if currNode.left is not None:
                        parentNode = currNode
                        # search the left child tree
                        queue.append(currNode.left)
                    else:                 # the item is not in the set
                        currNode = None
                        parentNode = None
                        res = False
                        break
                else:
                    if currNode.right is not None:
                        parentNode = currNode
                        # search the right child tree
                        queue.append(currNode.right)
                    else:
                        parentNode = None
                        currNode = None
                        res = False
                        break
        return (res, parentNode, currNode)

    def add(self, item: T) -> bool:
        '''add node to tree, if the value is exists, return False'''
        node = TreeNode(item)           # instance of the node
        res: bool = False
        if(self.root is None):          # if the set is empty
            self.root = node
            res = True
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                if abs(currNode.ele - item) < 1e-9:  # if the item is already in the set
                    print("the item is already in the set")
                    res = False
                    break
                elif currNode.ele - item > 0:
                    if currNode.left:
                        # if the item is smaller than the currNode.ele
                        queue.append(currNode.left)
                    else:
                        currNode.left = node
                        res = True
                        break
                else:          # if the item is larger than the currNode.ele
                    if currNode.right:
                        queue.append(currNode.right)
                    else:
                        currNode.right = node
                        res = True
                        break
        return res

    def delete(self, item: T) -> bool:
        '''delete the item, if not exist, return False'''
        # search the item wheather in the set
        res, parentNode, currNode = self.findElem(item)
        if not res:
            # if item does not in the set, return false
            return False
        else:
            if currNode:
                parentOfInsteadNode: Optional[TreeNode] = None
                insteadNode: Optional[TreeNode] = None
                if currNode.left is not None:
                    parentOfInsteadNode = currNode
                    insteadNode = currNode.left
                    if insteadNode.right is not None:
                        while insteadNode.right is not None:
                            parentOfInsteadNode = insteadNode
                            insteadNode = insteadNode.right
                        parentOfInsteadNode.right = insteadNode.left
                        insteadNode.left = currNode.left
                    insteadNode.right = currNode.right
                    currNode.left = None
                    currNode.right = None
                elif currNode.right is not None:
                    parentOfInsteadNode = currNode
                    insteadNode = currNode.right
                    if insteadNode.left is not None:
                        while insteadNode.left is not None:
                            parentOfInsteadNode = insteadNode
                            insteadNode = insteadNode.left
                        parentOfInsteadNode.left = insteadNode.right
                        insteadNode.right = currNode.right
                    currNode.right = None
                else:
                    parentOfInsteadNode = None
                    insteadNode = None
                if parentNode is not None:
                    if parentNode.left == currNode:
                        parentNode.left = insteadNode
                    else:
                        parentNode.right = insteadNode
                else:
                    self.root = insteadNode
        return True

    def getSize(self) -> int:
        '''get size of tree'''
        if self.root is None:
            return 0        # if the set is empty, return 0
        else:               # count the size
            size = 0
            # queue for count
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                size += 1
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            return size

    def to_list(self) -> List[Any]:
        '''transfer tree to list'''
        res: List[Any] = []
        if self.root is None:
            return res
        else:
            queue = [self.root]
            while queue:
                currNode = queue.pop(0)
                res.append(currNode.ele)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        return res

    def from_list(self, tlist: List[Any]) -> None:
        '''build tree from list'''
        if tlist != []:
            for i in tlist:
                self.add(i)
        return

    def filter(self, func: Callable[[T], bool]) -> None:
        '''filter the node, the rule is defined by func'''
        self.it = self.__iter__()
        if self.it != -1:
            de_stack = []
            while self.it < len(self.stack):
                value = self.stack[self.it].ele
                if func(value) is False:
                    de_stack.append(self.stack[self.it])
                    self.stack.pop(self.it)
                else:
                    self.__next__()
            for item in de_stack:
                self.delete(item.ele)
        return

    def map(self, func: Callable[[T], Any]) -> None:
        '''map the node, the rule is defined by func'''
        self.it = self.__iter__()
        if self.it == -1:
            return
        else:
            map_queue = []
            delete_queue = []
            while self.it < len(self.stack):
                currNode = self.stack[self.it]
                map_value = func(currNode.ele)
                if map_value in map_queue:
                    delete_queue.append(currNode)
                else:
                    map_queue.append(map_value)
                self.__next__()
            for value in delete_queue:
                self.delete(value.ele)
                self.stack.remove(value)
            self.it = self.__iter__()
            while self.it < len(self.stack):
                currNode = self.stack[self.it]
                currNode.ele = func(currNode.ele)
                self.__next__()
            return

    def reduce(self, func: Callable[[T], T]) -> T:
        '''reduce the tree node to int'''
        it = self.__iter__()
        value: T = 0
        while it < len(self.stack):
            value += func(self.stack[self.it].ele)
            it = self.__next__()
        for item in self.stack:
            self.delete(item.ele)
        newNode = TreeNode(value)
        self.add(value)
        self.stack = [newNode]
        return value

    def mempty(self) -> 'BinaryTree':
        '''get mempty of BinaryTree'''
        return BinaryTree()

    def mconcat(self, tree: 'BinaryTree') -> None:
        '''mconcat of two tree'''
        if tree.root:
            it = tree.__iter__()
            while it < len(tree.stack):
                self.add(tree.stack[it].ele)
                it = tree.__next__()
            tree.__iter__()
            return
        else:
            return
