# Author: Kyla Moore
# Course: ITSC 3155

from BankAccount import *

newAccount = BankAccount("Caitlyn", 100.0)

newAccount.depositMoney(20.0)

newAccount.withdrawMoney(35.0)

print(newAccount.get_balance())