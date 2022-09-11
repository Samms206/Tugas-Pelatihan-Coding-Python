"""
#create a function
def my_function():
    print("\nHello Bwang!\n")
#call function
my_function()

#print untuk menampilkan output
print("ini yang kedua\n")

#tipe data
# string
# integer
# float
# boolean

nama = "sam"
umur = 13
tinggi = 165.5
x = True

print(type(nama),"\n")
print(type(umur),"\n")
print(type(tinggi), "\n")
print(type(x), "\n")
print(10*"=")

#concat di python
# +
# ,

#list 
#array -> index dimulai 0
hewan = ["monyet","kucing","gukguk","ica"]
print(hewan[2])

#tuple
makanan = ("bakso","mie")
# makanan[1] = "kerupuk"
# print(makanan[1])
#set
minuman = {"coca-cola","sprite"}


# pengkondisian
print(10*"=")
if 10 < 7:
    print("oke benar")
else:
    print("salah")
print("end")

#aritmatika
print(10*"=")
a = 20
b = 5
c = a + b
print(a , "+", b, "=", c)
print(a , "-", b, "=", a - b)
print(a , "/", b, "=", a / b)
print(a , "*", b, "=", a * b)
print(a , "%", b, "=", a % b)
print(10*"=")

z = input("masukan nama anda : ")
print("nama anda adalah = "+ z)
"""


print("\nPROGRAM KONVERSI TEMPERATUR\n")

#CELCIUS
celcius = float(input("Masukan suhu dalam celcius = "))
print("suhunya adalah = ",celcius,"Celcius")

reamur = (4/5) * celcius
print("suhunya adalah = ",reamur,"Reamur")

fahrenheit = ((9/5) * celcius) + 32
print("suhunya adalah = ",fahrenheit,"Fahrenheit")

kelvin = celcius + 273
print("suhunya adalah = ",kelvin,"Kelvin")

#FAHRENHEIT
print("\n")
fahrenheit = float(input("Masukan suhu dalam fahrenheit = "))
print("suhunya adalah = ",fahrenheit,"Fahrenheit")

celcius = ((5/9) * (fahrenheit -32 ))
print("suhunya adalah = ",celcius,"Celcius")

reamur = ((4/9) * (fahrenheit - 32))
print("suhunya adalah = ",reamur,"Reamur")

kelvin = ((5 / 9) * (fahrenheit - 32) + 273)
print("suhunya adalah = ",kelvin,"Kelvin")

#KELVIN
print("\n")
kelvin = float(input("Masukan suhu dalam kelvin = "))
print("suhunya adalah = ",kelvin,"Kelvin")

celcius = kelvin - 273
print("suhunya adalah = ",celcius,"Celcius")

reamur = (4/5) * (kelvin - 273)
print("suhunya adalah = ",reamur,"Reamur")

fahrenheit = 1.8 * (kelvin - 273) + 32
print("suhunya adalah = ",fahrenheit,"Fahrenheit")

print("\nPROGRAM MENENTUKAN BANGUN RUANG VOLUME BOLA\n")
# V = 4/3 x π x r^3

jari = int(input("masukan jari-jari untuk menentukan valume sebuah bola = "))
volume = jari*jari*jari*4/3*22/7
print("Volumme Lingkaran adalah = ",volume)

