"""
lab 12, 1 task rrr
random edit 1
"""

from arrays import Array, ArrayExpanded
from abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = ArrayExpanded(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        if len(self) == len(self._items):
            self._items.grow()
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        if len(self) <= len(self._items) // 4 and \
           len(self._items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            self._items.shrink()
        return oldItem
    def lst_items(self):
        """To get a list of all items in a stack"""
        res = []
        while self.isEmpty() == False:
            res.append(self.pop())
        return res

class Palindrome:
    """To search for palindroms"""
    def __init__(self):
        """Init function"""
        self.file_to_read = None
        self.file_to_write = None

    def read_file(self, file_name):
        """To read file and return a list of words"""
        lst = []
        with open(file_name, 'r', encoding='utf-8') as fil:
            for line in fil:
                line = line.strip().split()[0]
                if line[:4] == "+cs=":
                    line = line[4:]
                lst.append(line)
        return lst

    @staticmethod
    def write_to_file(filename, lst):
        """To write words to file"""
        with open(filename, 'w') as fil:
            for i in range(len(lst)):
                fil.write(lst[i] + '\n')
        fil.close()

    def find_palindromes(self, input_file, output_file_name):
        """To search for palindroms"""
        lst_words = self.read_file(input_file)
        result_words = []
        for i in range(len(lst_words)):
            stack_i = ArrayStack()
            lst_i = list(lst_words[i])

            for j in range(len(lst_words[i])):
                stack_i.push(lst_words[i][j])

            lst_letters = stack_i.lst_items()

            if lst_letters == lst_i:
                result_words.append(lst_words[i])

        self.write_to_file(output_file_name, result_words)
        return result_words



if __name__ == "__main__":
    pal = Palindrome()
    print(pal.find_palindromes('base (1).lst' , 'palindrome_ukr.txt'))
    # print(pal.read_file('words.txt'))
    # print(pal.find_palindromes('probe.txt'))
