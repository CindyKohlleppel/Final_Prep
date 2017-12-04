from operator import mul, add
from functools import reduce
"""
>>> digits = [1,8,2,8]
>>> len(digits)
4
>>> digits[3]
8
>>> [2,7] + digits * 2
[2,7,1,8,2,8,1,8,2,8]
>>> pairs = [[10,20], [30,40]]
>>> pairs[1]
[30,40]
>>> pairs[1][0]
30
"""

"""
>>> digits = [1,8,2,8]
>>> count(digits,8)
2
"""
digits = [1,8,2,8]
def count(s, value):
    total, index = 0,0
    while index < len(s):
        if s[index] == value:
            total += 1
        index += 1
    return total

"""
>>> digits = [1,8,2,8]
>>> count(digits, 8)
2
"""
def count2(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total

pairs = [[1,2],[2,2],[2,3],[4,4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count += 1

print("same_count is: ", same_count)

print(range(1,10))
print(list(range(5,8)))
print(list(range(4)))

for _ in range(3):
    print('Go Bears!')

odds = [1,3,5,7,9]
print([x+1 for x in odds])
print([x for x in odds if 25 % x == 0])


def divisors(n):
    return [1] + [x for x in range(2,n) if n % x == 0]

print(divisors(4))
print(divisors(12))

print([n for n in range(1, 1000) if sum(divisors(n)) ==n ])

def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * width + 2 * height

def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

area = 80
print(width(area, 5))
print(perimeter(16, 5))
print(perimeter(10,8))
print(minimum_perimeter(area))
print([minimum_perimeter(n) for n in range(1,10)])

def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

print(reduce(mul, [2,4,8], 1))

def divisors_of(n):
    divides_n = lambda x: n % x == 0
    return [1] + keep_if(divides_n, range(2,n))

print(divisors_of(12))

def sum_of_divisors(n):
    return reduce(add, divisors_of(n), 0)

def perfect(n):
    return sum_of_divisors(n) == n

print(keep_if(perfect, range(1,1000)))

apply_to_all = lambda map_fn, s: list(map(map_fn, s))
keep_if = lambda filter_fn, s: list(filter(filter_fn, s))

def product(s):
    return reduce(mul, s)

#product([1, 2, 3, 4, 5])
print(digits)
print(2 in digits)
print(1828 not in digits)

# Slicing
"""
Sequences contain smaller sequences within them. 
A slice of a sequence is any contiguous span of the original sequence, designated by a pair of integers. 
As with the range constructor, the first integer indicates the starting index of the slice and the second indicates one beyond the ending index.
In Python, sequence slicing is expressed similarly to element selection, using square brackets. 
A colon separates the starting and ending indices. 
Any bound that is omitted is assumed to be an extreme value: 0 for the starting index, and the length of the sequence for the ending index.
"""
print(digits[0:2])
print(digits[1:])

#Strings

print('I am string!')
print("I've got an apostrophe")

city = "Berkeley"
print(len(city))
print(city[3])

print("Berkeley" + " , CA")
print("Shabu " * 2)

print("here" in "Where's Waldo")

print(str(2) + ' is an element of ' + str(digits))

#Tree Class
def tree(root, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

# def right_binarize(tree):
#     """Construct a right-branching binary tree."""
#     if is_leaf(tree):
#         return tree
#     if len(tree) > 2:
#         tree = [tree[0], tree[1:]]
#     return [right_binarize(b) for b in tree]
#
# print(right_binarize([1, 2, 3, 4, 5, 6, 7]))


t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(t)
print(root(t))
print(branches(t))
print(root(branches(t)[1]))
print(is_leaf(t))
print(is_leaf(branches(t)[0]))

"""
Tree-recursive functions can be used to construct trees. 
For example, the nth Fibonacci tree has a root value of the nth Fibonacci number and, for n > 1, two branches that are also Fibonacci trees. 
A Fibonacci tree illustrates the tree-recursive computation of a Fibonacci number.
"""

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = root(left) + root(right)
        return tree(fib_n, [left, right])

print(fib_tree(5))

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)

print(count_leaves(fib_tree(5)))

"""
Partition trees. Trees can also be used to represent the partitions of an integer. 
A partition tree for n using parts up to size m is a binary (two branch) tree that represents the choices taken during computation. 
In a non-leaf partition tree:
        the left (index 0) branch contains all ways of partitioning n using at least one m,
        the right (index 1) branch contains partitions using parts up to m-1, and
        the root value is m.
The values at the leaves of a partition tree express whether the path from the root of the tree to the leaf represents a successful partition of n
"""
def partition_tree(n, m):
    """Returns a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])

print(partition_tree(2, 2))

def print_parts(tree, partition = []):
    if is_leaf(tree):
        if root(tree):
            print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(root(tree))
        print_parts(left, partition, [m])
        print_parts(right, partition)

print(print_parts(partition_tree(6,4)))