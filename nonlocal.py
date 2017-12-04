"""
>>> outside()
Inside!
Outside!
"""
def outside():
    msg = "Outside!"
    def inside():
        msg = "Inside!"
        print(msg)
    inside()
    print(msg)

