""" linked_list.py

Student: Edvin Lundberg
Mail: edvin.lundberg@gmail.com
Reviewed by: Axel Wohlin
Date reviewed: 28/04
"""


class LinkedList:
    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):  # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):  # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print("(", end="")
        f = self.first
        while f:
            print(f.data, end="")
            f = f.succ
            if f:
                print(", ", end="")
        print(")")

    # To be implemented

    def length(self):  # Optional
        """Returns the number of elements in list"""
        count = 0

        f = self.first
        while f:
            count += 1
            f = f.succ
        return count

    def mean(self):  # Optional
        """Returns the mean of list elements"""
        sum = 0

        f = self.first
        while f:
            sum += f.data
            f = f.succ
        return sum / self.length()

    def remove_last(self):  # Optional
        """Removes and returns last element in list"""
        f = self.first
        if f is None:
            raise ValueError
        elif f.succ:
            while f.succ.succ:
                f = f.succ
            last_e = f.succ.data
            f.succ = None
        else:
            last_e = f.data
            self.first = None

        return last_e

    def remove(self, x):  # Compulsory
        """Removes first instance of x, returns True/False weather successful"""
        f = self.first
        output = False

        if f:
            if f.data == x:
                output = True
                self.first = f.succ

            else:
                while f.succ:
                    if f.succ.data == x:
                        output = True
                        f.succ = f.succ.succ
                        break
                    f = f.succ

        return output

    def count(self, x):  # Optional
        """Returns number of x in list"""

        def _count(f, x):
            count = 0
            if f:
                if f.data == x:
                    count += 1 + _count(f.succ, x)
                else:
                    count += _count(f.succ, x)
            return count

        return _count(self.first, x)

    def to_list(self):  # Compulsory
        """Returns LinkedList data as Python list"""

        def _to_list(f):
            if f == None:
                return []
            else:
                return [f.data] + _to_list(f.succ)

        return _to_list(self.first)

    def remove_all(self, x):  # Compulsory
        """Removes all instances of x, and returns number of nodes removed."""

        def _remove_all(f, x):
            count = 0
            if f:
                if f.data == x:
                    self.first = f.succ
                    count += 1 + _remove_all(f.succ, x)
                elif f.succ:
                    if f.succ.data == x:
                        f.succ = f.succ.succ
                        count += 1 + _remove_all(f, x)
                    else:
                        count += _remove_all(f.succ, x)
            return count

        return _remove_all(self.first, x)

    def __str__(self):  # Compulsary
        string = "("
        for e in self:
            if string[-1].isdigit():
                string += ", "
            string += f"{e}"
        string += ")"
        return string

    def _copy(self):  # CompulsaryFF
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    """ Complexity for this implementation: 
    Växer med o(n^2) (Σ(n)) i insert, samt Θ(n) i for loopen.
    Alltid värsta scenario eftersom self är sorterad minst -> störst
    och insert behöver därmed traversera alla noder för varje nod som ska läggas till
    """

    def copy(self):  # Compulsary, should be more efficient
        """Returns an copy of self with no shared nodes"""
        ll_copy = LinkedList()
        p_list = self.to_list()
        for x in reversed(p_list):
            ll_copy.insert(x)
        return ll_copy

    """ Complexity for this implementation:
    Växer med Θ(n) i to_list(), samt Θ(n) i for loopen.
    Insert behöver aldrig gå längre än första nod så är konstant.
    """

    def __getitem__(self, ind):  # Optional
        i = 0
        for x in self:
            if i == ind:
                return x
            i += 1
        raise IndexError(f"Linked-List index out of range")


class Person:  # Compulsory
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self, other):
        return self.name[0] < other.name[0]

    def __le__(self, other):
        return self.name[0] <= other.name[0]

    def __eq__(self, other):
        return self.name[0] == other.name[0]


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7, 9]:
        lst.insert(x)
    lst.print()

    # Test code for remove_all method:
    print(lst.remove_all(9))
    lst.print()

    print(lst.remove_all(1))
    lst.print()

    print(lst.remove_all(5))
    lst.print()

    print(lst.remove_all(2))
    print(lst.remove_all(3))
    print(lst.remove_all(7))
    print(lst.first)
    print(lst)

    # Test code for Person class:
    p = Person("John Doe", 8401280000)
    plist = LinkedList()

    plist.insert(p)
    print(plist)

    q = Person("Erik Svensson", 7705020000)
    plist.insert(q)
    print(plist)


if __name__ == "__main__":
    main()
