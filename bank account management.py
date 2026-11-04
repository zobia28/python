class BankAccount:
    interest_rate = 0.02  # 2% interest rate
    
    def __init__(self, owner_name, initial_balance):
        self.__owner_name = owner_name
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = initial_balance
    
    @property
    def owner_name(self):
        return self.__owner_name
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance cannot be negative")
            return
        self.__balance = value
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return False
        self.__balance += amount
        return True
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        self.__balance -= amount
        return True
    
    def apply_interest(self):
        interest = self.__balance * self.interest_rate
        self.__balance += interest
        return interest
    
    def display_info(self):
        print(f"Account Owner: {self.__owner_name}")
        print(f"Balance: ${self.__balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")


# When you run this, type one of the test case names (e.g., original_test_case, account_creation, etc.)
try:
    test_case = input().strip()
except EOFError:
    test_case = "original_test_case"  # Fallback if no input is provided

if test_case == "account_creation":
    account = BankAccount("Alice", 1000)
    print(f"Owner: {account.owner_name}")
    print(f"Initial balance: ${account.balance}")
    print(f"Interest rate: {BankAccount.interest_rate * 100}%")

elif test_case == "deposit_method":
    account = BankAccount("Bob", 500)
    print(f"Initial balance: ${account.balance}")
    
    result = account.deposit(300)
    print(f"Deposit result: {result}")
    print(f"New balance: ${account.balance}")
    
    result = account.deposit(-50)
    print(f"Negative deposit result: {result}")
    print(f"Balance after invalid deposit: ${account.balance}")

elif test_case == "withdraw_method":
    account = BankAccount("Charlie", 1000)
    
    result = account.withdraw(400)
    print(f"Withdrawal result: {result}")
    print(f"Balance after withdrawal: ${account.balance}")
    
    result = account.withdraw(-50)
    print(f"Negative withdrawal result: {result}")
    
    result = account.withdraw(1000)
    print(f"Excessive withdrawal result: {result}")
    print(f"Final balance: ${account.balance}")

elif test_case == "property_access":
    account = BankAccount("Dave", 800)
    
    print(f"Owner via property: {account.owner_name}")
    print(f"Balance via property: ${account.balance}")
    
    account.balance = 1200
    print(f"Balance after valid setter: ${account.balance}")
    
    account.balance = -500
    print(f"Balance after invalid setter: ${account.balance}")
    
    try:
        print(account.__owner_name)
    except AttributeError:
        print("Cannot access private owner_name directly")

elif test_case == "apply_interest":
    account = BankAccount("Eve", 2000)
    
    print(f"Initial balance: ${account.balance}")
    
    interest_earned = account.apply_interest()
    expected_interest = 2000 * 0.02
    
    print(f"Interest earned: ${interest_earned}")
    print(f"New balance after interest: ${account.balance}")
    print(f"Interest calculation correct: {interest_earned == expected_interest}")

elif test_case == "display_info":
    # Test display_info method format
    account = BankAccount("Frank", 1500)
    
    original_rate = BankAccount.interest_rate
    BankAccount.interest_rate = 0.03
    
    print("Display info output:")
    account.display_info()
    
    BankAccount.interest_rate = original_rate

else:
    account = BankAccount("Coddy", 1000)

    account.deposit(500)
    account.withdraw(200)
    account.apply_interest()

    account.display_info()

    account.balance = 5000
    print(f"Balance after setter: ${account.balance}")

    account.withdraw(10000)
    print(f"Final balance: ${account.balance}")
