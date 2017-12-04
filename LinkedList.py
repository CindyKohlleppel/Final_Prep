class Link:
    empty = ()

    def __init__(self, first, rest = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, item):
        if item == 0:
            return self.first
        else:
            return self.rest[item-1]

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link ({})'.format(self.first)
        else:
            return 'Link ({}, {})'.format(self.first, repr(self.rest))

hello = Link(0, Link(2))

print(hello.__len__())
print(hello.__getitem__(0))
print(hello[0])
print()

def flip_two(lnk):
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
    flip_two(lnk.rest.rest)

print("flip_two method")
one_lnk = Link(1)
flip_two(one_lnk)
print(one_lnk)
lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
flip_two(lnk)
print(lnk)
print()

def remove_duplicates(lnk):
    if lnk is Link.empty or lnk.rest is Link.empty:
        return
    #if the first value = second value
    elif lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
        return lnk
    else:
        remove_duplicates(lnk.rest)
        return lnk

print("remove_duplicates method")
lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
unique = remove_duplicates(lnk)
print(len(unique))
print(len(lnk))

def reverse(lnk):
    #always check if there is one node or no nodes
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    #if statement already takes care of the first one
    #call reverse function on the rest of the linked lis
    rev_rest = reverse(lnk.rest)
    #begin where the 2nd node
    #the last will point to the first
    lnk.rest.rest = lnk
    #the one before that will be empty
    lnk.rest = Link.empty
    return rev_rest

print()
print("reverse method")
a = Link(1, Link(2, Link(3)))
r = reverse(a)
print(r.first)
print(r.rest.first)

def multiply_lnks(lst_of_lnks):
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rest))

print()
print("multiply linked lists method")
a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(p.first)
print(p.rest.first)
print(p.rest.rest)

def even_weighted(lst):
    return [i * lst[i] for i in range(len(lst)) if i % 2 == 0]

print()
print("even weighted lists method")
x = [1,2,3,4,5,6]
print(even_weighted(x))
