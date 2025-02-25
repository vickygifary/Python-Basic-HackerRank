import sys
import string

class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def purchase(self, req_items, money):
        total_cost = req_items * self.item_price
        
        if req_items > self.num_items:
            print("Not enough items in the machine")
        elif money < total_cost:
            print("Not enough coins")
        else:
            self.num_items -= req_items
            change = money - total_cost
            print(change)

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().split("\n")
    num_items, item_price = map(int, input_data[0].split())
    vm = VendingMachine(num_items, item_price)
    
    n = int(input_data[1])
    
    for i in range(2, 2 + n):
        req_items, money = map(int, input_data[i].split())
        vm.purchase(req_items, money)
