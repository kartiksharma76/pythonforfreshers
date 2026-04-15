class BankAccount:
    bank_name = "State Bank of India"  # Class variable
    
    def __init__(self, account_holder, balance):
        self.bank_name =  account_holder  # Instance variable
        self.balance = balance  # Instance variable

        # Instance Method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

        #instance method access to private variable
    def get_balance(self):
        return self.balance
    
    # class method
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
    
    # static method
    @staticmethod
    def interest_rate():
        return 5  # Example interest rate
    
    # creaating Object
account1 = BankAccount("Kartik", 1000)

# acess public variable
print("Name :", account1.bank_name)  # Output: Name : Kartik

# Access Protected Variable (possible but not recommended)
print("Balance :", account1.balance)  # Output: Balance : 1000

# Accessing private variable (not possible, will raise an error)
# print(account1.__balance)  # This will raise an AttributeError

# Using instance method to access private variable
print("Balance using method:", account1.get_balance())  # Output: Balance using method: 1000


# Using Instance Method
account1.deposit(500)  # Output: Deposited 500. New balance: 1500

# Using Class Method
print("Bank Name:", BankAccount.get_bank_name())  # Output: Bank Name: State

# Using Static Method
print("Interest Rate:", BankAccount.interest_rate(), "%")  # Output: Interest Rate: 5 %

