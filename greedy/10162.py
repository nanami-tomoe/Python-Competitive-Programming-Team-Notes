t = int(input())

a = 300
b = 60
c = 10

cnt_a = cnt_b = cnt_c = 0

while t > 0:
    if t >= 300:
        cnt_a += t // a
        t %= a
    elif t >= 60:
        cnt_b += t // b
        t %= 60
    elif t >= 10:
        cnt_c += t // c
        t %= 10
    elif t < 10:
        break
        

if t != 0:
    print(-1)
else:
    print(cnt_a, cnt_b, cnt_c)