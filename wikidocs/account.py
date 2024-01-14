import random

class Account:

    account_count = 0


    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001

        Account.account_count +=1
 
    def deposit(self,num):
        if num >=1:
            self.balance+=num
    
    def withdraw(self,num):
        if num <= self.balance:
            self.balance-=num

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", f"{self.balance:,}")


    @classmethod
    def get_account_num(cls):
        print(cls.account_count)

kim = Account("김민수", 100)
lee = Account("리민수", 100)


lee.deposit(1000000000)
lee.display_info()
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)

# print(Account.account_count)

kim.get_account_num()