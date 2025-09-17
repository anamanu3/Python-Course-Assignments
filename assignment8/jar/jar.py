class Jar:
    def __init__(self, capacity=12):
        if isinstance(capacity, int) is False:
            raise ValueError("Capacity must be a non-neg integer!")

        if capacity < 0:
            raise ValueError("Capacity must be a non-neg integer!")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = "🍪" * self._size
        return cookies

    def deposit(self, n):
        if isinstance(n, int) is False:
            raise ValueError("Deposit must be integer")
        if n < 0:
            raise ValueError("Deposit cannot be negative!")

        new_total = self._size + n

        if new_total > self._capacity:
            raise ValueError("Too many cookies!")
        self._size = new_total

    def withdraw(self, n):
        if isinstance(n, int) is False:
            raise ValueError("Withdraw must be an integer")

        if n < 0:
            raise ValueError("Withdraw cannot be negative")

        new_total = self._size - n

        if new_total < 0:
            raise ValueError("Not enough cookies!!")
        self._size = new_total

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
