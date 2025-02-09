# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 00:29:16 2024

@author: demar
"""

def print_current(D):
    print("\n\nCurrent Balances:\n")
    k = D.keys()
    v = D.values()
    for i in k:
        print(f'{i:>10s}', end=" ")  #print the names, end each print with empty space and 10 padding
    print('\n')
    for j in v:
        number = f'${abs(j):.2f}'    #get the number formatted to a string
        if j < 0:
            number = '-' + number    #add on the negative sign if needed
        print(' '*(10-len(number)) + number, end = ' ')    #print spaces equal to 10 - length of the number string
    print('\n')   

#initialize
num_users = int(input("Number of accounts: "))
accounts = dict()
for n in range(num_users):
    name = str(input("Name: "))
    balance = float(input("Balance: "))
    accounts[name] = balance
    
#main loop
flag = 1
transactions = []
while(flag):
    print()
    transact = {}
    for x in accounts:
        print(f'Processing {x}')
        choice = int(input("Transaction Type:\n1. Nothing\n2. Deposit\n3. Withdrawal\n: "))
        if choice == 1:
            transact[x] = 0
        elif choice == 2:
            amount = float(input("Amount: "))
            accounts[x] += amount
            transact[x] = amount
        elif choice == 3:
            amount = float(input("Amount: "))
            accounts[x] -= amount
            transact[x] = -amount
    transactions.append(transact)
    print()
    print_current(accounts)
    flag = int(input("Enter:\n0 to stop, 1 to continue\n:"))
    
#print records at the end
print("\nRecord of Transactions\n")
print("Round", end=' ')
for a in accounts:
    print("{0:>10s}".format(a), end=' ')
    
print('\n'+"-"*(11*len(accounts)+6))

for t in range(len(transactions)):
    print(f'{t+1:^5d}', end=' ')
    for n in transactions[t]:
        b = transactions[t][n]
        string = f'${abs(b):.2f}'
        if b < 0: string = '-' + string
        print(" "*(10-len(string))+string, end=' ')
    print()