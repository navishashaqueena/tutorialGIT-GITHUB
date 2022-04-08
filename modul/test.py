class ObjekData:

    def __init__(self, nama, phone, email, nik) -> None:
        self.nama = nama
        self.phone = phone
        self.email = email
        self.nik = nik

    def talk(self):
        return f'nama : {self.nama}, no. tlp : {self.phone}, email : {self.email}, nik : {self.nik}'


data = ObjekData('rifki', 4356915, 'dwhiny@yahoo.com', 3175071510770001)

print(data.talk())
