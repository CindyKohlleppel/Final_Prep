class Instructor:
    count = 0

    def __init__(self, name):
        self.name = name
        #self.count would be based on instance
        #Instructor.count makes it class level
        Instructor.count += 1

c = Instructor('cindy')
w = Instructor('weiying')

c.count = 11231
print(c.count)
w.count = 0
print(w.count)
Instructor.count = 3
print(Instructor.count)


#can reset the count value or change the value after the methods