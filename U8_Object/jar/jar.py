class Jar:
    def __init__(self, capacity=12): #12 is jsust the default value, if user pass a diff value it will be over-write by that
        #check type is int
        if not isinstance (capacity, int):
            raise ValueError
        #check type is >0
        if capacity <0:
            raise ValueError
        #set Internal variables to be assess by whole object
        self._capacity = capacity
        self._size = 0 #internal counter for cookies


    def __str__(self):
       #using str method to return cookies n times
        return "🍪" *self._size

    def deposit(self, n):
        #check if adding will exceed capacity
        if n + self.size > self.capacity: #we ask property self and capacity for current self & capacity
            raise ValueError
        else:
            self._size += n #we change internal variables in dunder init so it's ._

    def withdraw(self, n):
        #check if enough cookies to withdraw
        if n > self.size:
            raise ValueError
        else:
            self._size -= n #take away cookies from jar and write this new values to internal varialbes

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    cookies = Jar (20)
    cookies.deposit (10)
    cookies.withdraw(5)
    print (cookies)

if __name__ == "__main__":
    main()
