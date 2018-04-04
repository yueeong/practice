from arrseq import ArraySequences

arr_methods = ArraySequences()

print(arr_methods.anagram_checker('abc', 'a b c'))

from linkedlist import Node

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c
c.next_node = a

