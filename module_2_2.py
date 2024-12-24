first = 11
second = 12
third = 14

print('Ввод в консоль:')
print(first)
print(second)
print(third)

print('\nВывод на консоль:')
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
