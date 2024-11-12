operator = str(input('Pilih operator "pertambahan", "pengurangan", "perkalian", atau "pembagian": '))
number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))


if operator == 'pertambahan':
  res = number1 + number2
elif operator == 'pengurangan':
  res = number1 - number2
elif operator == 'perkalian':
  res = number1 * number2
elif operator == 'pembagian':
  res = number1 / number2


print(f'{operator} dari {number1} dan {number2} adalah {res}')