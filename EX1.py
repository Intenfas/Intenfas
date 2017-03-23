from functools import partial

class Set:

    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)
print ("str(Set)"+str(s))

class Set1(Set):
    def __repr__(self):
        return "Set: " + str(self.dict.keys())

s2 =Set1([1,2,3,4,])
s2.add(10)
print ("str(Set1)"+str(s2))
print ("---------\n")

print ("-----\n")

def exp(base, power):
    return base ** power


def two_to_the(power):
    return exp(2, power)

two_to_the = partial(exp, 2) # is now a function of one variable
print two_to_the(3)
print ("---------\n")

def double(x):
 return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
print ("double for X in xs"+str(twice_xs))
twice_xs = map(double, xs) # same as above
print ("map"+str(twice_xs))
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]
print ("---------\n")

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5]) # [1 * 4, 2 * 5] = [4, 10]
print ("products"+str(products)+"\n")
def is_even(x):
 """True if x is even, False if x is odd"""
 return x % 2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
print ("x_evens" + " = " +str(x_evens) )
x_evens = filter(is_even, xs) # same as above
print ("filter_x_evens"+str(x_evens))
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]
print ("x_evens" + " = " +str(x_evens) )

print ("--reduce nultiply--")
x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24
print ("x_product = "+str(x_product))


print ("\n---word cut---")
documents=["aa","bbb","GGG"]

for i in range(len(documents)):
    document = documents[i]
    print (i, document)
print ("\n-------\n")

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)
print ("zip list1+list2 ="+str(zip(list1, list2)))


pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
print ("pairs unzip"+str(zip(*pairs)))


def magic(**args, *kwargs):
    print "unnamed args:", args
    print "keyword args:", kwargs
magic( 'a',1,2,key="word", key2="word2",)





