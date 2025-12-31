class Matematika:
    @staticmethod
    def tambah(a, b):
        return a + b

result = Matematika.tambah(5, 7)
print("Hasil penjumlahan:", result)

class BankAccount:
    no = ""
    balance = 0
    active = True
    
    def __init__(self, no, balance):
        self.no = no
        self.balance = balance
    
    @classmethod
    def deactivate_account(cls, no, balance):
        account = cls(no, balance)
        account.active = False
        return account

account1 = BankAccount('987654', 500)
print(f"{account1.no} - Saldo: {account1.balance} - Aktif: {account1.active}")

account2 = BankAccount.deactivate_account('123456', 1000)
print(f"{account2.no} - Saldo: {account2.balance} - Aktif: {account2.active}")

class Category:
    _name = ""
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama kategori tidak boleh kosong")
        self._name = name

category = Category()
category.name = "Elektronik"
print("Nama Kategori:", category.name)