""" bst.py

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Axel Wohlin
Date reviewed: 28/04
"""

from linked_list import LinkedList
from random import random


class BST:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):  # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):  # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        """Inserts key as new leaf in BTS"""

        def _insert(r, key):
            if r is None:
                return self.Node(key)
            elif key < r.key:
                r.left = _insert(r.left, key)
            elif key > r.key:
                r.right = _insert(r.right, key)
            else:
                pass  # Already there
            return r

        self.root = _insert(self.root, key)

    def iter_insert(self, key):
        """Inserts key as new leaf in BTS"""
        if self.root:
            r = self.root
            while r.key != key:
                if key < r.key:
                    if r.left:
                        r = r.left
                    else:
                        r.left = self.Node(key)
                        break
                else:
                    if r.right:
                        r = r.right
                    else:
                        r.right = self.Node(key)
                        break
        else:
            self.root = self.Node(key)

    def print(self):
        """Prints representations of BTS, in order of size"""

        def _print(r):
            if r:
                _print(r.left)
                print(r.key, end=" ")
                _print(r.right)

        _print(self.root)

    def contains(self, k):
        """True if value is in BTS"""
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def rec_contains(self, key):
        """True if value is in BTS"""

        def _contains(r, key):
            if r == None:
                result = False
            elif r.key == key:
                result = True
            else:
                if key < r.key:
                    result = _contains(r.left, key)
                else:
                    result = _contains(r.right, key)

            return result

        return _contains(self.root, key)

    def size(self):
        """Returns number of nodes in BST"""

        def _size(r):
            if r is None:
                return 0
            else:
                return 1 + _size(r.left) + _size(r.right)

        return _size(self.root)

    #
    #   Methods to be completed
    #

    def height(self):  # Compulsory
        """Returns BTSs longest chain (in number of nodes)"""

        def _height(r):
            if r is None:
                return 0
            else:
                return 1 + max(_height(r.left), _height(r.right))

        return _height(self.root)

    def __str__(self):  # Compulsory
        string = "<"
        for e in self:
            if string[-1].isdigit():
                string += ", "
            string += f"{e}"
        string += ">"
        return string

    def to_list(self):  # Compulsory
        """Returns BST data in Python List format"""
        p_list = []
        for e in self:
            p_list.append(e)
        return p_list

    def to_LinkedList(self):  # Compulsory
        """Returns BST data in LinkedList format"""
        ll = LinkedList()
        p_list = self.to_list()
        for e in reversed(p_list):
            ll.insert(e)
        return ll

    def get_smallest(self, r=None):
        """Returns smallest value in given tree/subtree"""
        if r:
            while r.left:
                r = r.left
        else:
            r = self.root
            self.get_smallest(r)
        return r.key

    def get_largest(self, r=None):
        """Returns largest value in given tree/subtree"""
        if r:
            while r.right:
                r = r.right
        else:
            r = self.root
            self.get_largest(r)
        return r.key

    def remove(self, key):
        """Removes key from BST without damaging structure"""

        def _remove(r, k):  # Compulsory
            if r is None:
                return None
            elif k < r.key:
                r.left = _remove(r.left, k)
                # r.left = left subtree with k removed
            elif k > r.key:
                r.right = _remove(r.right, k)
                # r.right =  right subtree with k removed
            else:  # This is the key to be removed
                if r.left is None:  # Easy case
                    return r.right
                elif r.right is None:  # Also easy case
                    return r.left
                else:  # This is the tricky case.
                    sub = self.get_smallest(r.right)
                    # Find the smallest key in the right subtree
                    r.key = sub
                    # Put that key in this node
                    r.right = _remove(r.right, sub)
                    # Remove that key from the right subtree
            return r  # Remember this! It applies to some of the cases above

        self.root = _remove(self.root, key)

    def ipl(self):  # Compulsory
        """Returns the internal path legnth of the BST"""

        def _ipl(r, n=1):
            if r == None:
                return 0
            else:
                return n + _ipl(r.left, n + 1) + _ipl(r.right, n + 1)

        return _ipl(self.root)


def random_tree(n):  # Useful
    bst = BST()
    for _ in range(n):
        bst.insert(random())
    return bst


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.iter_insert(x)
    t.print()
    print()

    print("size  : ", t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.rec_contains(k)}")

    print("\nA random BST with:")
    for n in [10, 100, 1000, 10000, 100000]:
        ran_tree = random_tree(n)
        print(
            f"""{n} nodes
    height of {ran_tree.height()}
    mean node height: {ran_tree.ipl() / n}
    """
        )


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? 
    Ja,
    lka effektiv som existerande metod, fast enklare att skriva
2. computing height?
    Nej
3. contains?
    Nja,
    Det går, men är inte lika effektiv, theta(n)
4. insert?
    Nej
5. remove?
    Nej


Results for ipl of random trees
===============================
# TEST RESULTS
A random BST with:
10 nodes
    height of 6
    mean node height: 3.7
    
100 nodes
    height of 16
    mean node height: 7.67
    
1 000 nodes
    height of 21
    mean node height: 11.425
    
10 000 nodes
    height of 32
    mean node height: 16.7104
    
100 000 nodes
    height of 41
    mean node height: 21.8331


# MEAN NODE HEIGHT
Teoretiska uttrycket, 1.39log2(n) + O(1), ger:
1.39log2(10) + O(1)      = 4.617480052 + O(1)
1.39log2(100) + O(1)     = 9.234960104 + O(1)
1.39log2(1 000) + O(1)   = 13.85244016 + O(1)
1.39log2(10 000) + O(1)  = 18.46992021 + O(1)
1.39log2(100 000) + O(1) = 23.08740026 + O(1)

Experiment resultatet avviker från det teoretiska värdet 
som kan tillskrivas slumpen av random_tree, 
att uttrycket baseras på det "genomsnittliga trädet" 
samt den okända konstanten O(1).
Dock så växer de på liknande sätt.


# HEIGHT
Höjden verkar öka med andtingen en potensfunktion, i stil med h = sqr(n)
eller en logaritmisk, kasnke h = 8*lg(x)
Tillväxten avtar med större storlek på träden, högre n gav även 
mer varierande test resultat.
"""
