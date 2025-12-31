class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"halo {nama}, saya {self.nama}")

mahasiswa1 = Mahasiswa()
print(type(mahasiswa1))  # Output: <class '__main__.Mahasiswa'>

mahasiswa1.nim = '123'
mahasiswa1.nama = 'Budi'

mahasiswa1.perkenalan()
mahasiswa1.hello('saya')