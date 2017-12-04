class Counter:
    numCountersMade = 0

    def __init__(self, count = 0):
        self.count = count
        Counter.numCountersMade += 1

    def increment(self):
        self.count += 1

    def __str__(self):
        return "Counter: " + str(self.count)

    def clear(self):
        self.count = 0

c1 = Counter()
print(c1.numCountersMade)
c2 = Counter(100)
print(c1)
print(c2)
c1.increment()
print(c1)
print(c2)
print(c1.numCountersMade)
c2.clear()
print(c2)