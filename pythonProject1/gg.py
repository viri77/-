total = 0
for x in range(1, 33):
    for y in range(1, 33):
        for a in range(1, 33):
            for b in range(1,33):
                if (x**3)+(y**3)==(a**3)+(b**3) and a != b and a != x and a != x and b != x and b != y and x != a:
                    total += 1
                    print('x =', x,'y=',y , 'a =', a, 'b =', b)
                    print(x**3+y**3)
                    print(a**3+b**3)
print('Общее количество натуральных решений =', total)