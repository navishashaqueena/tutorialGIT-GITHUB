class ObjekData:

    def __init__(self, nama, phone, email) -> None:
        self.nama = nama
        self.phone = phone
        self.email = email

    def talk(self):
        return f'nama : {self.nama}, no. tlp : {self.phone}, email : {self.email}'


data = ObjekData('rifki', 4356915, 'dwhiny@yahoo.com')

print(data.talk())
