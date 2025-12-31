class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

mhs = Mahasiswa('001', 'Andi')

print(mhs.nim)   # Output: 001
print(mhs.nama)  # Output: Andi

class BankAccount:
    no = ""
    saldo = 0
    
    def __init__(self, no, saldo):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        
        self.no = no
        self.saldo = saldo

account = BankAccount('123456', 1000)
print(account.no)     # Output: 123456
print(account.saldo)  # Output: 1000