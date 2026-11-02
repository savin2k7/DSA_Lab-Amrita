class Hashing:
    def __init__(self):
        self.size = 11
        self.chain = [[] for i in range(self.size)]
        self.linear = [None] * self.size
        self.quadratic = [None] * self.size

    # Hash Function
    def hash_function(self, value):
        return value % self.size

    # Separate Chaining
    def insert_chaining(self, value):
        index = self.hash_function(value)

        if value not in self.chain[index]:
            self.chain[index].append(value)
            print(value, "Added using Separate Chaining")
        else:
            print("Duplicate value")

    # Linear Probing
    def insert_linear(self, value):
        index = self.hash_function(value)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] == None:
                self.linear[pos] = value
                print(value, "Added using Linear Probing")
                return

            elif self.linear[pos] == value:
                print("Duplicate value")
                return

        print("Hash table is full")

    # Quadratic Probing
    def insert_quadratic(self, value):
        index = self.hash_function(value)

        for i in range(self.size):
            pos = (index + i ** 2) % self.size

            if self.quadratic[pos] == None:
                self.quadratic[pos] = value
                print(value, "Added using Quadratic Probing")
                return

            elif self.quadratic[pos] == value:
                print("Duplicate value")
                return

        print("No empty position found")

    # Search using Separate Chaining
    def search_chaining(self, value):
        index = self.hash_function(value)

        if value in self.chain[index]:
            return True
        else:
            return False

    # Search using Linear Probing
    def search_linear(self, value):
        index = self.hash_function(value)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.linear[pos] == None:
                return False

            elif self.linear[pos] == value:
                return True

        return False

    # Search using Quadratic Probing
    def search_quadratic(self, value):
        index = self.hash_function(value)

        for i in range(self.size):
            pos = (index + i ** 2) % self.size

            if self.quadratic[pos] == None:
                return False

            elif self.quadratic[pos] == value:
                return True

        return False

    # Display Separate Chaining
    def display_chaining(self):
        print("\nSeparate Chaining:")

        for i in range(self.size):
            print(i, ":", self.chain[i])

    # Display Linear Probing
    def display_linear(self):
        print("\nLinear Probing:")

        for i in range(self.size):
            print(i, ":", self.linear[i])

    # Display Quadratic Probing
    def display_quadratic(self):
        print("\nQuadratic Probing:")

        for i in range(self.size):
            print(i, ":", self.quadratic[i])


# Main Program

h = Hashing()

values = [21, 32, 43, 54, 65, 76]

for value in values:
    h.insert_chaining(value)
    h.insert_linear(value)
    h.insert_quadratic(value)

h.display_chaining()
h.display_linear()
h.display_quadratic()

print("\nSearch 43:")

print("Separate Chaining:", h.search_chaining(43))
print("Linear Probing:", h.search_linear(43))
print("Quadratic Probing:", h.search_quadratic(43))