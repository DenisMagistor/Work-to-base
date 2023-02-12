class CountObject:
    instance = 0

    def __init__(self):
        self.__class__.instance += 1

b= CountObject().instance
c= CountObject().instance
q= CountObject().instance

print(b, c, q)