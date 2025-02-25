import sys

class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        self.elements[val] = self.elements.get(val, 0) + 1

    def remove(self, val):
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def __contains__(self, val):
        return val in self.elements

    def __len__(self):
        return sum(self.elements.values())


if __name__ == '__main__':
    multiset = Multiset()
    
    # Read input from stdin
    q = int(sys.stdin.readline().strip())
    
    for _ in range(q):
        operation = sys.stdin.readline().strip().split()
        
        if operation[0] == "add":
            multiset.add(int(operation[1]))
        elif operation[0] == "remove":
            multiset.remove(int(operation[1]))
        elif operation[0] == "query":
            print("True" if int(operation[1]) in multiset else "False")
        elif operation[0] == "size":
            print(len(multiset))
