#Operasi aritmatika

a = 10
b = 3
c = 4

# Operasi penjumlahan
hasil = a + b
print('a + b =',hasil)

# Operasi pengurangan
hasil = a - b
print('a - b =',hasil)

# Operasi perkalian
hasil = a * b
print('a * b =',hasil)

# Operasi pembagian
hasil = a / b
print('a / b =',hasil)

# Operasi perpangkatan (eksponen)
hasil = a ** b
print('a ** b =',hasil)

# Operasi modulus
hasil = a % b
print('a % b =',hasil)

# Operasi floor division
hasil = a // b
print('a // b =',hasil)


# Prioritas operasi
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -

x = 4
y = 2

hasil = x + y * x
print(hasil)

hasil = x ** y * x
print(hasil)