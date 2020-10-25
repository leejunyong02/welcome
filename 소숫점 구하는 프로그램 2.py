l = [i for i in range(2, 100)]

a = 2
b = 2
while a < 500 and b < 500:
    if l.count(a) == 0:
        a += b
    elif l.count(a) == 1:
        l.remove(a)
        a += b
    else:
        b += 1

print(l)


#---------------------------------------
        
l = [i for i in range(2, 100)]

a = 2   # 소수
b = 2   # 소수에 더해주는 수
while a < 100:
    while a < 100:
        if l.count(a) == 0:
            a += b
        elif l.count(a) == 1:
            l.remove(a)
            a += b
        else:
            a += 1

print(l)

#Github 파일 업로드 연습 중~~ ㅎ







        
