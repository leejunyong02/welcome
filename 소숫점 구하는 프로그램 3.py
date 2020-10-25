l = [i for i in range(2, 100)]

def wow(a, b):  #(소수이자 리스트에서 없어지면 안되는 수, 해당 소수)
    while a < 100:
        if l.index(a) == a:
            a += b
        
        elif l.count(a) == 0:
            a += b
            
        else:
            l.remove(a)
            a += b
    return l

print(l)

while a < 500:
    wow(a, b)
    a = b
    a += 1
    b += 1
print(l)
