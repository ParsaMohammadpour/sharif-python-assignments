class Person:
    id_counter = 1
    def __init__(self, name):
        self.name = name
        self.id = Person.id_counter
        Person.id_counter += 1

class Customer(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.balance = 0

    def inc_balance(self, amount):
        self.balance += amount

class Cashier(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.transaction_number = 0

class Tranaction:
    id_counter = 1
    def __init__(self, customer, cashier, amount):
        self.id = self.id_counter
        Tranaction.id_counter += 1
        self.customer = customer
        self.cashier = cashier
        self.amount = amount

class Flower:
    def __init__(self, name, number, price):
        self.number = number
        self.price = price
        self.name = name

users = []
flowers = []
transactions = []
while True:
    command = input().split()
    if command[0].__eq__('add') and command[1].__eq__('customer'):
        users.append(Customer(command[2]))
        print(users[len(users) - 1].id)
    elif command[0].__eq__('add') and command[1].__eq__('cashier'):
        users.append(Cashier(command[2]))
        print(users[len(users) - 1].id)
    elif command[0].__eq__('increase') and command[1].__eq__('balance') and command[2].__eq__('customer') and command[4].__eq__('amount'):
        customer = next(x for x in users if x.id == int(command[3]))
        customer.inc_balance(int(command[5]))
    elif command[0].__eq__('add') and command[1].__eq__('flower') and command[2].__eq__('name') and command[4].__eq__('price') and command[6].__eq__('amount'):
        flowers.append(Flower(name=command[3], price=int(command[5]), number=int(command[7])))
    elif command[0].__eq__('increase') and command[1].__eq__('amount') and command[2].__eq__('flower') and command[4].__eq__('amount'):
        flower = next(x for x in flowers if x.name.__eq__(command[3]))
        flower.number += int(command[5])
    elif command[0].__eq__('sell') and command[1].__eq__('flower') and command[2].__eq__('name') and command[4].__eq__('amount') and command[6].__eq__('to') and command[7].__eq__('customer') and command[9].__eq__('by') and command[10].__eq__('cashier'):
        flower = next(x for x in flowers if x.name.__eq__(command[3]))
        if flower.number < int(command[5]):
            print('insufficient flower!')
            continue
        costomer = customer = next(x for x in users if x.id == int(command[8]))
        if costomer.balance < (int(command[5]) * flower.price):
            print('customer does not have enough money!')
            continue
        flower.number -= int(command[5])
        costomer.balance -= (int(command[5]) * flower.price)
        transactions.append(Tranaction(customer=costomer, cashier=next(x for x in users if x.id == int(command[11])), amount=int(command[5]) * flower.price))
        print(f'transaction {transactions[len(transactions) - 1].id} successfully created!')
    elif command[0].__eq__('print') and command[1].__eq__('transaction') and command[2].__eq__('id'):
        transac = next(x for x in transactions if x.id == int(command[3]))
        print(f'transaction {transac.id}: customer: {transac.customer.name} cashier: {transac.cashier.name} payment amount: {transac.amount}')
    elif command[0].__eq__('print') and command[1].__eq__('salary') and command[2].__eq__('slip') and command[3].__eq__('cashier'):
        cashier = next(x for x in users if x.id == int(command[4]))
        cashier_trans = [x for x in transactions if x.cashier.id == cashier.id]
        print(f'salary slip: cashier {cashier.name} {cashier.id} {len(cashier_trans) * 70000}')
    elif command[0].__eq__('exit'):
        break