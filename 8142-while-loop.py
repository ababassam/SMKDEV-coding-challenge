#Pada coding challenge #8142 kita menghitung kubus berdasarkan angka yang di input oleh user


input_number = int(input("input_number ="))
counter = 1

'''
> variabel input_number bernilai inputan user yang akan disimpan sebagai  yang kemudian dikonversi menjadi data type integer,
  sehingga inputan yang tidak dapat dikonversi menjadi integer akan menghasilkan value error.
> counter: Variabel loop yang digunakan untuk menghitung dari 1 sampai input_number.
'''


while counter <= input_number: 
    print(f'Current Number is : {counter} and the cube is {counter**3}')
    counter +=1 

'''
> Loop while berhenti ketika counter > input_number
> Kode print(f'Current Number is : {counter} and the cube is {counter**3}') adalah perintah untuk mencetak angka saat ini dan kubusnya ke konsol.
  - print() adalah fungsi bawaan Python yang digunakan untuk mencetak sesuatu ke konsol.
  - f adalah string literal f-string, yang memungkinkan kita untuk memasukkan variabel dan ekspresi ke dalam string.
  - {counter} adalah variabel yang berisi angka saat ini.
  - counter**3 adalah ekspresi yang menghitung kubus dari angka saat ini.
> Increment counter sebesar 1
'''
