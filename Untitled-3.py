class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Melakukan penyetoran uang
        self.balance += amount
        print(f"Deposited {amount} into {self.owner}'s account. New balance: {self.balance}")

    def withdraw(self, amount):
        # Melakukan penarikan uang jika saldo mencukupi
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
        else:
            print(f"Insufficient funds. Cannot withdraw {amount}. Current balance: {self.balance}")

# Membuat objek dari class "BankAccount"
account_example = BankAccount("duta armi", balance=10000)

# Menampilkan informasi awal saldo
print(f"Initial balance for {account_example.owner}'s account: {account_example.balance}")

# Melakukan beberapa penyetoran dan penarikan
account_example.deposit(500)
account_example.withdraw(200)
account_example.withdraw(800)

# Menampilkan saldo terkini
print(f"Current balance for {account_example.owner}'s account: {account_example.balance}")
