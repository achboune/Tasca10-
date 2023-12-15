# Programa per mostrar el patró
n = 3

# Part superior del patró
for i in range(1, n + 1):
    print('*' * i)

# Part inferior del patró
for i in range(n - 1, 0, -1):
    print('*' * i)
