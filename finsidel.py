def stars(n):
    print('X' * n)
    
x = int(input('how many stars do you want: '))
for i in range(x):
    stars(i)

for i in range(x, 0, -1):
    stars(i)
    