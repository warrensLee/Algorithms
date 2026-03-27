from typing import Optional, TypeVar
from bst import BST, BSTNode

T = TypeVar('T')


class AVL(BST):
    def getHeight(self, node: Optional[BSTNode]) -> int:
        return -1 if node is None else node.height

    def getBalance(self, node: Optional[BSTNode]) -> int:
        return 0 if node is None else self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y: Optional[BSTNode]) -> Optional[BSTNode]:                          # Right Rotation visualtiozation:
        # given a node y we assume that has two children and want to rotate right                         y           ->        x
        # so first we must identify the left child of y, which we will call x                       x                 ->           y
        # then we must identify the right child of x, which we will call T2                              T2                    T2  
        # T2 represents a temporary value as we will need to reassign it as the 
        # left child of y after rotation.
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2

        # after rotation we need to update the heights of the nodes that were involved in the rotation
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))

        # now return new root x:
        return x

    def rotateLeft(self, x: Optional[BSTNode]) -> Optional[BSTNode]:                          # Left Rotation visualtiozation:
        # given a node x we assume that has two children and want to rotate left                         x           ->        y
        # so first we must identify the right child of x, which we will call y                              y        ->    x           
        # then we must identify the left child of y, which we will call T2                              T2                     T2
        # T2 represents a temporary value as we will need to reassign it as the 
        # left child of x after rotation.
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2

        # after rotation we need to update the heights of the nodes that were involved in the rotation
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # now return new root y:
        return y


    def _insert(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # now to insert we will first act like a normal BST insert
        # then update height as recursion unwinds
        # next we will check the balance factor of each node
        # then if necessary we will perform rotations
        # finally we will return the subtree root
        
        
        # escape the recursion
        # create new node at first empty spot
        # (after correct traversal)
        if node is None:
            return BSTNode(key)

        # if we have found a node with the same key
        # that we are trying to insert
        if key == node.key:
            return node
        
        # now to recursively insert
        if key < node.key:
            node.left = self._insert(key, node.left)
        else:
            node.right = self._insert(key, node.right)

        # update height of the ancestor node because child heights might have changed by this point
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        # now get the balance factor of the ancestor node to check whether this node became unbalanced
        balance = self.getBalance(node)

        # now check for left heaviness and left child
        if balance > 1 and key < node.left.key:
            return self.rotateRight(node)
        # now check for right heaviness and right child
        if balance < -1 and key > node.right.key:
            return self.rotateLeft(node)
        # now check for left heaviness and right child
        if balance > 1 and key > node.left.key:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        # now check for right heaviness and left child
        if balance < -1 and key < node.right.key:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node
        

        

    def _remove(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # now to remove we will first act like a normal BST remove
        # then update height as recursion unwinds
        # next we will check the balance factor of each node
        # then if necessary we will perform rotations to rebalance

        # if we have found a node with the same key
        # that we are trying to insert
        if node is None:
            return node
        
        # now to recursively search
        if key < node.key:
            node.left = self._remove(key, node.left)
        elif key > node.key:
            node.right = self._remove(key, node.right)
            
        else:
            # node with 0 or 1 children:

            # no left child
            if node.left is None:
                return node.right
            # no right child
            if node.right is None:
                return node.left
            
            # node with 2 children
            temp = self._findMinimum(node.right)
            node.key = temp.key
            node.right = self._remove(temp.key, node.right)

        # update height of the ancestor node because child heights might have changed by this point
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

        # now get the balance factor of the ancestor node to check whether this node became unbalanced
        balance = self.getBalance(node)

        # now check for left heaviness and left child
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rotateRight(node)
        # now check for right heaviness and right child
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self.rotateLeft(node)
        # now check for left heaviness and right child
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        # now check for right heaviness and left child
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        
        return node

    def insert(self, key: T) -> Optional[BSTNode]:
        self.root = self._insert(key, self.root)
        return self.root

    def remove(self, key: T) -> Optional[BSTNode]:
        self.root = self._remove(key, self.root)
        return self.root
